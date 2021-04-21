Python – Remove keys with Values Greater than K ( Including mixed values )



Given a dictionary with key-value pairs, remove all the keys with values
greater than K, including mixed values.

>  **Input** : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6,
> ‘geeks’ : ‘CS’}, K = 7  
>  **Output** : {‘Gfg’ : 3, ‘for’ : 6, ‘geeks’ : ‘CS’}  
>  **Explanation** : All values greater than K are removed. Mixed value is
> retained.
>
>  **Input** : test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6,
> ‘geeks’ : ‘CS’}, K = 1  
>  **Output** : {‘geeks’ : ‘CS’}  
>  **Explanation** : Only Mixed value is retained.

 **Method #1 : Using isinstance() + loop**

This is one of the ways in which this task can be performed. In this, we use
instance to get integral values and and comparisons to get values not greater
than K.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove keys with Values Greater than K ( Including mixed values )

# Using loop + isinstance()

 

# initializing dictionary

test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10,
'for' : 6, 'geeks' : 'CS'} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 6

 

# using loop to iterate keys of dictionary

res = {}

for key in test_dict:

 

 # testing for data type and then condition, order is imp.

 if not (isinstance(test_dict[key], int) and test_dict[key]
> K):

 res[key] = test_dict[key]

 

# printing result 

print("The constructed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
    The constructed dictionary : {'Gfg': 3, 'for': 6, 'geeks': 'CS'}
    

**Method #2 : Using dictionary comprehension + isinstance()**

The combination of above functions is used to solve this problem. This
performs task similar to above method. The only difference being that it
performs in one liner using dictionary comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove keys with Values Greater than K ( Including mixed values )

# Using dictionary comprehension + isinstance()

 

# initializing dictionary

test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10,
'for' : 6, 'geeks' : 'CS'} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 6

 

# using list comprehension to perform in one line

res = {key : val for key, val in test_dict.items() if not
(isinstance(val, int) and (val > K))}

 

# printing result 

print("The constructed dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 3, 'is': 7, 'best': 10, 'for': 6, 'geeks': 'CS'}
    The constructed dictionary : {'Gfg': 3, 'for': 6, 'geeks': 'CS'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

