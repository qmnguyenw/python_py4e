Converting an image to ASCII image in Python



 **Introduction to ASCII art**

* * *

ASCII art is a graphic design technique that uses computers for presentation
and consists of pictures pieced together from the 95 printable (from a total
of 128) characters defined by the ASCII Standard from 1963 and ASCII compliant
character sets with proprietary extended characters (beyond the 128 characters
of standard 7-bit ASCII). The term is also loosely used to refer to text based
visual art in general. ASCII art can be created with any text editor, and is
often used with free-form languages. Most examples of ASCII art require a
fixed-width font (non-proportional fonts, as on a traditional typewriter) such
as Courier for presentation. Among the oldest known examples of ASCII art are
the creations by computer-art pioneer Kenneth Knowlton from around 1966, who
was working for Bell Labs at the time. “Studies in Perception I” by Ken
Knowlton and Leon Harmon from 1966 shows some examples of their early ASCII
art. ASCII art was invented, in large part, because early printers often
lacked graphics ability and thus characters were used in place of graphic
marks. Also, to mark divisions between different print jobs from different
users, bulk printers often used ASCII art to print large banners, making the
division easier to spot so that the results could be more easily separated by
a computer operator or clerk. ASCII art was also used in early e-mail when
images could not be embedded. You can find more about them. [Source : Wiki.

 **How it works:**

* * *

here are the steps the program takes to generate the ASCII  
image:

  * Convert the input image to grayscale.
  * Split the image into M×N tiles.
  * Correct M (the number of rows) to match the image and font aspect ratio.
  * Compute the average brightness for each image tile and then look up a suitable ASCII character for each.
  * Assemble rows of ASCII character strings and print them to a fle to form the fnal image.

 **Requirements**

  

  

* * *

You will do this program in python and we will use Pillow which is Python
Imaging Library for read in the images, access their underlying data, and
create and modify them and also the scientific module Numpy to compute
averages.

 **The Code**

* * *

You’ll begin by defining the grayscale levels used to generate the ASCII art.
Then you’ll look at how the image is split into tiles and how average
brightness is computed for those tiles. Next, you’ll work on replacing the
tiles with ASCII characters to generate the final output. Finally, you’ll set
up command line parsing for the program to allow a user to specify the output
size, output filename, and so on.

 **Defining the Grayscale Levels and Grid**

As the frst step in creating your program, defne the two grayscale levels used
to convert brightness values to ASCII characters as global values.

    
    
    >>>gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^". "    #70 levels of gray
    >>>gscale2 = "@%#*+=-:. "         #10 levels of gray
    

The value gscale1 at u is the 70-level grayscale ramp, and gscale2 at v is the
simpler 10-level grayscale ramp. Both of these values are stored as strings,
with a range of characters that progress from darkest to lightest.

Now that you have your grayscale ramps, you can set up the image. The
following code opens the image and splits it into a grid:

    
    
        # open image and convert to grayscale
    >>>    image = Image.open(fileName).convert('L')
        # store dimensions
    >>>    W, H = image.size[0], image.size[1]
        # compute width of tile
    >>>    w = W/cols
        # compute tile height based on aspect ratio and scale
    >>>    h = w/scale
        # compute number of rows
    >>>    rows = int(H/h)
    

**Computing the average brightness**  
Next, you compute the average brightness for a tile in the grayscale image.
The function getAverageL() does the job.

  

  

    
    
    #Given PIL Image, return average value of grayscale value
    >>>def getAverageL(image):
        # get image as numpy array
    ...    im = np.array(image)
        # get shape
    ...    w,h = im.shape
        # get average
    ...    return np.average(im.reshape(w*h))
    

First, the image tile is passed in as a PIL Image object. Convert image into a
numpy array at second step, at which point ‘im’ becomes a two-dimensional
array of brightness for each pixel. At third step , you store the dimensions
(width and height) of the image. At fourth step, numpy.average() computes the
average of the brightness values in the image by using numpy.reshape() to frst
convert the two-dimensional array of the dimensions width and height (w,h)
into a ?at one-dimensional array whose length is a product of the width times
the height (w*h). The numpy.average() call then sums these array values and
computes the average.

 **Generating the ASCII Content from the Image**

    
    
        # ascii image is a list of character strings
    >>>    aimg = []
        # generate list of dimensions
    >>>    for j in range(rows):
    ...        y1 = int(j*h)
    ...        y2 = int((j+1)*h)
            # correct last tile
    ...        if j == rows-1:
    ...            y2 = H
            # append an empty string
    ...        aimg.append("")
    ...        for i in range(cols):
                # crop image to tile
    ...            x1 = int(i*w)
    ...            x2 = int((i+1)*w)
                # correct last tile
    ...            if i == cols-1:
    ...                x2 = W
                # crop image to extract tile
    ...            img = image.crop((x1, y1, x2, y2))
                # get average luminance
    ...            avg = int(getAverageL(img))
                # look up ascii char
    ...            if moreLevels:
    ...                gsval = gscale1[int((avg*69)/255)]
    ...            else:
    ...                gsval = gscale2[int((avg*9)/255)]
                # append ascii char to string
    ...            aimg[j] += gsval
    

In this section of the program, the ASCII image is first stored as a list of
strings, which is initialized at first step. Next, you iterate through the
calculated number of row image tiles, and at second steo and the following
line, you calculate the starting and ending y-coordinates of each image tile.
Although these are ?oating-point calculations, truncate them to integers
before passing them to an image-cropping method. Next, because dividing the
image into tiles creates edge tiles of the same size only when the image width
is an integer multiple of the number of columns, correct for the y-coordinate
of the tiles in the last row by setting the y-coordinate to the image’s actual
height. By doing so, you ensure that the top edge of the image isn’t
truncated. At third step, you add an empty string into the ASCII as a compact
way to represent the current image row. You’ll fill in this string next. (You
treat the string as a list of characters.) At fourth step and the next line,
you compute the left and right x-coordinates of each tile, and at fifth step,
you correct the x-coordinate for the last tile for the same reasons you
corrected the y-coordinate. Use image.crop() at sixth step to extract the
image tile and then pass that tile to the getAverageL() function defined
above, you scale down the average brightness value from [0, 255] to [0, 9]
(the range of values for the default 10-level grayscale ramp). You then use
gscale2 (the stored ramp string) as a lookup table for ASCII Art 95 the
relevant ASCII value. The line at eight step is similar, except that it’s used
only when the command line ?ag is set to use the ramp with 70 levels. Finally,
you append the looked-up ASCII value, gsval, to the text row at last step, and
the code loops until all rows are processed.

 **Adding Command Line interface and Writing the ASCII Art Strings to a text
File**

To add command line interface use the python built-in module argparse.  
And now finally , take the generated list of ASCII character strings and write
those strings to a text file.

    
    
    # open a new text file
    >>> f = open(outFile, 'w')
    # write each string in the list to the new file
    >>> for row in aimg:
    ...    f.write(row + '\n')
    # clean up
    >>> f.close()
    

* * *

Then add these parts to create your program. The complete code is given below.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert an image to ASCII image.

import sys, random, argparse

import numpy as np

import math

 

from PIL import Image

 

# gray scale level values from: 

# http://paulbourke.net/dataformats/asciiart/

 

# 70 levels of gray

gscale1 =
"$@B%8&WM;#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^'. "

 

# 10 levels of gray

gscale2 = '@%#*+=-:. '

 

def getAverageL(image):

 

 """

 Given PIL Image, return average value of grayscale value

 """

 # get image as numpy array

 im = np.array(image)

 

 # get shape

 w,h = im.shape

 

 # get average

 return np.average(im.reshape(w*h))

 

def covertImageToAscii(fileName, cols, scale, moreLevels):

 """

 Given Image and dims (rows, cols) returns an m*n list of Images 

 """

 # declare globals

 global gscale1, gscale2

 

 # open image and convert to grayscale

 image = Image.open(fileName).convert('L')

 

 # store dimensions

 W, H = image.size[0], image.size[1]

 print("input image dims: %d x %d" % (W, H))

 

 # compute width of tile

 w = W/cols

 

 # compute tile height based on aspect ratio and scale

 h = w/scale

 

 # compute number of rows

 rows = int(H/h)

 

 print("cols: %d, rows: %d" % (cols, rows))

 print("tile dims: %d x %d" % (w, h))

 

 # check if image size is too small

 if cols > W or rows > H:

 print("Image too small for specified cols!")

 exit(0)

 

 # ascii image is a list of character strings

 aimg = []

 # generate list of dimensions

 for j in range(rows):

 y1 = int(j*h)

 y2 = int((j+1)*h)

 

 # correct last tile

 if j == rows-1:

 y2 = H

 

 # append an empty string

 aimg.append("")

 

 for i in range(cols):

 

 # crop image to tile

 x1 = int(i*w)

 x2 = int((i+1)*w)

 

 # correct last tile

 if i == cols-1:

 x2 = W

 

 # crop image to extract tile

 img = image.crop((x1, y1, x2, y2))

 

 # get average luminance

 avg = int(getAverageL(img))

 

 # look up ascii char

 if moreLevels:

 gsval = gscale1[int((avg*69)/255)]

 else:

 gsval = gscale2[int((avg*9)/255)]

 

 # append ascii char to string

 aimg[j] += gsval

 

 # return txt image

 return aimg

 

# main() function

def main():

 # create parser

 descStr = "This program converts an image into ASCII art."

 parser = argparse.ArgumentParser(description=descStr)

 # add expected arguments

 parser.add_argument('--file', dest='imgFile',
required=True)

 parser.add_argument('--scale', dest='scale',
required=False)

 parser.add_argument('--out', dest='outFile',
required=False)

 parser.add_argument('--cols', dest='cols',
required=False)

 parser.add_argument('--
morelevels',dest='moreLevels',action='store_true')

 

 # parse args

 args = parser.parse_args()

 

 imgFile = args.imgFile

 

 # set output file

 outFile = 'out.txt'

 if args.outFile:

 outFile = args.outFile

 

 # set scale default as 0.43 which suits

 # a Courier font

 scale = 0.43

 if args.scale:

 scale = float(args.scale)

 

 # set cols

 cols = 80

 if args.cols:

 cols = int(args.cols)

 

 print('generating ASCII art...')

 # convert image to ascii txt

 aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels)

 

 # open file

 f = open(outFile, 'w')

 

 # write to file

 for row in aimg:

 f.write(row + '\n')

 

 # cleanup

 f.close()

 print("ASCII art written to %s" % outFile)

 

# call main

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

Input:

    
    
    $python "ASCII_IMAGE_GENERATOR.py" --file data/11.jpg --cols 120

 **Resources**

1\. Wikipedia : ASCII_ART  
2\. Python Playground: Geeky Projects for the Curious Programmer by Mahesh
Venkitachalam.  
3\. Gray Scale Level Values  
4\. Github Code for this article

This article is contributed by **Subhajit Saha**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

