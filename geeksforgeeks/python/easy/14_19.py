Autorun a Python script on windows startup



Adding a Python script to windows start-up basically means the python script
will run as the windows boots up. This can be done by two step processe –

 **Step #1:** **Adding script to windows Startup folder**  
After the windows boots up it runs (equivalent to double-clicking) all the
application present in its startup directory.  
 **Address:**

> C:\Users\current_user\AppData\Roaming\Microsoft\Windows\Start
> Menu\Programs\Startup\

By default the AppData folder under the _current_user_ is hidden so enable
hidden files to get it and paste the shortcut of the script in the given
address or the script itself. Also the **.PY** files default must be set to
python IDE else the script may end up opening as a text instead of executing.  
  
**Step #2:** **Adding script to windows Registry**  
This process can be risky if not done properly, it involves editing the
windows registry key _HKEY_CURRENT_USER_ from the python script itself. This
registry contains the list of programs that must run once the user Login. just
like few application which pops up when windows starts because the cause
change in registry and add their application path to it.

 **Registry Path:**

  

  

> HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run

Below is the Python code :

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to add current script to the registry

 

# module to edit the windows registry 

import winreg as reg 

import os 

 

def AddToRegistry():

 

 # in python __file__ is the instant of

 # file path where it was executed 

 # so if it was executed from desktop,

 # then __file__ will be 

 # c:\users\current_user\desktop

 pth = os.path.dirname(os.path.realpath(__file__))

 

 # name of the python file with extension

 s_name="mYscript.py"

 

 # joins the file name to end of path address

 address=os.join(pth,s_name) 

 

 # key we want to change is HKEY_CURRENT_USER 

 # key value is Software\Microsoft\Windows\CurrentVersion\Run

 key = HKEY_CURRENT_USER

 key_value = "Software\Microsoft\Windows\CurrentVersion\Run"

 

 # open the key to make changes to

 open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)

 

 # modifiy the opened key

 reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address)

 

 # now close the opened key

 reg.CloseKey(open)

 

# Driver Code

if __name__=="__main__":

 AddToRegistry()  
  
---  
  
 __

 __

 **Note:** Further codes can be added to this script for the task to be
performed at every startup and the script must be **run as Administrator** for
the first time.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

