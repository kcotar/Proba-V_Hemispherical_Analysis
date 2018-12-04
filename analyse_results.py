# ****************
#    Imports
# ****************
import os, glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from datetime import datetime, timedelta
from astropy.table import Table
from lmfit import Parameters, minimize
from astropy.modeling import models, fitting
from astropy.stats import sigma_clip
 

# ****************
#    Definition of functions
# ****************
def do_scatter(data, x_col, y_col, c_col=None, path='img.png', title='', fit_res=None, fit_func=None):
	title_add = ''
	if fit_res is not None:
		# compute fitted function
		min_x = np.min(data[x_col])
		max_x = np.max(data[x_col])
		x_data_range = np.linspace(min_x, max_x, num=100)
		plt.plot(x_data_range, fit_func(fit_res, x_data_range, 0., func_value=True), label='Fit', lw=1., c='black')
		# compute RMSE of the fit
		y_from_fit = fit_func(fit_res, data[x_col], data[y_col], func_value=True)
		y_residuals = y_from_fit - data[y_col]
		y_rmse = np.sqrt(np.nansum((y_residuals)**2)/len(y_from_fit))
		title_add += '  RMSE: {:.3f}'.format(y_rmse)
		y_std = np.nanstd(y_residuals)
		title_add += '  STD: {:.3f}'.format(y_std)
	if c_col is not None:
		u_id = np.unique(data[c_col])
		c_map = plt.cm.get_cmap('jet')
		n_u_id = len(u_id)
		for i_u in range(n_u_id):
			idx_plot = data[c_col] == u_id[i_u]
			plt.scatter(data[x_col][idx_plot], data[y_col][idx_plot], c=c_map(1.*i_u/n_u_id), s=8, lw=0, label=u_id[i_u])
	else:
		plt.scatter(data[x_col], data[y_col], c='black', s=8, lw=0)
	plt.xlabel(x_col.split('_')[0])
	plt.ylabel(y_col.split('_')[0])
	plt.title(title + title_add)
	plt.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", borderaxespad=0)
	plt.savefig(path, dpi=350, bbox_inches="tight")
	plt.close()

def plot_correlation_matrix(in_data, title='', path =''):
    fig, ax = plt.subplots(figsize=(5, 5.5))
    mat_ax = ax.matshow(np.abs(in_data), cmap='Greys', vmin=0, vmax=1, interpolation="none")
    tics_labels = [val.split('_')[0] for val in in_data.columns.values]
    plt.title(title)
    plt.xticks(range(in_data.shape[1]), tics_labels, rotation='vertical')
    plt.yticks(range(in_data.shape[0]), tics_labels, rotation='horizontal')
    fig.colorbar(mat_ax, orientation="horizontal", pad=0.05)
    plt.tight_layout()
    if path != '':
        plt.savefig(path, dpi=400)
    else:
        plt.show()
    plt.close()


def exp_function(param, x_ref, y_ref, func_value=False):
	param_values = param.valuesdict()
	y_fit = param_values['y_amp'] * np.exp(-1.*param_values['x_amp']*(x_ref)) + param_values['y_offset']
	if func_value:
		return y_fit
	else:
		return np.power(y_ref - y_fit, 2)


def lin_function(param, x_ref, y_ref, func_value=False):
	param_values = param.valuesdict()
	y_fit = -1. * param_values['x_amp'] * (x_ref) + param_values['y_offset']
	if func_value:
		return y_fit
	else:
		return np.power(y_ref - y_fit, 2)


def invlin_function(param, x_ref, y_ref, func_value=False):
	param_values = param.valuesdict()
	y_fit = -1. * param_values['x_amp'] * x_ref / (param_values['x_offset'] + x_ref) #+ param_values['y_offset']
	if func_value:
		return y_fit
	else:
		return np.power(y_ref - y_fit, 2)


