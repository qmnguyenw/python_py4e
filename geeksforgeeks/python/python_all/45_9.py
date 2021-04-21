Python – Columns to Dictionary Conversion in Matrix



Given a Matrix, Convert to Dictionary with elements in 1st row being keys, and
subsequent rows acting as values list.

>  **Input** : test_list = [[4, 5, 7], [10, 8, 4], [19, 4, 6], [9, 3, 6]]  
>  **Output** : {4: [10, 19, 9], 5: [8, 4, 3], 7: [4, 6, 6]}  
>  **Explanation** : All columns mapped with 1st row elements. Eg. 4 -> 10,
> 19, 9.
>
>  **Input** : test_list = [[4, 5, 7], [10, 8, 4], [19, 4, 6], [9, 3, 7]]  
>  **Output** : {4: [10, 19, 9], 5: [8, 4, 3], 7: [4, 6, 7]}  
>  **Explanation** : All columns mapped with 1st row elements. Eg. 7 -> 4, 6,
> 7.

 **Method #1 : Using list comprehension + dictionary comprehension**

This is one of the ways in which this task can be performed. In this, list
comprehension is responsible for construction of values and mapping and
dictionary conversion is done using dictionary comprehension.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Columns to Dictionary Conversion in Matrix

# Using dictionary comprehension + list comprehension

 

# initializing list

test_list = [[4, 5, 7], [10, 8, 3], [19,
4, 6], [9, 3, 6]]

 

# printing original list

print("The original list : " + str(test_list))

 

# dictionary comprehension performing re making of result 

# dictionary

res = {test_list[0][idx]: [test_list[ele][idx]

 for ele in range(1, len(test_list))]

 for idx in range(len(test_list[0]))}

 

# printing result 

print("Reformed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[4, 5, 7], [10, 8, 3], [19, 4, 6], [9, 3, 6]]
    Reformed dictionary : {4: [10, 19, 9], 5: [8, 4, 3], 7: [3, 6, 6]}
    

**Method #2 : Using dictionary comprehension + zip()**

This is yet another way to solve this problem. In this, we map all column
elements with each other using zip() and dictionary comprehension is used to
perform remaking of dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Columns to Dictionary Conversion in Matrix

# Using dictionary comprehension + zip()

 

# initializing list

test_list = [[4, 5, 7], [10, 8, 3], [19,
4, 6], [9, 3, 6]]

 

# printing original list

print("The original list : " + str(test_list))

 

# appropriate slicing before zip function 

res = {ele[0]: list(ele[1:]) for ele in
zip(*test_list)}

 

# printing result 

print("Reformed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[4, 5, 7], [10, 8, 3], [19, 4, 6], [9, 3, 6]]
    Reformed dictionary : {4: [10, 19, 9], 5: [8, 4, 3], 7: [3, 6, 6]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

