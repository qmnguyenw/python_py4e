Python program to add two binary numbers



Given two binary numbers, write a Python program to compute their sum.

 **Examples:**

    
    
     **Input:**  a = "11", b = "1"
    **Output:** "100"
    
    **Input:** a = "1101", b = "100"
    **Output:** 10001
    

**Approach:**

  *  **Naive Approach:** The idea is to start from the last characters of two strings and compute digit sum one by one. If the sum becomes more than 1, then store carry for the next digits.
  *  **Using inbuilt function:** Calculate the result by using the inbuilt **bin()** and **int()** function.

 **Method 1:** Naive Approach:

The idea is to start from the last characters of two strings and compute digit
sum one by one. If the sum becomes more than 1, then store carry for the next
digits.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to add two binary numbers.

 

# Driver code

# Declaring the variables

a = "1101"

b = "100"

max_len = max(len(a), len(b))

a = a.zfill(max_len)

b = b.zfill(max_len)

 

# Initialize the result

result = ''

 

# Initialize the carry

carry = 0

 

# Traverse the string

for i in range(max_len - 1, -1, -1):

 r = carry

 r += 1 if a[i] == '1' else 0

 r += 1 if b[i] == '1' else 0

 result = ('1' if r % 2 == 1 else '0') +
result

 

 # Compute the carry.

 carry = 0 if r < 2 else 1

 

if carry != 0:

 result = '1' + result

 

print(result.zfill(max_len))  
  
---  
  
 __

 __

 **Output:**

    
    
    10001
    

**Method 2:** Using inbuilt functions:

We will first convert the binary string to a decimal using **int()**function
in python. The _int()_ function in Python and Python3 converts a number in the
given base to decimal. Then we will add it and then again convert it into a
binary number using **bin()**function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to add two binary numbers.

 

# Driver code

# Declaring the variables

a = "1101"

b = "100"

 

# Calculating binary value using function

sum = bin(int(a, 2) + int(b, 2))

 

# Printing result

print(sum[2:])  
  
---  
  
 __

 __

 **Output:**

    
    
    10001
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