def fit_to_function(data, x_col, y_col, fit_function, n_clip=1, std_clip=3.):
	# TODO: fits to both functions, comparisson itd
	# print data[x_col]
	# print data[y_col]
	x_data = data[x_col].data
	y_data = data[y_col].data
	idx_use = np.isfinite(data[x_col])
	for i_c in range(n_clip):
		print np.sum(idx_use)
		fit_param = Parameters()
		fit_param.add('y_offset', value=0., vary=True, brute_step=0.05, min=-3, max=3)
		fit_param.add('x_offset', value=0., vary=True, brute_step=0.05, min=-3, max=3)
		fit_param.add('x_amp', value=-1., vary=True, brute_step=0.05, min=-4, max=4)
		fit_param.add('y_amp', value=1., vary=True, brute_step=0.05, min=-4, max=4)
		fit_res = minimize(fit_function, fit_param, method='least-squares', args=(x_data[idx_use], y_data[idx_use]), **{'nan_policy': 'omit'})
		fit_res_curve = fit_function(fit_param, x_data, y_data, func_value=True)	
		y_data_diff = y_data - fit_res_curve
		y_diff_std = np.nanstd(y_data_diff[idx_use])
		idx_use = np.logical_and(idx_use, np.abs(y_data_diff) < y_diff_std * std_clip)
	fit_res_params = fit_res.params
	fit_res_params.pretty_print()
	return fit_res_params

def astropy_function(x_ref, y_ref):
	model_init2 = models.Shift(0.5) | (models.PowerLaw1D() + models.Linear1D()) 
	fitter2 = fitting.LevMarLSQFitter()
	model_res2 = fitter2(model_init2, x_ref, y_ref)
	return model_res2

def astropy_function_curve(model, x_ref, n_points=75):
	x_vals = np.linspace(np.nanmin(x_ref), np.nanmax(x_ref), n_points)
	y_vals = model(x_vals)
	return x_vals, y_vals

def do_scatter_astropy(data, x_col, y_col, c_col=None, path='img.png', title='', fit_model=None, x_lim=None, y_lim=None):
	title_add = ''
	if fit_model is not None:
		# compute fitted function
		x_fit, y_fit = astropy_function_curve(fit_model, data[x_col])
		plt.plot(x_fit, y_fit, label='Fit', lw=1., c='black')
		# compute RMSE of the fit
		y_from_fit = fit_model(data[x_col])
		y_residuals = y_from_fit - data[y_col]
		y_rmse = np.sqrt(np.nansum((y_residuals)**2)/len(y_from_fit))
		title_add += '  RMSE: {:.3f}'.format(y_rmse)
		y_std = np.nanstd(y_residuals)
		title_add += '  STD: {:.3f}'.format(y_std)
	if c_col is not None:
		u_id = np.unique(data[c_col])
		c_map = plt.cm.get_cmap('jet')
		n_u_id = len(u_id)
		for i_u in range(n_u_id):
			idx_plot = data[c_col] == u_id[i_u]
			plt.scatter(data[x_col][idx_plot], data[y_col][idx_plot], c=c_map(1.*i_u/n_u_id), s=8, lw=0, label=u_id[i_u])
	else:
		plt.scatter(data[x_col], data[y_col], c='black', s=8, lw=0)
	plt.xlabel(x_col.split('_')[0])
	plt.ylabel(y_col.split('_')[0])
	if x_lim is not None:
        	plt.xlim(x_lim)
	if y_lim is not None:
        	plt.ylim(y_lim)
	plt.title(title + title_add)
	plt.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", borderaxespad=0)
	plt.savefig(path, dpi=350, bbox_inches="tight")
	plt.close()


# ****************
#     Main
# ****************
# processing steps settings
fit_all = True
fit_locations = True
fit_leave_one_out = True

#input settings
degrees = '180'

# interpolated data input +/-2 days around ground observation
in_dir = 'Timeseries_hemis_'+degrees+'_fitpoly08'
csv_data = 'hemis_'+degrees+'_and_ts_data_TOC_days0_qua.csv'
out_dir = 'res_fit_final_days0'

# original data input +/- 10 days around ground observation
#in_dir = 'rezultati_'+degrees+'_filtered'
#csv_data = '_hemis_sat_data_Probav_TOC.txt'
#out_dir = 'res_fit_final'

# some plot settings
plot_ylim_dict = {'LAI2000_Log':(0,3.5 ),
		  'TotalSiteFactor':(0,0.7),
		  'Openness':(0,50)}
plot_xlim_dict = {'NDVI':(0.4, 0.9), 'NDWI':(-0.5,0.2),'SAVI':(0.1,0.6),'EVI':(0.1,0.7), 'FAPAR':(0.4,0.9),'FCOVER':(0.3,1),'LAI':(0.5,5), 'MSAVI':(0.1,0.6)} 

os.chdir(in_dir)

data_all = Table.read(csv_data, format='ascii.csv')

hemis_params = ['LAI2000_Log','TotalSiteFactor','Openness']
bio_params = ['NDVI','NDWI','SAVI','MSAVI','EVI','LAI','FAPAR','FCOVER']

