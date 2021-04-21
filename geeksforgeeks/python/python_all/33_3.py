Python program to compute arithmetic operation from String



Given a String with the multiplication of elements, convert to the summation
of these multiplications.

> **Input** : test_str = ‘5×10, 9×10, 7×8’  
> **Output** : 196  
> **Explanation** : 50 + 90 + 56 = 196.
>
>  **Input** : test_str = ‘5×10, 9×10’  
> **Output** : 140  
> **Explanation** : 50 + 90 = 140.  
>

**Method 1 : Using map() + mul + sum() + split()**

The combination of the above functions can be used to solve this problem. In
this, we perform summation using sum() and multiplication using mul(), split()
is used to split elements for creating operands for multiplication. The map()
is used to extend the logic to multiplication to each computation.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing module

from operator import mul

 

# initializing string

test_str = '5x6, 9x10, 7x8'

 

# printing original string

print("The original string is : " + str(test_str))

 

# sum() is used to sum the product of each computation

res = sum(mul(*map(int, ele.split('x'))) for ele
in test_str.split(', '))

 

# printing result

print("The computed summation of products : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : 5x6, 9x10, 7x8
    The computed summation of products : 176
    
    

**Method 2 : Using eval() + replace()**

In this, we convert multiplication symbol to the operator for multiplication(‘
***** ‘), similarly, comma symbol is converted to arithmetic “ **+** ” symbol.
Then eval() performs internal computations and returns the result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = '5x6, 9x10, 7x8'

 

# printing original string

print("The original string is : " + str(test_str))

 

# using replace() to create eval friendly string

temp = test_str.replace(',', '+').replace('x', '*')

 

# using eval() to get the required result

res = eval(temp)

 

# printing result

print("The computed summation of products : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : 5x6, 9x10, 7x8
    The computed summation of products : 176
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

