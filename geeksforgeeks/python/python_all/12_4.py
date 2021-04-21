Python program to remove K length words in String



Given a String, write a Python program to remove all the words with K length.

**Examples:**

>  **Input** : test_str = ‘Gfg is best for all geeks’, K = 3  
> **Output** : is best geeks  
> **Explanation** : Gfg, for and all are of length 3, hence removed.
>
>  **Input** : test_str = ‘Gfg is best for all geeks’, K = 2  
> **Output** : Gfg best for all geeks  
> **Explanation** : is of length 2, hence removed.

**Method #1 : Using** **split()** **+** **join()** **+** **list
comprehension** **+** **len()**

  

  

In this each word is split using split(), and then lengths are checked using
len(), and then are omitted matching K. At last words are joined.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove K length words in String

# Using split() + join() + list comprehension + len()

 

# initializing string

test_str = 'Gfg is best for all geeks'

 

# printing original string

print("The original string is : " + (test_str))

 

# initializing K

K = 3

 

# getting splits

temp = test_str.split()

 

# omitting K lengths

res = [ele for ele in temp if len(ele) != K]

 

# joining result

res = ' '.join(res)

 

# printing result

print("Modified String : " + (res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : Gfg is best for all geeks
    Modified String : is best geeks

 **Method #2 : Using** **filter()** **+** **lambda** **+** **split()** **+**
**len()** **+** **join()**

In this, we perform task of filtering using filter() + lamnda, rest all the
functionalities are similar to above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove K length words in String

# Using filter() + lambda + split() + len() + join()

 

# initializing string

test_str = 'Gfg is best for all geeks'

 

# printing original string

print("The original string is : " + (test_str))

 

# initializing K

K = 3

 

# getting splits

temp = test_str.split()

 

# omitting K lengths

# filtering using filter() and lambda

res = list(filter(lambda ele: len(ele) != K, temp))

 

# joining result

res = ' '.join(res)

 

# printing result

print("Modified String : " + (res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : Gfg is best for all geeks
    Modified String : is best geeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

