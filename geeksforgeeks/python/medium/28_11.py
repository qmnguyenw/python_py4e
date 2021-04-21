Quine in Python



Quine is a program which takes no input but outputs a copy of its own code. We
have discussed quine in C.

The shortest possible quine in python is just a single line of code!

 __

 __  
 __

 __

 __  
 __  
 __

_='_=%r;print _%%_';print _%_  
  
---  
  
 __

 __

In case of Python3.x

 __

 __  
 __

 __

 __  
 __  
 __

_='_=%r;print (_%%_)';print (_%_)  
  
---  
  
 __

 __

 **Explanation:**  
The above code is a classic use of string formatting. Firstly, we are defining
a variable ___ and assigning it ‘_=%r;print _%%_’. Secondly, we are printing
__%__. Here we are printing _ with _ as input to string formatting. So _%r_ in
_ gets the value of _. You can even use _%s_ instead of _%r_. We used double
_%_ in ‘_=%r;print _%%_’ to escape _%_.

But you may say that the below code is the smallest, right!

  

  

 __

 __  
 __

 __

 __  
 __  
 __

print open(__file__).read()  
  
---  
  
 __

 __

You need to note that it is indeed the smallest python program that can print
its own source code but it is not a quine because a quine should not use
_open()_ function to print out its source code.

This article is contributed by **Sri Sanketh Uppalapati**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

