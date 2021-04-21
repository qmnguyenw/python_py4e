Simple Multithreaded Download Manager in Python



 **Introduction**

A Download Manager is basically a computer program dedicated to the task of
downloading stand alone files from internet. Here, we are going to create a
simple Download Manager with the help of threads in Python. Using multi-
threading a file can be downloaded in the form of chunks simultaneously from
different threads. To implement this, we are going to create simple command
line tool which accepts the URL of the file and then downloads it.

 **Prerequisites**  
Windows machine with Python installed.

 **Setup**  
Download the below mentioned packages from command prompt.

  1.  **Click package:** Click is a Python package for creating beautiful command line interfaces with as little code as necessary. It’s the “Command Line Interface Creation Kit”.
    
        pip install click

  2.  **Requests package:** In this tool, we are going to download a file based on the URL(HTTP addresses). Requests is an HTTP Library written in Python which allows you to send HTTP requests. You can add headers, form data, multi-part files, and parameters with simple Python dictionaries and access the response data in the same way.
    
        pip install requests

  3.  **threading package:** To work with threads we need threading package.
    
        pip install threading

 **Implementation**

  

  

( **Note:** The program has been split into parts to make it easy to
understand. Make sure that you are not missing any part of the code while
running the code.)

  * Create new python file in editor
  * First import the required packages to that you’ll need to write

 __

 __  
 __

 __

 __  
 __  
 __

#N ote: This code will not work on online IDE

 

# Importing the required packages

import click

import requests

import threading

 

# The below code is used for each chunk of file handled

# by each thread for downloading the content from specified 

# location to storage

def Handler(start, end, url, filename):

 

 # specify the starting and ending of the file

 headers = {'Range': 'bytes=%d-%d' % (start, end)}

 

 # request the specified part and get into variable 

 r = requests.get(url, headers=headers, stream=True)

 

 # open the file and write the content of the html page 

 # into file.

 with open(filename, "r+b") as fp:

 

 fp.seek(start)

 var = fp.tell()

 fp.write(r.content)  
  
---  
  
 __

 __

Now we are going to implement the actual functionality of in the download_file
function.

  * The first step is to decorate the function with click.command() so that we can add command line arguments. We can also give options for respective commands.
  * For our implementation upon entering command –help we are going to display the options that can be used. In our program there are two options that can be used. One is “number_of_threads” and the other is “name”. By default “number_of_threads” is taken as 4. To change it, we can specify while running the program.
  * “name” option is given so that we can give our own name to the file that is going to be downloaded. The arguments for the function can be specified using click.argument().
  * For our program we need to give the URL of the file we want to download.

 __

 __  
 __

 __

 __  
 __  
 __

#Note: This code will not work on online IDE

 

@click.command(help="It downloads the specified file with specified
name")

@click.option('—number_of_threads',default=4, help="No of
Threads")

@click.option('--name',type=click.Path(),help="Name of the
file with extension")

@click.argument('url_of_file',type=click.Path())

@click.pass_context

def download_file(ctx,url_of_file,name,number_of_threads):  
  
---  
  
 __

 __

The following code goes under the “download_file” function.

  * In this function we first check for the “name”. If the “name” is not given then use the name from url.
  * Next step is to connect to the URL and Get the content and size of the content.

 __

 __  
 __

 __

 __  
 __  
 __

r= requests.head(url_of_file)

if name:

 file_name = name

else:

 file_name = url_of_file.split('/')[-1]

try:

 file_size = int(r.headers['content-length'])

except:

 print "Invalid URL"

 return  
  
---  
  
 __

 __

Create file with size of the content

 __

 __  
 __

 __

 __  
 __  
 __

part= int(file_size) / number_of_threads

fp = open(file_name, "wb")

fp.write('\0' * file_size)

fp.close()  
  
---  
  
 __

 __

Now we create Threads and pass the Handler function which has the main
functionality :

 __

 __  
 __

 __

 __  
 __  
 __

for i in range(number_of_threads):

 start = part * i

 end = start + part

 

 # create a Thread with start and end locations

 t = threading.Thread(target=Handler,

 kwargs={'start': start, 'end': end, 'url': url_of_file,
'filename': file_name})

 t.setDaemon(True)

 t.start()  
  
---  
  
 __

 __

Finally join the threads and call the “download_file” function from main

 __

 __  
 __

 __

 __  
 __  
 __

main_thread= threading.current_thread()

for t in threading.enumerate():

 if t is main_thread:

 continue

 t.join()

print '%s downloaded' % file_name

 

if __name__ == '__main__':

 download_file(obj={})  
  
---  
  
 __

 __

We are done with coding part and now follow the commands showed below to run
the .py file.

![1](https://media.geeksforgeeks.org/wp-content/uploads/116.png)

    
    
    “python filename.py” –-help

This command shows the “Usage” of the click command tool and options that the
tool can accepts.  
Below is the sample command where we try to download an jpg image file from a
URL and also gave a name and number_of_threads.

![2](https://media.geeksforgeeks.org/wp-content/uploads/212.png)

Finally, we are successfully done with it and this is one of the way to build
a simple multithreaded download manager in Python.

This article is contributed by **Rahul Bojanapally**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

