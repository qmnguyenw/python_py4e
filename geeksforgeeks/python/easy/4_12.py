Common Operations on Fuzzy Set with Example and Code



 **What is Fuzzy Set ?**

Fuzzy refers to something that is unclear or vague . Hence, Fuzzy Set is a Set
where every key is associated with value, which is between 0 to 1 based on the
certainity .This value is often called as degree of membership. Fuzzy Set is
denoted with a Tilde Sign on top of the normal Set notation.

 **Operations on Fuzzy Set with Code :**

 **1\. Union :**

Consider 2 Fuzzy Sets denoted by A and B, then let’s consider Y be the Union
of them, then for every member of A and B, Y will be:

  

  

    
    
     degree_of_membership(Y)= max(degree_of_membership(A), degree_of_membership(B)) 
    
    

**EXAMPLE :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Example to Demonstrate the

# Union of Two Fuzzy Sets

A = dict()

B = dict()

Y = dict()

 

A = {"a": 0.2, "b": 0.3, "c": 0.6, "d":
0.6}

B = {"a": 0.9, "b": 0.9, "c": 0.4, "d":
0.5}

 

print('The First Fuzzy Set is :', A)

print('The Second Fuzzy Set is :', B)

 

 

for A_key, B_key in zip(A, B):

 A_value = A[A_key]

 B_value = B[B_key]

 

 if A_value > B_value:

 Y[A_key] = A_value

 else:

 Y[B_key] = B_value

 

print('Fuzzy Set Union is :', Y)  
  
---  
  
 __

 __

 **Output**

    
    
    The First Fuzzy Set is : {'a': 0.2, 'b': 0.3, 'c': 0.6, 'd': 0.6}
    The Second Fuzzy Set is : {'a': 0.9, 'b': 0.9, 'c': 0.4, 'd': 0.5}
    Fuzzy Set Union is : {'a': 0.9, 'b': 0.9, 'c': 0.6, 'd': 0.6}
    
    
    

**2\. Intersection :**

Consider 2 Fuzzy Sets denoted by A and B, then let’s consider Y be the
Intersection of them, then for every member of A and B, Y will be:

    
    
    degree_of_membership(Y)= min(degree_of_membership(A), degree_of_membership(B)) 
    
    

**EXAMPLE :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Example to Demonstrate

# Intersection of Two Fuzzy Sets

A = dict()

B = dict()

Y = dict()

 

A = {"a": 0.2, "b": 0.3, "c": 0.6, "d":
0.6}

B = {"a": 0.9, "b": 0.9, "c": 0.4, "d":
0.5}

 

print('The First Fuzzy Set is :', A)

print('The Second Fuzzy Set is :', B)

 

 

for A_key, B_key in zip(A, B):

 A_value = A[A_key]

 B_value = B[B_key]

 

 if A_value < B_value:

 Y[A_key] = A_value

 else:

 Y[B_key] = B_value

print('Fuzzy Set Intersection is :', Y)  
  
---  
  
 __

 __

 **Output**

    
    
    The First Fuzzy Set is : {'a': 0.2, 'b': 0.3, 'c': 0.6, 'd': 0.6}
    The Second Fuzzy Set is : {'a': 0.9, 'b': 0.9, 'c': 0.4, 'd': 0.5}
    Fuzzy Set Intersection is : {'a': 0.2, 'b': 0.3, 'c': 0.4, 'd': 0.5}
    
    
    

**3\. Complement :**

Consider a Fuzzy Sets denoted by A , then let’s consider Y be the Complement
of it, then for every member of A , Y will be:

  

  

    
    
    degree_of_membership(Y)= 1 - degree_of_membership(A)
    
    

**EXAMPLE :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Example to Demonstrate the

# Difference Between Two Fuzzy Sets

A = dict()

Y = dict()

 

A = {"a": 0.2, "b": 0.3, "c": 0.6, "d":
0.6}

 

print('The Fuzzy Set is :', A)

 

 

for A_key in A:

 Y[A_key]= 1-A[A_key]

 

print('Fuzzy Set Complement is :', Y)  
  
---  
  
 __

 __

 **Output**

    
    
    The Fuzzy Set is : {'a': 0.2, 'b': 0.3, 'c': 0.6, 'd': 0.6}
    Fuzzy Set Complement is : {'a': 0.8, 'b': 0.7, 'c': 0.4, 'd': 0.4}
    
    
    

**4\. Difference :**  
Consider 2 Fuzzy Sets denoted by A and B, then let’s consider Y be the
Intersection of them, then for every member of A and B, Y will be:

    
    
    degree_of_membership(Y)= min(degree_of_membership(A), 1- degree_of_membership(B)) 
    
    

**EXAMPLE :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Example to Demonstrate the

# Difference Between Two Fuzzy Sets

A = dict()

B = dict()

Y = dict()

 

A = {"a": 0.2, "b": 0.3, "c": 0.6, "d":
0.6}

B = {"a": 0.9, "b": 0.9, "c": 0.4, "d":
0.5}

 

print('The First Fuzzy Set is :', A)

print('The Second Fuzzy Set is :', B)

 

 

for A_key, B_key in zip(A, B):

 A_value = A[A_key]

 B_value = B[B_key]

 B_value = 1 - B_value

 

 if A_value < B_value:

 Y[A_key] = A_value

 else:

 Y[B_key] = B_value

 

print('Fuzzy Set Difference is :', Y)  
  
---  
  
 __

 __

 **Output**

    
    
    The First Fuzzy Set is : {"a": 0.2, "b": 0.3, "c": 0.6, "d": 0.6}
    The Second Fuzzy Set is : {"a": 0.9, "b": 0.9, "c": 0.4, "d": 0.5}
    Fuzzy Set Difference is : {"a": 0.1, "b": 0.1, "c": 0.6, "d": 0.5}
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

