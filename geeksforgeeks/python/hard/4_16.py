OpenCV – The Gunnar-Farneback optical flow



In this article, we will know about Dense Optical Flow by Gunnar FarneBack
technique, it was published in a research paper named ‘Two-Frame Motion
Estimation Based on Polynomial Expansion’ by Gunnar Farneback in 2003.  
 **Prerequisites:** OpenCV

 **Optical Flow:**  
Optical flow is known as the pattern of apparent motion of objects, i.e, it is
the motion of objects between every two consecutive frames of the sequence,
which is caused by the movement of the object being captured or the camera
capturing it. Consider an object with intensity _I (x, y, t)_ , after time
_dt_ , it moves to by _dx_ and _dy_ , now, the new intensity would be, _I
(x+dx, y+dy, t+dt)_.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200505141430/Annotation-2020-05-05-141404.png)  
We, assume that the pixel intensities are constant between the two frames,
i.e.,  
 _I (x, y, t) = I (x+dx, y+dy, t+dt)_  
Taylor approximation is done on the RHS side, resulting in,  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200505143944/Annotation-2020-05-05-143915.png)  
On dividing by _δt_ , we obtain the **Optical Flow Equation** , i.e.,  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200505143755/Annotation-2020-05-05-143734.png)  
where, _u = dx/dt_ and _v = dy/dt_.  
Also, _dI/dx_ is the image gradient along the horizontal axis, _dI/dy_ is the
image gradient along the vertical axis and dI/dt is along the time.  
Since, we have just one equation to find two unknowns, we use different
methods to solve,

  * Sparse Optical Flow (Lucas Kanade Method)
  * Dense Optical Flow (Gunnar Farneback Method)

 **Gunnar Farneback Optical Flow**  
In dense optical flow, we look at all of the points(unlike Lucas Kanade which
works only on corner points detected by Shi-Tomasi Algorithm) and detect the
pixel intensity changes between the two frames, resulting in an image with
highlighted pixels, after converting to hsv format for clear visibility.  
It computes the magnitude and direction of optical flow from an array of the
flow vectors, i.e., _(dx/dt, dy/dt)_. Later it visualizes the angle
(direction) of flow by hue and the distance (magnitude) of flow by value of
HSV color representation.For visibility to be optimal, strength of HSV is set
to 255. OpenCV provides a function **cv2.calcOpticalFlowFarneback** to look
into dense optical flow.  
 **Syntax:**

    
    
    cv2.calcOpticalFlowFarneback(prev, next, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags[, flow])
    

**Parameters**

*  **prev :** First input image in 8-bit single channel format.
*  **next :** Second input image of same type and same size as _prev_.
*  **pyr_scale :** parameter specifying the image scale to build pyramids for each image (scale < 1). A classic pyramid is of generally 0.5 scale, every new layer added, it is halved to the previous one.
*  **levels :** _levels=1_ says, there are no extra layers (only the initial image) . It is the number of pyramid layers including the first image.
*  **winsize :** It is the average window size, larger the size, the more robust the algorithm is to noise, and provide fast motion detection, though gives blurred motion fields.
*  **iterations :** Number of iterations to be performed at each pyramid level.
*  **poly_n :** It is typically 5 or 7, it is the size of the pixel neighbourhood which is used to find polynomial expansion between the pixels.
*  **poly_sigma :** standard deviation of the gaussian that is for derivatives to be smooth as the basis of the polynomial expansion. It can be 1.1 for _poly= 5_ and 1.5 for _poly_ = 7.
*  **flow :** computed flow image that has similar size as _prev_ and type to be CV_32FC2.
*  **flags :** It can be a combination of-  
OPTFLOW_USE_INITIAL_FLOW uses input flow as initial apporximation.  
OPTFLOW_FARNEBACK_GAUSSIAN uses gaussian _winsize*winsize_ filter.

