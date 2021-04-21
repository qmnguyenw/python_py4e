Designing GUI applications Using PyQt in Python



Building GUI applications using **PYQT designer tool** is comparatively less
time consuming than code the widgets. It is one of the fastest and easiest
ways to create GUIs.

The normal approach is to write the code even for the widgets and for the
functionalities as well. But using Qt-designer, one can simply drag and drop
the widgets, which comes very useful while developing big-scale applications.

 **Installation of PyQt5 :**

  * For Linux :
    
         sudo apt-get install python3-pyqt5

  * For Windows :
    
         pip install pyqt5
     pip install pyqt5-tools 
    

Let’s create a signup form using the QT designer tool. No code is required for
creating forms, buttons, text boxes, etc! It is rather drag and drop
environment. So, using PyQt is a lot simpler than Tkinter.

![](https://media.geeksforgeeks.org/wp-
content/uploads/Sign_Up_Form-300x249.png)

  

  

QT Designer will be located at MyPythonInstallationDir\Lib\site-
packages\pyqt5-tools, and is named designer.exe (on Windows OS).  
Open Qt Designer, then select **Main Window** and click **Create**. Set your
preferred size of the window by dragging the edges of the window.  
![](https://media.geeksforgeeks.org/wp-content/uploads/PyQt_new_window.png)

 **To create the layout of Singup form, following widgets are needed :**

  1. Three text edit boxes.
  2. One button.
  3. Four Text Labels (SignId Banner, UserName label, Password and Confirm Password label).

One has to find those widgets in **Widget Tool Box**. Just drag and drop the
required widgets onto the Main Window or the window working on.  
![](https://media.geeksforgeeks.org/wp-content/uploads/Selection_003-1.png)

To change the appearance of the window or the widget, just right click on the
widget and click **Change StyleSheet**.

![](https://media.geeksforgeeks.org/wp-content/uploads/Selection_004.png)

To get preview of the window, press Ctrl + R .

 **Save the file :**  
The file will be saved with **.ui**

