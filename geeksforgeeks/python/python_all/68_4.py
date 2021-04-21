Outline specific area on Google Map using GeoJson



 **Folium** builds on the data wrangling strengths of the Python ecosystem and
the mapping strengths of the leaflet.js library. Manipulate your data in
Python, then visualize it in on a Leaflet map via folium. It supports Image,
Video, GeoJSON, and TopoJSON overlays.

 **Installation:**

To install this module type the below command in the terminal.

    
    
    pip install folium

 **Example 1:** To create Base Map

 __

 __  
 __

 __

 __  
 __  
 __

# import folium package

import folium 

 

 

# Map method of folium return Map object 

# Here we pass coordinates of location

# to view on map and starting Zoom level = 4 

 

map = folium.Map(location =[28.704060, 77.102493],

 zoom_start = 4)

 

map  
  
---  
  
 __

 __

 **Output:**

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200517113201/out17.jpg)

The class used in the above example is **folium.Map()**. This class method
will always be the first thing that you execute when working with Folium. The
purpose of this class is to generate the default map object that will be
rendered by your notebook, and the object that we will be building on top of
for our visualizations.

 **Parameters used:** There are several parameters within this class which
are:

  *  **location:** this parameter basically define the default location that will be shown by the map as the central location.
  *  **zoom_start:** which defines the default magnification level of the map.
  *  **control_scale:** enables/disables the map scale for a given zoom level.

 **Now, to outline area using GeoJson follow these steps:**

  * Open geojson.io
  * Mark the area you want to outline on the map.
  * A JSON file will get generated on the left side, save that file with the name outline.json. See the below image.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200517113811/outline.jpg)

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import folium 

 

 

# provide path of ouline.json 

# file that is in the data folder

outline = 'outline.json'

 

folium.GeoJson(outline,

 name ="madhyapradesh").add_to(map)

 

map  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200517114417/outputfinal.jpg)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

