from hemis_functions import *
from copy import deepcopy

degrees = '180'

hemispherical_dir = 'Hemispherical_data/ANALIZA/'+degrees+'/'
ts_ref = Table.read('hemis_sat_data_Probav_TOC_all_ts_qua-ref_fitpoly08.csv')
print ts_ref

out_dir = 'Timeseries_hemis_'+degrees+'_fitpoly18'
system('mkdir '+out_dir)
chdir(out_dir)

# determine statistics of the following hemispherical parameters
get_stat = ['LAI2000_Log', 'Openness', 'TotalSiteFactor']

hemis_all = list([])
hemis_all_means = list([])
for place_name in LOCATIONS.columns.values:
	xlsx_files = glob.glob(hemispherical_dir+'*/*'+LOCATIONS[place_name]['Symbol']+'*.xlsx')
	print 'Reading '+place_name+' xlsx files. This can take few minutes per file!'
	print 'Number of files is '+str(len(xlsx_files))
	hemis_values = parse_hemis_xlsx(xlsx_files, mean=False)
	hemis_values = Table.from_pandas(hemis_values)
	hemis_values['Location'] = place_name
	hemis_all.append(hemis_values)
	# determine means
	hemis_values_means = deepcopy(hemis_values)
	for s_date in np.unique(hemis_values_means['Acquisition_Date_Time']):
		idx_date = hemis_values_means['Acquisition_Date_Time'] == s_date
		for s_col in get_stat:
			hemis_values_means[s_col][idx_date] -= np.mean(hemis_values_means[s_col][idx_date])
	hemis_all_means.append(hemis_values_means)
	
hemis_all = vstack(hemis_all)
hemis_all_means = vstack(hemis_all_means)
print ''
print 'Hemis statistics std:'
for s_col in get_stat:
	print s_col, np.std(hemis_all_means[s_col])
print ''
print hemis_all
print hemis_all_means

# output means

# add JD date
hemis_all['jul_date_hemis'] = np.float64(0)
for i_l in range(len(hemis_all)):	
	hemis_all['jul_date_hemis'][i_l] = string_to_jul(hemis_all['Acquisition_Date_Time'][i_l])
hemis_all.sort('jul_date_hemis')
# print hemis_all

# match JD of hemis with JD of sat data

# 2 days around original ground date
n_days_around = 2  # obs +/- days
days_step = 2

# only the actual date of ground observation
#n_days_around = 0  # obs +/- days
#days_step = 1

ts_ref['jul_date_hemis'] = np.float64(0)
for loc in np.unique(hemis_all['Location']):
	# print loc
	hemis_all_loc = hemis_all[hemis_all['Location'] == loc]
	for jd_hemis in np.unique(hemis_all_loc['jul_date_hemis']):
		# make a list of ref ts dates to be linked to this observation
		jds_use = np.linspace(-n_days_around, n_days_around, (2*n_days_around)/days_step+1) + jd_hemis
		# apply jd_hemis to the observations with date of jds_use
		for jd_ts in jds_use:
			idx_ts = np.logical_and(ts_ref['jul_date']==jd_ts, ts_ref['Location']==loc)
			ts_ref['jul_date_hemis'][idx_ts] = jd_hemis

# join both datasets
hemis_ts_data = join(hemis_all, ts_ref, keys=['jul_date_hemis', 'Location'])
# print hemis_ts_data

# compute vegetation indices for the selected subset of data
veg_indices_all = list([])
for ts_row in hemis_ts_data:
	indices = compute_indices(ts_row['BLU'], ts_row['RED'], ts_row['NIR'], ts_row['SWR'])
	veg_indices_all.append(indices)

veg_indices_all = vstack(veg_indices_all)
hemis_ts_data = hstack([hemis_ts_data, veg_indices_all])
# print hemis_ts_data

hemis_ts_data.write('hemis_'+degrees+'_and_ts_data_TOC_days2_qua.csv', overwrite=True)




