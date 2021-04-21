Python – Sort Dictionary by Values and Keys



Given a dictionary, sort according to descended values, if similar values,
then by keys lexicographically.

> **Input** : test_dict = {“gfg” : 1, “is” : 1, “best” : 1, “for” : 1, “geeks”
> : 1}  
>  **Output** : {“best” : 1, “is” : 1, “for” : 1, “geeks” : 1, “gfg” : 1}  
>  **Explanation** : All values are equal, hence lexicographically sorted
> keys.
>
>  **Input** : test_dict = {“gfg” : 5, “is” : 4, “best” : 3, “for” : 2,
> “geeks” : 1}  
>  **Output** : {“gfg” : 5, “is” : 4, “best” : 3, “for” : 2, “geeks” : 1}  
>  **Explanation** : All values are different, hence descending ordered
> sorted.

 **Method : Using sorted() + items() + dictionary comprehension + lambda**

The combination of above functions can be used to solve this problem. In this,
we perform task of sorting using sorted(), dictionary comprehension is used to
remake dictionary, items() is used to extract items to sorted.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Dictionary by Values and Keys

# Using sorted() + items() + dictionary comprehension + lambda

 

# initializing dictionary

test_dict = {"Gfg" : 1, "is" : 3, "Best" : 2,
"for" : 3, "Geeks" : 2}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# - sign for descended values, omit if low-high sorting required

res = {val[0] : val[1] for val in
sorted(test_dict.items(), key = lambda x: (-x[1],
x[0]))}

 

# printing result 

print("Sorted dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 1, 'is': 3, 'Best': 2, 'for': 3, 'Geeks': 2}
    Sorted dictionary : {'for': 3, 'is': 3, 'Best': 2, 'Geeks': 2, 'Gfg': 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

