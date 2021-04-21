Python Program to Check Prime Number



Given a positive integer, check if the number is prime or not. A prime is a
natural number greater than 1 that has no positive divisors other than 1 and
itself. Examples of first few prime numbers are {2, 3, 5,

 **Examples:**

    
    
    **Input:** n = 11
    **Output:** true
    
    **Input:**  n = 15
    **Output:** false
    
    **Input:**  n = 1
    **Output:** false
    

**School Method :**

 __

 __  
 __

 __

 __  
 __  
 __

# A school method based Python3

# program to check if a number

# is prime

 

def isPrime(n):

 

 # Corner case

 if n <= 1:

 return False

 

 # Check from 2 to n-1

 for i in range(2, n):

 if n % i == 0:

 return False;

 

 return True

 

# Driver Program to test above function

print("true") if isPrime(11) else print("false")

print("true") if isPrime(14) else print("false")

 

# This code is contributed by Smitha Dinesh Semwal  
  
---  
  
 __

 __

 **Output:**

    
    
    true
    false
    

Time complexity of this solution is O(n)

  

  

  
 **Optimized School Method :**

 __

 __  
 __

 __

 __  
 __  
 __

# A optimized school method based

# Python3 program to check 

# if a number is prime 

 

 

def isPrime(n) : 

 # Corner cases 

 if (n <= 1) : 

 return False

 if (n <= 3) : 

 return True

 

 # This is checked so that we can skip 

 # middle five numbers in below loop 

 if (n % 2 == 0 or n % 3 == 0) : 

 return False

 

 i = 5

 while(i * i <= n) : 

 if (n % i == 0 or n % (i + 2) == 0) : 

 return False

 i = i + 6

 

 return True

 

 

# Driver Program 

 

if(isPrime(11)) : 

 print(" true") 

else : 

 print(" false") 

 

if(isPrime(15)) : 

 print(" true") 

else : 

 print(" false") 

 

 

# This code is contributed 

# by Nikita Tiwari.   
  
---  
  
__

__

**Output:**

    
    
    true
    false
    

Please refer complete article on Primality Test | Set 1 (Introduction and
School Method) for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

