Python – Sort Dictionary by Values Summation



Give a dictionary with value lists, sort the keys by summation of values in
value list.

>  **Input** : test_dict = {‘Gfg’ : [6, 7, 4], ‘best’ : [7, 6, 5]}  
>  **Output** : {‘Gfg’: 17, ‘best’: 18}  
>  **Explanation** : Sorted by sum, and replaced.
>
>  **Input** : test_dict = {‘Gfg’ : [8], ‘best’ : [5]}  
>  **Output** : {‘best’: 5, ‘Gfg’: 8}  
>  **Explanation** : Sorted by sum, and replaced.

 **Method #1 : Using sorted() + dictionary comprehension + sum()**

The combination of above functions can be used to solve this problem. In this,
we first sum all the list elements using sum() and then next step is to
perform sorting of all the keys according to sum extracted using sorted().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary by Values Summation

# Using dictionary comprehension + sum() + sorted()

 

# initializing dictionary

test_dict = {'Gfg' : [6, 7, 4], 'is' : [4, 3,
2], 'best' : [7, 6, 5]} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# summing all the values using sum()

temp1 = {val: sum(int(idx) for idx in key) 

 for val, key in test_dict.items()}

 

# using sorted to perform sorting as required

temp2 = sorted(temp1.items(), key = lambda ele :
temp1[ele[0]])

 

# rearrange into dictionary

res = {key: val for key, val in temp2}

 

# printing result 

print("The sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 7, 4], 'is': [4, 3, 2], 'best': [7, 6, 5]}
    The sorted dictionary : {'is': 9, 'Gfg': 17, 'best': 18}
    

**Method #2 : Using map() + dictionary comprehension + sorted() + sum()**

The combination of above functions can be used to solve this problem. In this,
we perform the task of mapping the logic of summation using map().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary by Values Summation

# Using map() + dictionary comprehension + sorted() + sum()

 

# initializing dictionary

test_dict = {'Gfg' : [6, 7, 4], 'is' : [4, 3,
2], 'best' : [7, 6, 5]} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# summing all the values using sum()

# map() is used to extend summation to sorted()

temp = {key: sum(map(lambda ele: ele, test_dict[key])) for
key in test_dict}

res = {key: temp[key] for key in sorted(temp, key =
temp.get)} 

 

# printing result 

print("The sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 7, 4], 'is': [4, 3, 2], 'best': [7, 6, 5]}
    The sorted dictionary : {'is': 9, 'Gfg': 17, 'best': 18}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

