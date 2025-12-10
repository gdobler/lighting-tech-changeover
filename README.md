# Hyperspectral Observations of Lighting Technology Changeover

**Project Team:** Lan Yu [1], Federica B Bianco [1,2], Andreas Karpf [2], Mohit S Sharma [2], Gregory Dobler [1,2]

<i>
  <small>[1] - University of Delaware</small>
<br>
  <small>[2] - Center for Urban Science and Progress (New York University)</small>
</i>

---

PROJECT DESCRIPTION.

This respository collects the pipeline and some output from our research on the proliferation of LEDs in response to 2017 NYC retrofitted policy. 

The CNN_Training_Data folder contains the manually labeled spectra and lighting types used for the 1D CNN training. 
In this folder, the 2013 spectra (with 872 wavelength) were interpolated to match the 848 wavelength channels of the 2018 spectra.
After interpolation across the target wavelength grid, the resulting 2013 spectra dataset has a shape of 713 × 848, while the 2018 spectra dataset have a shape of 616 × 848.
