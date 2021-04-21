Stamen Toner ,Stamen Terrain and Mapbox Bright Maps in Python-Folium



Folium library is a powerful data visualization library in Python used by
people to visualize geospatial data and maps. With the Folium library, we can
create map of any location in the world with the help of latitude and
longitude of that location. We can also create interesting visualizations by
superimposing markers as well as clusters of markers on top of the map. We can
create maps of different styles such as street level, stamen map, and Mapbox
Bright map. The maps can be created by Folium using the ‘map’ function. The
maps are interactive which means we can zoom in and out after the map is
created by specifying the zoom level according to our choice. The default map
style is the open street map, which shows a street view of an area when we
zoom in and show the borders of the world countries when we zoom out. Folium
library has various features. One of the most important features is map styles
with which we can create different map styles using the tiles parameter. The
tiles include stamen tone, stamen terrain, etc. Stamen toner is used for
visualizing features like river meanders and coastal zones. Another tile style
is stamen terrain which is used for visualizing features like hill shading and
natural vegetation colors.

### Stamen Toner Maps

These are high-contrast Black and White maps. They are used for data mashups
and for exploring and visualizing river meanders and coastal zones.

### Stamen Terrain Maps

These maps are used to highlight hill shading and natural vegetation colors.
They showcase advanced labeling features and linework generalization of dual
carriageway roads.

### Mapbox Bright Maps

These are maps that similar to the default style, except that the borders are
not visible with a low zoom level. They differ form the default style because
default style displays country names in each country’s native language whereas
Mapbox Bright style tile displays all country names in English.

 **Example 1:** **Stamen Tonner map of the world centered around Mumbai**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np 

import pandas as pd

import folium

 

# define the world map

world_map = folium.Map()

 

# create a Stamen Toner map of the world

# centered around Mumbai

world_map = folium.Map(location =[19.11763765873,
72.9060384756], 

 zoom_start = 10, tiles ='Stamen Toner')

 

# display map

world_map  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200527003144/ss12.jpg)

 **Example 2:** **Stamen Terrain map of the world centered around Mumbai**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np 

import pandas as pd

import folium

 

# define the world map

world_map = folium.Map()

 

# create a Stamen Terrain map of the world 

# centered around Mumbai with a zoom level 

# of 10

world_map = folium.Map(location =[19.11763765873,
72.9060384756],

 zoom_start = 10, tiles ='Stamen Terrain')

 

# display map

world_map  
  
---  
  
 __

 __

 **Output :**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200527003147/ss23.jpg)

 **Example 3:** **Mapbox Bright map of the world centered around Mumbai**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np 

import pandas as pd

import folium

 

# define the world map

world_map = folium.Map()

 

# create a Mapbox Bright map of the world 

# centered around Mumbai with a zoom level 

# of 10

world_map = folium.Map(location =[19.11763765873,
72.9060384756], 

 zoom_start = 10, tiles ='Mapbox Bright')

 

# display the map

world_map  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200527003150/ss32.jpg)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

