Python program to Compute a Polynomial Equation



The following article contains programs to compute a polynomial equation given
that the coefficients of the polynomial are stored in a List.

 **Examples:**

    
    
    # Evaluate value of 2x3 - 6x2 + 2x - 1 for x = 3
    **Input:** poly[] = {2, -6, 2, -1}, x = 3
    **Output:** 5
    
    # Evaluate value of 2x3 + 3x + 1 for x = 2
    **Input:** poly[] = {2, 0, 3, 1}, x = 2
    **Output:** 23
    
    # Evaluate value of 2x + 5 for x = 5
    **Input:** poly[] = {2, 5}, x = 5
    **Output:** 15
    
    

The equation will be of type:

![c_{n}x^{n} + c_{n-1}x^{n-1} + c_{n-2}x^{n-2} + … + c_{1}x +
c_{0}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-0deb263098a987de137f46ea70a88026_l3.png)

We will be provided with the value of variable and we have to compute the
value of the polynomial at at that point. To do so we have two approaches.

  

  

### Approach

  *  **Naive Method:** Using for loop to compute the value.
  *  **Optimised Method:** Using Horner’s Method for computing the value.

 **Naive method:**

In this approach, the following methodology will be followed. This is the most
naive approach to do such questions.

  * First coefficient **c n** will be multiplied with **x n**
  * Then coefficient **c n-1** will be multiplied with **x n-1**
  * The results produced in the above two steps will be added
  * This will go on till all the coefficient are covered.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# 2x3 - 6x2 + 2x - 1 for x = 3

poly = [2, -6, 2, -1]

x = 3

n = len(poly)

 

# Declaring the result

result = 0

 

# Running a for loop to traverse through the list

for i in range(n):

 

 # Declaring the variable Sum

 Sum = poly[i]

 

 # Running a for loop to multiply x (n-i-1)

 # times to the current coefficient

 for j in range(n - i - 1):

 Sum = Sum * x

 

 # Adding the sum to the result

 result = result + Sum

 

# Printing the result

print(result)  
  
---  
  
 __

 __

 **Output:**

    
    
    5
    

**Time Complexity:** O(n2)

 **Optimized method:**

Horner’s method can be used to evaluate polynomial in O(n) time. To understand
the method, let us consider the example of 2x3 – 6x2 \+ 2x – 1. The polynomial
can be evaluated as ((2x – 6)x + 2)x – 1. The idea is to initialize result as
the coefficient of xn which is 2 in this case, repeatedly multiply the result
with x and add the next coefficient to result. Finally, return the result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# + poly[1]x(n-2) + .. + poly[n-1]

def horner(poly, n, x):

 

 # Initialize result

 result = poly[0]

 

 # Evaluate value of polynomial

 # using Horner's method

 for i in range(1, n):

 

 result = result*x + poly[i]

 

 return result

 

# Driver program to

# test above function.

 

 

# Let us evaluate value of

# 2x3 - 6x2 + 2x - 1 for x = 3

poly = [2, -6, 2, -1]

x = 3

n = len(poly)

 

print("Value of polynomial is:", horner(poly, n, x))  
  
---  
  
 __

 __

 **Output:**

    
    
    Value of polynomial is: 5
    

**Time Complexity:** O(n)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

