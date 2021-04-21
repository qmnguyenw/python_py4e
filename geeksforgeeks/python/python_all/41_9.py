Python – Extract indices of Present, Non Index matching Strings



Given two strings, extract indices of all characters from string 1 which are
present in other string, but not in same index.

>  **Input** : test_str1 = ‘pplg’, test_str2 = ‘pineapple’  
>  **Output** : [0, 1, 2]  
>  **Explanation** : ppl is found in 2nd string, also not on same index as
> 1st.
>
>  **Input** : test_str1 = ‘pine’, test_str2 = ‘pineapple’  
>  **Output** : []  
>  **Explanation** : Found in other string on same index.

 **Method #1 : Using enumerate() + loop**

In this, we employ nested loop to check for each character its occurrence in
2nd string, and then if it’s in other position, if found the index is
appended.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract indices of Present, Non Index matching Strings

# using loop + enumerate()

 

# initializing strings

test_str1 = 'apple'

test_str2 = 'pineapple'

 

# printing original Strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# the replaced result 

res = []

for idx, val in enumerate(test_str1):

 

 # if present in string 2

 if val in test_str2:

 

 # if not present at same index

 if test_str2[idx] != val: 

 res.append(idx)

 

# printing result 

print("The extracted indices : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string 1 is : apple
    The original string 2 is : pineapple
    The extracted indices : [0, 1, 2, 3, 4]
    

**Method #2 : Using enumerate() + zip() + list comprehension**

In this, we perform the task of getting indices using enumerate() and pairing
of both strings is done using zip(), the conditional checks occur using list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract indices of Present, Non Index matching Strings

# using enumerate() + zip() + list comprehension

 

# initializing strings

test_str1 = 'apple'

test_str2 = 'pineapple'

 

# printing original Strings

print("The original string 1 is : " + str(test_str1))

print("The original string 2 is : " + str(test_str2))

 

# one-liner to solve this problem.

res = [idx for idx, (x, y) in enumerate(zip(test_str1,
test_str2)) if x != y and x in test_str2]

 

# printing result 

print("The extracted indices : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string 1 is : apple
    The original string 2 is : pineapple
    The extracted indices : [0, 1, 2, 3, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

