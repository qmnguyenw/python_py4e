Python – List with most unique elements



Sometimes, while working with data, we can have a problem in which we need to
compute the list which has most number of unique elements. This can have
application in many domains. Lets discuss certain ways in which this task can
be performed.

 **Method #1 : Using list comprehension +max() + set()**  
The combination of above functionalities can be used to solve this problem. In
this, we compute the maximum occurring elements using max() and reduce the
logic to uniqueness using set().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# List with most unique elements

# using list comprehension + max() + set()

 

# Initializing lists

test_list1 = [1, 3, 4, 4, 4, 3, 3, 2,
2, 1]

test_list2 = [1, 3, 4, 6, 7]

test_list3 = [4, 5, 4, 3, 6, 7, 8]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

print("The original list 3 is : " + str(test_list3))

 

# List with most unique elements

# using list comprehension + max() + set()

res = [ele for ele in [set(test_list1), set(test_list2),
set(test_list3)]

 if len(ele) == max([len(sub) for sub in
[set(test_list1), set(test_list2), set(test_list3)]])][0]

 

# printing result 

print ("List with Most unique values : " + str(list(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 4, 4, 4, 3, 3, 2, 2, 1]
    The original list 2 is : [1, 3, 4, 6, 7]
    The original list 3 is : [4, 5, 4, 3, 6, 7, 8]
    List with Most unique values : [3, 4, 5, 6, 7, 8]
    

**Method #2 : Usingmax() + set() \+ key**  
This task can also be performed using combination of above functions. In this,
we extract the maximum frequency list using max() and key argument len.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# List with most unique elements

# using key + max() + set()

 

# Initializing lists

test_list1 = [1, 3, 4, 4, 4, 3, 3, 2,
2, 1]

test_list2 = [1, 3, 4, 6, 7]

test_list3 = [4, 5, 4, 3, 6, 7, 8]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

print("The original list 3 is : " + str(test_list3))

 

# List with most unique elements

# using key + max() + set()

temp = [set(test_list1), set(test_list2), set(test_list3)]

res = max(temp, key = len)

 

# printing result 

print ("List with Most unique values : " + str(list(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 4, 4, 4, 3, 3, 2, 2, 1]
    The original list 2 is : [1, 3, 4, 6, 7]
    The original list 3 is : [4, 5, 4, 3, 6, 7, 8]
    List with Most unique values : [3, 4, 5, 6, 7, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

