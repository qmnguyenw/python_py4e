Python | How to download windows lock-screen wallpapers



Have you ever seen these cool wallpaper in your Windows 10 Lock Screen,
whenever you open your PC/Laptop?  
![Wallpaper](https://media.geeksforgeeks.org/wp-
content/uploads/20190527235556/pic11.jpg)

Whenever we are connected to the internet, they are going to change randomly.
But ever wondered the working behind it? Well, those images are stored in the
following path:

    
    
    C:\Users\[[Your Username]]\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets

But there is a twist in the tale. The wallpapers are going to look like this.  
![Screenshot](https://media.geeksforgeeks.org/wp-
content/uploads/20190528000300/pic22.jpg)  
These are actually the images without their extensions, that is their
extension is removed.

You might be thinking of copying the images one by one and then changing the
extension of the image one by one, and that too manually.  
Well, to make your life easier, Python is there for you. It will do the task
just for you, that too with a single code.

Below is the Python implementation –

  

  

 **Note: Make a folder named WALLPAPER on the Desktop.**

 __

 __  
 __

 __

 __  
 __  
 __

import os

import shutil

 

os.chdir('C:\\')

username = os.environ['USERNAME']

 

# The folder which contains the wallpaper files

source = ("C:\\Users\\"+ username
+"\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\")

 

# You will have to add the path of your

# destination here. Just make sure the

# folder exists on the desktop.

destination = ("C:\\Users\\"+ username +"\\Desktop\\WALLPAPER\\")

 

for the_file in os.listdir(destination):

 

 path_of_file = os.path.join(destination, the_file)

 base_file, ext = os.path.splitext(the_file)

 

 if ext ==".jpg":

 try:

 if os.path.isfile(path_of_file):

 os.unlink(path_of_file)

 

 except Exception as e:

 print(e)

 

for name_of_file in os.listdir(source):

 shutil.copy( source + name_of_file, destination)

 print(name_of_file)  
  
---  
  
 __

 __

But still, the folder will look like this.  
![Folder1](https://media.geeksforgeeks.org/wp-
content/uploads/20190529004846/Shotte2.jpg)

 **So what to do next?**  
See the below Python code, save it as a copy in the same WALLPAPER folder on
the desktop and RUN IT there.

