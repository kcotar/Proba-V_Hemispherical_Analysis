#****************
# Imports
#****************
import os, glob, math
import lai, fapar, fcover
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#import statsmodels.formula.api as sm
#import seaborn as sns
#from scipy.optimize import curve_fit

from datetime import datetime, timedelta
from osgeo import gdal
from scipy.ndimage import morphology


#****************
# Definition of functions
#****************

def get_pixel_location(geo, x, y):
    im_x = long(math.floor((x - geo[0])/geo[1]))
    im_y = long(math.floor((y - geo[3])/geo[5]))
    return (im_x, im_y)


def probav_get_date(str):
    pos = str.find('_100M')
    return datetime.strptime(str[pos-8:pos], '%Y%m%d').date()

def probav_get_images(dir, suffix='p2atm'):
    tifs = glob.glob(dir+'*/*_'+suffix+'.tif')
    dates = [probav_get_date(os.path.basename(tif)) for tif in tifs]
    return pd.DataFrame(tifs, index=dates, columns=['GeoTiff'])

def copernicus_get_date(str):
    str = str.split('_')[3]
    return datetime.strptime(str[0:8], '%Y%m%d').date()

def copernicus_get_products(dir):
    # get lai, fapar and fcover images
    tifs = glob.glob(dir+'*/g2_BIOPAR_LAI_*00.tif')
    dates = [copernicus_get_date(os.path.basename(tif)) for tif in tifs]
    return pd.DataFrame(tifs, index=dates, columns=['GeoTiff'])
    # tifs_lai = glob.glob(dir+'*/g2_BIOPAR_LAI_*00.tif')
    # tifs_fco = glob.glob(dir+'*/g2_BIOPAR_FCOVER_*00.tif')
    # tifs_fap = glob.glob(dir+'*/g2_BIOPAR_FAPAR_*00.tif')
    # if len(tifs_lai) == len(tifs_fco) and len(tifs_fco) == len(tifs_fap):
    #     tifs = zip(tifs_lai, tifs_fco, tifs_fap)
    #     dates = [copernicus_get_date(os.path.basename(tif)) for tif in tifs_lai]
    #     return pd.DataFrame(tifs, index=dates, columns=['lai','fcover','fapar'])

def modis_get_date(str):
    str = str.split('.')[1]
    return datetime.strptime(str[1:8], '%Y%j').date()

def modis_get_products(dir):
    # get lai and fapar images
    tifs = glob.glob(dir+'*/MOD*_lai.tif')
    dates = [modis_get_date(os.path.basename(tif)) for tif in tifs]
    return pd.DataFrame(tifs, index=dates, columns=['GeoTiff'])

def get_veg_bands_numbers(sensor):
    # band numbers to be used, starts with 1
    if sensor == 'Proba-V':
        return (1, 2, 3, 4)
    if sensor == 'Sentinel-2':
        return (1, 3, 7, 10)
    if sensor == 'Landsat-8':
        return (2, 4, 5, 8)

