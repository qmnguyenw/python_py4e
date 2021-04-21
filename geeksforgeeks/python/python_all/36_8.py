Python – Concatenate Tuple elements by delimiter



Given a tuple, concatenate each element of tuple by delimiter.

>  **Input** : test_tup = (“Gfg”, “is”, 4, “Best”), delim = “, ”  
>  **Output** : Gfg, is, 4, Best  
>  **Explanation** : Elements joined by “, “.
>
>  **Input** : test_tup = (“Gfg”, “is”, 4), delim = “, ”  
>  **Output** : Gfg, is, 4  
>  **Explanation** : Elements joined by “, “.

 **Method #1 : Using list comprehension**

In this, we iterate for each element in tuple using loop in list comprehension
and concatenate using + operator.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Tuple elements by delimiter

# Using list comprehension

 

# initializing tuple

test_tup = ("Gfg", "is", 4, "Best")

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# initializing delim 

delim = "-"

 

# using str() to convert elements to string 

# join to convert to string

res = ''.join([str(ele) + delim for ele in test_tup])

 

# striping stray char 

res = res[ : len(res) - len(delim)]

 

# printing result 

print("Concatenated Tuple : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original tuple is : ('Gfg', 'is', 4, 'Best')
    Concatenated Tuple : Gfg-is-4-Best
    

**Method #2 : Using join() + map()**

In this, we convert all chars to string using str() and map to perform str()
to all elements, then concatenation using join().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Tuple elements by delimiter

# Using join() + map()

 

# initializing tuple

test_tup = ("Gfg", "is", 4, "Best")

 

# printing original tuple

print("The original tuple is : " + str(test_tup))

 

# initializing delim 

delim = "-"

 

# for joining, delim is used 

res = delim.join(map(str, test_tup))

 

# printing result 

print("Concatenated Tuple : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original tuple is : ('Gfg', 'is', 4, 'Best')
    Concatenated Tuple : Gfg-is-4-Best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

