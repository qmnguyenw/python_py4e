Python – Summation of tuple dictionary values



Sometimes, while working with data, we can have a problem in which we need to
find the summation of tuple elements that are received as values of
dictionary. We may have a problem to get index wise summation. Let’s discuss
certain ways in which this particular problem can be solved.

 **Method #1 : Usingtuple() + sum() + zip() + values()**  
The combination of above methods can be used to perform this particular task.
In this, we just zip together equi index values extracted by values() using
zip(). Then find summation using respective function. Finally result is
returned as index wise summation as a tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of tuple dictionary values

# Using tuple() + sum() + zip() + values()

 

# Initializing dictionary

test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3,
2), 'best' : (1, 4, 9)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Summation of tuple dictionary values

# Using tuple() + sum() + zip() + values()

res = tuple(sum(x) for x in
zip(*test_dict.values()))

 

# printing result

print("The summation from each index is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'is': (8, 3, 2), 'best': (1, 4, 9), 'gfg': (5, 6, 1)}
    The summation from each index is : (14, 13, 12)
    

**Method #2 : Usingtuple() + map() + values()**  
This is yet another way in which this task can be performed. The difference is
that we use map() instead of loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Summation of tuple dictionary values

# Using tuple() + map() + values()

 

# Initializing dictionary

test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3,
2), 'best' : (1, 4, 9)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Summation of tuple dictionary values

# Using tuple() + map() + values()

temp = []

for sub in test_dict.values():

 temp.append(list(sub))

res = tuple(map(sum, temp))

 

# printing result

print("The summation from each index is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'is': (8, 3, 2), 'best': (1, 4, 9), 'gfg': (5, 6, 1)}
    The summation from each index is : (14, 13, 12)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

