Python | Adding markers to volcano locations using folium package



  
Python is a multipurpose language and its utilities extend to more than just
normal programming. It can be used to develop games, crawl the internet, or
develop deep learning models.

We’ll be using the Python library named **folium**(with Pandas) along with
the _Volcanoes_USA_ dataset (which contains the necessary data used in this
project). The script will create a saved web page. Upon opening it the user
will be directed to google maps, where the locations of the volcanoes will be
marked, their colors set according to the elevation.

 **Setup:**  
First, Install libraries like folium, pandas, and the dataset mention above:

    
    
    pip3 install folium
    pip3 install pandas
    

Now, you need to download the required dataset, Volcanoes_USA.txt. Remember to
download this in the same directory in which you will save the Python script.
Also, do remove the apostrophes “‘” from the values of the ‘NAME’ column in
the dataset, wherever present.

 **Pre-defined functions:**

  

  

  *  **Mean()** – A pandas function which can calculate the mean of the values of in an array/Series.
  *  **Map()** – Generate a base map of given width and height with either default tilesets or a custom tileset URL.
  *  **Marker()** – Create a simple stock Leaflet marker on the map, with optional popup text or Vincent visualization.

 **User defined functions :**

  *  **color()** – used to assign color to the marker according to the elevation of volcano.

Below is the implementation:

 __

 __  
 __

 __

 __  
 __  
 __

#import the necesssary packages

import folium

import pandas as pd

 

# importing the dataset as a csv file,

# and storing it as a dataframe in 'df'

df=pd.read_csv('Volcanoes.txt')

 

# calculating the mean of the latitudes

# and longitudes of the locations of volcanoes

latmean=df['LAT'].mean()

lonmean=df['LON'].mean()

 

# Creating a map object using Map() function.

# Location parameter takes latitudes and

# longitudes as starting location.

# (Map will be centered at those co-ordinates) 

map5 = folium.Map(location=[latmean,lonmean],

 zoom_start=6,tiles = 'Mapbox bright')

 

# Function to change the marker color 

# according to the elevation of volcano

def color(elev):

 if elev in range(0,1000):

 col = 'green'

 elif elev in range(1001,1999):

 col = 'blue'

 elif elev in range(2000,2999):

 col = 'orange'

 else:

 col='red'

 return col

 

# Iterating over the LAT,LON,NAME and

# ELEV columns simultaneously using zip()

for lat,lan,name,elev in
zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):

 # Marker() takes location coordinates 

 # as a list as an argument

 folium.Marker(location=[lat,lan],popup = name,

 icon= folium.Icon(color=color(elev),

 icon_color='yellow',icon = 'cloud')).add_to(map5)

 

# Save the file created above

print(map5.save('test7.html'))  
  
---  
  
 __

 __

Output:  
![](https://media.geeksforgeeks.org/wp-content/uploads/volcanoes.jpg)

 **Reference:**  
http://python-visualization.github.io/folium/docs-v0.5.0/modules.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

