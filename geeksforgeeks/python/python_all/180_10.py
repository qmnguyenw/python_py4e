Python Program for Find remainder of array multiplication divided by n



Given multiple numbers and a number n, the task is to print the remainder
after multiply all the number divide by n.  
 **Examples:**

    
    
    **Input :** arr[] = {100, 10, 5, 25, 35, 14}, 
                n = 11
    **Output :** 9
    100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9

 **Naive approach:** First multiple all the numbers then take % by n then find
the remainder, But in this approach, if the number is maximum of 2^64 then it
gives the wrong answer.  
 **Approach that avoids overflow :** First take a remainder or individual
number like arr[i] % n. Then multiply the remainder with the current result.
After multiplication, again take the remainder to avoid overflow. This works
because of the distributive properties of modular arithmetic. ( a * b) % c = (
( a % c ) * ( b % c ) ) % c

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to

# find remainder when

# all array elements

# are multiplied.

# Find remainder of arr[0] * arr[1]

# * .. * arr[n-1]

def findremainder(arr, lens, n):

 mul = 1

 # find the individual

 # remainder and

 # multiple with mul.

 for i in arr:

 mul = mul * (i % n)

 return mul % n

# Driven code

arr = [100, 10, 5, 25, 35, 14]

lens = len(arr)

n = 11

# print the remainder

# of after multiple

# all the numbers

print(findremainder(arr, lens, n))

# This code is contributed by "rishabh_jain".  
  
---  
  
 __

 __

 **Output:**

    
    
    9

Please refer complete article on Find remainder of array multiplication
divided by n for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

