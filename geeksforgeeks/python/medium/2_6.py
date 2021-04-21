Configuration for Django WebSocket Application on Ubuntu Server



This tutorial will walk you through each step in detail on how to configure
your django websocket application on a _Ubuntu 20.10 server_. This article
assumes you are familiar with Django and have a ubuntu remote server running
up. To learn more about Django, checkout – Django Tutorial

First, let’s see what all we will be using to put this into production,

  1.  **Nginx** – Web and Proxy Server
  2.  **Daphne** – our ASGI (Asynchronous Server Gateway Interface) server which will serve our Django application
  3.  **Redis Backend Server** – which will handle our web socket connections ( **ws://** )

### **Nginx** configuration

Install Nginx and Supervisor

    
    
    $ sudo apt install nginx supervisor

In your /etc/nginx/sites-available/ folder create your server and add the
below content,

    
    
    upstream redis_backend_server{
    server localhost:6379;
    }
    
    upstream app_server {
    server localhost:9090;
    }
    
    server {
    listen 80;
    listen 443 ssl;
    keepalive_timeout 700;
    
    ssl_certificate <path to your cert>;
    ssl_certificate_key <path to your key>;
    
    server_name foo.com www.foo.com;
    access_log <path to your access logs>;
    error_log <path to your error logs>;
    
    add_header X-Frame-Options SAMEORIGIN;
    add_header Content-Security-Policy "frame-ancestors self https://foo.com";
    
    location /static/ {
    
    root /var/www/staticfiles/;
    
      }
    
    if ($scheme = http) {
           return 301 https://$server_name$request_uri;
      }
    
    location / {
           include proxy_params;
           proxy_pass http://app_server;
      }
    
    location /ws {
       proxy_pass http://redis_backend_server;
       proxy_http_version 1.1;
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection "upgrade";
    
    
       proxy_ssl_certificate <path to your cert>;
       proxy_ssl_certificate_key <path to your key>;
    
       proxy_redirect off;
       proxy_set_header Host $host;
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Host $server_name;
       proxy_set_header X-Forwarded-Proto  $scheme;
       }
    }

 **Note** – Replace foo with your IP or your domain name.

  

  

Now save the configuration and restart Nginx,

    
    
    $ sudo service nginx reload

Check if the configurations are done correctly as below,

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210110181348/Screenshotfrom20210110181331.png)

Once that is done, let’ move on to our actual application server.

### Daphne Configuration

Install Daphne

    
    
    $ pip3 install daphne

Test if things are working,

    
    
    $ daphne -p 8001 project.asgi:application

You should see something similar in your terminal,

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210110181753/Screenshotfrom20210110181713.png)

  

  

Go to <server-ip>:8001 in your browser to check if the application is working.

In the /etc/supervisor/conf.d/ folder create django_server and add the content
below,

    
    
    [fcgi-program:django_server]
    # TCP socket used by Nginx backend upstream
    socket=tcp://localhost:9090
    
    # Directory where your site's project files are located
    directory= <path>
    
    # Each process needs to have a separate socket file, so we use process_num
    # Make sure to update "mysite.asgi" to match your project name
    command=<path to daphne> -u /run/daphne/daphne%(process_num)d.sock --endpoint fd:fileno=0 --access-log - --proxy-headers project.asgi:application
    
    # Number of processes to startup, roughly the number of CPUs you have
    numprocs=1
    # Give each process a unique name so they can be told apart
    process_name=asgi%(process_num)d
    
    # Automatically start and recover processes
    autostart=true
    autorestart=true
    
    # Choose where you want your log to go
    stdout_logfile=<path to your asgi logs>
    redirect_stderr=true

 **Note** – replace project with your project name

once that is done we have to create a dir for our sockets to run,

    
    
    $ sudo mkdir /run/daphne/

Restart and update the supervisor configurations,

    
    
    $ sudo supervisorctl reread
    $ sudo supervisorctl update

I know it’s a lot to take in, we just have one more step to get our server up
and running. So stay with me.

### Redis Backend Server Configuration

This is the server that will handle all our web socket connections that the
Daphne server forwards.

Install redis server

    
    
    $ sudo apt install redis-server

Edit the Redis configurations to run as a service with our systemd

    
    
    $ sudo nano /etc/redis/redis.conf

Change “supervised no” to “supervised systemd” in the config file

    
    
    $ sudo systemctl restart redis.service

Check if the server is Active and running

    
    
    sudo systemctl status redis

You should get the below response

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210110181013/Screenshotfrom20210110181001.png)

Finally with all in place and running, you should be seeing your application
up and running on your server.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210110182205/Screenshotfrom20210110182130.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

