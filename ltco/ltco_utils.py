#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
from hyss_util import *


def read_scan(year):
    """
    Load in one of the hyperspectral scans
    """

    # -- set the file name
    if str(year) == "2013":
        fname = os.path.join(os.environ["LTCO_HSI0"],
                             "full frame 20ms faster_VNIR.raw")
    elif str(year) == "2018":
        fname = os.path.join(os.environ["LTCO_HSI1"], "night_00000.raw")

    # -- read hyperspectral cube
    return read_hyper(fname)



def get_source_locations(year):
    """
    Read the locations of the active pixels.
    """

    # -- set the filename
    if str(year) == "2013":
        fname = "../output/hsi0_overlap_location_bridge.npy"

    elif str(year) == "2018":
        fname = "../output/hsi1_overlap_location_bridge.npy"

    # -- load source locations
    return np.load(fname)



def get_wavelengths(year):
    """
    Read the wavelengths.
    """

    # -- load the scan and return the wavelengths
    return read_scan(year).waves



def load_cleaned_cube(year):
    """
    Read the full cleaned data cube.
    """
    
    # -- set names
    hname = "hsi0" if str(year) == "2013" else "hsi1" if \
        str(year) == "2018" else "ERROR"
    uname = "../output/filtered_{0}_half0.npy".format(hname)
    lname = "../output/filtered_{0}_half1.npy".format(hname)

    return np.hstack([np.load(uname), np.load(lname)])



def get_sensor_correction_params(imgL13, imgL18, default=True):
    """
    Determine the scaling and noise parameters to correct 2018 scan 
    **USING ALIGNED IMAGES**.
    """

    # -- if using the default overwrite inputs
    if default:
        imgL13 = align_image(get_luminosity_image(2013), 2013)
        imgL18 = align_image(get_luminosity_image(2018), 2018)
    
    # -- define the region for calculating linear scaling model
    pat_rr = [420, 465]
    pat_cc = [150, 200]

    # -- extract the patches
    patch13 = imgL13[pat_rr[0]:pat_rr[1], pat_cc[0]:pat_cc[1]]
    patch18 = imgL18[pat_rr[0]:pat_rr[1], pat_cc[0]:pat_cc[1]]

    # -- calculate the slope and offset for sensor sensitivity correction (clip to remove outliers)
    clp = (-5, 5)
    amp, off = np.polyfit(patch18.flatten().clip(-5, 5), patch13.flatten().clip(clp[0], clp[1]), 1)

    # -- noise amplitude roughly determined by clipping values to < 1 and comparing std dev
    sig = 0.21
    
    return amp, off, sig



def correct_luminosity_image(img, amp, off, sig, seed=302):
    """
    Create corrected image.
    """
    
    # -- get rows and columns
    nrow, ncol = img.shape[:2]
    
    # -- create a noise realization
    np.random.seed(seed)
    noise = np.random.randn(nrow, ncol) * sig

    # -- create scaled image and final, noisy image
    return img * amp + off + noise



def get_luminosity_image(year):
    """
    Load a luminosity image.
    """

    # -- set the filename
    if str(year) == "2013":
        hname = "hsi0"

    elif str(year) == "2018":
        hname = "hsi1"

    fname = "../output/{0}_filter_mean.npy".format(hname)
    
    # -- get mean brightness images and save them if necessary
    if os.path.isfile(fname):
        print("Loading {0}".format(fname))

        return np.load(fname)

    else:
        print("{0} not found!  creating and writing...".format(fname))
        print("NOT IMPLEMENTED")
        
        return None



def align_image(img, year):
    """
    Align the images.
    """
    
    # -- set the method
    if str(year) == "2013":
        return img[238:933, 0:1087]

    elif str(year) == "2018":
        return (resize(img.astype(float), (695, 1252)))[:, 165:1252]
