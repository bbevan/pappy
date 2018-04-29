# pappy
Pappy's Wonderful FFT2 Library, Built On Numpy!

The idea is to build a class blueprinting an FFT2 object.

What can pappy help with?

#Depends on numpy for numpy.fft.fft2 and a numpy array

x = pappy()

x.phase()           #returns the phase array (all arrays are numpy arrays)

x.frequency()        #returns the frequency array

x.show()            #show us a nice, centered FFT2

x.show(hist="eq")   #show us the histogram equalized version

x.show(hist="norm") #we want just a totally normalized array shown

x.show(phase="separate")  #separate the phase from the frequency and display both

x.write()           #save the FFT2 to png

All of this at least. 
