Python – Sort dictionary by max/min element in value list



Given dictionary, perform sort on basis of maximum or minimum element present
in dictionary values list.

>  **Input** : test_dict = {“Gfg” : [6, 4], “best” : [8, 4], “for” : [7, 13],
> “geeks” : [15, 5]}  
>  **Output** : {‘geeks’: [15, 5], ‘for’: [7, 13], ‘best’: [8, 4], ‘Gfg’: [6,
> 4]}  
>  **Explanation** : Max of values is 15, occurs in “geeks” key, hence at 1st
> position and so on.
>
>  **Input** : test_dict = {“Gfg” : [6, 4], “best” : [8, 4]}  
>  **Output** : {‘best’: [8, 4], ‘Gfg’: [6, 4]}  
>  **Explanation** : Max of values is 8, occurs in “best” key, hence at 1st
> position and so on.

 **Method #1 : Using sorted() + max() + dictionary comprehension + reverse +
lambda**

The combination of above functions can be used to solve this problem. In this,
we perform the task of sorting using sorted(), maximum is extracted using
max(), reverse is used to get maximum element 1st and lambda function is used
to extent max() logic to sorted function.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort dictionary by max / min element in value list

# Using sorted() + max() + dictionary comprehension + reverse + lambda

 

# initializing dictionary

test_dict = {"Gfg" : [6, 4], "is" : [10, 3],
"best" : [8, 4],

 "for" : [7, 13], "geeks" : [15, 5]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# lambda function driving maximum operation on sorted()

# dictionary comprehension used to reconstruct dictionary

res = {key: test_dict[key] for key in sorted(test_dict, key
= lambda ele: max(test_dict[ele]),

 reverse = True)}

 

# printing result 

print("Reverse Sorted dictionary on basis of max values : " +
str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 4], 'is': [10, 3], 'best': [8, 4], 'for': [7, 13], 'geeks': [15, 5]}
    Reverse Sorted dictionary on basis of max values : {'geeks': [15, 5], 'for': [7, 13], 'is': [10, 3], 'best': [8, 4], 'Gfg': [6, 4]}
    

**Method #2 : Using sorted() + min() + dictionary comprehension + reverse +
lambda**

This is similar method to above function, the only difference being that we
perform sort on basis of highest minimum value in dictionary values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort dictionary by max / min element in value list

# Using sorted() + min() + dictionary comprehension + reverse + lambda

 

# initializing dictionary

test_dict = {"Gfg" : [6, 4], "is" : [10, 3],
"best" : [8, 4],

 "for" : [7, 13], "geeks" : [15, 5]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# lambda function driving minimum operation on sorted()

# dictionary comprehension used to reconstruct dictionary

res = {key: test_dict[key] for key in sorted(test_dict, key
= lambda ele: min(test_dict[ele]),

 reverse = True)}

 

# printing result 

print("Reverse Sorted dictionary on basis of min values : " +
str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [6, 4], 'is': [10, 3], 'best': [8, 4], 'for': [7, 13], 'geeks': [15, 5]}
    Reverse Sorted dictionary on basis of min values : {'for': [7, 13], 'geeks': [15, 5], 'Gfg': [6, 4], 'best': [8, 4], 'is': [10, 3]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

