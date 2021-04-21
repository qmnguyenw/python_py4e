Python – Avoid Last occurrence of delimitter



Given an Integer list, perform join with the delimiter, avoiding the extra
delimiter at the end.

>  **Input** : test_list = [4, 7, 8, 3, 2, 1, 9], delim = “*”  
> **Output** : 4*7*8*3*2*1*9  
> **Explanation** : The rear “*” which usually occurs in concatenation, is
> avoided.
>
>  **Input** : test_list = [4, 7, 8, 3], delim = “*”  
> **Output** : 4*7*8*3  
> **Explanation** : The rear “*” which usually occurs in concatenation, is
> avoided.  
>

**Method #1: Using** **String slicing**

In this, we use string slice to slice off the last character from the string
after forming.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Avoid Last occurrence of delimitter

# Using map() + join() + str()

 

# initializing list

test_list = [4, 7, 8, 3, 2, 1, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing delim

delim = "$"

 

# appending delim to join

# will leave stray "$" at end

res = ''

for ele in test_list:

 res += str(ele) + "$"

 

# removing last using slicing

res = res[:len(res) - 1]

 

# printing result

print("The joined string : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 7, 8, 3, 2, 1, 9]
    The joined string : 4$7$8$3$2$1$9
    

**Method #2 : Using map() + join() + str()**

In this, we completely avoid loop method to solve this problem, and employ
map() to convert to string and join() to perform task of join.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Avoid Last occurrence of delimitter

# Using map() + join() + str()

 

# initializing list

test_list = [4, 7, 8, 3, 2, 1, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing delim

delim = "$"

 

# map extends string conversion logic

res = delim.join(map(str, test_list))

 

# printing result

print("The joined string : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 7, 8, 3, 2, 1, 9]
    The joined string : 4$7$8$3$2$1$9
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

