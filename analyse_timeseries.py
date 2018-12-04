from hemis_functions import *

chdir('Timeseries_plots')
marks = ['2014-01-01', '2015-01-01', '2016-01-01', '2017-01-01']
marks_hemis = ['2015-09-17','2015-10-22','2015-12-21','2016-04-07','2016-05-20','2016-06-10','2016-07-20','2016-08-18','2016-09-07','2016-10-07','2016-12-08']
locations = np.unique(sat_data['Location'])

data_out = list([])
for loc in locations:
	print loc
	# QUA
	# idx_use = np.logical_and(sat_data['Location']==loc, sat_data['QUA']=='True')
	# QUA-REF	
	idx_use = np.logical_and(sat_data['Location']==loc, np.logical_and(sat_data['BLU']>3e-3, sat_data['RED']>3e-3))
	idx_use = np.logical_and(idx_use, np.logical_and(np.logical_and(sat_data['RED']<0.065,sat_data['BLU']<0.065), sat_data['NIR']<0.5))
	# time subseting
	idx_use = np.logical_and(idx_use, np.logical_and(sat_data['jul_date']<2457800, sat_data['jul_date']>string_to_jul(marks[1])-60))
	sat_data_loc = sat_data[idx_use]

	# data smothing/filtering/intepolation/svasta
	sat_data_loc_sg = poly_fit_data(sat_data_loc, 'jul_date', cols_use)
	data_out.append(sat_data_loc_sg)

        # compute fit error
	sat_data_loc_er = poly_fit_data(sat_data_loc, 'jul_date', cols_use, return_complete=False)
	er = np.sqrt(np.sum((sat_data_loc[cols_use].to_pandas().values - sat_data_loc_er[cols_use].to_pandas().values)**2))
	
	plt.plot(sat_data_loc['jul_date'], sat_data_loc['RED'], lw=1, c='red', label='Red')
	plt.plot(sat_data_loc['jul_date'], sat_data_loc['BLU'], lw=1, c='blue', label='Blue')
	plt.plot(sat_data_loc['jul_date'], sat_data_loc['NIR'], lw=1, c='green', label='Nir-IR')
	plt.plot(sat_data_loc['jul_date'], sat_data_loc['SWR'], lw=1, c='orange', label='SWIR')
	plt.plot(sat_data_loc_sg['jul_date'], sat_data_loc_sg['RED'], lw=2, c='red', label='', linestyle='--')
	plt.plot(sat_data_loc_sg['jul_date'], sat_data_loc_sg['BLU'], lw=2, c='blue', label='', linestyle='--')
	plt.plot(sat_data_loc_sg['jul_date'], sat_data_loc_sg['NIR'], lw=2, c='green', label='', linestyle='--')
	plt.plot(sat_data_loc_sg['jul_date'], sat_data_loc_sg['SWR'], lw=2, c='orange', label='', linestyle='--')
	ref_l = 'SWR'
	"""
	plt.plot(sat_data_loc['jul_date'], sat_data_loc[ref_l+'_1'])
	plt.plot(sat_data_loc['jul_date'], sat_data_loc[ref_l+'_2'])
	plt.plot(sat_data_loc['jul_date'], sat_data_loc[ref_l+'_3'])
	plt.plot(sat_data_loc['jul_date'], sat_data_loc[ref_l+'_4'])
	"""
	for mark in marks:
		plt.axvline(x=string_to_jul(mark), c='black', alpha=0.7)
	for mark in marks_hemis:
		plt.axvline(x=string_to_jul(mark), c='black', alpha=0.3, linestyle='--')

	plt.title(loc)
	x_marks = ['2014-01-01', '2014-07-01', '2015-01-01', '2015-07-01', '2016-01-01', '2016-07-01', '2017-01-01']
	x_pos = [string_to_jul(s) for s in x_marks]
	plt.xticks(x_pos, x_marks)
	plt.xlim((2456950, 2457800))
	plt.ylim((0., 0.45))
	plt.legend(loc=2)
        plt.title('Error: '+str(er))
	#plt.show()
	plt.savefig(loc+'_qua-ref_fit_poly08.png', dpi=450)
	plt.close()

data_out = vstack(data_out)
data_out.remove_columns(['Satellite_Date','Altitude','Sat_Date','QUA','QUA_val'])

chdir('..')
data_out.write('hemis_sat_data_Probav_TOC_all_ts_qua-ref_fitpoly08.csv', overwrite=True)


