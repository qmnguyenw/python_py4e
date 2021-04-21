Python – Replace Non-None with K



Sometimes, while working with Python lists we can have a problem in which we
need to perform the replacment of all the elements that are non-None. This
kind of problem can have application in many domains such as web development
and day-day programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [2, None, None, 5, ”], K = 9  
>  **Output** : [9, None, None, 9, ”]
>
>  **Input** : test_list = [”, None], K = 10  
>  **Output** : [”, None]

 **Method #1 : Using list comprehension**  
This is one of the ways in which this task can be performed. In this, we
perform the task of traversing and replacement inside comprehension as one
liner using conditions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace Non-None with K

# Using list comprehension

 

# initializing list

test_list = [59, 236, None, 3, '']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing K 

K = 'Gfg'

 

# Replace Non-None with K

# Using list comprehension

res = [K if ele else ele for ele in test_list]

 

# printing result 

print("List after replacement : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [59, 236, None, 3, '']
    List after replacement : ['Gfg', 'Gfg', None, 'Gfg', '']
    

