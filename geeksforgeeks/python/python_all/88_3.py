Python – Replace index elements with elements in Other List



Sometimes, while working with Python data, we can have a problem in which we
have two lists and we need to replace positions in one list with the actual
elements from other list. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using list comprehension**  
This is one way to solve this problem. In this we just iterate through the
list and assign the index value from one list to other.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Replace index elements with elements in Other List

# using list comprehension

 

# Initializing lists

test_list1 = ['Gfg', 'is', 'best']

test_list2 = [0, 1, 2, 1, 0, 0, 0, 2,
1, 1, 2, 0]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Replace index elements with elements in Other List

# using list comprehension

res = [test_list1[idx] for idx in test_list2]

 

# printing result 

print ("The lists after index elements replacements is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [‘Gfg’, ‘is’, ‘best’]  
> The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]  
> The lists after index elements replacements is : [‘Gfg’, ‘is’, ‘best’, ‘is’,
> ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’]

  

  

**Method #2 : Usingmap() \+ lambda**  
The combination of above functions can be used to perform this task. In this,
we perform task of extension of logic to every element using map() and lambda
functions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Replace index elements with elements in Other List

# using map() + lambda

 

# Initializing lists

test_list1 = ['Gfg', 'is', 'best']

test_list2 = [0, 1, 2, 1, 0, 0, 0, 2,
1, 1, 2, 0]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Replace index elements with elements in Other List

# using map() + lambda

res = list(map(lambda idx: test_list1[idx], test_list2))

 

# printing result 

print ("The lists after index elements replacements is : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [‘Gfg’, ‘is’, ‘best’]  
> The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]  
> The lists after index elements replacements is : [‘Gfg’, ‘is’, ‘best’, ‘is’,
> ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

