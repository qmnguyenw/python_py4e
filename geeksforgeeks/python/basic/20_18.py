Django Introduction and Installation



Django is a Python-based web framework which allows you to quickly create web
application without all of the installation or dependency problems that you
normally will find with other frameworks.  
When you’re building a website, you always need a similar set of components: a
way to handle user authentication (signing up, signing in, signing out), a
management panel for your website, forms, a way to upload files, etc. Django
gives you ready-made components to use.

#### Why Django?

  1. It’s very easy to switch database in Django framework.
  2. It has built-in admin interface which makes easy to work with it.
  3. Django is fully functional framework that requires nothing else.
  4. It has thousands of additional packages available.
  5. It is very scalable.

#### Popularity of Django

Django is used in many popular sites like as: Disqus, Instagram, Knight
Foundation, MacArthur Foundation, Mozilla, National Geographic etc. There are
more than 5k online sites based on the Django framework. ( Source )  
Sites like Hot Frameworks assess the popularity of a framework by counting the
number of GitHub projects and StackOverflow questions for each platform, here
Django is in 6th position. Web frameworks often refer to themselves as
“opinionated” or “un-opinionated” based on opinions about the right way to
handle any particular task. Django is somewhat opinionated, hence delivers the
in both worlds( opinionated & un-opinionated ).

#### Features of Django

 **Versatility of Django**  
Django can build almost any type of website. It can also work with any client-
side framework and can deliver content in any format such as HTML, JSON, XML
etc. Some sites which can be built using Django are wikis, social networks,
new sites etc.

 **Security**  
Since Django framework is made for making web development easy, it has been
engineered in such a way that it automatically do the right things to protect
the website. For example, In the Django framework instead of putting a
password in cookies, the hashed password is stored in it so that it can’t be
fetched easily by hackers.

 **Scalability**  
Django web nodes have no stored state, they scale horizontally – just fire up
more of then when you need them. Being able to do this is the essence of good
scalability. Instagram and Disqus are two Django based products that have
millions of active users, this is taken as an example of the scalability of
Django.

  

  

 **Portability**  
All the codes of the Django framework are written in Python, which runs on
many platforms. Which leads to run Django too in many platforms such as Linux,
Windows and Mac OS.

 **Installation of Django**

  * Install python3 if not installed in your system ( according to configuration of your system and OS) from here . Try to download the latest version of python it’s python3.6.4 this time.

 **Note-** Installation of Django in Linux and Mac is similar, here I am
showing it in windows for Linux and mac just open terminal in place of command
prompt and go through the following commands.

  *  **Install pip-** Open command prompt and enter following command-
    
        python -m pip install -U pip

![django-introduction](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-55-1.png)

  *  **Install virtual environment-** Enter following command in cmd-
    
        pip install virtualenv

![django-introduce](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-56-1.png)

  *  **Set Virtual environment-** Setting up the virtual environment will allow you to edit the dependency which generally your system wouldn’t allow.  
Follow these steps to set up a virtual environment-

    1. Create a virtual environment by giving this command in cmd-
        
                virtualenv env_site

![django-installation](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-57-1.png)

    2. Change directory to env_site by this command-
        
                cd env_site

![django-install](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-58-3.png)

  

  

    3. Go to Script directory inside env_site and activate virtual environment-
        
                cd Script
        
                activate

![django-introduction-installation](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-60-2.png)

  *  **Install Django-** Install django by giving following command-
    
        pip install django

![django-basics](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-62-1.png)

  * Return to the env_site directory-
    
        cd ..

![django](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-63-1.png)

  * Start a project by following command-
    
        django-admin startproject geeks_site

![django-introduction-install](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-64-1.png)

  * Change directory to geeks_site
    
        cd geeks_site

![django-introduction-project](https://media.geeksforgeeks.org/wp-
content/uploads/Screenshot-65.png)

  *  **Start the server-** Start the server by typing following command in cmd-
    
        python manage.py runserver

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-66-1.png)

  * To check whether server is running or not go to web browser and enter **http://127.0.0.1:8000/** as url.

![](https://media.geeksforgeeks.org/wp-content/uploads/Screenshot-67.png)

 **Benefits of Django Architecture –**

    * Rapid Development
    * Loosely Coupled
    * Ease of Modification

 **Drawbacks of MVC Architecture –**

    * Too much load on Model Component
    * Development Complexity is high
    * Two components are controlling View

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

