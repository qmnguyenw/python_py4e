Python – Similar index elements frequency



Sometimes, while working with Python list, we can have a problem in which we
need to check if one element has similar index occurrence in other list. This
can have possible application in many domains. Lets discuss certain ways in
which this task can be performed.

 **Method #1 : Usingsum() + zip()**  
The combination of above functions can be used to perform this task. In this,
we perform summation of elements that after zipping cross lists together
match.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Similar index elements frequency

# using sum() + zip()

 

# Initializing lists 

test_list1 = [1, 3, 5, 6, 8]

test_list2 = [4, 3, 6, 6, 10]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Similar index elements frequency

# using sum() + zip()

res = sum(x == y for x, y in zip(test_list1,
test_list2))

 

# printing result 

print ("Number of elements having similar index : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 5, 6, 8]
    The original list 2 is : [4, 3, 6, 6, 10]
    Number of elements having similar index : 2
    

**Method #2 : Using list comprehension +enumerate()**  
The combination of above functionalities can be used to perform this task. In
this, we iterate through each element in lists and increase the sum
accordingly.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Similar index elements frequency

# using list comprehension + enumerate()

 

# Initializing lists 

test_list1 = [1, 3, 5, 6, 8]

test_list2 = [4, 3, 6, 6, 10]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Similar index elements frequency

# using list comprehension + enumerate()

res = len([key for key, val in enumerate(zip(test_list1,
test_list2)) if val[0] == val[1]])

 

# printing result 

print ("Number of elements having similar index : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 3, 5, 6, 8]
    The original list 2 is : [4, 3, 6, 6, 10]
    Number of elements having similar index : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

