PyQt5 – How to automate Progress Bar while downloading using urllib?



 **PyQt5** is one of the emerging GUI libraries in terms of developing Python
GUI Desktop apps. It has rich and robust functionality which ensures
production quality apps. Learning PyQt5 library is an add-on to your
knowledge. You can develop your consumer quality, highly professional apps.

In this article, we will learn how to automate the **Progress Bar in PyQt5**.
By automating what we mean is to dynamically change and set the value of
**progress bar.** Suppose, you are downloading any file over the internet and
want to show the progress of the download, then this article will surely help
you.

In the present example, we are using the **U** _ **rllib**_ _ ****_ library to
download the files as its the most common library to download files using
python.

> **Syntax** :  
>
>
>  
>
>
>  
>
>
> self.progressBar = QProgressBar(self)
>
> QProgressBar class is for creating the progress bar object.  
>

Firstly, go through the following code, then we will explain what the whole
thing does.

 **Code :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import urllib.request

from PyQt5.QtWidgets import *

import sys

 

class GeeksforGeeks(QWidget):

 

 def __init__(self):

 super().__init__()

 

 # calling a defined method to initialize UI

 self.init_UI()

 

 # method for creating UI widgets

 def init_UI(self):

 

 # creating progress bar

 self.progressBar = QProgressBar(self)

 

 # setting its size

 self.progressBar.setGeometry(25, 45, 210, 30)

 

 # creating push button to start download

 self.button = QPushButton('Start', self)

 

 # assigning position to button

 self.button.move(50, 100)

 

 # assigning activity to push button

 self.button.clicked.connect(self.Download)

 

 # setting window geometry

 self.setGeometry(310, 310, 280, 170)

 

 # setting window action

 self.setWindowTitle("GeeksforGeeks")

 

 # showing all the widgets

 self.show()

 

 # when push button is pressed, this method is called

 def Handle_Progress(self, blocknum, blocksize, totalsize):

 

 ## calculate the progress

 readed_data = blocknum * blocksize

 

 if totalsize > 0:

 download_percentage = readed_data * 100 / totalsize

 self.progressBar.setValue(download_percentage)

 QApplication.processEvents()

 

 # method to download any file using urllib

 def Download(self):

 

 # specify the url of the file which is to be downloaded

 down_url = '' # specify download url here

 

 # specify save location where the file is to be saved

 save_loc = 'C:\Desktop\GeeksforGeeks.png'

 

 # Dowloading using urllib

 urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress)

 

 

# main method to call our app

if __name__ == '__main__':

 

 # create app

 App = QApplication(sys.argv)

 

 # create the instance of our window

 window = GeeksforGeeks()

 

 # start the app

 sys.exit(App.exec())  
  
---  
  
 __

 __

 **Explanation :**

Below is the syntax for **urllib** , we have to study all the parameters it
takes.  

> _**Synatx:** urllib.request.urlretrieve(url, filename, reporthook)_
>
>  **Parameters:** This method will take following parameters **:**  
>  The **first parameter** is the url of the file, which is to be downloaded.
>
>  
>
>
>  
>
>
> The **second parameter** , if present, specifies the file location to save
> the file (if this argument is not passed, the location will be a temp file
> with an auto-generated name).
>
> The **third parameter** is a callable that will be called when the file is
> being downloaded and once after another, each block would be read. The
> callable (which is a function Handle_Progress in this case) will be passed
> as three arguments :
>
>   * a count of blocks transferred so far (blocknum)
>   * block size in bytes (blocksize)
>   * the total size of the file (totalsize)
>

The function _Handle_Progress_ hence receives three arguments. The current
downloaded size of the file is calculated dynamically by multiplying blocknum
and blocksize and is stored in the variable readed_data.

The rest of the work is done by the formula for calculating the percentage. We
multiply readed_data by 100 and divide it by the total size of the file. It
gives us the current download percentage. Then we set this download percentage
to the progress bar using setValue() method of progressBar object.

    
    
    self.progressBar.setValue(download_percentage)
    
    
    

**Output :**

https://media.geeksforgeeks.org/wp-
content/uploads/20200503011612/PyQt5-Progress-Bar-Demonstration.mp4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

