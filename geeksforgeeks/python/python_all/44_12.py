Python – Extract Indices of substring matches



Given a String List, and a substring, extract list of indices of Strings, in
which that substring occurs.

>  **Input** : test_list = [“Gfg is good”, “for Geeks”, “I love Gfg”, “Gfg is
> useful”], K = “Gfg”  
>  **Output** : [0, 2, 3]  
>  **Explanation** : “Gfg” is present in 0th, 2nd and 3rd element as
> substring.
>
>  **Input** : test_list = [“Gfg is good”, “for Geeks”, “I love Gfg”, “Gfg is
> useful”], K = “good”  
>  **Output** : [0]  
>  **Explanation** : “good” is present in 0th substring.

 **Method #2 : Using loop + enumerate()**

This is brute way in which this task can be done. In this, we iterate for all
the elements along with their indices using enumerate() and conditional
statements are used to get required result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Indices of substring matches

# Using loop + enumerate()

 

# initializing list

test_list = ["Gfg is good", "for Geeks", "I love Gfg", "Its
useful"]

 

# initializing K 

K = "Gfg"

 

# printing original list

print("The original list : " + str(test_list))

 

# using loop to iterate through list 

res = []

for idx, ele in enumerate(test_list):

 if K in ele:

 res.append(idx)

 

# printing result 

print("The indices list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg is good', 'for Geeks', 'I love Gfg', 'Its useful']
    The indices list : [0, 2]
    

**Method #2 : Using list comprehension + enumerate()**

This is yet another way in which this task can be solved. In this, we perform
the similar task as above method using list comprehension and enumerate() is
used to get compact solution.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Indices of substring matches

# Using list comprehension + enumerate()

 

# initializing list

test_list = ["Gfg is good", "for Geeks", "I love Gfg", "Its
useful"]

 

# initializing K 

K = "Gfg"

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension and enumerate to offer compact solution

res = [idx for idx, val in enumerate(test_list) if K in
val]

 

# printing result 

print("The indices list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg is good', 'for Geeks', 'I love Gfg', 'Its useful']
    The indices list : [0, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

