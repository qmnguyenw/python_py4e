Matplotlib.pyplot.title() in Python



 **Matplotlib** is an amazing visualization library in Python for 2D plots of
arrays. Matplotlib is a multi-platform data visualization library built on
NumPy arrays and designed to work with the broader SciPy stack.

## Matplotlib.pyplot.title()

The title() method in matplotlib module is used to specify title of the
visualization depicted and displays the title using various attributes.

>  **Syntax:** matplotlib.pyplot.title(label, fontdict=None, loc=’center’,
> pad=None, **kwargs)
>
>  **Parameters:**
>
>   *  **label**(str): This argument refers to the actual title text string
> of the visualization depicted.
>   *  **fontdict**(dict) : This argument controls the appearance of the
> text such as text size, text alignment etc. using a dictionary. Below is the
> default fontdict:
>

>
>  
>
>
>  
>
>
> fontdict = {‘fontsize’: rcParams[‘axes.titlesize’],  
> ‘fontweight’ : rcParams[‘axes.titleweight’],  
> ‘verticalalignment’: ‘baseline’,  
> ‘horizontalalignment’: loc}
> *  **loc**(str): This argument refers to the location of the title, takes
> string values like 'center', 'left' and 'right'.
> *  **pad**(float): This argument refers to the offset of the title from
> the top of the axes, in points. Its default values in None.
> *  ****kwargs:** This argument refers to the use of other keyword arguments
> as text properties such as color, fonstyle, linespacing,
> backgroundcolor, rotation etc.

