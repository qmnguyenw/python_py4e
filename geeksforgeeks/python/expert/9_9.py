Send SMS updates to mobile phone using python



If you are running any python script and want to send regular updates from
your script to mobile phone through SMS, you can use SinchSMS API to send SMS.

 **Approach :**  
Create a app on Sinch and get the **key** and **secret** of the app and use
these credentials in the following script to send SMS to your mobile.

 **Limitation of Sinch :**  
If you don’t have any credits(you have to pay for credits), you can only send
SMS to the registered mobile numbers on Sinch.  
You can use way2sms to send sms to any number(I will be discussing how to use
way2sms in another article), but without purchased credits, on way2sms also,
you can’t send more than 100 SMS per day.

 __

 __  
 __

 __

 __  
 __  
 __

# python script for sending message update

 

import time

from time import sleep

from sinchsms import SinchSMS

 

# function for sending SMS

def sendSMS():

 

 # enter all the details

 # get app_key and app_secret by registering

 # a app on sinchSMS

 number = 'your_mobile_number'

 app_key = 'your_app_key'

 app_secret = 'your_app_secret'

 

 # enter the message to be sent

 message = 'Hello Message!!!'

 

 client = SinchSMS(app_key, app_secret)

 print("Sending '%s' to %s" % (message, number))

 

 response = client.send_message(number, message)

 message_id = response['messageId']

 response = client.check_status(message_id)

 

 # keep trying unless the status retured is Successful

 while response['status'] != 'Successful':

 print(response['status'])

 time.sleep(1)

 response = client.check_status(message_id)

 

 print(response['status'])

 

if __name__ == "__main__":

 sendSMS()  
  
---  
  
 __

 __

For execution of script, edit the number, app_key and app_secret fields and
then simply run the script.

I have written complete script for sending SMS updates to mobile phone using
sinchSMS and way2sms by fetcing latest updates from our placement
website(aitplacements.com). GitHub link : stayUpdated

 **Exercise :** Create a python script which updates you on your mobile phone
if price of a particular product lowers down to certain price on amazon.com

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

  
  

  

My Personal Notes _arrow_drop_up_

Save

