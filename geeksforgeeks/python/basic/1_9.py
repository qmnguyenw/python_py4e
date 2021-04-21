Panclus module in Python



 **Panclus** is a very useful module for the programmers to convert text to
speech in several languages, translating the text as well as predicting the
date of the solar and lunar eclipse in a single line of code. But Panclus is
no longer in use the current version named PanclusGz is released recently
since the name Panclus is used to install it. The full name of Panclus Gz is
Giga Panclus which include many sub-modules with more features than older
versions of Panclus.

 **Installation:**

    
    
    pip install PanclusGz
    pip install countryinfo

When you will type this in the command prompt both the libraries will be
installed. The PanclusGz is the main library and the countryinfo library is
used to perform other operations of the main module. The sub-modules that are
inside PanclusGz are listed below:

  * Locations
  * Dependencies
  * Gz
  * Installer

Now Let’s discuss all of them in details:

##  **Locations**

The locations module dose not meant for finding any location it is mainly used
for getting the weather reports about the temperature, wind speed, it’s a
description and the weather type. Locations also have many more attributes
related to the information of a country and its area and capital.

  

  

 **Import the module:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from PanclusGz import locations as ls  
  
---  
  
 __

 __

  

**Example 1:** For finding the weather forecast.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

ls.get_weather('India')  
  
---  
  
 __

 __

  
**Output:**  

![](https://media.geeksforgeeks.org/wp-content/uploads/20210208134401/4.png)

Your output will depend on your location and the current time.

  

  

**Example 2:** To get the area of any country.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

ls.area('India')  
  
---  
  
 __

 __

  
**Output:**

    
    
    3287590

The area will be displayed in Kilometer square.

**Example 3:** To find the calling code of any country.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

ls.country_code('India')  
  
---  
  
 __

 __

  
**Output:**

    
    
    ['91']

**Example 4:** To find the capital of a country.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

ls.capital('India')  
  
---  
  
 __

 __

**Output:**

    
    
    New Delhi

**Example 4:** To get the full information of a country.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

ls.full_info('India')  
  
---  
  
 __

 __

  
**Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210208205420/Screenshot409.png)

##  **Gz**

Gz is the main module in PanclusGz. Gz has more attributes in it than
locations. Gz can act as the main module in making voice assistants.

Benefits of Gz are:

  * Used in AI building.
  * Taking data from Wikipedia.
  * Automating your pc.

**Import the module:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from PanclusGz import Gz as gz  
  
---  
  
 __

 __

  

**Example 1:** Searching in Wikipedia.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

gz.wikit('what is programming')  
  
---  
  
 __

 __

  
**Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20210208141740/5.png)

**Example 2:** Opening any file from your pc.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

gz.openfile('cmd')  
  
---  
  
 __

 __

  
This will open the command prompt. You can also open any other file.

 **Example 3:** Calculating the date of solar and lunar eclipses.

 **For solar eclipse:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

gz.date_solar_eclipse()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20210208142626/6.png)

**For lunar eclipse:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

gz.date_lunar_eclipse()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20210208143037/7.png)

**Example 4:** Displaying time.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

gz.show_time()  
  
---  
  
 __

 __

  
This will display the current time.

### **Installer**

The installer is a small app to install python packages.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from PanclusGz import Installer

Installer.root.mainloop()  
  
---  
  
 __

 __

**Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20210208144038/8.png)

##  **Dependencies**

It is only used to see the dependencies of the package.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from PanclusGz import dependencies

dependencies.show_dependencies()  
  
---  
  
 __

 __

**Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20210208145101/9.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

