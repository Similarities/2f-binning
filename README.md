# 2f-binning
Two frequency binning (x,y) part I: linear



Image data analysis for scientific purpose - e.g. spectral measurements start with an image (3D: x,y and counts), where usually x is the
spectral axis (energy, wavelength etc). y is the extended signal and has to be integrated in terms of counts/px ((counts/px) dpx) 
in order to derive a 2D plot. 
In seldom cases the x-axis scales linearly with the measurand (energy). 
Binning includes integration in y (to 1D) and gives in x aequidistant bins with >1px (e.g. 10px).
