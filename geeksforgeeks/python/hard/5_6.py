How To Visualize Sparse Matrix in Python using Matplotlib?



 **Matplotlib** is an amazing visualization library in Python for 2D plots of
arrays. Matplotlib is a multi-platform data visualization library built on
NumPy arrays and designed to work with the broader SciPy stack.

## Visualize Sparse Matrix using Matplotlib

 ** _Spy_** is a function used to visualize the array as an image similar to
matplotlib imshow function, but it is used in case of sparse matrix instead of
dense matrix. A _sparse matrix_ is a matrix where most of the elements are
zero.

![](https://media.geeksforgeeks.org/wp-content/uploads/Sparse-Matrix-Array-
Representation1.png)

Sparse matrix and its representation

Spy function uses two plotting styles to visualize the array, these are:

  * Image style
  * Marker style

Both the styles can be used for full arrays but in case of spmatrix instances
only the marker style works. If _marker_ or _markersize_ is _None_ then imshow
function is used, and all the remaining keyword arguments are passed to this
function; else, a Line2D object will be returned with the value of marker
determining the marker type, and any remaining keyword arguments passed to
plot function.

>  **Syntax:** matplotlib.pyplot.spy(Z, precision=0, marker=None,
> markersize=None, aspect=’equal’, origin=’upper’, \\*\\*kwargs)
>
>  
>
>
>  
>
>
>  **Return value:**
>
> The return type depends on the plotting style, i.e. AxesImage or Line2D.

 **Parameters:** Parameter| Value| Use| Z| array-like (M, N)| The array to be
plotted| Precision| float or ‘present’, optional  
default:zero| If precision is 0, any non-zero value will be plotted; else,
values of |Z| > precision will be plotted.  
For spmatrix instances, there is a special case: if precision is ‘present’,
any value present in the array will be plotted, even if it is identically
zero.| Origin| {‘upper’, ‘lower’}, optional  
default:’upper’| Place the [0, 0] index of the array in the upper left or
lower left corner of the axes.| Aspect| {‘equal’, ‘auto’, None} or float,
optional  
default:’equal’| It controls the aspect ratio of the axes. The aspect is of
particular relevance for images since it may distort the image, i.e. pixel
will not be square.  
---|---|---  
  
* ‘equal’: Ensures an aspect ratio of 1. Pixels will be square.
* ‘auto’: The axes is kept fixed and the aspect is adjusted so that the data fit in the axes. In general, this will result in non-square pixels.
* None: Use rcParams[“image.aspect”]

