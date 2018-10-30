# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 22:45:26 2016

@author: LAPTOP
"""

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from PIL import Image
import numpy as np

progname = '<< reads 16bit.tif picture as an array (intel bite order), integrates in ROI(y) and changes constant binnsizes in x (>1!!!)'

version = '0.0.1.......................... by Zombie.SoC+++ similarities +++ 2016'






class DATA:
    def __init__(self,filename,liste):
        
        self.filename = filename     
        
        self.liste=liste
        
        self.X0=liste[3]
        
        self.XM=liste[2]
        
        self.Y1=liste[1]
        
        self.Y2=liste[0]
        
        self.binrange=liste[4]
        
        self.matrix=[]
        
        self.DIMX=self.X0-self.XM
        
        self.DIMY=self.Y2-self.Y1
        
        self.small=[]
        
        self.binnedy =[]

                
        
    def openImage(self):
            
        image = Image.open(self.filename)
            
            #makes np.matrix from image file *thats so easy :D*
        self.matrix1 = np.array(image)
            
        image.close()
            
        self.matrix=self.matrix1
            
        self.plot = plt.imshow(self.matrix)
            
        print 'loaded array has the following dimensions:'
            
        print 'y', self.matrix.shape
            
        return self.matrix
        
        
        
    def ROI(self):
            
            #plots picture and ROI
            
        ax = plt.gca()
            
        r = plt.Rectangle((self.XM, self.Y1), self.X0-self.XM, self.Y2-self.Y1,fill=False )
            
        plt.setp(r, linewidth=2, color='w')
            
        ax.add_artist(r)
            
        plt.show()
            
            
            #creates new array of ROI
        small2=self.matrix[self.Y1:self.Y2,self.XM:self.X0]
            
            #before sum has to be converted to float (integers of whatever bit
            # introduce a strange limitation of maximum value, 32bit is not enough)
            
        img = np.array(small2, dtype=np.float)
            #print small2.shape, 'shape of subarray dy mal dx'
            
            
        self.small=img
            
        return self.small
        
        
            
    def test_32bit(self):
        
        maximum_count = np.amax(self.binnedy)
            
        if maximum_count < 2**32:
                
            print 'test for 32bit overload:  2**32 -maximumcount > = 0'
                
            print 2**32-maximum_count, 'max count'
            
            print "test passed"
                
                
        else: 
                
            print "over 32 bit maximum"           

            
            
    def BIN(self):
            
            #integration/summs subarray in y
        flat=self.small.sum(axis=0)
            
        bincount=self.DIMX/self.binrange
        
        print 'number  of bins',bincount
            
            
            
            #evaluates rest
        rest=self.DIMX-(bincount*self.binrange)
        
        print 'loss of bins at right side:', rest
            
            # deletes rest from matrix at first entries
            
        iterable =(x+1 for x in range (rest))
            
        reste=np.fromiter(iterable,np.uint32)
            
        flatshort=np.delete(flat,(self.DIMX-reste),0)
            
            
           # print "now subarray ready for reshaping"
                        
        binns=flatshort.reshape(bincount,self.binrange)
            
        self.binnedy=binns.sum(axis=1)
        

            # creates x array in respect to binrange (was used for indexing)

        interable =(x+1 for x in range (bincount))
            
        binnedx=np.fromiter(interable,np.float)
            
        xarr=binnedx*self.binrange+(self.XM-self.binrange/2)
       
        scaley=self.binnedy
            
        plt.plot(xarr, scaley, 'b')
            
        plt.plot(xarr, scaley, linewidth=2.0)

        plt.show()
        
    
        return self.binnedy
            

        


        #initialises object openImage,ROI,BIN
        #self.xy defined things can only be called, if in constructor
        # and later overwritten !!! not good 


    
def INPUT():
    
    print("define ROI in Y,X:")
    
    Ymin= input("Ymin:") 
    
    Ymax= input("Ymax:") 
    
    Xmin=input("Xmin:")
    
    Xmax=input("Xmax:")
    
    binrange=input("binrange x (in px):")
    
    liste=(Ymax,Ymin,Xmin,Xmax,binrange)
    
    return liste
        

# initialises classDATA
liste=INPUT()

print "input parameter", liste

execute_it = DATA('test.tif', liste)
execute_it.openImage()
execute_it.ROI()
execute_it.BIN()
execute_it.test_32bit()

