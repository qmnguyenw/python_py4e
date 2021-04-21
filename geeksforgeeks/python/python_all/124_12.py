Python | Finding ‘n’ Character Words in a Text File



This article aims to find words with a certain number of character. In the
code mentioned below, a python program is given to find the words contain
three characters in the text file.

 **Examples:**

>  **Input :** Hello, how are you ?
>
>  **Output :**  
>  how  
> are  
> you

 **Code: Python program to find the words contain three characters in the text
file**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

count= 1

chrw = ""

 

# text file

file = open('textfile.txt', 'r')

while 1:

 sp = file.read(1)

 

 if count<= 3:

 chrw = chrw + sp

 

 if count>3:

 if sp ==" ":

 count = 0

 if len(chrw)>0:

 print(chrw)

 chrw =""

 elif sp !=" ":

 chrw =""

 count = count + 1

 

 if not sp:

 break

 

file.close()   
  
---  
  
__

__

**Output:**

    
    
     **how 
    are 
    you**

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

