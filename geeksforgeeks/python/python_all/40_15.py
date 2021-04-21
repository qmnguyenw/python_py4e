Python – Extract Tuples with all Numeric Strings



Given a list of tuples, extract only those tuples which have all numeric
strings.

>  **Input** : test_list = [(“45”, “86”), (“Gfg”, “1”), (“98”, “10”)]  
>  **Output** : [(’45’, ’86’), (’98’, ’10’)]  
>  **Explanation** : Only number representating tuples filtered.
>
>  **Input** : test_list = [(“Gfg”, “1”)]  
>  **Output** : []  
>  **Explanation** : No tuple containing just numbers.

 **Method #1 : Using list comprehension + all() + isdigit()**

In this, we check for string being numeric string using isdigit() and all() is
used to check for all strings. List comprehension is used to iterate all
tuples.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Tuples with all Numeric Strings

# Using all() + list comprehension + isdigit()

 

# initializing list

test_list = [("45", "86"), ("Gfg", "1"), ("98",
"10"), ("Gfg", "Best")]

 

# printing original list

print("The original list is : " + str(test_list))

 

# all() checks for all digits()

res = [sub for sub in test_list if all(ele.isdigit() for
ele in sub)]

 

# printing result 

print("Filtered Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('45', '86'), ('Gfg', '1'), ('98', '10'), ('Gfg', 'Best')]
    Filtered Tuples : [('45', '86'), ('98', '10')]
    

**Method #2 : Using lambda + filter() + isdigit()**

In this, we perform task of filtering using filter() + lambda, and isdigit()
is used to check for numerics.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Tuples with all Numeric Strings

# Using lambda + filter() + isdigit()

 

# initializing list

test_list = [("45", "86"), ("Gfg", "1"), ("98",
"10"), ("Gfg", "Best")]

 

# printing original list

print("The original list is : " + str(test_list))

 

# all() checks for all digits()

res = list(filter(lambda sub : all(ele.isdigit() for
ele in sub), test_list))

 

# printing result 

print("Filtered Tuples : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('45', '86'), ('Gfg', '1'), ('98', '10'), ('Gfg', 'Best')]
    Filtered Tuples : [('45', '86'), ('98', '10')]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

