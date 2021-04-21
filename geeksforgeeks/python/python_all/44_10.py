Python – Convert List to delimiter separated String



Given List of elements, convert it to delimiter separated String.

>  **Input** : test_list = [7, “Gfg”, “best”, 9], delim = “*”  
>  **Output** : 7*Gfg*best*9*  
>  **Explanation** : All elements are concatenated with “*” as joiner.
>
>  **Input** : test_list = [7, “Gfg”, “best”, 9], delim = “#”  
>  **Output** : 7#Gfg#best#9#  
>  **Explanation** : All elements are concatenated with “#” as joiner.

 **Method #1 : Using loop + str()**

This is one of the ways in which this task can be performed. In this, we run a
loop to add delimiter at end of each element, after converting each element to
string.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List to delimiter separated String

# Using loop + str()

 

# initializing list

test_list = [7, "Gfg", 8, "is", "best", 9] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing delim 

delim = "*"

 

res = '' 

 

# using loop to add string followed by delim 

for ele in test_list:

 res = res + str(ele) + delim

 

# printing result 

print("The resultant string : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [7, 'Gfg', 8, 'is', 'best', 9]
    The resultant string : 7*Gfg*8*is*best*9*
    

**Method #2 : Using join() + str()**

This is yet another way in which this task can be performed. In this we
perform the task of joining each element by delim using join() and conversion
to string is done using str().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List to delimiter separated String

# Using join() + str()

 

# initializing list

test_list = [7, "Gfg", 8, "is", "best", 9] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing delim 

delim = "*"

 

# using map to convert each element to string 

temp = list(map(str, test_list))

 

# join() used to join with delimiter

res = delim.join(temp)

 

# printing result 

print("The resultant string : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [7, 'Gfg', 8, 'is', 'best', 9]
    The resultant string : 7*Gfg*8*is*best*9
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

