Voice Assistant using python



As we know Python is a suitable language for script writers and developers.
Let’s write a script for Voice Assistant using Python. The query for the
assistant can be manipulated as per the user’s need.  
Speech recognition is the process of converting audio into text. This is
commonly used in voice assistants like Alexa, Siri, etc. Python provides an
API called **SpeechRecognition** to allow us to convert audio into text for
further processing. In this article, we will look at converting large or long
audio files into text using the SpeechRecognition API in python.  

#### Modules needed

  * **Subprocess:-** This module is used for getting system subprocess details which are used in various commands i.e Shutdown, Sleep, etc. This module comes buit-in with Python.   

  * **Wolframalpha:-** It is used to compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology. To install this module type the below command in the terminal.  

    
    
    pip install wolframaplha

  *   * **Pyttsx3:-** This module is used for conversion of text to speech in a program it works offline. To install this module type the below command in the terminal.  
 **pip install pyttsx3**  

  * **Tkinter:-** This module is used for building GUI and comes inbuit with Python. This module comes buit-in with Python.   

  * **Wikipedia:-** As we all know Wikipedia is a great source of knowledge just like GeeksforGeeks we have used Wikipedia module to get information from Wikipedia or to perform Wikipedia search. To install this module type the below command in the terminal.  

    
    
    pip install wikipedia

  *   * **Speech Recognition:-** Since we’re building an Application of voice assistant, one of the most important things in this is that your assistant recognizes your voice (means what you want to say/ ask). To install this module type the below command in the terminal.  

    
    
    pip install SpeechRecognition

  *   * **Web browser:-** To perform Web Search. This module comes buit-in with Python.   

  * **Ecapture:-** To capture images from your Camera. To install this module type the below command in the terminal.  

    
    
    pip install ecapture

  *   * **Pyjokes:-** Pyjokes is used for collection Python Jokes over the Internet. To install this module type the below command in the terminal.  
 **pip install pyjokes**  

  * **Datetime:-** Date and Time is used to showing Date and Time. This module comes built-int with Python.   

  * **Twilio:-** Twilio is used for making call and messages. To install this module type the below command in the terminal.  

    
    
    pip install twilio

  *   * **Requests:** Requests is used for making GET and POST requests. To install this module type the below command in the terminal.  
 **pip install requests**  

  * **BeautifulSoup:** Beautiful Soup is a library that makes it easy to scrape information from web pages. To install this module type the below command in the terminal.  

    
    
    pip install beautifulsoup4

  * 

**Note:** You can remove some of the import file if you don’t want to get that
feature as here twilio for making call and messages if you don’t want to use
that you can simply remove that function.  

#### Implementation

Import the below libraries.  

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import subprocess

import wolframalpha

import pyttsx3

import tkinter

import json

import random

import operator

import speech_recognition as sr

import datetime

import wikipedia

import webbrowser

import os

import winshell

import pyjokes

import feedparser

import smtplib

import ctypes

import time

import requests

import shutil

from twilio.rest import Client

from clint.textui import progress

from ecapture import ecapture as ec

from bs4 import BeautifulSoup

import win32com.client as wincl

from urllib.request import urlopen  
  
---  
  
 __

 __

