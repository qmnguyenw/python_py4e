Using Google Cloud Function to generate data for Machine Learning model



Prerequisite: Deploy cloud function on Google Cloud Platform

Do you search for data to train your model online? What if we tell that you
can generate your own data in just a few lines on code?

All you need is a **Google Cloud Platform** account and know how to deploy
simple code to Cloud Function. We will be using Google Sheets to store the
data. You can use Cloud SQL or Google Cloud Storage Bucket or Firebase to
store the data. All you need to do is enable the necessary APIs.

 **Enabling the APIs and creating the credentials:**

  1. Go to Marketplace in Cloud Console.
  2. Click on ENABLE APIS AND SERVICES
  3. Then Search for Google Drive API and enable it
  4. Then go to the Credentials tab on the left navigation bar on the screen.
  5. Then click on Create Credentials then select Service Account Key
  6. Then create a new service account by giving it a name and set the Role to Editor under the Projects sub-field and keep the key type as JSON and click on Create button. Keep the Downloaded JSON safely.

After all these steps are done your page should look something like this

  

  

![Home Screen](https://media.geeksforgeeks.org/wp-
content/uploads/20191224151806/gfg128-5.png)

  7. Again go to Dashboard and follow the same steps. This time search for Google Sheets and enable the API.

 **Creating the Spreadsheet**

  1. Create a Spreadsheet in Google Sheets
  2. The look up the downloaded JSON file for the field _client_email_ and copy that email.
  3. Open the newly created spreadsheet and click on the share option and type the paste the _client_email_ there.

So, the boring part is done. Now, lets jump into the code.

 **Setting up Cloud Functions**

  1. Create a new Cloud Function and change the _Runtime_ to _Python 3.7_
  2. Go to _requirements.txt_ and delete the boilerplate text and add the following lines to it.

 _gspread >=3.1.0  
oauth2client>=4.1.3_

  3. Now the most important and the best part, _writing the code_. Delete the entire boilerplate code and paste the following code

 __

 __  
 __

 __

 __  
 __  
 __

import gspread

from oauth2client.service_account import ServiceAccountCredentials

from datetime import datetime

 

def update(request):

 # geting the variables ready

 data = {

 # your client_json contents as dictionary

 }

 

 request_json = request.get_json()

 request_args = request.args

 temp = ""

 

 if request_json and 'temp' in request_json:

 temp = request_json['temp']

 elif request_args and 'temp' in request_args:

 temp = request_args['temp']

 

 # use creds to create a client to interact with the Google Drive API

 scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

 

 creds = ServiceAccountCredentials.from_json_keyfile_dict(data, scope)

 

 client = gspread.authorize(creds)

 

 # Find a workbook by name and open the first sheet

 # Make sure you use the right name here.

 sheet = client.open("Temperature").sheet1

 

 row = [datetime.now().strftime("% d/% m/% Y % H:% M:% S"), temp]

 index = 2

 sheet.insert_row(row, index)  
  
---  
  
 __

 __

 **Code Explanation –**

> -> First, we get the necessary imports. _gspread_ is the library for
> performing handling of Google Sheets. Then, we are importing _oauth2client_.
> This will handle our authentication of the generated credentials. Then, we
> are importing _datetime_ to log the data correctly with the current time and
> date.
>
> -> Coming into the _upate(request)_ , first we add our credentials in the
> _data_ dictionary. Then, we store the user request parameters in a variable
> called _request_json_ and then we are initializing _temp_ and then assigning
> the _‘temp’_ key value into the variable.
>
> -> We are defining our scope for the authentication. We are using
> _oauth2client_ to make the necessary authentication with the specified
> scopes.  
> Then, open your Google Spreadsheet by specifying your Sheet name there.
> Then, we are inserting the date and time of logging and the parameter in the
> sheet at the specified row in _index_ variable.

  4. Now type _upate_ in the _Function to execute_ and then click on _ddeploy_

After that your Cloud Function page should look like this  
![Cloud Function](https://media.geeksforgeeks.org/wp-
content/uploads/20191225033020/gfg221-1.png)  
After this, you need to click on the function name, here _function-1_  
![function](https://media.geeksforgeeks.org/wp-
content/uploads/20191225040032/gfg313.png)  
  
Then, go to _trigger_ tab  
![url](https://media.geeksforgeeks.org/wp-
content/uploads/20191225040341/gfg411.png)  
  
After that, note the URL that is shown in there. This is the URL you will send
GET request along with the data parameter to add the parameter value to the
spreadsheet.

 **Setting up IoT device**  
You can use _Nodemcu_ or _Arduino_ for sending the data to Google Sheets, but
you will be requiring a WiFi module along with it and ofcourse, Raspberry Pi
can also be used. Now, all you have to do is send http request to the Cloud
Function URL along with the parameters, here _temp_ or temperature. This would
edit the spreadsheet and add the parameter values to the spreadsheet.

With that being said, this is how you can use Cloud Functions to log data to
Google Sheets. You can do the same for Cloud SQL or any other means of
storage. The stored data can be used as training data for its relevant Machine
Learning model.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

