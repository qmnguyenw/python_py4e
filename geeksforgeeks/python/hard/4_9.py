Plotting Geospatial Data using GeoPandas



GeoPandas is an open source tool to add support for geographic data to Pandas
objects. In this, article we are going to use GeoPandas and Matplotlib for
plotting geospatial data.

## Installation

We are going to install GeoPandas, Matplotlib, NumPy and Pandas.

    
    
    pip install geopandas
    pip install matplotlib
    pip install numpy
    pip install pandas
    

**Note:** If you don’t want to install these modules locally on your computer,
use Jupyter Notebook or Google Colab.

## Getting Started

### Importing modules and dataset

We are going to import Pandas for the dataframe data structure, NumPy for some
mathematical functions, GeoPandas for supporting and handling geospatial data
and Matplotlib for actually plotting the maps.

    
    
    import pandas as pd
    import geopandas as gpd
    import numpy as np
    import matplotlib.pyplot as plt

GeoPandas gives us some default datasets along with its installation to play
around with. Let’s read one of the datasets.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

import geopandas as gpd

import numpy as np

import matplotlib.pyplot as plt

 

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world.head()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200604111356/World.png)

world.head()

Some of the other datasets to play with are _‘naturalearth_cities’_ and
_‘nybb’._ Feel free to experiment with them later. We can use _world_ and plot
the same using Matplotlib.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

world.plot()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200604111553/WorldPlot.png)

World Plot

### Analyse the datasets

Now, if we see _world_ , we have a lot of fields. One of them is GDP
estimate(or _gdp_md_est_ ). However, to show how easily data can be filtered
in or out in pandas, let’s filter out all continents except Asia.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

worldfiltered= world[world.continent == "Asia"]

worldfiltered.plot(column ='gdp_md_est', cmap ='Reds')  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200604112721/AsiaPlot.png)

GDP of Countries in Asia

 _cmap_ property is used to plot the data in the shade specified. The darker
shades mean higher value while the lighter shades means lower value. Now,
let’s analyse the data for population estimate( _pop_est_ ).

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

world.plot(column='pop_est')  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200604121701/WorldPop.png)

Population Estimate

The above image is not very good in conveying the data. So let’s change some
properties to make it more comprehensible. First, let’s increase the size of
the figure and then set an axis for it. We first plot the world map without
any data to on the axis and then we overlay the plot with the data on it with
the shade red. This way the map is more clear and dark and makes the data more
understandable. However, this map is still a little vague and won’t tell us
what the shades mean.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

fig, ax= plt.subplots(1, figsize =(16, 8))

world.plot(ax = ax, color ='black')

world.plot(ax = ax, column ='pop_est', cmap ='Reds')  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200604122602/WorldPopRed.png)

World Population

Let’s import the toolkits that allow us to make dividers within the plot.
After this we are going to plot the graph as we did before, but this time we
are going to add a _facecolor._ The _facecolor_ property is going to change
the background to a color it is set to(in this case, light blue). Now we need
to create a divider for creating the color box within the graph, much like
dividers in HTML. We are creating a divider and setting its properties like
size, justification etc.

Then we need to create the color box in the divider we created. So obviously,
the highest value in the color box is going to be the highest population in
the dataset and the lowest value is going to be zero.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from mpl_toolkits.axes_grid1 import make_axes_locatable

 

 

fig, ax = plt.subplots(1, figsize =(16, 8),

 facecolor ='lightblue')

 

world.plot(ax = ax, color ='black')

world.plot(ax = ax, column ='pop_est', cmap ='Reds',

 edgecolors ='grey')

 

# axis for the color bar

div = make_axes_locatable(ax)

cax = div.append_axes("right", size ="3 %", pad = 0.05)

 

# color bar

vmax = world.pop_est.max()

mappable = plt.cm.ScalarMappable(cmap ='Reds',

 norm = plt.Normalize(vmin = 0, vmax = vmax))

cbar = fig.colorbar(mappable, cax)

 

ax.axis('off')

plt.show()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200604124013/WorldPopRedColor.png)

World Population

Thus in this article we have seen how we can use GeoPandas to get geospatial
data and plot it using Matplotlib. Custom datasets can be used to analyse
specific data and city-wise data can also be used. Also, GeoPandas can be used
with Open Street Maps, which provides very specific geospatial data(example,
streets, hospitals in a city etc., ). The same knowledge can be extended
further and can be used for specific statistical and data analysis.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

