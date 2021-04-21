Python – Concatenate Ranged Values in String list



Given list of strings, perform concatenation of ranged values from Strings
list.

>  **Input** : test_list = [“abGFGcs”, “cdforef”, “asalloi”], i, j = 3, 5  
>  **Output** : FGorll  
>  **Explanation** : All string sliced, FG, or and ll from all three strings
> and concatenated.
>
>  **Input** : test_list = [“aGFGcs”, “cforef”, “aalloi”], i, j = 1, 4  
>  **Output** : GFGforall  
>  **Explanation** : Similar slicing operation different ranges.

 **Method #1 : Using loop + string slicing**

This is brute way in which this task can be performed. In this we iterate for
all strings and perform concatenation of values of range of each string.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Ranged Values in String list

# Using loop

 

# initializing list

test_list = ["abGFGcs", "cdforef", "asalloi"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing range

i, j = 2, 5

 

res = ''

for ele in test_list:

 

 # Concatenating required range

 res += ele[i : j]

 

# printing result 

print("The Concatenated String : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['abGFGcs', 'cdforef', 'asalloi']
    The Concatenated String : GFGforall
    

**Method #2 : Using list comprehension + string slicing**

This is yet another way in which this task can be performed. In this, we
extract a particular range of string in one liner using list comprehension and
string slicing as above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Concatenate Ranged Values in String list

# Using list comprehension + string slicing

 

# initializing list

test_list = ["abGFGcs", "cdforef", "asalloi"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing range

i, j = 2, 5

 

# join() used to join slices together

res = ''.join([sub[i : j] for sub in test_list])

 

# printing result 

print("The Concatenated String : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['abGFGcs', 'cdforef', 'asalloi']
    The Concatenated String : GFGforall
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

