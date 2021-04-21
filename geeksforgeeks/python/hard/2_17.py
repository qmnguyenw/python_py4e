Upload and Download files from Google Drive storage using Python



In this article, we are going to see how can we download files from our Google
Drive to our PC and upload files from our PC to Google Drive using its API in
Python. It is a REST API that allows you to leverage Google Drive storage from
within your app or program. So, let’s go ahead and write a Python script to do
that.

 **Requirements:**

  * Python (2.6 or higher)
  * A Google account with Google Drive enabled
  * Google API client and Google OAuth libraries

 **Installation:**

Install the required libraries by running this command:

> pip install –upgrade google-api-python-client google-auth-httplib2 google-
> auth-oauthlib
>
>  
>
>
>  
>

 **Setup:**

  * Now, to work with Google Drive API, we have to set up our account and enable **Google Drive API.**
  * To set up your account, you can follow the steps given in the article.
  * So, now we are ready to write the Python script.

Please make sure the file **credentials.json** is in the same directory.

### Getting Started

First of all, we will import the required libraries. Then we will define a
class **DriveAPI** with a constructor and two functions for uploading and
downloading files. Inside the constructor, we will check if the file ‘
**token.pickle’** exists or not. If it exists, that means we have the access
to the Google Drive storage and we don’t need to ask for it again. We may have
to refresh the token if it’s been a long time since the token was used. if it
doesn’t exist or is invalid, the script will open up a new tab in the browser
and ask for access to Google Drive.

Once the access is granted, it will connect to the drive and fetch a list of
files in the Google Drive storage for that account and print that list. Each
item of the list contains an id and name for that file in Google Drive.

Now, Inside the **FileDownload** function, we will write the code to download
a file. We need two things to do this. First is the **id** of that file in
Drive and second is the **name** you want it to be saved as. Now, we will make
a request to the Drive service to get us the file with the given **id.** Then,
we will use a **BytesIO** object which will write the file to the memory. We
will use the **MediaIoBaseDownload** class to receive the file from the server
and write it in memory with the **BytesIO** object. Since the file size may
vary from a few bytes to very large, we will prefer downloading the file in
Chunks. We can also pass the chunk size **** if we don’t want to use the
default one. Now, we will run a while loop and in each iteration of this loop,
we will download a chunk of the file. Once it’s done, we will write the file
from memory to our Hard Drive Storage. We will wrap this whole process in a
try-except block so that if something goes wrong, our script doesn’t throw an
error.

To Upload a File, we will use the **FileUpload** function. We only need the
file path to upload a file. From the file path, we can easily extract the file
name and find its mime-type using the **mimetypes** module. We will create a
dictionary with the key “name” which contains the file name. Now, we will use
the **MediaFileUpload** class to generate the media file, and then we will
create a new file in the drive with the create function and it will save our
file data to that newly created file.

 **Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import the required libraries

from __future__ import print_function

import pickle

import os.path

import io

import shutil

import requests

from mimetypes import MimeTypes

from googleapiclient.discovery import build

from google_auth_oauthlib.flow import InstalledAppFlow

from google.auth.transport.requests import Request

from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

 

class DriveAPI:

 global SCOPES

 

 # Define the scopes

 SCOPES = ['https://www.googleapis.com/auth/drive']

 

 def __init__(self):

 

 # Variable self.creds will

 # store the user access token.

 # If no valid token found

 # we will create one.

 self.creds = None

 

 # The file token.pickle stores the

 # user's access and refresh tokens. It is

 # created automatically when the authorization

 # flow completes for the first time.

 

 # Check if file token.pickle exists

 if os.path.exists('token.pickle'):

 

 # Read the token from the file and

 # store it in the variable self.creds

 with open('token.pickle', 'rb') as token:

 self.creds = pickle.load(token)

 

 # If no valid credentials are available,

 # request the user to log in.

 if not self.creds or not self.creds.valid:

 

 # If token is expired, it will be refreshed,

 # else, we will request a new one.

 if self.creds and self.creds.expired and
self.creds.refresh_token:

 self.creds.refresh(Request())

 else:

 flow = InstalledAppFlow.from_client_secrets_file(

 'credentials.json', SCOPES)

 self.creds = flow.run_local_server(port=0)

 

 # Save the access token in token.pickle

 # file for future usage

 with open('token.pickle', 'wb') as token:

 pickle.dump(self.creds, token)

 

 # Connect to the API service

 self.service = build('drive', 'v3',
credentials=self.creds)

 

 # request a list of first N files or

 # folders with name and id from the API.

 results = self.service.files().list(

 pageSize=100, fields="files(id, name)").execute()

 items = results.get('files', [])

 

 # print a list of files

 

 print("Here's a list of files: \n")

 print(*items, sep="\n", end="\n\n")

 

 def FileDownload(self, file_id, file_name):

 request = self.service.files().get_media(fileId=file_id)

 fh = io.BytesIO()

 

 # Initialise a downloader object to download the file

 downloader = MediaIoBaseDownload(fh, request, chunksize=204800)

 done = False

 

 try:

 # Download the data in chunks

 while not done:

 status, done = downloader.next_chunk()

 

 fh.seek(0)

 

 # Write the received data to the file

 with open(file_name, 'wb') as f:

 shutil.copyfileobj(fh, f)

 

 print("File Downloaded")

 # Return True if file Downloaded successfully

 return True

 except:

 

 # Return False if something went wrong

 print("Something went wrong.")

 return False

 

 def FileUpload(self, filepath):

 

 # Extract the file name out of the file path

 name = filepath.split('/')[-1]

 

 # Find the MimeType of the file

 mimetype = MimeTypes().guess_type(name)[0]

 

 # create file metadata

 file_metadata = {'name': name}

 

 try:

 media = MediaFileUpload(filepath, mimetype=mimetype)

 

 # Create a new file in the Drive storage

 file = self.service.files().create(

 body=file_metadata, media_body=media,
fields='id').execute()

 

 print("File Uploaded.")

 

 except:

 

 # Raise UploadError if file is not uploaded.

 raise UploadError("Can't Upload File.")

 

if __name__ == "__main__":

 obj = DriveAPI()

 i = int(input("Enter your choice:

 "1 - Download file, 2- Upload File, 3- Exit.\n"))

 

 if i == 1:

 f_id = input("Enter file id: ")

 f_name = input("Enter file name: ")

 obj.FileDownload(f_id, f_name)

 

 elif i == 2:

 f_path = input("Enter full file path: ")

 obj.FileUpload(f_path)

 

 else:

 exit()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201123080713/Capture-660x156.PNG)

This will attempt to open a new window in your default browser. If this fails,
copy the URL from the console and manually open it in your browser. Now, Log
in to your Google account if you aren’t already logged in. If there are
multiple accounts, you will be asked to choose one of them. Then, click on the
Allow button to proceed. After the authentication has been completed, your
browser will display a message saying “ **The authentication flow has been
completed. You may close this window.** ” Now, the program will print a list
of files in your Google drive and ask you if you want to Upload or Download a
file.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

