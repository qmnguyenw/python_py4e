Send mail from your Gmail account using Python



Here, we are going to learn how to send a simple basic mail using Python code.
Python, being a powerful language don’t need any external library to import
and offers a native library to send emails- “SMTP lib”. “smtplib” creates a
Simple Mail Transfer Protocol client session object which is used to send
emails to any valid email id on the internet. Different websites use different
port numbers.  
In this article, we are using a Gmail account to send a mail. Port number used
here is ‘587’. And if you want to send mail using a website other than Gmail,
you need to get the corresponding information.

 **Steps to send mail from Gmail account:**

  1. First of all, “smtplib” library needs to be imported.
  2. After that, to create a session, we will be using its instance SMTP to encapsulate an SMTP connection.
    
        s = smtplib.SMTP('smtp.gmail.com', 587)

In this, you need to pass the first parameter of the server location and the
second parameter of the port to use. For Gmail, we use port number 587.

  3. For security reasons, now put the SMTP connection in the TLS mode. TLS (Transport Layer Security) encrypts all the SMTP commands. After that, for security and authentication, you need to pass your Gmail account credentials in the login instance.The compiler will show an authentication error if you enter invalid email id or password.
  4. Store the message you need to send in a variable say, message. Using the sendmail() instance, send your message. sendmail() uses three parameters: **sender_email_id, receiver_email_id and message_to_be_sent**. The parameters need to be in the same sequence.

This will send the email from your account. After you have completed your
task, terminate the SMTP session by using quit().

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate Sending mail from

# your Gmail account 

import smtplib

 

# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)

 

# start TLS for security

s.starttls()

 

# Authentication

s.login("sender_email_id", "sender_email_id_password")

 

# message to be sent

message = "Message_you_need_to_send"

 

# sending the mail

s.sendmail("sender_email_id", "receiver_email_id", message)

 

# terminating the session

s.quit()  
  
---  
  
 __

 __

 **Sending same message to multiple people**

  

  

If you need to send the same message to different people. You can use for loop
for that.  
For example, you have a list of email ids to which you need to send the same
mail. To do so, insert a “for” loop between the initialization and termination
of the SMTP session. Loop will initialize turn by turn and after sending the
email, SMTP session will be terminated.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate Sending mail

# to multiple users 

# from your Gmail account 

import smtplib

 

# list of email_id to send the mail

li = ["xxxxx@gmail.com", "yyyyy@gmail.com"]

 

for dest in li:

 s = smtplib.SMTP('smtp.gmail.com', 587)

 s.starttls()

 s.login("sender_email_id", "sender_email_id_password")

 message = "Message_you_need_to_send"

 s.sendmail("sender_email_id", dest, message)

 s.quit()  
  
---  
  
 __

 __

 **Important Points:**

  * This code can send simple mail which **doesn’t have any attachment or any subject**.
  * One of the most amazing things about this code is that we can send any number of emails using this and Gmail mostly put your mail in the primary section. Sent mails would not be detected as Spam generally.
  * File handling can also be used to fetch email id from a file and further used for sending the emails.

 **Next:** Send mail with attachments from your Gmail account using Python

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

