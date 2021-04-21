Python | Checking triangular inequality on list of lists



Given a list of lists, the task is to find whether a sublist satisfies the
triangle inequality.

The **triangle inequality** states that for any triangle, the sum of the
lengths of any two sides must be greater than or equal to the length of the
remaining side. In other words, a triangle is valid if sum of its two sides is
greater than the third side. If three sides are a, b and c, then three
conditions should be met.

    
    
    a + b > c 
    a + c > b 
    b + c > a  
    

![](https://media.geeksforgeeks.org/wp-content/uploads/check-whether-triangle-
valid-not-sides-given1.jpg)

**Method #1 : Using List comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find whether a sublist

# satisfies the triangle inequality.

 

# List initialization

Input = [[1, 3, 1], [4, 5, 6]]

 

# Sorting sublist

for elem in Input:

 elem.sort()

 

# Using list comprehension

Output = [(p, q, r) for p, q, r in Input if (p + q)>=
r]

 

# Printing output

print(Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [(4, 5, 6)]
    

