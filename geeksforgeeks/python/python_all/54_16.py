Python – Replace sublist from Initial element



Given a list and replacement sublist, perform the replacement of list sublist
on basis of initial element of replacement sublist.

>  **Input** : test_list = [3, 7, 5, 3], repl_list = [7, 8]  
>  **Output** : [3, 7, 8, 3]  
>  **Explanation** : Replacement starts at 7 hence 7 and 8 are replaced.
>
>  **Input** : test_list = [3, 7, 5, 3, 9, 10], repl_list = [5, 6, 7, 4]  
>  **Output** : [3, 7, 5, 6, 7, 4]  
>  **Explanation** : Replacement starts at 5 and goes till end of list.

 **Method : Using list comprehension + list slicing**  
The combination of above functionalities can be used to solve this problem. In
this, we extract the index of beginning element, and then perform the
appropriate slicing of list according to requirements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace substring from Initial element

# Using list slicing + list comprehension

 

# initializing list

test_list = [5, 2, 6, 4, 7, 1, 3]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing repl_list 

repl_list = [6, 10, 18]

 

# Replace substring from Initial element

# Extracting index

idx = test_list.index(repl_list[0])

 

# Slicing till index, and then adding rest of list

res = test_list[ :idx] + repl_list + test_list[idx +
len(repl_list):]

 

# printing result 

print("Substituted List : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [5, 2, 6, 4, 7, 1, 3]
    Substituted List : [5, 2, 6, 10, 18, 1, 3]
    

