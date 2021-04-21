Python | Test if string contains element from list



During web development in Python, we generally come across a problem where we
need to test if a particular element from a given list lies as sub-string or
not. This kind of problem is also very common in Machine Learning domain.
Let’s discuss certain ways in which this can be done.

 **Method #1 : Using list comprehension**  
This problem can be solved using the list comprehension, in this, we check for
the list and also with string elements if we can find a match, and return
true, if we find one and false is not using the conditional statements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# checking if string contains list element

# using list comprehension

 

# initializing string 

test_string = "There are 2 apples for 4 persons"

 

# initializing test list

test_list = ['apples', 'oranges']

 

# printing original string 

print("The original string : " + test_string)

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension

# checking if string contains list element

res = [ele for ele in test_list if(ele in test_string)]

 

# print result

print("Does string contain any list element : " +
str(bool(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : There are 2 apples for 4 persons
    The original list : ['apples', 'oranges']
    Does string contain any list element : True
    

**Method #2 : Usingany()**  
Using any function is the most classical way in which you can perform this
task and also efficiently. This function checks for match in string with match
of each element of list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# checking if string contains list element

# using list comprehension

 

# initializing string 

test_string = "There are 2 apples for 4 persons"

 

# initializing test list

test_list = ['apples', 'oranges']

 

# printing original string 

print("The original string : " + test_string)

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension

# checking if string contains list element

res = any(ele in test_string for ele in test_list)

 

# print result

print("Does string contain any list element : " + str(res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : There are 2 apples for 4 persons
    The original list : ['apples', 'oranges']
    Does string contain any list element : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

