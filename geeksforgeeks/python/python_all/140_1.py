Python | Get matching substrings in string



The testing of a single substring in a string has been discussed many times.
But sometimes, we have a list of potential substrings and check which ones
occur in a target string as a substring. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Using list comprehension**  
Using list comprehension is the naive and brute force method to perform this
particular task. In this method, we try to get the matching string using the
“in” operator and store it in new list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get matching substrings in string

# Using list comprehension

 

# initializing string 

test_str = "GfG is good website"

 

# initializing potential substrings

test_list = ["GfG", "site", "CS", "Geeks", "Tutorial"
]

 

# printing original string 

print("The original string is : " + test_str)

 

# printing potential strings list

print("The original list is : " + str(test_list))

 

# using list comprehension

# Get matching substrings in string

res = [sub for sub in test_list if sub in test_str]

 

# printing result 

print("The list of found substrings : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GfG is good website
    The original list is : ['GfG', 'site', 'CS', 'Geeks', 'Tutorial']
    The list of found substrings : ['GfG', 'site']
    

**Method #2 : Usingfilter() \+ lambda**  
This task can also be performed using the filter function which performs the
task of filtering out the resultant strings that is checked for existence
using the lambda function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get matching substrings in string

# Using lambda and filter()

 

# initializing string 

test_str = "GfG is good website"

 

# initializing potential substrings

test_list = ["GfG", "site", "CS", "Geeks", "Tutorial"
]

 

# printing original string 

print("The original string is : " + test_str)

 

# printing potential strings list

print("The original list is : " + str(test_list))

 

# using lambda and filter()

# Get matching substrings in string

res = list(filter(lambda x: x in test_str, test_list))

 

# printing result 

print("The list of found substrings : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GfG is good website
    The original list is : ['GfG', 'site', 'CS', 'Geeks', 'Tutorial']
    The list of found substrings : ['GfG', 'site']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

