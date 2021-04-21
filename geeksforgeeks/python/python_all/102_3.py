Python program for multiplication and division of complex number



Given two complex numbers. The task is to multiply and divide them.

 **Multiplication of complex number:** In Python complex numbers can be
multiplied using * operator

 **Examples:**

    
    
    **Input:** 2+3i, 4+5i 
    **Output:** Multiplication is : (-7+22j) 
    
    **Input:** 2+3i, 1+2i
    **Output:** Multiplication is : (-4+7j) 
    

__

__  
__

__

__  
__  
__

# Python program to demonstrate

# multiplication of complex numbers

 

 

def mulComplex( z1, z2):

 return z1*z2

 

 

# driver code

z1 = complex(2, 3)

z2 = complex(4, 5)

 

 

print("Multiplication is :", mulComplex(z1,z2))  
  
---  
  
 __

 __

 **Output:**

    
    
    Multiplication is : (-7+22j)
    

**Division of complex number:** In Python, complex numbers can be divided
using the / operator.

  

  

 **Examples:**

    
    
    **Input:** 2+3i, 4+5i
    **Output:** Division  is : (0.5609756097560976+0.0487804878048781j)
    
    **Input:** 2+3i, 1+2i
    **Output:** Division is :(1.6-0.2j) 
    

__

__  
__

__

__  
__  
__

# Python program to demonstrate

# division of complex numbers

 

 

def divComplex( z1, z2):

 return z1 / z2

 

# driver code

 

z1 = complex(2, 3)

z2 = complex(4, 5)

 

print( "Division is :", (divComplex(z1, z2))  
  
---  
  
 __

 __

 **Output:**

    
    
    Division is : (0.5609756097560976+0.0487804878048781j)
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

