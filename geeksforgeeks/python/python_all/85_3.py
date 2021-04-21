Python – Replace all repeated occurrences with N



Sometimes, while working with Python list, we can have a problem in which we
need to replace an element with another. But one can have variations of these
such as increase of number and keeping the first occurrence. This can have
applications in various domains. Lets discuss certain ways in which this task
can be performed.

 **Method #1 : Usingenumerate() + set() \+ loop**  
The combination of above functions can be used to perform this task. In this,
we iterate the list and then store the 1st occurrence in set, the consecutive
values are tested using in and replaced inplace.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Replace all repeated occurrences of K with N

# using enumerate() + set() + loop

 

# Initializing list

test_list = [1, 3, 3, 1, 4, 4, 1, 5,
5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing N 

N = 'rep'

 

# Replace all repeated occurrences of K with N

# using enumerate() + set() + loop

his = set([])

for idx, ele in enumerate(test_list):

 if ele in his:

 test_list[idx] = N

 his.add(ele)

 

# printing result 

print ("The duplication altered list : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 3, 1, 4, 4, 1, 5, 5]
    The duplication altered list : [1, 3, 'rep', 'rep', 4, 'rep', 'rep', 5, 'rep']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

