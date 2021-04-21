Python | Shuffle two lists with same order



Sometimes, while working with Python list, we can have a problem in which we
need to perform shuffle operation in list. This task is easy and there are
straightforward functionalities available in Python to perform this. But
sometimes, we need to shuffle two lists so that their shuffle orders are
consistent. Let’s discuss a way in which this task can be performed.

 **Method : Usingzip() + shuffle() \+ * operator**  
In this method, this task is performed in three steps. Firstly, the lists are
zipped together using zip(). Next step is to perform shuffle using inbuilt
shuffle() and last step is to unzip the lists to separate lists using *
operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Shuffle two lists with same order

# Using zip() + * operator + shuffle()

import random

 

# initializing lists

test_list1 = [6, 4, 8, 9, 10]

test_list2 = [1, 2, 3, 4, 5]

 

# printing lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Shuffle two lists with same order

# Using zip() + * operator + shuffle()

temp = list(zip(test_list1, test_list2))

random.shuffle(temp)

res1, res2 = zip(*temp)

 

# Printing result

print("List 1 after shuffle : " + str(list(res1)))

print("List 2 after shuffle : " + str(list(res2)))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list 1 : [6, 4, 8, 9, 10]
    The original list 2 : [1, 2, 3, 4, 5]
    List 1 after shuffle : [6, 10, 4, 8, 9]
    List 2 after shuffle : [1, 5, 2, 3, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

