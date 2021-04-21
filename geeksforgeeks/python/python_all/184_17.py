Python Program for nth Catalan Number



Catalan numbers are a sequence of natural numbers that occurs in many
interesting counting problems like following.

 **1)** Count the number of expressions containing n pairs of parentheses
which are correctly matched. For n = 3, possible expressions are ((())),
()(()), ()()(), (())(), (()()).

 **2)** Count the number of possible Binary Search Trees with n keys (See
this)  
See this for more applications.

The first few Catalan numbers for n = 0, 1, 2, 3, … are **1, 1, 2, 5, 14, 42,
132, 429, 1430, 4862, …**

## Recommended: Please solve it on “ _ _PRACTICE__ ” first, before moving on
to the solution.

 **Recursive Solution**  
Catalan numbers satisfy the following recursive formula.  
![C_0=1 \\ and \\ C_n_+_1=\\sum_{i=0}^{n}C_iC_n_-_i \\ for \\ n\\geq
0;](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5caf1032c7225d073dd41cd7a9fa4e38_l3.png)

  

  

Following is the implementation of above recursive formula.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# A recursive function to find nth catalan number

def catalan(n):

 # Base Case

 if n <= 1 :

 return 1

 

 # Catalan(n) is the sum of catalan(i)*catalan(n-i-1)

 res = 0

 for i in range(n):

 res += catalan(i) * catalan(n-i-1)

 

 return res

 

# Driver Program to test above function

for i in range(10):

 print(catalan(i), end= ' ')

# This code is contributed by Nikhil Kumar Singh (nickzuck_007)  
  
---  
  
 __

 __

 **Output:**

    
    
    1 1 2 5 14 42 132 429 1430 4862
    

**Dynamic Programming Solution –**  
We can observe that the above recursive implementation does a lot of repeated
work (we can the same by drawing recursion tree). Since there are overlapping
subproblems, we can use dynamic programming for this. Following is a Dynamic
programming based implementation in C++.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A dynamic programming based function to find nth

# Catalan number

def catalan(n):

 if (n == 0 or n == 1):

 return 1

 

 # Table to store results of subproblems

 catalan = [0 for i in range(n + 1)]

 

 # Initialize first two values in table

 catalan[0] = 1

 catalan[1] = 1

 

 # Fill entries in catalan[] using recursive formula

 for i in range(2, n + 1):

 catalan[i] = 0

 for j in range(i):

 catalan[i] = catalan[i] + catalan[j] *
catalan[i-j-1]

 

 # Return last entry

 return catalan[n]

 

# Driver code

for i in range (10):

 print (catalan(i))

# This code is contributed by Aditi Sharma  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    1
    2
    5
    14
    42
    132
    429
    1430
    4862
    

Please refer complete article on Program for nth Catalan Number for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

