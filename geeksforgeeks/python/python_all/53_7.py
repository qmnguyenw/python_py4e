Python – Dictionary Values Mean



Given a dictionary, find mean of all the values present.

>  **Input** : test_dict = {“Gfg” : 4, “is” : 4, “Best” : 4, “for” : 4,
> “Geeks” : 4}  
>  **Output** : 4.0  
>  **Explanation** : (4 + 4 + 4 + 4 + 4) / 4 = 4.0, hence mean.
>
>  **Input** : test_dict = {“Gfg” : 5, “is” : 10, “Best” : 15}  
>  **Output** : 10.0  
>  **Explanation** : Mean of these is 10.0

 **Method #1 : Using loop + len()**

This is brute way in which this task can be performed. In this, we loop
through each value and perform summation and then the result is divided by
total keys extracted using len().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Values Mean

# Using loop + len()

 

# initializing dictionary

test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8,
"for" : 6, "Geeks" : 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# loop to sum all values 

res = 0

for val in test_dict.values():

 res += val

 

# using len() to get total keys for mean computation

res = res / len(test_dict)

 

# printing result 

print("The computed mean : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 4, 'is': 7, 'Best': 8, 'for': 6, 'Geeks': 10}
    The computed mean : 7.0
    

**Method #2 : Using sum() + len() + values()**

The combination of above functions can be used to solve this problem. In this,
we perform summation using sum() and size() of total keys computed using
len().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Values Mean

# Using sum() + len() + values()

 

# initializing dictionary

test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8,
"for" : 6, "Geeks" : 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# values extracted using values()

# one-liner solution to problem.

res = sum(test_dict.values()) / len(test_dict)

 

# printing result 

print("The computed mean : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 4, 'is': 7, 'Best': 8, 'for': 6, 'Geeks': 10}
    The computed mean : 7.0
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

