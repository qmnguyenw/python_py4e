How to Deploy Django application on Heroku ?



Django is an MVT web framework used to build web applications. It is robust,
simple, and helps web developers to write clean, efficient, and powerful code.
In this article, we will learn how to deploy a Django project on Heroku in
simple steps. For this, a Django project should be ready, visit the following
link to prepare one:https://www.geeksforgeeks.org/django-tutorial/

###  **Prerequisites** :

  * Django
  * Postgres installed

 **Requirements.txt file:** Create requirements.txt file in the same directory
as your manage.py. Run the following command in the console with the virtual
environment activated:

    
    
     (myvenv) $ pip install dj-database-url gunicorn whitenoise
    
    
    
     (myvenv) $ pip freeze > requirements.txt
    

Check your requirements.txt. It will be updated with the packages currently
installed in your project.

 **Procfile:** Create a file named Procfile in the same directory as
manage.py. you will see the Heroku logo as Procfile’s icon. Add the following
line to it:

    
    
    web: gunicorn <project_name>.wsgi --log-file -
    

Here project name will be the name of the folder in which your settings.py is
present. Procfile explicitly declares what command should be executed to start
your app.

  

  

 **Runtime.txt file:** Create runtime.txt file in the same directory as your
manage.py. Add the python version you want to use for your web app:

    
    
    python-3.7.1 
    

**Settings.py:** Modify your settings.py as per the instructions below:

1.Set debug as False.

    
    
    DEBUG = False
    

2\. Modify allowed hosts.

    
    
    ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
    

3\. To disable Django’s static file handling and allow WhiteNoise to take over
add ‘nostatic’ to the top of your ‘INSTALLED_APPS’ list.

    
    
    INSTALLED_APPS = [
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',
        # ...
    ]
    

4\. Add WhiteNoise to the MIDDLEWARE list. The WhiteNoise middleware should be
placed directly after the Django SecurityMiddleware (if you are using it) and
before all other middleware:

    
    
    MIDDLEWARE = [
     'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
     # ...
    ]
    

5\. Update your database settings.

    
    
    import dj_database_url
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '<database_name>',
            'USER': '<user_name>',
            'PASSWORD': '<password>',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
    

6\. To serve files directly from their original locations (usually in
STATICFILES_DIRS or app static subdirectories) without needing to be collected
into STATIC_ROOT by the collectstatic command; set WHITENOISE_USE_FINDERS to
True.

  

  

    
    
    WHITENOISE_USE_FINDERS = True
    
    
    

7\. WhiteNoise comes with a storage backend that automatically takes care of
compressing your files and creating unique names for each version so they can
safely be cached forever. To use it, just add this to your settings.py:

    
    
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    
    

**Final modified Contents of settings.py:**

    
    
    import dj_database_url
    
    
    ...
    
    
    
    DEBUG = False
    
    ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
    
    INSTALLED_APPS = [
        'whitenoise.runserver_nostatic',
        
        #...
        
    ]
    
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        
        #...
    ]
    
    
    ...
    
    
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '<database_name>',
            'USER': '<username>',
            'PASSWORD': '<password>',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    
    WHITENOISE_USE_FINDERS = True
    
    
    ...
    
    
    
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
    
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    

**Heroku account**

1\. Install your Heroku toolbelt which you can find here:
https://toolbelt.heroku.com/

2\. Authenticate your Heroku account either running the below command in cmd
or gitbash

    
    
    $heroku login
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200707224041/Capture.JPG)

Here the directory of the project(resume) to be deployed is active

> Sometimes the cmd or git bash may freeze at certain commands. Just use
> CTRL+C to come out of it.

3\. Commit any changes on git before deploying.

    
    
    $ git status
    $ git add -A .
    $ git commit -m "additional files and changes for Heroku"
    

4\. Pick your application name which will be displayed on the domain name–
**[your app’s name].herokuapp.com** and create the application using below
command:

    
    
    $ heroku create <your_app's_name>
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200707234551/create.JPG)

5\. **Debugging:** If collectstatic failed during a build, a traceback was
provided that will be helpful in diagnosing the problem. If you need
additional information about the environment collectstatic was run in, use the
DEBUG_COLLECTSTATIC configuration.

    
    
    $ heroku config:set DEBUG_COLLECTSTATIC=1
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200707234550/collectstatic.JPG)

6\. **Disabling Collectstatic:** Sometimes, you may not want Heroku to run
collectstatic on your behalf. You can disable the collectstatic build step
with the DISABLE_COLLECTSTATIC configuration:

    
    
    $heroku config:set DISABLE_COLLECTSTATIC=1
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200707234553/disable.JPG)

7\. Finally, do a simple git push to deploy our application:

    
    
    $ git push heroku master
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200707234554/gitpush.JPG)

8\. When we deployed to Heroku, we created a new database and it’s empty. We
need to run the migrate and createsuperuser commands.

    
    
    $ heroku run python manage.py migrate
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200707234556/migrate.JPG)

    
    
    $ heroku run python manage.py createsuperuser
    
    
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200707234552/createsuper.JPG)

The command prompt will ask you to choose a username and a password again.
These will be your login details on your live website’s admin page.

9\. To open your site run:

    
    
    $ heroku open
    

**Resolving Errors**

In case you see application error on your website run:

    
    
    $heroku logs --tail
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200707234555/logs.JPG)

It displays recent logs and leaves the session open for real-time logs to
stream in. By viewing a live stream of logs from your app, you can gain
insight into the behavior of your live application and debug current problems.
When you are done, press Ctrl+C to return to the prompt.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

