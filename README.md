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


Today, lighting has become an integral part of city operations, especially for energy conservation ([Dubois et al., 2011](https://www.sciencedirect.com/science/article/pii/S0378778811002933?casa_token=91IH26yCMqQAAAAA:JlWBUqcO775K1m91zBknN_UKtE3K-8RoGtB1I7QZtQ62QdxUMHJ68lrNXe-2_fkh-h9ryjWbkQ), [Montoya et al., 2017](https://www.sciencedirect.com/science/article/pii/S0378778816314967?casa_token=LRgEMMcaLEUAAAAA:pcb7VNp0k7m4qJiNSvEipMCm9IYMbKaQGdfQmG2El-N6tx_qvjz78TnvTuRCh6i80_EDh360dA)) and associated reductions in carbon emissions ([Azevedo et al., 2009](https://ieeexplore.ieee.org/abstract/document/4804756/), [Humphreys, 2008](https://www.cambridge.org/core/journals/mrs-bulletin/article/solidstate-lighting/7FE266662925E382E933DF0616929C77), [Principi and Fioretti, 2014](https://www.sciencedirect.com/science/article/pii/S0959652614007392?casa_token=rs0lkpO2g2AAAAAA:C7IIuJUz25KiAvQw_UFhOVgclnAFtPUuzYza0aq1ufCuA99owofZDoApjbXEepq5KFQRb266ag) ). From 2003 to 2012, electricity consumption for lighting in commercial buildings had decreased from 38% to 17% ([EIA, 2022](https://www.eia.gov/energyexplained/electricity/use-of-electricity.php)), while other categories, such as cooking, heating, and cooling, had continued to increase. Electricity used for lighting has declined over time due to the development of lighting technology that can achieve higher energy efficiency with better lighting quality ([Montoya et al., 2017](https://www.sciencedirect.com/science/article/pii/S0378778816314967?casa_token=LRgEMMcaLEUAAAAA:pcb7VNp0k7m4qJiNSvEipMCm9IYMbKaQGdfQmG2El-N6tx_qvjz78TnvTuRCh6i80_EDh360dA), [Principi and Fioretti, 2014](https://www.sciencedirect.com/science/article/pii/S0959652614007392?casa_token=rs0lkpO2g2AAAAAA:C7IIuJUz25KiAvQw_UFhOVgclnAFtPUuzYza0aq1ufCuA99owofZDoApjbXEepq5KFQRb266ag), [Dupuis & Krames, 2008](https://ieeexplore.ieee.org/abstract/document/4542883), [Quirk, 2009](https://nature.berkeley.edu/classes/es196/projects/2009final/QuirkI_2009.pdf)). Although new lighting technologies have advantages in durability and energy efficiency, the resistance to change imposed by the current technological trajectory slowed the transition ([Lefevre et al, 2006](https://www.oecd.org/env/cc/37671771.pdf), [Menaneau and Lefebvre, 2000](https://www.sciencedirect.com/science/article/pii/S0048733399000384), [Almeida et al., 2013](https://www02.core.ac.uk/download/pdf/38627595.pdf), [Maria et al., 2009](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1467-9485.2009.00506.x), [Khorasanizadeh, 2016](https://www.sciencedirect.com/science/article/pii/S0959652616305340?casa_token=WUi6sf_YJ6wAAAAA:yO-kfIDGQjPgPeVamoBOzPlzTFDVL-sAoUwQYvGyrQcWwGeZXWb8maeEiZyhT7hk6zmvZaC73Q)). As an example, LED sales were only 1% in 2010, and only 7% until 2014 ([IEA, 2021](https://www.iea.org/reports/lighting)).Technological trajectory is defined as a path by which innovation occurred and improved to the highest possible efficiency level ([Sharma and Tripathi, 2017](https://www.sciencedirect.com/topics/social-sciences/technological-trajectory#:~:text=Technological%20trajectories%20can%20be%20defined,and%20economic%20factors%20%5B17%5D.)). And this resistance is caused by the unpredictability of technological evolution and the invasion of the mainstream market. In examining the technological competition between incandescent lamps and CFLs (Compact Fluorescent Lamps), [Menaneau and Lefebvre (2000)](https://www.sciencedirect.com/science/article/pii/S0048733399000384) identified three factors that contributed to this slow development. First of all, new technologies have not benefited from cumulative learning or economies of scale. Also, dominant technologies develop evaluation standards based on their inherent advantages (for example, incandescent lamps are more appealing to customers because they are less expensive). Finally, there is inaction among various stakeholders. Further barriers to the diffusion of CFL technology are identified by [Haworth and Rosenow (2013)](https://www.sciencedirect.com/science/article/pii/S0301421513011907): obtaining information about a new product requires much time and effort, some CFLs are ugly, and so on. 

Researchers believe that public policies, such as tax rebates, subsidization, and phase-out of incandescent light bulbs play a decisive complementary role in overcoming the “lock-in” situation ([Mir et al., 2020](https://www.mdpi.com/1996-1073/13/21/5821), [Afman et al., 2010](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.352.2974&rep=rep1&type=pdf), [Chappin & Afman, 2013](https://www.sciencedirect.com/science/article/pii/S2210422412000706?casa_token=GZpCnwqSjZ4AAAAA:gexHmxn4tTvRfTs3xMFMOQBJ1rtcPX-XagTcEesv1_gsaHoL_98XKkHuv_kX1e6HhbKNy1nwjQ), [Mills and Schleich, 2014](https://www.sciencedirect.com/science/article/pii/S0140988314002047?casa_token=b78n1bEq0q0AAAAA:GGc7mKj_oP6a94XIvW3Nd4mPcA8MIrOLFbxLuBG5TCIx9FyOH3D0AYo3Cl-fubOShASWSuwYDw)). Therefore, as a national leader in using sustainable street lighting, NYC Department of Transportation (DOT) operated the largest municipal street lighting system in the United States and launched LED pilot projects and programs to evaluate LED luminaires’ performance in energy saving and carbon emission reduction ([NYC Department of Transportation, n.d.](https://www1.nyc.gov/html/dot/downloads/pdf/sustainablestreetlighting.pdf)). In 2013, Mayor Michael R. Bloomberg and Transportation Commissioner Janette Sadik-Khan announced that 250,000 high-pressure sodium street lights were planned to be replaced by LEDs by 2017 ([City of New York, 2013](https://www1.nyc.gov/office-of-the-mayor/news/343-13/mayor-bloomberg-transportation-commissioner-sadik-khan-all-250-000-street-lights-in/#/0)). 



In this research, using empirical measurements of lighting technology use via time-dependent images of the Manhattan skyline, we will show the changeover from energy inefficient to energy-efficient lighting and the proliferation of LED.

This repository collects the data analysis pipeline for this project, in the directory pipeline, from data collection, image processing, source selection, to source classification, and the code used to generate the plots in our publications, plus additional material (many many additional figures, simulations, tests).

The steps of the pipeline, and the codes that perform them, are as follow.


The hyperspectral imaging data used in this work was obtained by the “[Urban Observatory](http://MUONetwork.org)” (UO) facility in New York City (NYC). This VNIR instrument observation is located in downtown Brooklyn and faces north. Images below showed the camera and our research area's daytime image. 

![camera_image](https://github.com/gdobler/lighting-tech-changeover/blob/main/images/camera.png)
![daytime_image](https://github.com/gdobler/lighting-tech-changeover/blob/main/images/daytime.png)



Two night-time hyper-spectral images (one from the 2015 and the other from the 2018) of NYC have been used to identify and type lighting technologies. 

The steps of the pipeline, and the codes that perform them, are as follow.

The first step is to process the data. There are two hyperspectral scans that need to be cleaned. HSI0(2015) has a raw image of 4.05GB while HSI1(2018) has an image of 8.07GB. After applying 20 times 3-sigma clipping and a Gaussian filter to both images, the clean image was created. A minimum of xxx GB is needed for cleaning xxx. Below are the cleaned scans of both images.

In the event that you are unable to process it, you can use the cleaned image data: xxx.npy.

As these two scans are taken by different instruments, and the detector in 2018 is able to capture more faint sources than the detector in 2015, there may be a bias in the resultant images. The increased number of "active" pixels in the 2018 scan can be attributed to a more sensitive sensor. To correct this, two steps are taken. Initially, we think that two scans would be aligned and could be compared source by source. We use the Manhattan Bridge as the template, resizing the 2018 scan and then selecting the overlapping area in the 2015 scan. However, from the image below, it is evident that two scans cannot be perfectly aligned. While the left side of the Manhattan Bridge necklace lights have been aligned, the right side and Empire State Building remain misaligned. In addition, determining a single source’s affiliation is difficult as some sources may become inactive or disappear over time.

Although we cannot resolve the mismatch issue, we can still compare the sources and examine the changes in lighting technologies. Therefore, by adding a Gaussian nosie to the 2018 scan, we can correct the sensor sensitivity difference between the two images.

The sensor sensitivity correction code is stored in xxx.npy and the overlapping area in both scans(after sensor sensitivity correction) are stored in: xxx.npy.



Next, we need to manually select the sources and label them with the names of the lighting technologies in each image. We begin by combining the mean brightness and location of each "active" pixel. Next, we plotted the distribution of pixels' average brightnesses and divided it into 10 chunks with intervals of 0.7. We then manually selected, identified, and labeled the "active" pixels in each chunk. Due to the fact that our lighting templates cannot include every lighting technology on the market, and some sources with low signal-to-noise cannot be identified. For these spectra, we add a class called "unknown".

In the end, we ended up with 713 hand-labeled sources in the 2015 scan and 616 sources in the 2018 scan. Labeled sources and its location is stored in xxx.npy.


To identify lighting technologies in each image, we applied web scrapping techniques (using Beautiful Soup) to collect templates from lighting databases (The National Oceanic and Atmospheric Administration (NOAA) and Lamp Spectral Power Distribution Database (LSPDD)). Using auto-correlation, we prune the templates by hand to represent the minimal set required for technology separation, as Dobler et al., (2016) did.

The following are our final 20 templates:


You can now build the model and print the lighting technologies in both scans. The first method we use here is the coefficient method. We calculate the correlation between pixels' spectra in our two scans and all lab measured templates. With the highest correlation among these templates and keeping the sources that are positively correlated with our templates, we will be able to print both images with active pixels accompanied by their associated lighting types.
