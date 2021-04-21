Python – Tuple value product in dictionary



Sometimes, while working with data, we can have a problem in which we need to
find the product of tuple elements that are received as values of dictionary.
We may have a problem to get index wise product. Let’s discuss certain ways in
which this particular problem can be solved.

 **Method #1 : Usingtuple() + loop + zip() + values()**  
The combination of above methods can be used to perform this particular task.
In this, we just  
zip together equi index values extracted by values() using zip(). Then find
product using respective function. Finally result is returned as index wise
product as a tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Tuple Values Product

# Using tuple() + loop + zip() + values()

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# Initializing dictionary

test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3,
2), 'best' : (1, 4, 9)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Dictionary Tuple Values Product

# Using tuple() + loop + zip() + values()

res = tuple(prod(x) for x in zip(*test_dict.values()))

 

# printing result

print("The product from each index is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'gfg': (5, 6, 1), 'is': (8, 3, 2), 'best': (1, 4, 9)}
    The product from each index is : (40, 72, 18)
    

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

# Dictionary Tuple Values Product

# Using tuple() + map() + values()

 

# getting Product

def prod(val) :

 res = 1

 for ele in val:

 res *= ele

 return res 

 

# Initializing dictionary

test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3,
2), 'best' : (1, 4, 9)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Dictionary Tuple Values Product

# Using tuple() + map() + values()

temp = []

for sub in test_dict.values():

 temp.append(list(sub))

res = tuple(map(prod, temp))

 

# printing result

print("The product from each index is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'gfg': (5, 6, 1), 'is': (8, 3, 2), 'best': (1, 4, 9)}
    The product from each index is : (40, 72, 18)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

