Python – Resolve Float Keys in Dictionary



Given a dictionary with variety of floating-point keys, find a way to access
them as single value.

>  **Input** : test_dict = {“010.78” : “Gfg”, “9.0” : “is”, “10” : “Best”}, K
> = “09.0”  
>  **Output** : “is”  
>  **Explanation** : 09.0 -> 9.0 whose value is “is”.
>
>  **Input** : test_dict = {“010.78” : “Gfg”, “9.0” : “is”, “10” : “Best”}, K
> = “10.0”  
>  **Output** : “Best”  
>  **Explanation** : 10.0 -> 10 whose value is “Best”.

 **Method #1 : Using float() + loop**

This is one of the ways to solve this problem. In this, strategy used is to
convert key into float value using float(), it resolves to single value, and
perform check of input string after conversion to float(), both resolve to
common float value.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Resolve Float Keys in Dictionary

# Using float() + loop()

 

# initializing dictionary

test_dict = {"010.78" : "Gfg", "9.0" : "is", "10" :
"Best"}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = "10.78"

 

# performing resolution

res = dict()

for key in test_dict:

 res[float(key)] = test_dict[key]

 

# converting compare value to float 

convK = float(K)

 

# performing value access 

res = res[convK]

 

# printing result 

print("Value of resolved float Key : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'010.78': 'Gfg', '9.0': 'is', '10': 'Best'}
    Value of resolved float Key : Gfg
    

**Method #2 : Using dictionary comprehension + float()**

This computes in similar way as above method. The difference being for
conversion one liner dictionary comprehension is employed.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Resolve Float Keys in Dictionary

# Using dictionary comprehension + float()

 

# initializing dictionary

test_dict = {"010.78" : "Gfg", "9.0" : "is", "10" :
"Best"}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = "10.78"

 

# performing resolution using dictionary comprehension

res = {float(key) : test_dict[key] for key in test_dict}

 

# converting compare value to float 

convK = float(K)

 

# performing value access 

res = res[convK]

 

# printing result 

print("Value of resolved float Key : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'010.78': 'Gfg', '9.0': 'is', '10': 'Best'}
    Value of resolved float Key : Gfg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

