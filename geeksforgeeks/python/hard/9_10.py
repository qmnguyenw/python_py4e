Template matching using OpenCV in Python



 **Template matching** is a technique for finding areas of an image that are
similar to a patch (template).  
A patch is a small image with certain features. The goal of template matching
is to find the patch/template in an image.  
To find it, the user has to give two input images: **Source Image (S)** – The
image to find the template in and **Template Image (T)** – The image that is
to be found in the source image.

  * It is basically a method for searching and finding the location of a template image in a larger image.
  * The idea here is to find identical regions of an image that match a template we provide, giving a threshold
    * The threshold depends on the accuracy with which we want to detect the template in the source image.
    * For instance, if we are applying face recognition and we want to detect the eyes of a person, we can provide a random image of an eye as the template and search the source (the face of a person).
    * In this case, since “eyes” show a large amount of variations from person to person, even if we set the threshold as 50%(0.5), the eye will be detected.
    * In cases where almost identical templates are to be searched, the threshold should be set high.(t>=0.8)

 ** **How Template Matching Works?****

  * The template image simply slides over the input image (as in 2D convolution)
  * The template and patch of input image under the template image are compared.
  * The result obtained is compared with the threshold.
  * If the result is greater than threshold, the portion will be marked as detected.
  * In the function cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) the first parameter is the mainimage, second parameter is the template to be matched and third parameter is the method used for matching.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# template matching

import cv2

import numpy as np

 

# Read the main image

img_rgb = cv2.imread('mainimage.jpg').

 

# Convert it to grayscale

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

 

# Read the template

template = cv2.imread('template',0)

 

# Store width and height of template in w and h

w, h = template.shape[::-1]

 

# Perform match operations.

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

 

# Specify a threshold

threshold = 0.8

 

# Store the coordinates of matched area in a numpy array

loc = np.where( res >= threshold) 

 

# Draw a rectangle around the matched region.

for pt in zip(*loc[::-1]):

 cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h),
(0,255,255), 2)

 

# Show the final image with the matched area.

cv2.imshow('Detected',img_rgb)  
  
---  
  
 __

 __

 **Limitations of Template Matching:**

  1. Pattern occurrences have to preserve the orientation of the reference pattern image(template)
  2. As a result, it does not work for rotated or scaled versions of the template as a change in shape/size/shear etc. of object w.r.t. template will give a false match.
  3. The method is inefficient when calculating the pattern correlation image for medium to large images as the process is time consuming.

To avoid the issue caused by the different sizes of the template and original
image we can use **multiscaling**. In case where, just because the dimensions
of your template do not match the dimensions of the region in the image you
want to match, does not mean that you cannot apply template matching.

 **Multiscaling mechanism in Template Matching**

  

  

The process of Multi scaling is as follows:

  1. Loop over the input image at multiple scales (i.e. make the input image progressively smaller and smaller).
  2. Apply template matching using cv2.matchTemplate and keep track of the match with the largest correlation coefficient (along with the x, y-coordinates of the region with the largest correlation coefficient).
  3. After looping over all scales, take the region with the largest correlation coefficient and use that as your “matched” region.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# multiscaling in template matching

import cv2

import numpy as np

 

# Read the main image

img_rgb = cv2.imread('mainimage.jpg')

 

# Convert to grayscale

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

 

# Read the template

template = cv2.imread('template',0)

 

# Store width and height of template in w and h

w, h = template.shape[::-1]

found = None

 

for scale in np.linspace(0.2, 1.0, 20)[::-1]:

 

 # resize the image according to the scale, and keep track

 # of the ratio of the resizing

 resized = imutils.resize(img_gray, width =
int(img_gray.shape[1] * scale))

 r = img_gray.shape[1] / float(resized.shape[1])

 

 # if the resized image is smaller than the template, then break

 # from the loop

 # detect edges in the resized, grayscale image and apply template 

 # matching to find the template in the image edged 

 # = cv2.Canny(resized, 50, 200) result = cv2.matchTemplate(edged,
template,

 # cv2.TM_CCOEFF) (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

 # if we have found a new maximum correlation value, then update

 # the found variable if found is None or maxVal > found[0]:

 if resized.shape[0] < h or resized.shape[1] < w:

 break

 found = (maxVal, maxLoc, r)

 

# unpack the found varaible and compute the (x, y) coordinates

# of the bounding box based on the resized ratio

(_, maxLoc, r) = found

(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1]
* r))

(endX, endY) = (int((maxLoc[0] + tW) * r),
int((maxLoc[1] + tH) * r))

 

# draw a bounding box around the detected result and display the image

cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255),
2)

cv2.imshow("Image", image)

cv2.waitKey(0)  
  
---  
  
 __

 __

 **Step by step explanation of above code:**

  * After storing the width and height of template in w and r, we initialize a variable found to keep track of the region and scale of the image with the best match. From there we start looping over the multiple scales of the image using the np.linspace function. This function accepts three arguments, the starting value, the ending value, and the number of equal chunk slices in between. In this example, we’ll start from 100% of the original size of the image and work our way down to 20% of the original size in 20 equally sized percent chunks.
  * We then resize the image according to the current scale and compute the ratio of the old width to the new width — as you’ll see later, it’s important that we keep track of this ratio. We make a check to ensure that the input image is larger than our template matching. If the template is larger, then our cv2.matchTemplate call will throw an error, so we just break from the loop if this is the case.
  * At this point we can apply template matching to our resized image:
    * The cv2.minMaxLoc function takes our correlation result and returns a 4-tuple which includes the minimum correlation value, the maximum correlation value, the (x, y)-coordinate of the minimum value, and the (x, y)-coordinate of the maximum value, respectively. We are only interested in the maximum value and (x, y)-coordinate so we keep the maximums and discard the minimums.
  * After that we inspect the regions of the image that are getting matched at each iteration of the scale. From there, we update our found variable found to keep track of the maximum correlation value found thus far, the (x, y)-coordinate of the maximum value, along with the ratio of the original image width to the current, resized image width.
  * After we have looped over all scales of the image, we unpack our found variable and then compute our starting and ending (x, y)-coordinates of our bounding box . Special care is taken to multiply the coordinates of the bounding box by the ratio to ensure that the coordinates match the original dimensions of the input image.
  * Finally, we draw our bounding box and display it to our screen.

This article is contributed by **Pratima Upadhyay**. If you like GeeksforGeeks
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

