'''
Created on Apr 29, 2018

@author: Brandon Bevan
'''

import numpy
import matplotlib.pyplot as plt

import imageio

class Fourier2:
    

    def __init__(self, image):
        self.img = imageio.imread(image)
        self.trans = numpy.fft.fft2(self.img)
        self.phase = self.trans.imag
        self.freq = self.trans.real
        self.inverse = numpy.fft.ifft2(self.trans)
        
    def viewfft2(self):
        fp = abs(self.trans)

        # The following two lines are for the sake of Histogram equalization. This is the dirtiest implementation imaginable. 
        # We use the mean as the maximum value since the max of an fft2 is usually an outlier.
        mx = fp.max()
        mn = fp.min()

        fp = numpy.divide(fp, mx)

        # Shift for viewing
        fps = numpy.fft.fftshift(fp)
    
        plt.imshow(fps, vmin=mn, vmax=mx)
    
        plt.show()
        
   
    def viewifft2(self):
        fp = abs(self.inverse)

        # The following two lines are for the sake of Histogram equalization. This is the dirtiest implementation imaginable. 
        # We use the mean as the maximum value since the max of an fft2 is usually an outlier.
        mx = fp.mean()
        mn = fp.min()

        #fp = numpy.divide(fp, mx)
        
        fps = fp
    
        plt.imshow(fps, vmin=0.0, vmax=1.0)
    
        plt.show()
        
        
        
    
        