Python | Get email alert when the website is up



In this article, we are going to learn how to check whether any website is
running or it’s down with a simple Python script. We will use Python’s
requests library for sending **‘get’** request and **‘smtplib’** library for
sending email notification when the website is up.It means we don’t need to
check every time. Our Python program will notify us via email when the site is
running.  
This script simply checks whether a website is up or not. If it is up then it
will send an email about this, if it is down then it will keep checking and
when the site will be up, it will send an email and terminate.  
 **Installation:**  
Go to command prompt and write this command:  

    
    
    pip install requests, smtplib
    

**Below are the steps:**

  * Put the entire code into a try block, to handle the exception.
  * Send a get request to the website we want.
  * If website is not running, then we don’t get a response thus throwing an exception.
  * Then in except block we just print that website is not running.
  * If there is no exception thrown, then it means we got the response and website is running.
  * Now Create SMTP session for login through gmail.
  * Enter your correct gmail id and password.
  * Send the mail and done.

 **Below is the implementation:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import smtplib, requests, time

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

while(1):

 try:

 # Replace the url for your desired website

 url = "https://www.facebook.com/"

 # Send the get request to the website

 r = requests.get(url)

 # creates SMTP session

 s = smtplib.SMTP("smtp.gmail.com", 587)

 # start TLS for security

 s.starttls()

 # Authentication

 s.login("sender_gmail_id", "sender_password")

 # Instance of MIMEMultipart

 msg = MIMEMultipart("alternative")

 # Write the subject

 msg["Subject"]= url + " is working now."

 msg["From"]="sender_gmail_id"

 msg["To"]="receiver_gmail_id"

 # Plain text body of the mail

 text = url + " is running now."

 # Attach the Plain body with the msg instance

 msg.attach(MIMEText(text, "plain"))

 # HTML body of the mail

 html ="<h2>Your site is running now.</h2><br/><a href ='"

 + url + "'>Click here to visit.</a>"

 # Attach the HTML body with the msg instance

 msg.attach(MIMEText(html, "html"))

 # Sending the mail

 s.sendmail("sender_gmail_id", "receiver_gmail_id",
msg.as_string())

 s.quit()

 print('sent')

 break

 except:

 print('site is down yet...')

 print('sleeping...')

 # Sleeping for 60 seconds. We can change this interval.

 time.sleep(60)

 print('Trying again')

 continue  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

