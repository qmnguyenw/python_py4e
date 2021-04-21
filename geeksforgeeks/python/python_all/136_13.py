Python | Remove Keys from dictionary starting with K



Sometimes, while working with dictionaries, we can have a particular use case
in which we need to remove certain keys. There can be many criteria upon which
we may need to perform this task. One such criteria can be removal on basis of
starting substring. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using Naive method +startswith() + pop()**  
This particular task can be performed using combination of above functions,
which is a brute force method to perform this task. The pop function is used
to remove the key value pair and startswith provide the condition upon which
this has to be performed.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Keys from dictionary starting with K

# Using Naive Method + startswith() + pop()

 

# initializing dictionary

test_dict = {"Apple" : 1, "Star" : 2, "App" : 4,
"Gfg" : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing Substring 

K = "Ap"

 

# Using Naive Method + startswith() + pop()

# Remove Keys from dictionary starting with K

res = list(test_dict.keys())

for key in res:

 if key.startswith(K):

 test_dict.pop(key)

 

# printing result 

print("Dictionary after key removal : " + str(test_dict))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Apple': 1, 'Star': 2, 'App': 4, 'Gfg': 3}
    Dictionary after key removal : {'Star': 2, 'Gfg': 3}
    

**Method #2 : Using list comprehension + dict() + startswith() + items()**  
There is also 1 liner alternative to perform this particular task in which we
get all the keys and values using items() and then reconstruct the
dictionary with keys that do not start with K using startswith function. The
dict function at the end performs the conversion from list to dictionary.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Keys from dictionary starting with K

# Using list comprehension + dict() + startswith() + items()

 

# initializing dictionary

test_dict = {"Apple" : 1, "Star" : 2, "App" : 4,
"Gfg" : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing Substring 

K = "Ap"

 

# Using list comprehension + dict() + startswith() + items()

# Remove Keys from dictionary starting with K

res = dict( [(x, y) for x, y in test_dict.items() if not
x.startswith(K)] )

 

# printing result 

print("Dictionary after key removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'Apple': 1, 'Star': 2, 'App': 4, 'Gfg': 3}
    Dictionary after key removal : {'Star': 2, 'Gfg': 3}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

