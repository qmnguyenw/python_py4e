Increment and Decrement Operators in Python



If you’re familiar with Python, you would have known Increment and Decrement
operators ( both pre and post) are not allowed in it.

Python is designed to be consistent and readable. One common error by a novice
programmer in languages with ++ and -- operators is mixing up the differences
(both in precedence and in return value) between pre and post
increment/decrement operators. Simple increment and decrement operators aren’t
needed as much as in other languages.

You don’t write things like :

    
    
    for (int i = 0; i < 5; ++i)
    

In Python, instead we write it like below and syntax is as follow:

 **for variable_name in range(start, stop, step)**

  

  

  * start: Optional. An integer number specifying at which position to start. Default is 0
  * stop: An integer number specifying at which position to end.
  * step: Optional. An integer number specifying the incrementation. Default is 1

 __

 __  
 __

 __

 __  
 __  
 __

# A Sample Python program to show loop (unlike many

# other languages, it doesn't use ++)

# this is for increment operator here start = 1, 

# stop = 5 and step = 1(by default)

print("INCREMENTED FOR LOOP")

for i in range(0, 5):

 print(i)

 

# this is for increment operator here start = 5, 

# stop = -1 and step = -1 

print("\n DECREMENTED FOR LOOP")

for i in range(4, -1, -1):

 print(i)  
  
---  
  
 __

 __

    
    
     **Output-1:** INCREMENTED FOR LOOP
    0
    1
    2
    3
    4
    **Output-2:** DECREMENTED FOR LOOP
    4
    3
    2
    1
    0
    

This article is contributed by Basavaraja. If you like GeeksforGeeks and would
like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
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