def get_indices(path, coord_x, coord_y, sensor='Proba-V'):
    # get available quality mask
    path_mask = path[0:-4]
    atcor_mask = False
    if os.path.exists(path_mask+'_mask.tif'):
        path_mask += '_mask.tif'
        atcor_mask = True
    else:
        path_mask = path_mask[0:path_mask.find('__')] + '_q.tif'
    ref_img = gdal.Open(path)
    mask_img = gdal.Open(path_mask)
    blu_b, red_b, nir_b, swr_b = get_veg_bands_numbers(sensor)
    geoinfo = ref_img.GetGeoTransform()
    img_x, img_y = get_pixel_location(geoinfo, coord_x, coord_y)
    # read quality mask
    qua = np.array(mask_img.GetRasterBand(1).ReadAsArray())
    # select quality threshold
    # select appropriate quality mask reading procedure
    if atcor_mask:
        qua_ok = qua > 33  # exclude cloud, snow and cirrus pixels (hazy pixels are included - 34)
        #qua_ok = qua > 50  # also excludes water/shadow pixels
    else:
        # useful only for original Proba-V mask
        cloud_snow_shadow = np.logical_or(np.logical_or(np.bitwise_and(qua, 1),
                                                        np.bitwise_and(qua, 3)),
                                          np.bitwise_and(qua, 4))
        ok_pixels = np.logical_and(np.logical_and(np.bitwise_and(qua, 128),
                                                  np.bitwise_and(qua, 64)),
                                   np.logical_and(np.bitwise_and(qua, 32),
                                                  np.bitwise_and(qua, 16)))
        qua_ok = np.logical_and(ok_pixels == 1, cloud_snow_shadow == 0)
    # erode binary quality mask
    print qua[img_y, img_x], qua_ok[img_y, img_x]
    qua_ok = morphology.binary_erosion(qua_ok, structure=np.ones((5,5)), iterations=1, border_value=0)
    print qua[img_y, img_x], qua_ok[img_y, img_x]
    if qua_ok[img_y,img_x] or filter_bad_obs == False:
        # read individual colour bands
        blu = np.array(ref_img.GetRasterBand(blu_b).ReadAsArray(img_x, img_y, 1, 1))
        red = np.array(ref_img.GetRasterBand(red_b).ReadAsArray(img_x, img_y, 1, 1))
        nir = np.array(ref_img.GetRasterBand(nir_b).ReadAsArray(img_x, img_y, 1, 1))
        swr = np.array(ref_img.GetRasterBand(swr_b).ReadAsArray(img_x, img_y, 1, 1))
        # get indices for observed pixel
        return compute_indices(blu[0], red[0], nir[0], swr[0])
    else:
        # bad pixel
        return pd.DataFrame()

def get_reflectance(path, coord_x, coord_y, sensor='Proba-V'):
    # get available quality mask
    path_mask = path[0:-4]
    atcor_mask = False
    if os.path.exists(path_mask+'_mask.tif'):
        path_mask += '_mask.tif'
        atcor_mask = True
    else:
        path_mask = path_mask[0:path_mask.find('__')] + '_q.tif'
    ref_img = gdal.Open(path)
    mask_img = gdal.Open(path_mask)
    blu_b, red_b, nir_b, swr_b = get_veg_bands_numbers(sensor)

    geoinfo = ref_img.GetGeoTransform()
    img_x, img_y = get_pixel_location(geoinfo, coord_x, coord_y)
    # read quality mask
    qua = np.array(mask_img.GetRasterBand(1).ReadAsArray())
    # select quality threshold
    # select appropriate quality mask reading procedure
    if atcor_mask:
        qua_ok = qua > 33  # exclude cloud, snow and cirrus pixels (hazy pixels are included - 34)
        #qua_ok = qua > 50  # also excludes water/shadow pixels
    else:
        # useful only for original Proba-V mask
        cloud_snow_shadow = np.logical_or(np.logical_or(np.bitwise_and(qua, 1),
                                                        np.bitwise_and(qua, 3)),
                                          np.bitwise_and(qua, 4))
        ok_pixels = np.logical_and(np.logical_and(np.bitwise_and(qua, 128),
                                                  np.bitwise_and(qua, 64)),
                                   np.logical_and(np.bitwise_and(qua, 32),
                                                  np.bitwise_and(qua, 16)))
        qua_ok = np.logical_and(ok_pixels == 1, cloud_snow_shadow == 0)
    # erode binary quality mask
    print qua[img_y, img_x], qua_ok[img_y, img_x]
    qua_ok = morphology.binary_erosion(qua_ok, structure=np.ones((5,5)), iterations=1, border_value=0)
    
    out_df = pd.DataFrame()
    out_df['QUA'] = qua_ok[img_y,img_x]
    out_df['QUA_val'] = qua[img_y,img_x]
    out_df['BLU'] = np.array(ref_img.GetRasterBand(blu_b).ReadAsArray(img_x, img_y, 1, 1))
    out_df['RED'] = np.array(ref_img.GetRasterBand(red_b).ReadAsArray(img_x, img_y, 1, 1))
    out_df['NIR'] = np.array(ref_img.GetRasterBand(nir_b).ReadAsArray(img_x, img_y, 1, 1))
    out_df['SWR'] = np.array(ref_img.GetRasterBand(swr_b).ReadAsArray(img_x, img_y, 1, 1))
    return out_df


