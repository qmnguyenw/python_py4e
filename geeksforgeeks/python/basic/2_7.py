Configuring HTTPD server on Docker Container and setting up Python Interpreter



In this article, we are going to discuss a step-by-step guide on how to
configure the apache web server on top of a docker container, and setting up a
Python interpreter. Basically, we are installing the product of apache which
is HTTPD on the docker container.

##  **What is Docker?**

In simple words, if I have to define docker, is a tool that can launch an
operating system (install any operating system) in seconds. If you have
noticed when we install any operating system it takes around one hour to
launch, but docker giving u the facility the convenience to launch any os
within seconds, and httpd is just a product of apache web service which we are
using for creating webpages.

###  **Prerequisites:**

  * You need Virtual Box installed in your os
  * And launch one Linux operating system(RHEL-8, Linux (64-bit)) in the VM to perform this practice.
  * Yum, should be configured in your VM.

##  **How to configure the HTTPD server on the Docker Container?**

  * First, we need to install docker in your VM so for that first use the following command to go inside the repo folder.

    
    
    cd /etc/yum.repos.d/

  * Create a repo by giving any name by the command **vim d.repo** and give this URL. You have to add this URL in the docker repo as you can see below.

![](https://media.geeksforgeeks.org/wp-content/uploads/20201215152206/ss1.png)

toDocker repo

  * After this, you can install docker by using the below command:

    
    
    yum install docker-ce  --nobest

  * To check docker installed or not run the command:

    
    
    rpm -q docker-ce

  * To start the service and to check the status of docker you can run the following commands:

Start docker service:

    
    
    systemctl start docker

Check docker status:

    
    
    systemctl status docker

###  **Now to configure the webserver on the top of the docker container these
are the steps:**

  * Launch a docker container with an image
  * Inside which we install the webserver program(Apache server)
  * Starting the server
  * Inside the docker, we install python interpreter(python3)

 **Before launching the container in docker make sure to stop firewall and
then restart docker.**

  

  

![](https://media.geeksforgeeks.org/wp-content/uploads/20201215154509/ss2.png)

Stop Firewalld

  * Now to launch one _os /container_ on the top of docker we need an image you can use the image, we are using the ubuntu: 20.10 image, you can get it from https://hub.docker.com/, to download the image we have to use just one command

    
    
    docker pull ubuntu:20.10

  * Now u can launch the container by this image: **docker run -i -t -name taskd ubuntu:20.10** , the command to come out of the container is **exit** , you can check how many oses stopped and running also by using the command:

    
    
    docker ps -a

![](https://media.geeksforgeeks.org/wp-content/uploads/20201215155619/ss4.png)

Lunch docker container

  * To go inside the exited docker container we have one command **docker attach taskd** here _taskd_ is the name which you give while launching the container, you can give any name as per you want. Before you go inside the container you have to first start the stopped container by below the command:

    
    
    docker start taskd

![](https://media.geeksforgeeks.org/wp-content/uploads/20201215160244/ss4.png)

Going inside the docker container

  * Now we can start the installation in the docker container first we use the command **apt-get update** , this command is used to download package information from all configured sources. So when you run the update command, it downloads the package information from the Internet. It is useful to get information on an updated version of packages or their dependencies.

![](https://media.geeksforgeeks.org/wp-content/uploads/20201215160641/ss5.png)

apt-get update

  * Now we can install an apache web server on the top of docker container by the command, **apt-get install apache2** , in ubuntu we have this command **apt-get** to download and install any software.

![](https://media.geeksforgeeks.org/wp-content/uploads/20201215161149/ss6.png)

Installing webserver(Apache) on the container

  * Now we have to install _systemctl_ by using the command:

    
    
    apt-get install systemctl

![](https://media.geeksforgeeks.org/wp-content/uploads/20201215161536/ss7.png)

Installing systemctl command in container

  * The command: **apt-get install net-tools** will help you to run the _ifconfig_ commands.

![](https://media.geeksforgeeks.org/wp-content/uploads/20201215162301/ss8.png)

Installing net-tools

![](https://media.geeksforgeeks.org/wp-content/uploads/20201215162509/ss9.png)

Running ifconfig to see IP

  * Use the below command to install vim:

    
    
    apt-get install vim

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201215162827/ss10.png)

Install vim to create a file

  * Now after this installation part gets done we have to configure the webserver we need to go to **cd /var/www/html/** and there we have to create a website using **vim hello.html**.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201215163151/ss11.png)

Creating a website

  * Now start the service by command, **systemctl start appache2** and check the status, make sure it’s active.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201215163412/ss12.png)

Starting the web service

  * Now get the IP by _ifconfig_ command and use the URL **IP/hello.html** in a browser.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201215163831/ss13.png)

See the website in the firefox

##  **Setting up the Python Interpreter in the Docker Container**

  * First, we need to install python3 by the command:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201222104919/ss14.png)

  *  **** To see python3 is installed or not

    
    
    python3 -V

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201222104738/ss17.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

