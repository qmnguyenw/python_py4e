matplotlib.pyplot.semilogy() function in Python



Matplotlib is the most popular and Python-ready package that is used for
visualizing the data. We use matplotlib for plotting high-quality charts,
graphs, and figures.

## matplotlib.pyplot.semilogy() Function

The **matplotlib.pyplot.semilogy() function** in pyplot module of matplotlib
library is used to make a plot with log scaling on the y axis.

>  **Syntax:** matplotlib.pyplot.semilogy(*args, **kwargs)
>
>  **Parameters:** This method accept the following parameters that are
> described below:
>
>   *  **basey:** This parameter is the base of the y logarithm and are
> optional with default value _10_.
>   *  **subsy:** This parameter is the sequence of location of the minor y
> ticks and is optional.
>   *  **nonposy:** This parameter is a non-positive values in y that can be
> masked as invalid, or clipped to a very small positive number.
>

>
>  **Returns:** This returns the following:
>
>  
>
>
>  
>
>
>   *  **lines:** This returns the list of Line2D objects representing the
> plotted data..
>

Below examples illustrate the matplotlib.pyplot.semilogy() function in
matplotlib.pyplot:  
 **Example #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing necessary libraries

import matplotlib.pyplot as plot

import numpy as np

 

# Year data for the semilogy plot

years = [1900, 1910, 1920, 1930, 1940, 1950,

 1960, 1970, 1980, 1990, 2000, 2010, 

 2017]

 

# index data - taken at end of every

# decade - for the semilogy plot

indexValues = [68, 81, 71, 244, 151, 200,
615,

 809, 824, 2633, 10787, 11577,

 20656]

 

# Display grid

plot.grid(True, which ="both")

 

# Linear X axis, Logarithmic Y axis

plot.semilogy(years, indexValues )

 

plot.ylim([10, 21000])

 

plot.xlim([1900, 2020])

 

# Provide the title for the semilogy plot

plot.title('Y axis in Semilogy using Python Matplotlib')

 

# Give x axis label for the semilogy plot

plot.xlabel('Year')

 

# Give y axis label for the semilogy plot

plot.ylabel('Stock market index')

 

# Display the semilogy plot

plot.show()  
  
---  
  
 __

 __

 **Output:**  
![null](https://media.geeksforgeeks.org/wp-
content/uploads/20200709103507/geeks_pics1.png)

 **Example #2:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing necessary libraries

import matplotlib.pyplot as plt

import numpy as np

 

 

fig, ax = plt.subplots(nrows = 2,

 ncols = 2,

 figsize =(10, 5))

x = np.random.randn(1000)

 

# Plot to each different index

ax[0, 0].loglog(x, x / 2);

ax[0, 1].semilogy(np.random.random(10),
np.random.random(10));

ax[1, 0].semilogx(np.random.random(10),
np.random.random(10));

ax[1, 1].hist(np.random.randn(1000));  
  
---  
  
 __

 __

 **Output:**  
![semilogy](https://media.geeksforgeeks.org/wp-
content/uploads/20200709105629/geeks_semilog.png)

 **Example #3:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing necessary libraries

import matplotlib.pyplot as plt

import numpy as np

 

 

x = [1, 2, 3, 4, 5]

y = [11, 22, 33, 44, 55]

 

fig, ax = plt.subplots()

ax.semilogy(x, y);  
  
---  
  
 __

 __

 **Output:**  
![semilogy\(\)](https://media.geeksforgeeks.org/wp-
content/uploads/20200709105631/geeky.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

