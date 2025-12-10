# Hyperspectral Observations of Lighting Technology Changeover

**Project Team:** Lan Yu [1, 4], ∗, Mary Manz, Mohit S. Sharma [2], Andreas Karpf [2], Federica B. Bianco [1,2,3,4], and Gregory Dobler [1,2,3,4]


<i>
  <small>[1] - Biden School of Public Policy and Administration, University of Delaware, Newark DE, 19716, USA </small>
<br>
  <small>[2] - Center for Urban Science and Progress, New York University, New York City NY, 10003, USA </small>
<br>
  <small>[3] - Department of Physics and Astronomy, University of Delaware, Newark DE, 19716, USA </small>
<br>
  <small>[4] - Data Science Institute, University of Delaware, Newark DE, 19716, USA7 </small>
</i>

---

PROJECT DESCRIPTION.

This repository collects the pipeline and selected outputs from our research on the proliferation of LEDs in response to the 2013 NYC lighting retrofit policy.

The CNN_Training_Data folder contains the manually labeled spectra and lighting types used for the 1D CNN training. 
In this folder, the 2013 spectra (with 872 wavelength) were interpolated to match the 848 wavelength channels of the 2018 spectra.
After interpolation across the target wavelength grid, the resulting 2013 spectra dataset has a shape of 713 × 848, while the 2018 spectra dataset have a shape of 616 × 848.
