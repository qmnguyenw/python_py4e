How to change password of superuser in Django?



Django provides us Admin Panel for it’s users to look over the database and
other activities. If you dont know how to create superuser then you can refer
to How to create superuser in Django?

 **How to change password of superuser in Django?**

For changing password of superuser, first reach the same directory as that of
manage.py and run the following command:

    
    
    python manage.py changepassword user_name

Changing password for user ‘user_name’

Enter the Password in-front of the Password field and press enter. Enter a
strong password so as to keep it secure.

  

  

    
    
    Password: ******

Then again enter the same Password for confirmation.

    
    
    Password (again): ******

This password is too short. It must contain at least 8 characters.

Enter the Password again in-front of the Password field and press enter. Enter
a strong password and at least of 8 characters so as to keep it secure.

    
    
    Password: ********
    
    
    Password (again): ********

Password changed successfully for user ‘user_name’.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201220232436/Screenshot298.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

