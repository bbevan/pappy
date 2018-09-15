# pappy
Pappy's Wonderful FFT2 Library, Built On Numpy!

The idea is to build a class blueprinting an FFT2 object.

What can pappy help with? Pappy contains a class called Fourier2 , which stores the 2D FFT and inverse 2D FFT of an image. Pappy helps you visualize things to the best of its ability, knowing the struggle from a teenee bit of experience.

```
from Fourier2 import Fourier2 as pappy
fourier = pappy("image.png")
```
Then you can do a number of things.

```
fourier.viewfrequency() #display the frequency information from "image.png"
fourier.viewphase()     #display the phase information from "image.png"
```

as well as a few other things that Pappy wants to help with in the future. Pappy depends on Numpy for smooth sailing. Free as in beer.

Enjoy

-Brandon