def compute_indices(blu, red, nir, swr):
    out_df = pd.DataFrame()
    out_df['NDVI'] = (nir - red) / (nir + red)
    out_df['NDWI'] = (swr - nir) / (swr + nir)
    l_savi = 0.5
    out_df['SAVI'] = (nir - red)/(nir + red + l_savi)*(1. + l_savi)
    out_df['MSAVI'] = (2.*nir + 1.- math.sqrt((2.*nir + 1.)**2. - 8.*(nir - red)))/2.0
    g_evi = 2.5; c1_evi = 6.0; c2_evi = 7.5; l_evi = 1.0
    out_df['EVI'] = g_evi*(nir - red)/(nir + c1_evi*red - c2_evi*blu + l_evi)
    out_df['LAI'] = lai.lai_regression_tree(red, nir, swr)
    out_df['FAPAR'] = fapar.fapar_regression_tree(red, nir, swr)
    out_df['FCOVER'] = fcover.fcover_regression_tree(red, nir, swr)
    # additional quick check for bad (cloud/snow/water/problematic etc.) pixel
    if out_df['NDVI'][0] > 0 and out_df['FAPAR'][0] > 0 and out_df['FCOVER'][0] > 0 and out_df['LAI'][0] > 0:
        return out_df
    else:
        if store_bad_indices:
            return df_out
        else:
            print '   Problematic pixel and indices values, discarding results'
            return pd.DataFrame()
    # Do not perform any value filtering as it can be done later in data processing steps
    return out_df

def get_copernicus_values(path, coord_x, coord_y):
    path_mask = path.replace('00.tif', '00_q.tif')
    lai_img = gdal.Open(path)
    fap_img = gdal.Open(path.replace('g2_BIOPAR_LAI_', 'g2_BIOPAR_FAPAR_'))
    fco_img = gdal.Open(path.replace('g2_BIOPAR_LAI_', 'g2_BIOPAR_FCOVER_'))
    mask_img = gdal.Open(path_mask)
    geoinfo = lai_img.GetGeoTransform()
    img_x, img_y = get_pixel_location(geoinfo, coord_x, coord_y)
    # read quality mask
    qua = np.array(mask_img.GetRasterBand(1).ReadAsArray())
    # select quality threshold and erode binary quality mask
    qua_ok = qua < 32
    #qua_ok = morphology.binary_erosion(qua < 32, structure=np.ones((3,3)), iterations=1, border_value=0)
    if qua_ok[img_y,img_x] or filter_bad_obs == False:
        out_df = pd.DataFrame()
        # read individual biophysical product
        out_df['LAI'] = np.array(lai_img.GetRasterBand(1).ReadAsArray(img_x, img_y, 1, 1))[0]
        out_df['FAPAR'] = np.array(fap_img.GetRasterBand(1).ReadAsArray(img_x, img_y, 1, 1))[0]
        out_df['FCOVER'] = np.array(fco_img.GetRasterBand(1).ReadAsArray(img_x, img_y, 1, 1))[0]
        return out_df
    else:
        # bad pixel
        return pd.DataFrame()

