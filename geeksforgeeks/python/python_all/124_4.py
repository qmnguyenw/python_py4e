Python | Max/Min of tuple dictionary values



Sometimes, while working with data, we can have a problem in which we need to
find the min/max of tuple elements that are received as values of dictionary.
We may have a problem to get index wise min/max. Let’s discuss certain ways in
which this particular problem can be solved.

 **Method #1 : Usingtuple() + min()/max() + zip() + values()**  
The combination of above methods can be used to perform this particular task.
In this, we just  
zip together equi index values extracted by values() using zip(). Then
find min/max value using respective function. Finally result is returned as
index wise max/min values as a tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Max / Min of tuple dictionary values

# Using tuple() + min()/max() + zip() + values()

 

# Initializing dictionary

test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3,
2), 'best' : (1, 4, 9)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Max / Min of tuple dictionary values

# Using tuple() + min()/max() + zip() + values()

res = tuple(max(x) for x in
zip(*test_dict.values()))

 

# printing result

print("The maximum values from each index is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'is': (8, 3, 2), 'gfg': (5, 6, 1), 'best': (1, 4, 9)}
    The maximum values from each index is : (8, 6, 9)
    

**Method #2 : Usingtuple() + map() + values() + * operator**  
This is yet another way in which this task can be performed. The difference is
that we use map() instead of loop and * operator for zipping the values
together.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Max / Min of tuple dictionary values

# Using tuple() + map() + values() + * operator

 

# Initializing dictionary

test_dict = {'gfg' : (5, 6, 1), 'is' : (8, 3,
2), 'best' : (1, 4, 9)}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Max / Min of tuple dictionary values

# Using tuple() + map() + values() + * operator

res = tuple(map(min, *test_dict.values()))

 

# printing result

print("The minimum values from each index is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {'is': (8, 3, 2), 'gfg': (5, 6, 1), 'best': (1, 4, 9)}
    The minimum values from each index is : (1, 3, 1)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

