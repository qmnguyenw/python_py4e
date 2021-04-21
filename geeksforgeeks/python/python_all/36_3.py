Python – Strip front and rear Punctuations from given String



Given a String strip rear and front punctuations.

> **Input** : test_str = ‘%$Gfg is b!!est(*^’  
>  **Output** : Gfg is b!!est  
>  **Explanation** : Front and rear punctuations are stripped.
>
>  **Input** : test_str = ‘%Gfg is b!!est(*^’  
>  **Output** : Gfg is b!!est  
>  **Explanation** : Front and rear punctuations are stripped.

 **Method #1 : Using punctuation() + loop**

In this, we use punctuation() to check for punctuations, from both rear and
front, once, non-pnc char is found, index is recorded and string is splitted.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Strip Punctuations from String 

# Using loop + punctuation

from string import punctuation

 

# initializing string

test_str = '%$Gfg is b !! est(*^&*'

 

# printing original string

print("The original string is : " + str(test_str))

 

# getting first non-pnc idx 

frst_np = [idx for idx in range(len(test_str)) if
test_str[idx] not in punctuation][0]

 

# getting rear non-pnc idx

rear_np = [idx for idx in range(len(test_str) - 1,
-1, -1) if test_str[idx] not in punctuation][0]

 

# spittd string 

res = test_str[frst_np : rear_np + 1]

 

# printing result 

print("The stripped string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : %$Gfg is b!!est(*^&*
    The stripped string : Gfg is b!!est
    

**Method #2 : Using strip() + split() + join()**

In this, we perform task of splitting using split(), to get individual words,
strip() is used to remove punctuations. Lastly join() is used to perform
joining of words.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Strip Punctuations from String 

# Using strip() + split() + join()

from string import punctuation

 

# initializing string

test_str = '%$Gfg is b !! est(*^&*'

 

# printing original string

print("The original string is : " + str(test_str))

 

# strip is used to remove rear punctuations

res = ' '.join([ele.strip(punctuation) for ele in
test_str.split()])

 

# printing result 

print("The stripped string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : %$Gfg is b!!est(*^&*
    The stripped string : Gfg is b!!est
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

