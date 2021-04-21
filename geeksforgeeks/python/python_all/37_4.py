Python – Filter String Tuples if String lengths equals K



Given List of tuples, filter tuples, whose element strings have length equal
to K.

>  **Input** : test_list = [(“ABC”, “Gfg”, “CS1”), (“Gfg”, “Best”), (“Gfg”,
> “WoOW”)], K = 3  
>  **Output** : [(‘ABC’, ‘Gfg’, ‘CS1’)]  
>  **Explanation** : All Strings have length 3 in above tuple.
>
>  **Input** : test_list = [(“ABCD”, “Gfg”, “CS1”), (“Gfg”, “Best”), (“Gfg”,
> “WoOW”)], K = 3  
>  **Output** : []  
>  **Explanation** : No Strings have length 3 in above tuples.

 **Method #1 : Using loop**

In this, we run nested loop to test each string, if equals to K, then the
tuple is appended to result list, else its omitted.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter String Tuples if String lengths equals K

# Using loop

 

# initializing list

test_list = [("ABC", "Gfg", "CS1"), ("Gfg", "Best"),
("Gfg", "WoW")]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

res_list = []

for sub in test_list:

 res = True

 for ele in sub:

 

 # check using len() the lengths

 if len(ele) != K :

 res = False

 break

 if res:

 res_list.append(sub)

 

# printing result 

print("The filtered tuples : " + str(res_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('ABC', 'Gfg', 'CS1'), ('Gfg', 'Best'), ('Gfg', 'WoW')]
    The filtered tuples : [('ABC', 'Gfg', 'CS1'), ('Gfg', 'WoW')]
    

**Method #2 : Using all() + list comprehension**

Compacted way, uses all() to check for lengths equivalence and iteration using
list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter String Tuples if String lengths equals K

# Using all() + list comprehension

 

# initializing list

test_list = [("ABC", "Gfg", "CS1"), ("Gfg", "Best"),
("Gfg", "WoW")]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# all checks for all lengths equals K 

res = [sub for sub in test_list if all(len(ele) ==
K for ele in sub)]

 

# printing result 

print("The filtered tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('ABC', 'Gfg', 'CS1'), ('Gfg', 'Best'), ('Gfg', 'WoW')]
    The filtered tuples : [('ABC', 'Gfg', 'CS1'), ('Gfg', 'WoW')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

