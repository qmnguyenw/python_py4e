Python Program to Count Non-Bouncy numbers



If any number is represented in such a way that when we are reading it from
left to right each ith Digit is greater or equal than i-1th digit is known as
an increasing number. And if digits of any number are decreasing from left to
right it’s known as decreasing number.

 **Example:**

>  **Increasing Number ?235668**
>
> all the digits from left to right are greater or equal to the previous
> digit.
>
>  **Decreasing Number ? 653221**
>
>  
>
>
>  
>
>
> all the digits from left to right are lesser than or equal to the previous
> digit.

But if the number is neither increasing nor decreasing is Known as **Bouncy
Number**.

 **Example:**

>  **523469 - >** Some Digits from left to right are decreasing from left to
> right and some are increasing. So this is the example of Bouncy Number.

The task in this article is to count the total number of Non-Bouncy Numbers
below 10k and print the final count in mod(109+7). To do this we will use the
Stars and Bars method to calculate the number of non-bouncy numbers in the
given range.

 **Stars and Bars Method:**

Stars and Bars method is a technique that is used to deal with combination
based problems. These type of problems arises when we want the number of
identical groups.

 **The formula for calculating identical groups:**

  

  

![count = \(N+M-1\)/N](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c907fee4eec46023273501a69073f5e3_l3.png)

Where N are the identical objects and M is the container or range.

 **Final Formula:**

![count=\\frac{N!}{M!\(N-M\)!}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e555f3b2d9a56b5f107840153d04219c_l3.png)

 **Examples:**

    
    
     **Input :** k = 6
    **Output :** 12951
     
    **Input :** k = 9
    **Output :** 140906
    

Below is the implementation:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import redunce function from functools

from functools import reduce

 

 

# define a function to 

# calculate nCr 

def nCr(n, k):

 

 # this approach is based on 

 # apporoach of stars and bar method

 # using reduce and lambda function

 # to calculate numer & denom

 numer = reduce(lambda x, y: x * y,

 list(range(n, n - k, -1))) 

 denom = reduce(lambda x, y: x * y,

 list(range(1, k + 1))) 

 

 # denom root of numer will be the final result

 return numer // denom 

 

# Driver Code

# input value of k

k = 6

 

# calculating r using function call

r = int((nCr(k + 10, 10) +

 nCr(k + 9, 9) 

 - 2 - 10 * k))

 

# print final result

print(r % (1000000000 + 7))   
  
---  
  
__

__

**Output:**

    
    
    12951
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

