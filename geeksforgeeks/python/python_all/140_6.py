Python | Convert None to empty string



Sometimes, while working with Machine Learning, we can encounter None values
and we wish to convert to the empty string for data consistency. This and many
other utilities can require the solution to this problem. Let’s discuss
certain ways in which this problem can be solved.

 **Method #1 : Using lambda**  
This task can be performed using the lambda function. In this we check for
string for None or empty string using the or operator and replace the None
values with empty string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Converting None to empty string

# Using lambda

 

# initializing list of strings

test_list = ["Geeks", None, "CS", None, None]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# using lambda

# Converting None to empty string

conv = lambda i : i or ''

res = [conv(i) for i in test_list]

 

# printing result 

print("The list after conversion of None values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Geeks', None, 'CS', None, None]
    The list after conversion of None values : ['Geeks', '', 'CS', '', '']
    

**Method #2 : Usingstr()**  
Simply the str function can be used to perform this particular task because,
None also evaluates to a “False” value and hence will not be selected and
rather a string converted false which evaluates to empty string is returned.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Converting None to empty string

# Using str()

 

# initializing list of strings

test_list = ["Geeks", None, "CS", None, None]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# using str()

# Converting None to empty string

res = [str(i or '') for i in test_list]

 

# printing result 

print("The list after conversion of None values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Geeks', None, 'CS', None, None]
    The list after conversion of None values : ['Geeks', '', 'CS', '', '']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

