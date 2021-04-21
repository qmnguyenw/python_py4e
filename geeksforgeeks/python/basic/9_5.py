How to setup Anaconda path to environment variable ?



Anaconda is an open-source software that contains Jupyter, spyder, etc that
are used for large data processing, data analytics, heavy scientific
computing. Anaconda works for R and python programming language. Spyder(sub-
application of Anaconda) is used for python. Opencv for python will work in
spyder. Package versions are managed by the package management system called
conda.

#### What is the environment variable?

Environment variables basically define the behavior of the environment. They
can affect the processes ongoing or the programs that are executed in the
environment. The region from which this variable can be accessed or over which
it is defined is termed as the scope of the variable.

#### Steps for setting up the environment variable:

#### Windows

  * Download Anaconda for Python. Make sure to download the “Python 3.7 Version” for the appropriate architecture.  
![Anaconda-version-download-Windows](https://media.geeksforgeeks.org/wp-
content/uploads/20200120153521/Ananconda-versions-download-Windows.jpg)

  * After the download is over, go through How to install Anaconda on windows? and follow the given instructions.
  * After the installation is done, we need to setup the environment variable.  
Go to **Control Panel - > System and Security -> System**  
Under **Advanced System Setting** option click on **Environment Variables** as
shown below:  
![Advanced System Settings](https://media.geeksforgeeks.org/wp-
content/uploads/20200121161603/System-Setting.jpg)

![Setting up Environment variable](https://media.geeksforgeeks.org/wp-
content/uploads/20200121161557/Environment-variable-setup-01.jpg)

  * Now, we have to alter the **“Path”** variable under System variables so that it also contains the path to the Anaconda environment. Select the **“Path”** variable and click on the **Edit** button as shown below:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200121164500/Environment-variable-setup-02-1.jpg)

  * We will see a list of different paths, click on the **New** button and then add the path where Anaconda is installed.  
![Adding new Path](https://media.geeksforgeeks.org/wp-
content/uploads/20200121161601/Environment-variable-setup-03.jpg)

  * Click on OK, Save the settings and it is done !! Now to check whether the installation is done correctly, open command prompt and type **anaconda-navigator**. It will start the anaconda navigator App, if installed correctly.

#### Linux

In Linux, there are several ways to install Anaconda. But we will refer to the
simplest and easy way to install Anaconda using terminal. Go through How to
install Anaconda on Linux? and follow the instructions. Generally, the Path
variable is automatically set in Linux at the time of installation, but it can
also be set manually by following steps:

  * Go to **Application - > Accessories -> Terminal**
  * For setting up Environment Variable, type the following command in the Terminal with the use of Installation path:
    
        export ANACONDA = /home/nikhil/anaconda3

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200121175938/Environment-variable-setup-Linux-01.png)

  * For setting up the Environment Value, type the following command in the Terminal with the use of Installation path:
    
        export PATH = $PATH:/home/nikhil/anaconda3/bin

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200121175940/Environment-variable-setup-Linux-02.png)

  * It is done!! Now to check whether the installation is done correctly, open Terminal and type **anaconda-navigator**. It will start the anaconda navigator App, if installed correctly.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

