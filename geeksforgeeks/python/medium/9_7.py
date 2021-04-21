Setup Sending Email in Django Project



Haven’t you observed, when you register on some websites, you get a mail from
that company or institution? The email would be, verification email or welcome
email, account creation successful email or thanks-regard email, etc. For
example, when you create a Google account, the first mail you get would be
something like, “Hi Xyz, Welcome to Google. Your new account comes with access
to Google products, apps, and services…..” Sending these types of emails from
your Django application is quite easy.  
Although you can refer to the documentation for knowing more about sending
emails in Django, but this is remarkably condensed and made easier.

 **How to send simple emails to the registered users of your Django
application**

Illustration of Django emails using an example. Consider a project named
geeksforgeeks having an app named geeks. Refer this to create Django project
and apps. Now let’s demonstrate this in geeksforgeeks project. In your “geeks”
app’s **settings.py** file, enter the following,

 __

 __  
 __

 __

 __  
 __  
 __

EMAIL_BACKEND= 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_HOST_USER = #sender's email-id

EMAIL_HOST_PASSWORD = #password associated with above email-id  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200426161218/Screenshot-1863-2.png)

In the above code, EMAIL_HOST_USER = ‘xabc6457@gmail.com’ and
EMAIL_HOST_PASSWORD = ‘xyz123abc@’ are the lines where you need to add the
sender’s mail id and password. xabc6457@gmail.com and xyz123abc@ are just
examples.

  

  

Now to use this in our application, move to **views.py** and add these lines
at the top section as below.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200426160536/Screenshot-1933-1.png)

 __

 __  
 __

 __

 __  
 __  
 __

from django.conf import settings

from django.core.mail import send_mail  
  
---  
  
 __

 __

Generally, emails are sent to the users who signup right? So, in the signup
view function, add these lines.

 __

 __  
 __

 __

 __  
 __  
 __

subject= 'welcome to GFG world'

message = f'Hi {user.username}, thank you for registering in
geeksforgeeks.'

email_from = settings.EMAIL_HOST_USER

recipient_list = [user.email, ]

send_mail( subject, message, email_from, recipient_list )  
  
---  
  
 __

 __

Now we will understand what exactly is happening. Here,

  * subject refers to the email subject.
  * message refers to the email message, the body of the email.
  * email_from refers to the sender’s details.This takes the EMAIL_HOST_USER from settings.py file, where you added those lines of code earlier.
  * recipient_list is the list of recipients to whom the mail has to be sent that is, whoever registers to your application they receive the email.
  * send_mail is an inbuilt Django function that takes subject, message, email_from, and recipient’s list as arguments, this is responsible to send emails.

After these extra lines of code has been added to your project, you can send
emails now. But if you are using Gmail, then the first time you make these
changes in your project and run, you might get **SMTP error**.

To correct that-  
1-Go to the Google account registered with the sender’s mail address and
select _Manage your account_

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200426163142/Screenshot-1945.png)  
2-Go to _security_ section at the left nav and scroll down. In _Less secure
app access_ , turn on the access. By default, it would be turned off.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200426163222/Screenshot-1955.png)  
 **Finally run the application.**  
Now, register any user to your application, and they will receive mail from
the email account you had mentioned.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

