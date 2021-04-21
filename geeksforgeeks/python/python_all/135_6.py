Python | Reversed Order keys in dictionary



While working with dictionary, we can sometimes, have a problem in which we
require to print dictionaries in the reversed order of their occurrence. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Usingreversed() + sorted() + keys() \+ loop**  
The combination of above functions can be used to perform this particular
task. The sorted function is used to sort the keys and reversed gets the
keys extracted using keys(), in descending order, which are printed using a
loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reversed Order keys in dictionary

# Using sorted() + keys() + reversed() + loop

 

# initializing dictionary

test_dict = {1 : "Gfg", 5 : "is", 4 : "the", 2
: "best"}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using sorted() + keys() + reversed() + loop

# Reversed Order keys in dictionary

res = []

for ele in reversed(sorted(test_dict.keys())):

 res.append(ele)

 

# printing result 

print("The reversed order of dictionary keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {1: 'Gfg', 2: 'best', 4: 'the', 5: 'is'}
    The reversed order of dictionary keys : [5, 4, 2, 1]
    

**Method #2 : Usinglist() + keys() + sorted() + reversed()**  
It is another method in which this task can be solved. This is just a small
variation of the above method, in this the list function is used to convert
the result to list rather than using the loop to print the variables.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reversed Order keys in dictionary

# Using sorted() + keys() + reversed() + list()

 

# initializing dictionary

test_dict = {1 : "Gfg", 5 : "is", 4 : "the", 2
: "best"}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using sorted() + keys() + reversed() + list()

# Reversed Order keys in dictionary

res = list(reversed(sorted(test_dict.keys())))

 

# printing result 

print("The reversed order of dictionary keys : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {1: 'Gfg', 2: 'best', 4: 'the', 5: 'is'}
    The reversed order of dictionary keys : [5, 4, 2, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

