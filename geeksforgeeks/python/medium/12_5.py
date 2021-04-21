Convert Python Script to .exe File



We create lots of Python programs per day and want to share them with the
world. It is not that you share that Python program with everyone, and they
will run this script in some IDLE shell. But you want everyone to run your
Python script without the installation of Python. So for this work, you can
convert the .py file to .exe file. In this article, you will learn how you can
convert .py file to .exe file. Follow the below steps for the same.

**Step 1:**  
Install the library pyinstaller.  
Type below command in the command prompt.  

    
    
    pip install pyinstaller

 **Step 2:**  
Go into the directory where your ‘.py’ file is located.

![Convert-.py-to.exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203133742/step-22.png)

  

  

**Step 3:**  
Press the shift⇧ button and simultaneously right-click at the same location.
You will get the below box.  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200202204743/Screenshot-5013.png)

**Step 4:**  
Click on ‘Open PowerShell window here’.

![python-.py-to .exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203132431/step44.png)

You will get a window shown below.

![convert .py to .exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203132656/step4-22.png)

  

  

 **Step 5:**  
Type the command given below in that PowerShell window.  

    
    
    pyinstaller --onefile -w 'filename.py'

Here the ‘.py’ file name is ‘1’.  
See below:

![Convert-.py-to.exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203133342/step-5.png)

In case you get an error at this point in the PowerShell window like this:

![convert .py to .exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203133226/step5-21.png)

The correction while typing the above command:  

    
    
    .\pyinstaller --onefile -w 'filename.py'
    
    For any missing package:
    pyinstaller --hidden-import 'package_name' --onefile 'filename.py'

![Convert-.py-to.exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203133303/step-5-3.png)

**Step 6:**  
After typing the command ‘Hit the Enter’.  
It will take some time to finish the process depending on the size of the file
and how big is your project.  
After the processing has been finished, the window will look as below:

![Convert-.py-to.exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203133402/step-6.png)

**Step 7:**  
See the directory it should look like this:

![Convert-.py-to.exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203133419/step-7.png)

‘build’ folder and ‘1.spec’ is of no use. You can delete these if you want, it
will not affect your ‘.exe’ file.

![Convert-.py-to.exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203133621/step7-2.png)

**Step 8:**  
Open ‘dist’ folder above. Here you will get your ‘.exe’ file.

![Convert-.py-to.exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203133508/step-8.png)

Right-click on the file and check the properties.

![Convert-.py-to.exe](https://media.geeksforgeeks.org/wp-
content/uploads/20200203133525/step-8-2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

