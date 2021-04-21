How to Brute Force ZIP File Passwords in Python?



In this article, we will see a Python program that will crack the zip file’s
password using the brute force method.

The ZIP file format is a common archive and compression standard. It is used
to compress files. Sometimes, compressed files are confidential and the owner
doesn’t want to give its access to every individual. Hence, the zip file is
protected with a password. If the password is common then it’s easily crack-
able. Here, we’ll use the brute force method to crack the zip file’s password.

A brute force method is a method where a set of predefined values are used to
crack a password until successful. This is basically a “hit and try” method.
This method might take a long time if the set of values are high, but its
success rate is high. The more the number of values, the greater the chances
of cracking passwords. Here we’ll be using “rockyou” text file of size 133 MB
with over 14 million sets of passwords to try. Download the text file here.

 **Approach:**

  * First, import the zipfile module.
  * Initialize the ZipFile object which helps in extracting the contents of the zip file.
  * Count the number of words present in “rockyou.txt” file and display it on the terminal.
  * Call the “crack_password” function which returns true if a password is found else returns false. Pass the name of the text file and the ZipFile object as parameters.
  * idx variable is used to keep track of line numbers.
  * Open the text file “rockyou.txt” in “rb” mode in order to handle file contents in binary form. This is because the file contains some special symbols which can’t be handled if the file is opened in “r” mode and will generate **UnicodeDecodeError**.
  * After opening the file, extract the line from the file and then split the word from it.
  * In the try block, extract the contents of the zip file by giving the password to pwd field of extractall method. **extractall()** method will extract all the contents of the zip file to the current working directory. The above program extracts a zip file named “gfg.zip” in the same directory as this python script.
  * If the password is incorrect, an exception will be generated. In except block, continue the loop to check other words in the file.
  * If the password is found return true else at last return false and display the desired message.

 **Below is the full implementation:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import zipfile

 

 

def crack_password(password_list, obj):

 # tracking line no. at which password is found

 idx = 0

 

 # open file in read byte mode only as "rockyou.txt"

 # file contains some special characters and hence

 # UnicodeDecodeError will be generated

 with open(password_list, 'rb') as file:

 for line in file:

 for word in line.split():

 try:

 idx += 1

 obj.extractall(pwd=word)

 print("Password found at line", idx)

 print("Password is", word.decode())

 return True

 except:

 continue

 return False

 

 

password_list = "rockyou.txt"

 

zip_file = "gfg.zip"

 

# ZipFile object initialised

obj = zipfile.ZipFile(zip_file)

 

# count of number of words present in file

cnt = len(list(open(password_list, "rb")))

 

print("There are total", cnt,

 "number of passwords to test")

 

if crack_password(password_list, obj) == False:

 print("Password not found in this file")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210201215044/Screenshotfrom20210201214613.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

