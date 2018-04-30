'''
Created on Apr 29, 2018

@author: Brandon Bevan
'''

import numpy
import matplotlib.pyplot as plt

import imageio

class Fourier2:
    

    def __init__(self, image):
        img = imageio.imread(image)
        self.trans = numpy.fft.fft2(img)
        self.phase = self.trans.imag
        self.freq = self.trans.real
        self.inverse = numpy.fft.ifft2(self.trans)
        
    def viewfft2(self,f):
        fp = numpy.absolute(f)

        # The following two lines are for the sake of Histogram equalization. This is the dirtiest implementation imaginable. 
        # We use the mean as the maximum value since the max of an fft2 is usually an outlier.
        
        if not id(f) == id(self.inverse):
            args = numpy.argmax(fp)
            fp[args]=0
        
        mx = fp.max()
        mn = fp.min()

        fp = numpy.divide(fp, mx)

        # Shift for viewing
        if not id(f) == id(self.inverse):
            fps = numpy.fft.fftshift(fp)
        else:
            fps = fp
            
    
        plt.imshow(fps, vmin=0, vmax=1.0)
    
        plt.show()
        
        
    
    def view(self):
        self.viewfft2(self.trans)
        
        
    def viewinverse(self):
        self.viewfft2(self.inverse)
        
    def viewphase(self):
        self.viewfft2(self.phase)
        
    def viewfrequency(self):
        self.viewfft2(self.freq)
        
        
        
    
        