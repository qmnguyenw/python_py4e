Python – K length consecutive characters



Given a String, extract all the K length consecutive characters.

>  **Input** : test_str = ‘geekforgeeeksss is bbbest forrr geeks’, K = 3  
>  **Output** : [‘eee’, ‘sss’, ‘bbb’, ‘rrr’]  
>  **Explanation** : K length consecutive strings extracted.
>
>  **Input** : test_str = ‘geekforgeeeksss is bbbest forrrr geeks’, K = 4  
>  **Output** : [‘rrrr’]  
>  **Explanation** : K length consecutive strings extracted.

 **Method #1 : Using loop**

In this, we maintain counter to check for elements consecution, if they are
exactly equal to K before separate element, then number, appending by itself K
times is returned.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K length consecutive characters

# Using loop

 

# initializing string

test_str = 'geekforgeeekssss is bbbbest forrrr geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 4

 

res = []

curr, cnt = None, 0

for chr in test_str:

 

 # increment for similar character

 if chr == curr:

 cnt += 1

 else:

 curr, cnt = chr, 1

 

 # if count exactly K, element is added

 if cnt == K:

 res.append(K * chr)

 

# printing result 

print("The K length similar characters : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeekssss is bbbbest forrrrrrr geeks
    The K length similar characters : ['ssss', 'bbbb', 'rrrr']
    

**Method #2 : Using split() + enumerate()**

In this, we create substring from each index, and if each element of those
substring are equal, then it is returned to result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# K length consecutive characters

# Using split() + enumerate()

 

# initializing string

test_str = 'geekforgeeekssss is bbbbest forrrr geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing K 

K = 4

 

res = []

for idx, ele in enumerate(test_str):

 

 # creating equi string 

 substr = ele * K

 

 # checking if equal to actual string 

 if test_str[idx : idx + K] == substr:

 res.append(substr)

 

# printing result 

print("The K length similar characters : " +
str(list(set(res))))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeekssss is bbbbest forrrrrrr geeks
    The K length similar characters : ['bbbb', 'ssss', 'rrrr']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

