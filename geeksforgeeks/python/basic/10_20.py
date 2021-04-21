Download and Install Python 3 Latest Version



How to Download and Install Python 3 Latest Version? In this article, you will
get the answer to all your questions related to installing Python on
Windows/Linux/macOS. Python was developed by Guido van Rossum in the early
1990s and its latest version is 3.7.4, we can simply call it as Python3.

To understand how to install Python You need to know _What Python is_ and
where it is actually installed in your system.

Let’s consider a few points:

  * Python is a widely-used general-purpose, high-level programming language.
  * Every Release of Python is open-source. Python releases have also been GPL-compatible.
  * Any version of Python can be downloaded from **Python Software Foundation** website at python.org.
  * Most of the languages, notably Linux provide a package manager through which you can directly install Python on your Operating System

In this Python tutorial of Installation and Setup, you’ll see how to install
Python on Windows, macOS, Linux, iOS, and Android.

## Python Latest Version Installation and Setup

> Here you can choose your OS and see the corresponding tutorial,
>
>  
>
>
>  
>
> * Windows
> * Linux
> * macOS / Mac OS X
> * Android
> * iOS (iPhone / iPad)
> * Online Interpreters of Python

### How to install Python on Windows?

Since windows don’t come with Python preinstalled, it needs to be installed
explicitly. Here we will define step by step tutorial on How to install Python
on Windows.

Follow the steps below :

#### Download Python Latest Version from python.org

  * First and foremost step is to open a browser and open https://www.python.org/downloads/windows/

![How-to-install-Python-for-windows-1](https://media.geeksforgeeks.org/wp-
content/uploads/20190926114235/How-to-install-Python-for-windows-1.png)

  * Underneath the **Python Releases for Windows** find **Latest Python 3 Release – Python 3.7.4** (latest stable release as of now is Python 3.7.4).
  * On this page move to **Files** and click on **Windows x86-64 executable installer** for 64-bit or **Windows x86 executable installer** for 32-bit.

![how-to-install-python-for-windows-steps](https://media.geeksforgeeks.org/wp-
content/uploads/20190926114317/how-to-install-python-for-windows-steps.png)

#### Install Python 3.7.4 Latest Version on Windows

  * Run the Python Installer from downloads folder  
![how to install python on windows](https://media.geeksforgeeks.org/wp-
content/uploads/20190926120522/Screenshot-130.png)

  * Make sure to mark **Add Python 3.7 to PATH** otherwise you will have to do it explicitly.  
It will start installing python on windows.  
![how to install python on windows](https://media.geeksforgeeks.org/wp-
content/uploads/20190926120809/Screenshot-2106.png)

  * After installation is complete click on **Close**.  
Bingo..!! Python is installed. Now go to windows and type IDLE.

![how-to-install-python-on-windows](https://media.geeksforgeeks.org/wp-
content/uploads/20190926121307/how-to-install-python-on-windows.png)  
This is Python Interpreter. I printed Hello geeks, python is working smoothly.

### How to install Python on Linux?

On every linux system including following OS,

* Ubuntu
* Linux Mint
* Debian
* openSUSE
* CentOS
* Fedora
* and my favourite one, Arch Linux.

You will find Python already installed. You can check it using the following
command from the terminal

    
    
    $ python --version

To check latest version of python 2.x.x :

    
    
    $ python2 --version

To check latest version of python 3.x.x :

    
    
    $ python3 --version

![how-to-install-python-on-linux](https://media.geeksforgeeks.org/wp-
content/uploads/20190926171029/how-to-install-python-on-linux.png)  
Clearly it won’t be the latest version of python. There can be multiple
methods to install python on a linux base system and it all depends on your
linux system.  
For almost every Linux system, the following commands would work definitely.

  

  

    
    
    $ sudo add-apt-repository ppa:deadsnakes/ppa
    $ sudo apt-get update
    $ sudo apt-get install python3.7
    

#### Download and install Python Latest Version on Linux

To install the latest version from source code of Python follow below steps

##### Download Python Latest Version from python.org

  * First and foremost step is to open a browser and open  
https://www.python.org/downloads/source/  
![how-to-install-python-on-linux-1](https://media.geeksforgeeks.org/wp-
content/uploads/20190926174526/how-to-install-python-on-linux-1.png)

  * Underneath the **Stable Releases** find **Download Gzipped source tarball** (latest stable release as of now is Python 3.7.4).

You can do all the above steps in a single command

    
        $ wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz

##### Install Python 3.7.4 Latest Version on Linux

For installing Python successfully on Linux, Enter Following command to get
the prerequisites and other source files

    
        $ sudo apt-get update
    $ sudo apt-get upgrade
    $ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev  libncursesw5-dev xz-utils tk-dev
    

Now we are all ready to unpack the file downloaded from the python official
website’  
Move to downloads directory using cd downloads in terminal  
and then enter following commands

    
        $ tar xvf Python-3.6.5.tgz
    $ cd Python-3.6.5
    $ ./configure --enable-optimizations --with-ensurepip=install
    $ make -j 8
    $ sudo make altinstall

