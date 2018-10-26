# 2f-binning
Two frequency binning (x,y) part I: linear



Image data analysis for scientific purpose - e.g. spectral measurements start with an image (3D: x,y and counts), where usually x is the
spectral axis (energy, wavelength etc). y is the extended signal and has to be integrated in terms of counts/px ((counts/px) dpx) 
in order to derive a 2D plot. 
In seldom cases the x-axis scales linearly with the measurand (energy). 
Binning includes integration in y (to 1D) and gives in x aequidistant bins with >1px (e.g. 10px).

Procedere:
first open image file (up to 16bit, tiff). 
define ROI (range of interest). 
sums over y to 1D entry, keeps original image bins (px) in x
change bin range in x by summing depending y-values to each new bin (new bin is >1px !!)
