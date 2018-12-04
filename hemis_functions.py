from os import chdir, system
import glob, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from astropy.table import Table, join, vstack, hstack
from scipy.interpolate import splrep, splev
from scipy.signal import savgol_filter, argrelextrema

# predefined settings for observation stands
LOCATIONS = pd.DataFrame(index=['Symbol', 'Y_coord', 'X_coord', 'Altitude'])
LOCATIONS['Malic'] = ['MA', 46.182777, 15.199722, 850]
LOCATIONS['Cigonca'] = ['CI', 46.364998, 15.580556, 250]
LOCATIONS['Trnovo'] = ['TR', 45.994167, 13.760278, 812]
LOCATIONS['Ovcarija'] = ['OV', 46.483055, 15.256111, 1200]

def string_to_jul(s):
	jul_date = np.int32(str(s).split('-'))
	jul_date = datetime(jul_date[0],jul_date[1],jul_date[2]).toordinal() + 1721424.5
	return jul_date

sat_data = Table.read('hemis_sat_data_Probav_TOC_all.csv', format='ascii.csv')
# add JD date
sat_data['jul_date'] = np.float64(0)
for i_l in range(len(sat_data)):	
	sat_data['jul_date'][i_l] = string_to_jul(sat_data['Satellite_Date'][i_l])

cols = sat_data.colnames
cols_use = [c for c in cols if 'RED' in c or 'BLU' in c or 'NIR' in c or 'SWR' in c]

def poly_fit_data(data, x_c, y_cols, return_complete=True):
	data_out = Table(data)
	x_data = data_out[x_c].data
	x_range = np.linspace(x_data[0], x_data[-1], x_data[-1]-x_data[0]+1)
	mean_x_data = np.mean(x_data)
	x_data -= mean_x_data
	n_x_range = len(x_range)
	if return_complete:
		data_ts = data[:0]
		for i in range(n_x_range):
			data_ts.add_row(data[0])
		data_ts['Sat_Date'] = ''
		data_ts['jul_date'] = x_range
		data_ts['QUA'] = 'True'
		data_ts['QUA_val'] = 0
	for y_c in y_cols:
		y_data = data[y_c].data
		idx_fit = np.isfinite(y_data)
		for i_f in range(5):
			# 1
			poly_coef = np.polyfit(x_data[idx_fit], y_data[idx_fit], 8)
			ts_fit = np.poly1d(poly_coef)(x_data)
			# 2
			#chb_coef = np.polynomial.chebyshev.chebfit(x_data[idx_fit], y_data[idx_fit], 17)
			#ts_fit = np.polynomial.chebyshev.chebval(x_data, chb_coef)
			# 3
			#leg_coef = np.polynomial.legendre.legfit(x_data[idx_fit], y_data[idx_fit], 17)
			#ts_fit = np.polynomial.legendre.legval(x_data, leg_coef)
			# 4
		    	#spline_coef = splrep(x_data[idx_fit], y_data[idx_fit], k=2, s=3)
			#ts_fit = splev(x_data, spline_coef)
			#
			diff = y_data - ts_fit
			std_diff = np.nanstd(diff)
			idx_fit = np.logical_and(idx_fit, np.abs(diff) < 2.5*std_diff)
		# output fited data
		if return_complete:			
			data_ts[y_c] = np.poly1d(poly_coef)(x_range-mean_x_data)
		else:
			data_out[y_c] = ts_fit
	if return_complete:
		return data_ts
	else:
		return data_out

def sg_filter_data(data, x_c, y_cols):
	data_out = Table(data)
	x_data = data[x_c].data
	for y_c in y_cols:
		y_data = data[y_c].data
		data_out[y_c] = savgol_filter(y_data, window_length=9, polyorder=2)
	return data_out

def parse_hemis_xlsx(files, mean=False):
    cols = 'D,BH:BU,CL:CQ,CV:CX'  # names of the columns to be read from xlsx file
    # pd.read_excel() is very slow for larger tables
    # dframes = [pd.read_excel(read_file, sheetname='Global', header=0, parse_cols=cols) for read_file in files]
    dframes = list([])
    for read_file in files:
        dframes.append(pd.read_excel(read_file, sheetname='Global', header=0, parse_cols=cols))
    # merge together all data frames
    out_dframe = pd.concat(dframes, ignore_index=True)
    # convert acquisition string to date type
    dates = out_dframe['Acquisition Date Time']
    out_dframe['Acquisition Date Time'] = [datetime.strptime(d, '%Y:%m:%d %H:%M:%S').date() for d in dates]
    # replace {-, , (, )} sign with something else in column names
    out_dframe.columns = out_dframe.columns.str.replace('-','_')
    out_dframe.columns = out_dframe.columns.str.replace(' ','_')
    out_dframe.columns = out_dframe.columns.str.replace('(','')
    out_dframe.columns = out_dframe.columns.str.replace(')','')
    if mean:
        # calculate column mean values
        out_dframe = out_dframe.groupby('Acquisition_Date_Time').mean()
        # add date field
        out_dframe['Acquisition_Date_Time'] = out_dframe.index.values
        out_dframe['index'] = range(0, len(files))
        # rename index values
        out_dframe.set_index('index', inplace=True)
    return out_dframe
