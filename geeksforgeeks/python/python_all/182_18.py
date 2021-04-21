Python Program for Number of elements with odd factors in given range



Given a range [ ** _n_** , ** _m_** ], find the number of elements that have
odd number of factors in the given range ( ** _n_** and **_m_** inclusive).

 **Examples:**

    
    
    **Input  :** n = 5, m = 100
    **Output :** 8
    The numbers with odd factors are 9, 16, 25, 
    36, 49, 64, 81 and 100
    
    **Input  :** n = 8, m = 65
    **Output :** 6
    
    **Input  :** n = 10, m = 23500
    **Output :** 150
    

A **Simple Solution** is to loop through all numbers starting from **_n_**.
For every number, check if it has an even number of factors. If it has an even
number of factors then increment count of such numbers and finally print the
number of such elements. To find all divisors of a natural number efficiently,
refer All divisors of a natural number

An **Efficient Solution** is to observe the pattern. Only those numbers, which
are **perfect Squares** have an odd number of factors. Let us analyze this
pattern through an example.

For example, 9 has odd number of factors, 1, 3 and 9. 16 also has odd number
of factors, 1, 2, 4, 8, 16. The reason for this is, for numbers other than
perfect squares, all factors are in the form of pairs, but for perfect
squares, one factor is single and makes the total as odd.

  

  

 **How to find number of perfect squares in a range?**  
The answer is difference between square root of **m** and **n-1** ( **not n**
)  
There is a little caveat. As both **n** and **m** are inclusive, if **n** is a
perfect square, we will get an answer which is less than one the actual
answer. To understand this, consider range [4, 36]. Answer is 5 i.e., numbers
4, 9, 16, 25 and 36.  
But if we do (36**0.5) – (4**0.5) we get 4. So to avoid this semantic error,
we take **n-1**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count number of odd squares

# in given range [n, m]

 

def countOddSquares(n, m):

 return int(m**0.5) - int((n-1)**0.5)

 

# Driver code

n = 5

m = 100

print("Count is", countOddSquares(n, m))

 

# This code is contributed by

# Mohit Gupta_OMG <0_o>  
  
---  
  
 __

 __

Output:

    
    
    Count is 8
    

Time Complexity: O(1)

Please refer complete article on Number of elements with odd factors in given
range for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

