Text Searching in Google using Selenium in Python



Selenium is a powerful tool for controlling web browsers through programs and
performing browser automation. It is functional for all browsers, works on all
major OS and its scripts are written in various languages i.e Python, Java,
C#, etc, we will be working with Python.

In this article, we are going to see how to automate our browser. We can just
select the word/sentence and speak Search **** and the word/sentence gets
automatically searched and provide you with accurate results.

 **Requirement:**

  * pyautogui: PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.
  * selenium : Selenium is a powerful tool for controlling web browsers through programs and performing browser automation.
  * speech_recognition: Speech Recognition is an important feature in several applications used such as home automation, artificial intelligence, etc.
  * We are using **chromedriver_autoinstaller** so that then we could see the meaning of the searched word. [Have Installed Chrome Latest Version In your local device).

 **Step-by-step Approach:**

 **Step 1:** Import required modules

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module.

 

# Web browser Automation

from selenium import webdriver

from time import sleep 

 

# Support for chrome 

import chromedriver_autoinstaller 

 

# Invoking speech module

import speech_recognition as sr

 

# Support file for speech recognition

import pyttsx3

 

# Automating task

import pyautogui   
  
---  
  
__

__

**Step 2:** Let’s invoke the speech recognition module and initiate our
internal speaker so that it could hear our voice as the input and could
initiate the process. **MyText** stores our voice command as a text.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

r= sr.Recognizer() 

with sr.Microphone() as source2: 

 r.adjust_for_ambient_noise(source2, duration = 0.2) 

 audio2 = r.listen(source2)

 MyText = r.recognize_google(audio2) 

 MyText = str(MyText.lower())  
  
---  
  
 __

 __

 **Step 3:** After selecting and speaking **search** using your voice will now
initiate the process. Using selenium and pyautogui automatically takes that
word and gives the appropriate search result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

if MyText == "search":

 

 # Automates 'copy' internally

 pyautogui.hotkey('ctrl', 'c')

 

 chrome_options = webdriver.ChromeOptions()

 

 capabilities = {'browserName': 'chrome',

 'javascriptEnabled': True}

 

 capabilities.update(chrome_options.to_capabilities())

 

 chromedriver_autoinstaller.install()

 

 # Invoking the chrome

 driver = webdriver.Chrome()

 

 # Adjusting the size of the window

 driver.set_window_size(1920, 1080)

 

 driver.implicitly_wait(10)

 

 driver.get("https://www.google.com/") 

 

 #Place where our selected word gets pasted

 driver.find_element_by_xpath(


"/html/body//form[@role='search']/div[2]/div[1]//div[@class='a4bIc']/input[@role='combobox']")

 .send_keys(pyautogui.hotkey('ctrl', 'v'))  
  
---  
  
 __

 __

 **Below is the full implementation:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

from selenium import webdriver 

from time import sleep 

import chromedriver_autoinstaller

import speech_recognition as sr 

import pyttsx3 

import pyautogui

 

while(True):

 

 try:

 r = sr.Recognizer() 

 with sr.Microphone() as source2: 

 

 r.adjust_for_ambient_noise(source2, duration = 0.2) 

 audio2 = r.listen(source2) 

 MyText = r.recognize_google(audio2) 

 MyText = str(MyText.lower())

 

 if MyText == "search":

 pyautogui.hotkey('ctrl', 'c')

 chrome_options = webdriver.ChromeOptions()

 capabilities = {'browserName': 'chrome',
'javascriptEnabled': True}

 capabilities.update(chrome_options.to_capabilities())

 chromedriver_autoinstaller.install()

 driver = webdriver.Chrome()

 driver.set_window_size(1920, 1080)

 driver.implicitly_wait(10)

 driver.get("https://www.google.com/") 

 driver.find_element_by_xpath(


"/html/body//form[@role='search']/div[2]/div[1]//div[@class='a4bIc']/input[@role='combobox']")

 .send_keys(pyautogui.hotkey('ctrl', 'v'))

 

 elif MyText == "stop":

 break

 

 except Exception as e:

 

 pyautogui.press('enter')  
  
---  
  
 __

 __

 _ ** _Demo:_**_

https://media.geeksforgeeks.org/wp-
content/uploads/20201228181551/For_article.mp4

  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