def get_modis_values(path, coord_x, coord_y):
    path_mask = path.replace('_lai.tif', '_q.tif')
    lai_img = gdal.Open(path)
    fap_img = gdal.Open(path.replace('_lai.tif', '_fapar.tif'))
    mask_img = gdal.Open(path_mask)
    geoinfo = lai_img.GetGeoTransform()
    img_x, img_y = get_pixel_location(geoinfo, coord_x, coord_y)
    # read quality mask
    qua = np.array(mask_img.GetRasterBand(1).ReadAsArray())
    # select quality threshold and erode binary quality mask
    qua_ok = np.logical_or(np.logical_and(np.logical_or(np.bitwise_and(qua, 8),
                                                        np.bitwise_and(qua, 16)),
                                          np.bitwise_and(qua, 24)),
                           np.bitwise_and(qua, 96))
    qua_ok = (qua_ok == 0)
    # qua_ok = morphology.binary_erosion(qua_ok, structure=np.ones((3,3)), iterations=1, border_value=0)
    if qua_ok[img_y,img_x] or filter_bad_obs == False:
        out_df = pd.DataFrame()
        # read individual biophysical product
        out_df['LAI'] = np.array(lai_img.GetRasterBand(1).ReadAsArray(img_x, img_y, 1, 1))[0]
        out_df['FAPAR'] = np.array(fap_img.GetRasterBand(1).ReadAsArray(img_x, img_y, 1, 1))[0]
        # additional quick check for bad (snow, urban, water... pixels) pixel
        if out_df['LAI'][0] < 10:
            return out_df
        else:
            return pd.DataFrame()
    else:
        # bad pixel
        return pd.DataFrame()


#************************************************
#****************  MAIN PROGRAM  ****************
#************************************************

#****************
# Predefined variables
#****************

# input directories for satellite imagery
satimg_toc_root = '//172.16.10.111/copernicus/PROBA-V_slo_z_okolico/L3_100m_TOC_C1/'
satimg_atcor_root = 'D:/Probav_popravljeni_atm/'
satimg_atcor_topo_root = 'P:/Tatjana_PROBA-V/popravljeni_atm_topo/'

# output directory
out_dir = 'd:/Klemen_podatki_koda/hemisferna/'

if not(os.path.isdir(out_dir)):
    os.mkdir(out_dir)

if not(os.path.isdir(out_dir_fit)):
    os.mkdir(out_dir_fit)

# predefined settings for observation stands
locations = pd.DataFrame(index=['Symbol', 'Y_coord', 'X_coord', 'Altitude'])
locations['Malic'] = ['MA', 46.182777, 15.199722, 850]
locations['Cigonca'] = ['CI', 46.364998, 15.580556, 250]
locations['Trnovo'] = ['TR', 45.994167, 13.760278, 812]
locations['Ovcarija'] = ['OV', 46.483055, 15.256111, 1200]

sat_imgs = probav_get_images(satimg_toc_root, suffix='ref')
suffix = '_Probav_TOC'
sensor_type = 'Proba-V'
data_out_csv = out_dir+'_hemis_sat_data'+suffix+'_all.txt'

dframes_to_merge = []
    for place_name in locations.columns.values:
        print place_name
	for sat_path in sat_imgs['GeoTiff']:
            print sat_path
            sat_ref = get_reflectance(sat_path, locations[place_name]['X_coord'], locations[place_name]['Y_coord'], sensor_type)
            # add additional information to the data frame
            sat_ref['Satellite_Date'] = sat_imgs[sat_imgs['GeoTiff']==sat_path].index.values[0]
            sat_ref['Location'] = place_name
            sat_ref['Altitude'] = locations[place_name]['Altitude']
            # merge satellite derived indices with ground hemispherical measurements
            dframes_to_merge.append(sat_ref.reset_index(drop=True))

#merge all observations together
hemis_sat_ref_all = pd.concat(dframes_to_merge, ignore_index=True)
# print hemis_sat_all
hemis_sat_ref_all.to_csv(data_out_csv, sep=',', decimal='.', index=False, float_format='%.4f',
                                       na_rep='NaN', encoding='utf-8')
            
