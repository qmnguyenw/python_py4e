Message Boxes using PyAutoGUI



 **PyAutoGUI** is a Python module which can automate your GUI and
programmatically control your keyboard and mouse. This article illustrates the
GUI functions to create display boxes.  
If you want to know more about PyAutoGUI and its ability to automate your
keyboard and mouse, follow this article : Mouse and Keyboard Automation using
PyAutoGUI

PyAutoGUI does not come with python, so go to command prompt and type the
following :

    
    
     pip3 install PyAutoGUI

 **alert()** : Displays a simple message box with text and a single OK button.
Returns the text of the button clicked on.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to show alert() function

import pyautogui

 

pyautogui.alert('GeekforGeeks alert box')  
  
---  
  
 __

 __

 **Output** : It will display the alert box with the given text and when
clicked OK it will return ‘OK’  
![](https://media.geeksforgeeks.org/wp-content/uploads/20200519085615/Alert-
box.png)

  
**confirm()** : Displays a message box with OK and Cancel buttons. Number and
text of buttons can be customized. Returns the text of the button clicked on.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to show confirm() function

import pyautogui

pyautogui.confirm('Geek Shall I proceed?')  
  
---  
  
 __

 __

 **Output** : It will display the alert box with the given text and on
clicking the button it will return the text on the button. In this case its
‘OK’  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200519091351/confirm.jpg)

To have multiple select options –

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to show confirm() function

# with multiple options

import pyautogui

pyautogui.confirm('Enter option Gfg', buttons =['A', 'B',
'C'])  
  
---  
  
 __

 __

 **Output** : On clicking A, it will return ‘A’ as output.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200519091703/options.png)

  
**prompt()** : Displays a message box with text input, and OK & Cancel
buttons. Returns the text entered, or None if Cancel was clicked.

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to show prompt() function

import pyautogui

pyautogui.prompt('What is your name?')  
  
---  
  
 __

 __

 **Output** : It will return the text entered, in this case ‘GeekForGeeks’ or
None if cancelled was clicked.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200519092116/prompt4.png)  

**password()** : Displays a message box with text input, and OK & Cancel
buttons. Typed characters appear as *. Returns the text entered, or None if
Cancel was clicked

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program to show password() function

import pyautogui

pyautogui.password('Enter password (text will be hidden)')  
  
---  
  
 __

 __

 **Output** : It will return the text/password entered, in this case
‘GeekForGeeks’ or None if cancelled was clicked.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200519092323/password4.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

