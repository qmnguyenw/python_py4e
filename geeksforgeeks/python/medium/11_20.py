Speech To Text using IBM Watson Studio



 **IBM Watson Studio** is an **integrated environment** designed to develop,
train, manage models, and deploy AI-powered applications and is a **Software
as a Service (SaaS)** solution delivered on the IBM Cloud. The IBM Cloud
provides lots of **services** like Speech To Text, Text To Speech, Visual
Recognition, Natural Language Classifier, Language Translator, etc.

The Speech to Text service transcribes audio to text to enable speech
transcription capabilities for applications.

#### Create an instance of the service

  1. Go to the Speech to Text page in the IBM Cloud Catalog.
  2. Sign up for a free IBM Cloud account or log in.
  3. Click **Create**.

#### Copy the Credentials to Authenticate to your service instance

  1. From the IBM Cloud Resource list, click on your Speech to Text service instance to go to the Speech to Text service dashboard page.
  2. On the **Manage** page, click **Show Credentials** to view your credentials.
  3. Copy the **API Key** and **URL** values.

 **Module Needed:**

  1.  **Json**
  2.  **ibm_watson:** This module does not comes pre-defined with Python. To install it type the below command in the terminal.
    
    
    pip install ibm_watson
    

Now you’re ready to use the IBM Cloud Services.

 **Below code illustrates the use of IBM Watson studio’s Speech To Text
Service using Python and web socket interface**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

#Python Program To Use IBM Watson

# Studio's Speech To Text Below Code

# Accepts only .mp3 Format of Audio

# File 

 

 

import json

from os.path import join, dirname

from ibm_watson import SpeechToTextV1

from ibm_watson.websocket import RecognizeCallback, AudioSource

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

 

 

# Insert API Key in place of 

# 'YOUR UNIQUE API KEY'

authenticator = IAMAuthenticator('YOUR UNIQUE API KEY') 

service = SpeechToTextV1(authenticator = authenticator)

 

#Insert URL in place of 'API_URL' 

service.set_service_url('API_URL')

 

# Insert local mp3 file path in

# place of 'LOCAL FILE PATH' 

with open(join(dirname('__file__'), r'LOCAL FILE PATH'), 

 'rb') as audio_file:

 

 dic = json.loads(

 json.dumps(

 service.recognize(

 audio=audio_file,

 content_type='audio/flac', 

 model='en-US_NarrowbandModel',

 continuous=True).get_result(), indent=2))

 

# Stores the transcribed text

str = ""

 

while bool(dic.get('results')):

 str =
dic.get('results').pop().get('alternatives').pop().get('transcript')+str[:]

 

print(str)  
  
---  
  
 __

 __

 **Output**

    
    
    The Output will be Transcript (Text) of audio file.
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

