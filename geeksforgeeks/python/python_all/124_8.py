Python | Get specific keys’ values



Sometimes, we require all the values, but many times, we have specified keys
of whose value list we require. This is quite common problem for web
development. Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension**  
This task can be performed using list comprehension adopted as the shorter way
to perform the longer task of checking using loop. This offers a one liner
approach to solve this problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get specific keys' values

# Using list comprehension

 

# initializing dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# initializing keys

filt_keys = ['gfg', 'best']

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Extract specific value list from dictionary

# Using list comprehension

res = [test_dict[key] for key in filt_keys]

 

# printing result

print("Filtered value list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'is': 2, 'best': 3, 'gfg': 1}
    Filtered value list is : [1, 3]
    

**Method #2 : Usingmap() + get()**  
The combination of above functions can offer a more compact solution for this
task. The map function can be used to extend the logic to whole dictionary and
get function is used to fetch key’s value.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get specific keys' values

# Using map() + get()

 

# initializing dictionary

test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

 

# initializing keys

filt_keys = ['gfg', 'best']

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Extract specific value list from dictionary

# Using map() + get()

res = list(map(test_dict.get, filt_keys))

 

# printing result

print("Filtered value list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'is': 2, 'best': 3, 'gfg': 1}
    Filtered value list is : [1, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

