Hosting Your Django Website on a CentOS VPS



Hosting any website/web application on a live server can sometimes become
difficult if proper steps are not taken while deploying it. There are mainly 3
different types of hosting:

  1.  ** _Shared Hosting_** – Usually used for small (single page) websites with limited traffic.
  2.  ** _VPS Hosting_** – VPS ( Virtual Private Server ) hosting is used for websites with good amount of content and medium to high traffic.
  3.  ** _Dedicated Hosting_** – This hosting is generally used for large business websites with a lot of content and high traffic.

In this article, we will be discussing mainly about VPS hosting.

## VPS

VPS or Virtual Private Server is a single physical machine used by many of its
users. A physical server somewhere in the world equipped with virtualization
serves its users as a separate dedicated system for them to use. It divides
the available resources among the different users and for each of its users,
it appears as if they are using a separate dedicated machine.

### Points to be kept in mind before hosting:

  * Make sure the server OS is updated and all the other software which it uses are up to date.
  * Check with the version of the local environment packages and libraries to be the same as on the VPS also.
  * If the versions are different, make sure you uninstall the existing versions and install the required same versions on the server.
  * Choose a server which will run on your VPS’s OS to serve your website files. ( In this article we will use Nginx).
  * Always check that whether your hosting provider has a good support for its customers or not.

## Root Access & SSH

When you buy a VPS, you will be provided with the root login credentials.
There are some hosting providers that have inbuilt terminal which can be used
with root access. In that case, SSH is generally not needed.

SSH (Secure Shell) is a command line interface for managing your VPS. It helps
you connect to your VPS shell securely. For the SSH access you might need to
contact the hosting provider if it is not enabled. If it is enabled then you
may proceed further.

  

  

### PuTTY

This is a free and open source terminal emulator which helps you access your
VPS’s shell using SSH from your local system. Download PuTTY on your local
system using the official website: https://www.putty.org/

For using PuTTY, first you need to have public and private key pairs. These
key pairs can be generated using PuTTYgen or they can be created using the
hosting interface (like WHM). After creating the public – private key pairs
you can download the same private key to your local system and after opening
PuTTY you can upload the private key file via: Connection -> SSH -> Auth as
shown in figure below:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200819150150/puttypkupload.jpg)

Browse Private Key File And Upload it for authorization in PuTTY for SSH
access

After uploading, go to session tab and enter the IP address of your server as
shown in image below:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200819151005/puttyenterip.jpg)

Then click open and you will be redirected to a terminal with the ssh access
of you server. From that terminal you can manage your server. That terminal is
almost same as using a terminal on your VPS machine.

 **Note** : There are many ways to connect to your server using ssh. Above
mentioned is just one way of doing it.

## Getting Ready For Deployment

Install all the required packages and libraries by verifying their versions
with your local environment. Also download the softwares required for running
you website.

  * Enable the EPEL repository

    
    
      $ sudo yum install epel-release

  * Install the required packages 

    
    
      $ sudo yum install <package/depedency_name> 

Now you can transfer your website files from local system to your VPS using
secure copy (scp) through PuTTY or you can create a repository of your website
on github and from there you can clone it into your VPS.

  

  

I recommend uploading your website files in the directory /var/www/<my-
website>.

For a Django website, creating a virtual environment is nowadays must since it
enables you to have separate projects running on same machine without
conflicting each others dependencies and versions. So, start by creating a
environment, activating it and ensuring all the dependencies to be installed
for your website inside the environment.

 **Note** : This article assumes you have a website ready on your localhost
for hosting and thus we will not go through the steps of creating new one.

After you are done installing dependencies and moving your website files, you
need to create a database server on you VPS. Here we will be using PostgreSQL.

## Setting Up Your Website Database On Your VPS

  * Create your database and new role (database user) for the website using psql and update your settings.py file accordingly.
  * Run the following command on your ssh terminal to create migrations for your database :

    
    
      (project_env) $ python manage.py makemigrations
    

  * Ensure that all the migrations are properly created and no errors occur while creating migrations. Now migrate the database :

    
    
      (project_env) $ python manage.py migrate
    

## Resetting Migration History On Local System

  * See the current migrations using command :

    
    
      (local_project_env) $ python manage.py showmigrations
    

  * Repeat this step to clear the migration history of all apps in your website/project :

( **Note** : Here my-app should be replaced with your app name.)

    
    
      (local_project_env) $ python manage.py migrate --fake my-app zero
    

  * Remove the actual migration files by navigating to the migration folder of each app and deleting everything inside that folder except __init__.py file. Be careful about not deleting __init__.py file.
  * Create the initial migrations and fake them :

    
    
      (local_project_env) $ python manage.py makemigrations
      (local_project_env) $ python manage.py migrate --fake-initial
    

## Migrating Your Existing Database to PostgreSQL On Your VPS

  * Dump existing data on local system :

    
    
      (local_project_env) $ python manage.py dumpdata > dump.json
    

  * Move the dump.json file from your local system to VPS using either github or secure copy(scp).
  * Run the python shell and remove contentype data :

( **Note** : Run the following commands on server’s terminal (ssh))

    
    
      (project_env) $ python manage.py shell 
       >>> from django.contrib.contenttypes.models import ContentType
       >>> ContentType.objects.all().delete()
       >>> quit
    

  * Load the dump.json file to your database:

    
    
      (project_env) $ python manage.py loaddata dump.json

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

