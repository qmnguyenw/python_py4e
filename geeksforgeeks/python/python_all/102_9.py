Sending Emails Using API in Flask-Mail



Python, being a powerful language don’t need any external library to import
and offers a native library to send emails- “SMTP lib”. “smtplib” creates a
Simple Mail Transfer Protocol client session object which is used to send
emails to any valid email id on the internet. This article revolves around how
we can send bulk customised emails to a group of people with the help of
Flask.

 **Installation :**

Three packages are required for flask mail to work, Install then using pip,

1) virtualenv:

    
    
    pip install virtualenv

2) Flask:

  

  

    
    
    pip install Flask

3) Flask-Mail :

    
    
    pip install Flask-Mail

After installing the packages, we have to use **virtualenv** (optional)  
1) Create a virtualenv  
Open cmd  
Go to the folder you want to use for your project.  
Write the following code:

    
    
            
    python3 -m venv env (macOS/Linux)
    py -m venv env (Windows)
    

Here **env** is name of your environment.  
2) Activate the environment  
 **On windows** :

    
    
    .\env\Scripts\activate

 **On macOS/ Linux** :

    
    
    source env/bin/activate

3) Make sure you get the (env) in the beginning displayed in picture below :  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200110005724/Capture301.png)

#### Configuring Flask-Mail

Flask-Mail is configured through the standard Flask config API. These are the
available options (each is explained later in the documentation):

1) **MAIL_SERVER** : Name/IP address of the email server.  
2) **MAIL_PORT** : Port number of server used.  
3) **MAIL_USE_TLS** : Enable/disable Transport Security Layer encryption.  
4) **MAIL_USE_SSL** : Enable/disable Secure Sockets Layer encryption  
5) **MAIL_DEBUG** : Debug support. The default is Flask application’s debug
status.  
6) **MAIL_USERNAME** : Username of the sender  
7) **MAIL_PASSWORD** : The password of the corresponding Username of the
sender.  
8) **MAIL_ASCII_ATTACHMENTS** : If set to true, attached filenames converted
to ASCII.  
9) **MAIL_DEFAULT_SENDER** : sets default sender  
10) **MAIL_SUPPRESS_SEND** : Sending suppressed if app.testing set to true  
11) **MAIL_MAX_EMAILS** : Sets maximum mails to be sent

> Note : Not all of the configuration is to be set.

#### Sending Emails using Flask-Mail

 **Classes in Flask-Mail:**  
Mail Class : Manages email-messaging requirements  
Message Class: encapsulates an email message

 **Let’s get our hands on the code.**

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

from flask import Flask

from flask_mail import Mail, Message

 

app = Flask(__name__)

mail = Mail(app) # instantiate the mail class

 

# configuration of mail

app.config['MAIL_SERVER']='smtp.gmail.com'

app.config['MAIL_PORT'] = 465

app.config['MAIL_USERNAME'] = 'yourId@gmail.com'

app.config['MAIL_PASSWORD'] = '*****'

app.config['MAIL_USE_TLS'] = False

app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

 

# message object mapped to a particular URL ‘/’

@app.route("/")

def index():

 msg = Message(

 'Hello',

 sender ='yourId@gmail.com',

 recipients = ['reciever’sid@gmail.com']

 )

 msg.body = 'Hello Flask message sent from Flask-Mail'

 mail.send(msg)

 return 'Sent'

 

if __name__ == '__main__':

 app.run(debug = True)  
  
---  
  
 __

 __

Save it in a file and then run the script in Python Shell or CMD & Visit
http://localhost:5000/.

> Note :  
> Due to Google’s built-in security features, Gmail service may block this
> login attempt. You may have to decrease the security level. Visit
> https://myaccount.google.com/lesssecureapps?pli=1 to decrease security.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