# temp fo ploting
hemis_params = ['LAI2000_Log','TotalSiteFactor']
# bio_params = ['EVI']

os.system('mkdir '+out_dir)
os.chdir(out_dir)

# do fit to all data
if fit_all:
	do_scatter(data_all, 'TotalSiteFactor', 'LAI2000_Log', path='all_LAI2000_Log_TotalSiteFactor_site.png', c_col='Location', title='Color by Acquisition_Date_Time')
	# correlation
	data_all_corr = data_all[list(np.hstack([hemis_params, bio_params]))].to_pandas().corr(method='pearson', min_periods=3)
	plot_correlation_matrix(data_all_corr, path='all_correlations.png')

	for h_param in hemis_params:
		for b_param in bio_params:
			print 'all_'+h_param+'_'+b_param
			fit_params = astropy_function(data_all[b_param], data_all[h_param])
			do_scatter_astropy(data_all, b_param, h_param, path='all_'+h_param+'_'+b_param+'_lin.png', 
					   fit_model=fit_params, c_col='Location', title='Color by Location', 
					   y_lim=plot_ylim_dict[h_param], x_lim=plot_xlim_dict[b_param])

if fit_locations:
	for location in np.unique(data_all['Location']):
		data_loc_sub = data_all[data_all['Location'] == location]
		data_loc_sub = data_loc_sub.filled()
		# correlation
		data_loc_sub_corr = data_loc_sub[list(np.hstack([hemis_params, bio_params]))].to_pandas().corr(method='pearson', min_periods=3)
		plot_correlation_matrix(data_loc_sub_corr, path=location+'_correlations.png')
		# individual site fits and plots
		for h_param in hemis_params:
			for b_param in bio_params:
				print location+'_'+h_param+'_'+b_param
				fit_params = astropy_function(data_loc_sub[b_param], data_loc_sub[h_param])
				do_scatter_astropy(data_loc_sub, b_param, h_param, path=location+'_'+h_param+'_'+b_param+'_lin.png', fit_model=fit_params, 
						   c_col='Acquisition_Date_Time', title='Color by ground acquisition date', 
					   	   y_lim=plot_ylim_dict[h_param], x_lim=plot_xlim_dict[b_param])

# leave one out test za 
if fit_leave_one_out:
	os.chdir('One_out_test')
	txt_out_std = open('leave_one_out_std.csv', 'w')
	txt_out_rms = open('leave_one_out_rmse.csv', 'w')
	for location in np.unique(data_all['Location']):
		# subsets of data for one and other locations
		data_loc_sub = data_all[data_all['Location'] == location]
		data_other_sub = data_all[data_all['Location'] != location]
		# fill maked out data
		data_loc_sub = data_loc_sub.filled()
		data_other_sub = data_other_sub.filled()
		# individual site fits and plots
		for h_param in hemis_params:
			for b_param in bio_params:
				print location+'_'+h_param+'_'+b_param
				fit_model_other = astropy_function(data_other_sub[b_param], data_other_sub[h_param])
				loc_predicted_data = fit_model_other(data_loc_sub[b_param])
				# prediction error compute
				pred_residuals = loc_predicted_data - data_loc_sub[h_param]
				pred_std = np.nanstd(pred_residuals)
				pred_rms = np.sqrt(np.nansum((pred_residuals)**2)/len(pred_residuals))
				# output results
				print pred_std
				out_str = location+','+h_param+','+b_param+','+str(pred_std)+'\n'
				txt_out_std.write(out_str)
				out_str = location+','+h_param+','+b_param+','+str(pred_rms)+'\n'
				txt_out_rms.write(out_str)
				# save plots
				do_scatter_astropy(data_loc_sub, b_param, h_param, path=location+'_'+h_param+'_'+b_param+'_2.png', fit_model=fit_model_other, 
						   c_col='Acquisition_Date_Time', title='Color by ground acquisition date', 
					   	   y_lim=plot_ylim_dict[h_param], x_lim=plot_xlim_dict[b_param])
				do_scatter_astropy(data_all, b_param, h_param, path=location+'_'+h_param+'_'+b_param+'_1.png', 
						   fit_model=fit_model_other, c_col='Location', title='Color by Location', 
						   y_lim=plot_ylim_dict[h_param], x_lim=plot_xlim_dict[b_param])
	txt_out_std.close()
	txt_out_rms.close()

