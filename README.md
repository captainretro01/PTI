# PTI
Plaintext Image format tools
This is the software for the creation and viewing of Plaintext Images (.pti) and
Colour Plaintext Images (.cpti).

Requires Python 3.11+ with Matplotlib and Numpy

img2pti.py takes a 1-bit Bitmap Image (.bmp) and uses it to create 1-bit Plaintext 
images.

ptiread.py takes a 1-bit Plaintext image and outputs the image in text characters 
to the terminal

ptiread2.py takes a 1-bit Plaintext image and uses matplotlib to render the image. 

img2cpti.py takes a colour Bitmap Image and uses it to create a Colour Plaintext 
image.

cptiread.py takes a Colour Plaintext image and uses matplotlib to render it.

OPERATIONS:

  All programs need to be run to select files (Cannot drag and drop or use arguments 
  in command line)
  
  For img2pti the Bitmaps must be 1-bit Black&White (Not grayscale)
  
  ptiread outputs to terminal and therefore you may need to change your terminal 
  settings so the font is smaller and so thet the font is black and the background 
  is white so the image is not inverted.
  
  ptiread2 uses matplotlib so you will be prompted to enter the pixel size, usually 
  - depending on the image size - between 0.1 and 0.5 are fine. Feel free to 
  experiment and provide feed back about what pixel sizes work with what resolutions.
  Also the image may be deformed, especially if you maximise the matplotlib window, 
  but you can fiddle with the zoom and pan tools to get the best looking image.
  
  img2cpti can be quite slow (especially with large images) and due to some measures 
  built in to prevent fatal errors sometimes there may be colour distortion.
  
  cptiread can also be very slow and also requires you to set the pixel size.
