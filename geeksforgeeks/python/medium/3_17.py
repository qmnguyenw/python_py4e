How to put the y-axis in logarithmic scale with Matplotlib ?



Axes’ in all plots using Matplotlib are linear by default, **yscale()** method
of the **matplotlib.pyplot** library can be used to change the y-axis scale to
logarithmic.

The method yscale() takes a single value as a parameter which is the type of
conversion of the scale, to convert y-axes to logarithmic scale we pass the
“log” keyword or the matplotlib.scale.LogScale class to the yscale method.

>  **Syntax :** matplotlib.pyplot.yscale(value, **kwargs)
>
>  **Parameters:**
>
>   *  _Value = { “linear”, “log”, “symlog”, “logit”, … }_
>   *  _ ****kwargs =** Different keyword arguments are accepted, depending on
> the scale (matplotlib.scale.LinearScale, LogScale, SymmetricalLogScale,
> LogitScale)_
>

>
>  **Returns :** Converts the y-axes to the given scale type. (Here we use the
> “log” scale type)
>
>  
>
>
>  
>

 **Linear Scale Example :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import matplotlib.pyplot as plt

 

data = [10**i for i in range(4)]

plt.plot(data)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201212213920/noscale-300x195.png)

Linear Scale

 **Logarithmic Scale Example :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import matplotlib.pyplot as plt

 

data = [10**i for i in range(4)]

 

# convert y-axis to Logarithmic scale

plt.yscale("log") 

plt.plot(data)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201212213930/logscale-300x198.png)

Logarithmic y-axis

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

