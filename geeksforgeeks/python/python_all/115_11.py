Python | Consecutive String Comparison



Sometimes, while working with data, we can have a problem in which we need to
perform comparison between a string and it’s next element in a list and return
all strings whose next element is similar list. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Usingzip() \+ loop**  
This is one way in which this task can be performed. In this, we use zip() to
combine the element and it’s next element and then compare for truth and save
it in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive String Comparison

# using zip() + loop

 

# initialize list 

test_list = ['gfg', 'gfg', 'is', 'best', 'best',
'for', 'geeks', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Consecutive String Comparison

# using zip() + loop

res = []

for i, j in zip(test_list, test_list[1: ]):

 if i == j:

 res.append(i)

 

# printing result

print("List of Consecutive similar elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'gfg', 'is', 'best', 'best', 'for', 'geeks', 'geeks']
    List of Consecutive similar elements : ['gfg', 'best', 'geeks']
    

**Method #2 : Using list comprehension + zip()**  
This task can also be performed using above functionalities. In this, we use
one-liner approach to solve this problem using list comprehension. The method
is similar to above one.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive String Comparison

# using zip() + list comprehension

 

# initialize list 

test_list = ['gfg', 'gfg', 'is', 'best', 'best',
'for', 'geeks', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Consecutive String Comparison

# using zip() + list comprehension

res = [i for (i, j) in zip(test_list, test_list[1:]) if
i == j]

 

# printing result

print("List of Consecutive similar elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'gfg', 'is', 'best', 'best', 'for', 'geeks', 'geeks']
    List of Consecutive similar elements : ['gfg', 'best', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

