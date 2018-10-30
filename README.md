# 2f-binning
Two frequency binning (x,y) part I: linear



Image data analysis for scientific purpose - 
e.g. spectral measurements start with an image (2D array: x,y and counts), 
where usually x is the spectral axis (energy, wavelength etc). 
y is the extended signal and has to be integrated in terms of counts/px ((counts/px) dpx) 
in order to derive a 2D plot. 

Part I: 
CONSTANT BINSIZE - linear scaling in x 
In seldom cases the x-axis scales linearly with the measurand (energy) - but for the start
this little tool was made for this simple case.

The binning includes:
1. integration in y (to 1D, means sums y(x)/ flattens)
2. equidistant (constant) bins x in user defined binsizes (>1, e.g. 10px bin) for which the 
according counts are conserved (sums y(dx))

Procedere:
first open image file (up to 16bit, tiff). 
User entry: define ROI (range of interest) in ymin, ymax, xmin, xmax
sums over y to 1D entry, keeps original image bins (px) in x
change bin range in x by summing depending y-values to each new bin (new bin is >1px !!)


Part II: 
DERIVE CONSTANT BINSIZE for non-linear x-axis scaling
Often the x-Axis (e.g. spectral axis) comes in px but in "real" scales with some other
nonlinear function (e.g. x^2). In order to implement the such a routine, the functional
dependency has to be attributed by rescaling the x-axis. This means x-axis which 
has naturally in the picture i-times constant binsize of 1px now has to become f(x) and 
hence, the y(f(x)) have to be summarized accordingly. Restriction: f(x) > 1px.
