Send mail with attachment from your Gmail account using Python



In last article, we have discussed the basics of sending a mail from a Gmail
account without any subject as well as without any attachment. Today, we will
learn how to send mail with attachment and subject using Python. Before moving
on, it is highly recommended to learn how to send a simple mail using Python
and learn the basics working of ‘smtplib’ library of Python.  
If you have read the previous article, you have gained the knowledge how a
session is created and how it works. Now, you need to learn to attach a file
and subject to the mail. For that you need to import some native libraries of
Python. From these libraries, you need to import the tools used in our
programs.

 **Steps to send mail with Attachments from Gmail account:**

  1. For adding an attachment, you need to import:
    * import smtplib
    * from email.mime.multipart import MIMEMultipart
    * from email.mime.text import MIMEText
    * from email.mime.base import MIMEBase
    * from email import encoders

These are some libraries which will make our work simple. These are the native
libraries and you dont need to import any external library for this.

  2. Firstly, create an instance of MIMEMultipart, namely “msg” to begin with.
  3. Mention the sender’s email id, receiver’s email id and the subject in the “From”, “To” and “Subject” key of the created instance “msg”.
  4. In a string, write the body of the message you want to send, namely body. Now, attach the body with the instance msg using attach function.
  5. Open the file you wish to attach in the “rb” mode. Then create an instance of MIMEBase with two parameters. First one is ‘_maintype’ amd the other one is ‘_subtype’. This is the base class for all the MIME-specific sub-classes of Message.  
Note that ‘_maintype’ is the Content-Type major type (e.g. text or image), and
‘_subtype’ is the Content-Type minor type (e.g. plain or gif or other media).

  6. set_payload is used to change the payload the encoded form. Encode it in encode_base64. And finally attach the file with the MIMEMultipart created instance msg.

After finishing up these steps, follow the instructions described in the
previous article to create a session, secure it and check the authenticity and
then after sending the mail, terminate the session.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate Sending mail with attachments

# from your Gmail account 

 

# libraries to be imported

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.base import MIMEBase

from email import encoders

 

fromaddr = "EMAIL address of the sender"

toaddr = "EMAIL address of the receiver"

 

# instance of MIMEMultipart

msg = MIMEMultipart()

 

# storing the senders email address 

msg['From'] = fromaddr

 

# storing the receivers email address 

msg['To'] = toaddr

 

# storing the subject 

msg['Subject'] = "Subject of the Mail"

 

# string to store the body of the mail

body = "Body_of_the_mail"

 

# attach the body with the msg instance

msg.attach(MIMEText(body, 'plain'))

 

# open the file to be sent 

filename = "File_name_with_extension"

attachment = open("Path of the file", "rb")

 

# instance of MIMEBase and named as p

p = MIMEBase('application', 'octet-stream')

 

# To change the payload into encoded form

p.set_payload((attachment).read())

 

# encode into base64

encoders.encode_base64(p)

 

p.add_header('Content-Disposition', "attachment; filename= %s" %
filename)

 

# attach the instance 'p' to instance 'msg'

msg.attach(p)

 

# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)

 

# start TLS for security

s.starttls()

 

# Authentication

s.login(fromaddr, "Password_of_the_sender")

 

# Converts the Multipart msg into a string

text = msg.as_string()

 

# sending the mail

s.sendmail(fromaddr, toaddr, text)

 

# terminating the session

s.quit()  
  
---  
  
 __

 __

 **  
Important Points:**

  

  

  * You can use loops to send mails to a number of people.
  * This code is simple to implement. But it will not work if you have enabled 2-step verification on your gmail account. It is required to switch off the 2-step verification first.
  * Using this method, Gmail will always put your mail in the primary section and the mails sent will not be Spam.

This article is contributed by **Rishabh Bansal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

