Python – Send email to a list of emails from a spreadsheet



Nowadays working with Google forms is quite popular. It is used to mass gather
information easily. Email addresses are one of the most common piece of
information asked. It is stored in a spreadsheet. In this article we shall see
how to send an email to all the email addresses present in a spreadsheet.

Prerequisite knowledge:

  1. Loading Excel spreadsheet as pandas DataFrame
  2. Send mail from your Gmail account using Python

Procedure:

  *  **Step 1:** Read the spreadsheet using the pandas library. The structure of the spreadsheet used here is :![](https://media.geeksforgeeks.org/wp-content/uploads/20200424142737/Screenshot-2284.png)
  *  **Step 2:** Extablish connection with your gmail account using smtplib library.
  *  **Step 3:** Extract the names and email addresses from the spreadsheet.
  *  **Step 4:** Run a loop and for every record send an email.
  *  **Step 5:** Close the smtp server.

The Python implementation is:

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to send email to a list of

# emails from a spreadsheet

 

# import the required libraries

import pandas as pd

import smtplib

 

# change these as per use

your_email = "XYZ@gmail.com"

your_password = "XYZ"

 

# establishing connection with gmail

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.ehlo()

server.login(your_email, your_password)

 

# reading the spreadsheet

email_list = pd.read_excel('C:/Users/user/Desktop/gfg.xlsx')

 

# getting the names and the emails

names = email_list['NAME']

emails = email_list['EMAIL']

 

# iterate through the records

for i in range(len(emails)):

 

 # for every record get the name and the email addresses

 name = names[i]

 email = emails[i]

 

 # the message to be emailed

 message = "Hello " + name

 

 # sending the email

 server.sendmail(your_email, [email], message)

 

# close the smtp server

server.close()  
  
---  
  
 __

 __

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

