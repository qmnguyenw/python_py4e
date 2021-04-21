Python – Reverse Range in String List



Given a string list, reverse each element of string list from ith to jth
index.

>  **Input** : test_list = [“Geeksforgeeks”, “Best”, “Geeks”], i, j = 1, 2  
>  **Output** : [‘ee’, ‘es’, ‘ee’]  
>  **Explanation** : Range of strings are extracted.
>
>  **Input** : test_list = [“Geeksforgeeks”], i, j = 1, 7  
>  **Output** : [‘eeksfor’]  
>  **Explanation** : Single string, from e to r (7 elements) are sliced.

 **Method #1 : Using loop + reversed() + string slicing**

The combination of above methods can be used to solve this problem. In this,
we perform reverse of range using reversed() extracted using slicing.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Common list elements and dictionary values 

# Using set() and intersection()

 

# initializing list

test_list = ["Geeksforgeeks", "Best", "Geeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing range 

i, j = 1, 3

 

res = []

for ele in test_list:

 

 # slicing and appending range

 res.append(ele[i : j + 1])

 

# printing result 

print("Sliced strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Geeksforgeeks', 'Best', 'Geeks']
    Sliced strings : ['eek', 'est', 'eek']
    

**Method #2 : Using map() + slicing + lambda**

This is yet another way in which this task can be performed. In this, we use
map() to extend the logic of slice made using lambda to entire list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Common list elements and dictionary values 

# Using map() + slicing + lambda

 

# initializing list

test_list = ["Geeksforgeeks", "Best", "Geeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing range 

i, j = 1, 3

 

# map used to extend logic to each string 

res = list(map(lambda x : x[i : j + 1], test_list))

 

# printing result 

print("Sliced strings : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Geeksforgeeks', 'Best', 'Geeks']
    Sliced strings : ['eek', 'est', 'eek']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

