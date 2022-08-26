#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

def read_header(hdrfile):
    """
    Read a Middleton header file.
    """

    # -- alert
    print("reading and parsing {0}...".format(os.path.split(hdrfile)[-1]))

    # -- open the file and read in the records
    recs = [rec for rec in open(hdrfile)]

    # -- parse for samples, lines, bands, and the start of the wavelengths
    for irec, rec in enumerate(recs):
        if 'samples' in rec:
            samples = int(rec.split("=")[1])
        elif 'lines' in rec:
            lines = int(rec.split("=")[1])
        elif 'bands' in rec:
            bands = int(rec.split("=")[1])
        elif "Wavelength" in rec:
            w0ind = irec+1

    # -- parse for the wavelengths
    waves = np.array([float(rec.split(",")[0]) for rec in 
                      recs[w0ind:w0ind+bands]])

    # -- return a dictionary
    return {"nrow":samples, "ncol":lines, "nwav":bands, "waves":waves}


def read_raw(rawfile, shape, dtype=np.uint16):
    """
    Read a Middleton raw file.
    """

    # -- alert
    print("reading {0}...".format(os.path.split(rawfile)[-1]))

    return np.fromfile(open(rawfile),dtype) \
        .reshape(shape[2],shape[0],shape[1])[:,:,::-1] \
        .transpose(1,2,0)


def read_hyper(fpath, fname=None, full=True):
    """
    Read a full hyperspectral scan.
    """

    # -- set up the file names
    if fname is not None:
        fpath = os.path.join(fpath,fname)

    # -- read the header
    hdr = read_header(fpath.replace("raw","hdr"))
    sh  = (hdr["nwav"],hdr["nrow"],hdr["ncol"])

    # -- if desired, only output data cube
    if not full:
        return read_raw(fpath,sh)

    # -- output full structure
    class output():
        def __init__(self,fpath):
            self.filname = fpath
            self.data    = read_raw(fpath,sh)
            self.waves   = hdr["waves"]
            self.nwav    = sh[0]
            self.nrow    = sh[1]
            self.ncol    = sh[2]

    return output(fpath)


def read_clean(fpath, fname=None, shape=None):
    """
    Read a cleaned hyperspectral scan.
    """

    # -- set up the file names
    if fname is not None:

        fpath = os.path.join(fpath,fname)

    # -- alert
    print("reading {0}...".format(os.path.split(fpath)[-1]))

    # -- read and return
    if shape is None:
        return np.fromfile(fpath,dtype=float)
    else:
        return np.fromfile(fpath,dtype=float).reshape(shape)



def sig_clipping_row(arr):

  """ 10 times 3 sig clipping across the row
  It performs 3sig clipping by calculating the median along each row (1-times), 
  and subtracts the final median value of each row.
  Return a masked array 
  
  arr: three dimensional array, first dimension is the channel """
  arr = np.ma.array(arr)

  loop_time = 0

  while loop_time < 10:

    # -- calculate the median value across the row
    med = np.ma.median(arr, axis=0,  keepdims=True)

    # -- calculate the sig across the row
    sig = arr.std(axis=0,  keepdims=True)

    # -- mask this array if it is larger than med + 3sig or smaller than med-3sig    
    arr.mask = (arr > med+3*sig)|(arr < med-3*sig)
	

    loop_time = loop_time +1

    # -- subtract the resultant median value after 10 times 3sig clipping
    if loop_time == 10:

        final = (arr.data - np.ma.median(arr, axis=0,  keepdims=True))

  return final.data





  # -- function to remove noise
def sig_clipping_col(arr):

  """ 10 times 3 sig clipping across the col
  It performs 3sig clipping by calculating the median along each col (1-times), 
  and subtracts the final median value of each col.
  Return a masked array 
  
  arr: three dimensional array, first dimension is the channel """
  arr = np.ma.array(arr)

  loop_time = 0

  while loop_time < 10:

    # -- calculate the median value across the col
    med = np.ma.median(arr, axis=1,  keepdims=True)

    # -- calculate the sig across the col
    sig = arr.std(axis=1,  keepdims=True)

    # -- mask this array if it is larger than med + 3sig or smaller than med-3sig
    arr.mask = (arr > med+3*sig)|(arr < med-3*sig)
	

    loop_time = loop_time +1

    # -- subtract the resultant median value after 10 times 3sig clipping
    if loop_time == 10:

        final = (arr.data - np.ma.median(arr, axis=1,  keepdims=True))

  return final.data
