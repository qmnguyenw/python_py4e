Python | Superfactorial of a number.



Given a number, the task is to find the Superfactorial of a number. The result
of multiplying the product of first n factorials is called **Superfactorial**
of a number.

    
    
    Superfactorial(n)= 1 ^ n * 2 ^ (n-1) * 3 ^ (n-2) * . . . . . * n ^ 1

 **Examples:**

>  **Input :** 3  
>  **Output :** 12  
> H(3) = 1! * 2! * 3! = 12
>
>  **Input :** 4  
>  **Output :** 288  
> H(4) = 1^4 * 2^3 * 3^2 * 4^1 = 288

An **efficient approach** is to compute all factorial iteratively till n, then
compute the product of all factorial till n.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find the

# Superfactorial of a number

 

# function to calculate the

# value of Superfactorial 

def superfactorial(n):

 

 # initialise the

 # val to 1

 val = 1

 ans = []

 for i in range(1, n + 1):

 val = val * i

 ans.append(val)

 # ans is the list with

 # all factorial till n.

 arr = [1]

 for i in range(1, len(ans)):

 arr.append((arr[-1]*ans[i]))

 

 return arr

 

# Driver Code

n = 5

arr = superfactorial(n)

print(arr[-1])  
  
---  
  
 __

 __

 **Output:**

    
    
    34560
    

**Time-complexity:** O(N)  
Since super-factorials of number can be huge, hence the numbers will overflow.
We can use boost libraries in C++ or BigInteger in Java to store the super-
factorial of a number N.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

