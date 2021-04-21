Python – Assigning Subsequent Rows to Matrix first row elements



Given a (N + 1) * N Matrix, assign each column of 1st row of matrix, the
subsequent row of Matrix.

>  **Input** : test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]]  
>  **Output** : {5: [2, 0, 9], 8: [5, 4, 2], 10: [2, 3, 9]}  
>  **Explanation** : 5 paired with 2nd row, 8 with 3rd and 10 with 4th
>
>  **Input** : test_list = [[5, 8], [2, 0], [5, 4]]  
>  **Output** : {5: [2, 0], 8: [5, 4]}  
>  **Explanation** : 5 paired with 2nd row, 8 with 3rd.

 **Method #1 : Using dictionary comprehension**

This is one of the ways in which this task can be performed. In this, we
iterate for rows and corresponding columns using loop and assign value list
accordingly in one-liner way using dictionary comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assigning Subsequent Rows to Matrix first row elements

# Using dictionary comprehension

 

# initializing list

test_list = [[5, 8, 9], [2, 0, 9], [5, 4,
2], [2, 3, 9]]

 

# printing original list

print("The original list : " + str(test_list))

 

# pairing each 1st col with next rows in Matrix

res = {test_list[0][ele] : test_list[ele + 1] for ele in
range(len(test_list) - 1)}

 

# printing result 

print("The Assigned Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]
    The Assigned Matrix : {5: [2, 0, 9], 8: [5, 4, 2], 9: [2, 3, 9]}
    

**Method #2 : Using zip() + list slicing + dict()**

This is yet another way in which this task can be performed. In this, we slice
elements to be first row and subsequent rows using list slicing and zip()
performs the task of required grouping. Returned

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assigning Subsequent Rows to Matrix first row elements

# Using zip() + list slicing + dict()

 

# initializing list

test_list = [[5, 8, 9], [2, 0, 9], [5, 4,
2], [2, 3, 9]]

 

# printing original list

print("The original list : " + str(test_list))

 

# dict() to convert back to dict type 

# slicing and pairing using zip() and list slicing

res = dict(zip(test_list[0], test_list[1:]))

 

# printing result 

print("The Assigned Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]
    The Assigned Matrix : {5: [2, 0, 9], 8: [5, 4, 2], 9: [2, 3, 9]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

