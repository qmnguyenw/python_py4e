Command Line File Downloader in Python



Python is one of the most popular general-purpose programming languages with a
wide range of use cases from general coding to complex fields like AI. One of
the reasons for such popularity of python as a programming language is the
availability of many built-in as well as third-party libraries and packages.

In this article, we are going to build a simple command-line file downloader,
which you can download a file if you have the download link.

#### Approach:

We are going to download files over HTTP instead of FTP. Once we have made the
request for the file, we will use the response as an input stream to write or
save the file to the file system. While Downloading, details like download
speed, time, and amount of file downloaded will be shown.

  * Take the file URL via command line
  * Open the file input or download stream over HTTP via requests.
  * Download the file by writing the file in chunks from the download/input stream into the file system.
  * Display the details
  * Save the file.

###  **Step-by-step implementation:**

 **Step 1:** Libraries required

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import requests

import sys

import time  
  
---  
  
 __

 __

