Python – Check if Splits are equal



Given String separated by delim, check if all splits are similar.

>  **Input** : ’45#45#45′, delim = ‘#’  
>  **Output** : True  
>  **Explanation** : All equal to 45.
>
>  **Input** : ‘4@5@5’, delim = ‘@’  
>  **Output** : False  
>  **Explanation** : 1st segment equal to 4, rest 5.

 **Method #1 : Using set() + len() + split()**

In this, we perform split to get elements in list format, then convert to set,
duplicates are removed, and check for len == 1, confirms all elements are
same.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if Splits are equal

# Using set() + len() + split()

 

# initializing string

test_str = '45# 45# 45# 45# 45'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing splt_chr 

splt_chr = "#"

 

# checking for length of set obtained, res stores boolean result

res = len(list(set(test_str.split(splt_chr)))) == 1

 

# printing result 

print("Are all splits equal ? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 45#45#45#45#45
    Are all splits equal ? : True
    

**Method #2 : Using split() + all()**

In this, we perform task of checking for all elements equal using all().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if Splits are equal

# Using split() + all()

 

# initializing string

test_str = '45# 45# 45# 45# 45'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing splt_chr 

splt_chr = "#"

 

# splitting using split()

new_list = test_str.split(splt_chr)

 

# checking all equal to 1st element

res = all(ele == new_list[0] for ele in new_list)

 

# printing result 

print("Are all splits equal ? : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : 45#45#45#45#45
    Are all splits equal ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

