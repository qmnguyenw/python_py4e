Python | Duplicate substring removal from list



Sometimes we can come to the problem in which we need to deal with certain
strings in a list which are separated by some separator and we need to remove
the duplicates in each of this kind of strings. Simple shorthands to solve
this kind of problems is always good to have. Let’s discuss certain ways in
which this can be done.

 **Method #1 : Usingset() + split()**  
This particular problem can be solved using the split function to have target
string and then set that actually would remove the duplicacy from the string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing duplicate substrings

# using set() + split()

 

# initializing list

test_list = [ 'aa-aa-bb', 'bb-cc', 'gg-ff-gg', 'hh-hh']

 

# printing original list

print("The original list : " + str(test_list))

 

# using set() + split()

# removing duplicate substrings

res = [set(sub.split('-')) for sub in test_list]

 

# print result

print("The list after duplicate removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['aa-aa-bb', 'bb-cc', 'gg-ff-gg', 'hh-hh']
    The list after duplicate removal : [{'aa', 'bb'}, {'cc', 'bb'}, {'gg', 'ff'}, {'hh'}]
    

**Method #2 : Using{} \+ split() \+ list comprehension**  
For the cases in which we require to fully segregate the strings as a separate
component, we can use these set of methods to achieve this task. The curly
braces convert to set and rest all the functionality is similar to method
above.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removing duplicate substrings

# using {} + split() + list comprehension

 

# initializing list

test_list = [ 'aa-aa-bb', 'bb-cc', 'gg-ff-gg', 'hh-hh']

 

# printing original list

print("The original list : " + str(test_list))

 

# using {} + split() + list comprehension

# removing duplicate substrings

res = list({i for sub in test_list for i in
sub.split('-')})

 

# print result

print("The list after duplicate removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['aa-aa-bb', 'bb-cc', 'gg-ff-gg', 'hh-hh']
    The list after duplicate removal : ['cc', 'ff', 'aa', 'hh', 'gg', 'bb']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

