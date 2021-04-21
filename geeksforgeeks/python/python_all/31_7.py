Python – Test for desired String Lengths



Given a String list, check for all string if it matches the desired string
length from 2nd list of sizes.

>  **Input** : test_list = [“Gfg”, ‘for’, ‘geeks’], len_list = [3, 3, 5]  
> **Output** : True  
> **Explanation** : All are of desired lengths.
>
>  **Input** : test_list = [“Gfg”, ‘for’, ‘geek’], len_list = [3, 3, 5]  
> **Output** : False  
> **Explanation** : geek has len 4, but desired is 5.

**Method #1: Using loop**

In this, we iterate for all the strings, and flag results false if we get any
string not matching the required size.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for desired String Lengths

# Using loop

 

# initializing string list

test_list = ["Gfg", 'is', 'best', 'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Lengths list 

len_list = [3, 2, 4, 3, 5]

 

res = True

for idx in range(len(test_list)):

 

 # checking for string lengths

 if len(test_list[idx]) != len_list[idx]:

 res = False

 break

 

# printing result 

print("Are all strings of required lengths : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Gfg', 'is', 'best', 'for', 'geeks']
    Are all strings of required lengths : True
    

**Method #2 : Using all()**

This returns True if all lengths match to be equal to desired lengths from
other lists.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for desired String Lengths

# Using all()

 

# initializing string list

test_list = ["Gfg", 'is', 'best', 'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Lengths list

len_list = [3, 2, 4, 3, 5]

 

# all() used to check for each element for length

res = all(len(test_list[idx]) == len_list[idx]

 for idx in range(len(test_list)))

 

# printing result

print("Are all strings of required lengths : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['Gfg', 'is', 'best', 'for', 'geeks']
    Are all strings of required lengths : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

