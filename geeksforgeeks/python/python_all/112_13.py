Python – Find Keys with specific suffix in Dictionary



Sometimes, while working with dictionaries, we can have a problem in which we
need to find the dictionary items that have some constraints on keys. One such
constraint can be a suffix match on keys. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Using dictionary comprehension +endswith()**  
The combination of above two methods can be used to perform this particular
task. In this, dictionary comprehension does the basic task of dictionary
construction and endswith() performs the utility task of checking keys
starting with specific suffix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Keys with specific suffix in Dictionary

# Using dictionary comprehension + endswith()

 

# Initialize dictionary

test_dict = {'all' : 4, 'geeks' : 5, 'are' : 8,
'freaks' : 10}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize suffix

test_suf = 'ks'

 

# Using dictionary comprehension + endswith()

# Keys with specific suffix in Dictionary

res = {key:val for key, val in test_dict.items() if
key.endswith(test_suf)}

 

# printing result 

print("Filtered dictionary keys are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'geeks': 5, 'freaks': 10, 'are': 8, 'all': 4}
    Filtered dictionary keys are : {'geeks': 5, 'freaks': 10}
    

**Method #2 : Usingmap() + filter() + items() + endswith()**  
This particular task can also be performed using the combination of above
functions. The map function ties the filter logic of endswith() to each
dictionary’s items extracted by items().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Keys with specific suffix in Dictionary

# Using map() + filter() + items() + endswith()

 

# Initialize dictionary

test_dict = {'all' : 4, 'geeks' : 5, 'are' : 8,
'freaks' : 10}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Initialize suffix 

test_suf = 'ks'

 

# Using map() + filter() + items() + endswith()

# Keys with specific suffix in Dictionary

res = dict(filter(lambda item: item[0].endswith(test_suf),
test_dict.items()))

 

# printing result 

print("Filtered dictionary keys are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary : {'geeks': 5, 'freaks': 10, 'are': 8, 'all': 4}
    Filtered dictionary keys are : {'geeks': 5, 'freaks': 10}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

