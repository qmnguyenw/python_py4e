Python | Unpacking dictionary keys into tuple



In certain cases, we might come in a problem in which we require to unpack
dictionary keys to tuples. This kind of problem can occur in cases we are just
concerned of keys of dictionaries and wish to have a tuple of it. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Usingtuple()**

The simple type casting of dictionary into a tuple in fact does the required
task. This function takes just the keys and converts them into key tuple as
required.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unpacking dictionary keys into tuple

# Using tuple()

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using tuple()

# Unpacking dictionary keys into tuple

res = tuple(test_dict)

 

# printing result

print("The unpacked dict. keys into tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 3, 'is': 2, 'Gfg': 1}
    The unpacked dict. keys into tuple is :  ('best', 'is', 'Gfg')
    

  

  

**Method #2 : Using"=" operator and multiple variables**  
This method can also be used to perform this particular task. In this, we
assign the comma separated variables to the dictionary. We use as many
variables as keys in dictionary. This method is not recommended in case of
unknown or many keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unpacking dictionary keys into tuple

# Using "=" operator and multiple variables

 

# initializing dictionary

test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using "=" operator and multiple variables

# Unpacking dictionary keys into tuple

a, b, c = test_dict

res = a, b, c

 

# printing result

print("The unpacked dict. keys into tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'best': 3, 'is': 2, 'Gfg': 1}
    The unpacked dict. keys into tuple is :  ('best', 'is', 'Gfg')
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