Bingo..!! The latest version of Python language is installed on your Linux
system. You can confirm it using the below command.

    
        python --version

### How to install Python on macOS / Mac OS X ?

Like Linux, macOS also comes with Python pre-installed on the system. It might
be Python version 2 or some similar outdated version. To update to the latest
version, we will use the Homebrew Package manager. It is one of the best and
convenient methods to install Python on macOS.  
To know more about Homebrew Package manager, visit here

  * #### Download and install Homebrew Package Manager

If you don’t have homebrew installed on your system, follow the steps below  
Open the Terminal Application of macOS from Application -> Utilities. Bash
terminal will open where you can enter commands  
Enter following command in macOS terminal

    
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    

![install-python-on-mac](https://media.geeksforgeeks.org/wp-
content/uploads/20191001121855/install-python-on-mac.png)

Enter the system password if prompted. This will install the Homebrew package
Manager on your OS.  
After you see a message called “Installation Successful”. You are ready to
install python version 3 on your macOS.  
![install-python-on-mac-4-](https://media.geeksforgeeks.org/wp-
content/uploads/20191001121845/install-python-on-mac-4-.png)

  * #### Install Python Latest Version on macOS / macOS X

To install python simple open Terminal app from Application -> Utilities  
and enter following command

    
        brew install python3

After command processing is complete, Python’s version 3 would be installed on
your mac.  
![install-python-on-mac-2](https://media.geeksforgeeks.org/wp-
content/uploads/20191001121848/install-python-on-mac-2.png)  
To verify the installation enter following commands in your Terminal app

    
        python
    
        pip3

![install-python-on-mac-1-](https://media.geeksforgeeks.org/wp-
content/uploads/20191001121851/install-python-on-mac-1-.png)  
Bingo..!! Python is installed on your computer. You can explore more about
python here

### How to install Python on Android ?

Python can run on Android through various apps from play store library.  
This tutorial will explain how to run python on Android using Pydroid 3 – IDE
for Python 3 application.  
![how-to-install-python-android-app](https://media.geeksforgeeks.org/wp-
content/uploads/20191001122519/how-to-install-python-android-app.png)  
 **Features :**

  * Offline Python 3.7 interpreter: no Internet is required to run Python programs.
  * Pip package manager and a custom repository for prebuilt wheel packages for enhanced scientific libraries, such as numpy, scipy, matplotlib, scikit-learn and jupyter.
  * Tensorflow is now also available.
  * Examples available out-of-the-box for quicker learning.
  * Complete Tkinter support for GUI.
  * Full-featured Terminal Emulator, with a readline support (available in pip).

#### Download Pydroid 3 – IDE for Python 3 app from Play store

  * To install Pydroid app go to play store link here – Pydroid 3 – IDE for Python 3

![How-to-install-python-on-android1](https://media.geeksforgeeks.org/wp-
content/uploads/20191001105624/Hw-to-install-python-on-android1.png)

  * After installation is complete, run the app and it will show as installing python.

![Hw-to-install-python-on-android2](https://media.geeksforgeeks.org/wp-
content/uploads/20191001105621/Hw-to-install-python-on-android2.png)

  * Wait for a minute and it will show the ide. Here you can enter the Python code.

![](https://media.geeksforgeeks.org/wp-content/uploads/20191001105619/Hw-to-
install-python-on-android3.png)

  * Click on the yellow button to run the code.

![](https://media.geeksforgeeks.org/wp-content/uploads/20191001105625/How-to-
install-python-on-android.png)  
Python is installed successfully. You can check more features of this app here

### How to install Python on iOS (iPhone / iPad)?

On iOS platform, Python can be installed using various apps from app store.
One of the most popular app is Pythonista. Pythonista is a complete
development environment for writing Python™ scripts on your iPad or iPhone.
Lots of examples are included — from games and animations to plotting, image
manipulation, custom user interfaces, and automation scripts.  
You can download and buy Pythonista app from here

![how-to-install-python-on-IOS](https://media.geeksforgeeks.org/wp-
content/uploads/20191001111114/how-to-install-python-on-IOS-300x142.png)

Since most of the apps are paid on IOS and it doesn’t allow any interpreters
officially. One can run Python from online IDEs and ide.geeksforgeeks.org.

### Online Interpreters of Python

In this modern era of digital technologies, one can run Python directly from
its browser without explicitly installing Python on OS.  
Here is a list of famous IDEs for python.

    * GeeksforGeeks IDE – ide.geeksforgeeks.org
    * Python Fiddle: pythonfiddle.com
    * Python Anywhere: www.pythonanywhere.com
    * Online gdp compiler – onlinegdb.com

For expensive computations for deep learning libraries like TensorFlow,
following IDEs can be used

    * kaggle – kaggle.com
    * JuPyter/IPython Notebook – jupyter.org
    * Google Colab – colab.research.google.com

These interpreters can run Python codes easily except for complex Django codes
or TensorFlow libraries. To run such advanced applications, you need to
install Python explicitly.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

