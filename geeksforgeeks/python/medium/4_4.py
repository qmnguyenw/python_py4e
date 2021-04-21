How to enable CORS headers in your Django Project?



When site A wants to access content from another site B, it is called a Cross-
Origin request. As it is disabled for security reasons, B sends an Access-
Control-Allow-Origin header in the response. By default, a domain is not
allowed to access an API hosted on another domain. If we want to allow our
REST API (say backend) hosted in our Django application to be accessed from
other applications (say front-end) hosted on another server, we must enable
CORS (Cross-Origin Resource Sharing).

### Steps to allow CORS in your Django Project –

1\. Install django-cors-headers using PIP:

    
    
    pip install django-cors-headers 

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201114105658/ss-660x152.png)

2\. Add corsheaders to installed applications section in the settings.py file:

    
    
    INSTALLED_APPS = [
    
       ...
    
       'corsheaders',
    
       ...
    
    ]

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201114113334/ss1-660x152.png)

  

  

3\. Add corsheaders.middleware.CorsMiddleware to middleware section in
settings.py file:

    
    
    MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      ...
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
      'corsheaders.middleware.CorsMiddleware',
    ]

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201114113556/ss2-660x100.png)

4\. If you want to allow access for all domains, set the following variable to
TRUE in settings.py file:

    
    
    CORS_ORIGIN_ALLOW_ALL = True

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201114113826/ss3-660x100.png)

Alternatively, you can specify which domains you want to give access to by
doing the following in settings.py file:

    
    
    CORS_ORIGIN_ALLOW_ALL = False
    CORS_ORIGIN_WHITELIST = (
      'http://localhost:8000',
    )

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201114114123/ss10-660x100.png)

That’s all! Now your API is accessible to other applications hosted on other
selected servers.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

