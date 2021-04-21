Python – All substrings Frequency in String



Given a String, extract all unique substrings with their frequency.

>  **Input** : test_str = “ababa”  
>  **Output** : {‘a’: 3, ‘ab’: 2, ‘aba’: 2, ‘abab’: 1, ‘ababa’: 1, ‘b’: 2,
> ‘ba’: 2, ‘bab’: 1, ‘baba’: 1}  
>  **Explanation** : All substrings with their frequency extracted.
>
>  **Input** : test_str = “GFGF”  
>  **Output** : {‘G’: 2, ‘GF’: 2, ‘GFG’: 1, ‘GFGF’: 1, ‘F’: 2, ‘FG’: 1, ‘FGF’:
> 1}  
>  **Explanation** : All substrings with their frequency extracted.

 **Method #1 : Using loop + list comprehension**

The combination of above functionalities can be used to solve this problem. In
this, we first extract all the substrings using list comprehension, post that
loop is used to increase frequency.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All substrings Frequency in String

# Using loop + list comprehension

 

# initializing string

test_str = "abababa"

 

# printing original string

print("The original string is : " + str(test_str))

 

# list comprehension to extract substrings

temp = [test_str[idx: j] for idx in range(len(test_str))

 for j in range(idx + 1, len(test_str) + 1)]

 

# loop to extract final result of frequencies

res = {}

for idx in temp:

 if idx not in res.keys():

 res[idx] = 1

 else:

 res[idx] += 1

 

# printing result 

print("Extracted frequency dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : abababa
    Extracted frequency dictionary : {'a': 4, 'ab': 3, 'aba': 3, 'abab': 2, 'ababa': 2, 'ababab': 1, 'abababa': 1, 'b': 3, 'ba': 3, 'bab': 2, 'baba': 2, 'babab': 1, 'bababa': 1}
    

**Method #2 : Using list comprehension**

This is yet another way in which this task can be performed. In this, we
perform both the tasks, of extracting substring and computing frequency in
single nested list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All substrings Frequency in String

# Using list comprehension

 

# initializing string

test_str = "abababa"

 

# printing original string

print("The original string is : " + str(test_str))

 

# list comprehension to extract substrings and frequency

res = dict()

for ele in [test_str[idx: j] for idx in
range(len(test_str)) for j in range(idx + 1,
len(test_str) + 1)]:

 res[ele] = 1 if ele not in res.keys() else res[ele] +
1

 

# printing result 

print("Extracted frequency dictionary : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : abababa
    Extracted frequency dictionary : {'a': 4, 'ab': 3, 'aba': 3, 'abab': 2, 'ababa': 2, 'ababab': 1, 'abababa': 1, 'b': 3, 'ba': 3, 'bab': 2, 'baba': 2, 'babab': 1, 'bababa': 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

