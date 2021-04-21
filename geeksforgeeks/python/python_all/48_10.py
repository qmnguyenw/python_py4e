Python – Convert Matrix to dictionary



Given a Matrix, convert it into dictionary with keys as row number and value
as nested list.

>  **Input** : test_list = [[5, 6, 7], [8, 3, 2]]  
>  **Output** : {1: [5, 6, 7], 2: [8, 3, 2]}  
>  **Explanation** : Matrix rows are paired with row number in order.
>
>  **Input** : test_list = [[5, 6, 7]]  
>  **Output** : {1: [5, 6, 7]}  
>  **Explanation** : Matrix rows are paired with row number in order.

 **Method #1 : Using dictionary comprehension + range()**

The combination of above functions can be used to solve this problem. In this,
we perform the task of iteration using dictionary comprehension and range()
can be used to perform numbering of rows.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to dictionary 

# Using dictionary comprehension + range()

 

# initializing list

test_list = [[5, 6, 7], [8, 3, 2], [8, 2,
1]] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# using dictionary comprehension for iteration

res = {idx + 1 : test_list[idx] for idx in
range(len(test_list))}

 

# printing result 

print("The constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[5, 6, 7], [8, 3, 2], [8, 2, 1]]
    The constructed dictionary : {1: [5, 6, 7], 2: [8, 3, 2], 3: [8, 2, 1]}
    

**Method #2 : Using dictionary comprehension + enumerate()**

The combination of above functions can be used to solve this problem. In this,
dictionary comprehension help in construction of dictionary and enumerate()
helps in iteration like range() in above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to dictionary 

# Using dictionary comprehension + enumerate()

 

# initializing list

test_list = [[5, 6, 7], [8, 3, 2], [8, 2,
1]] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# enumerate used to perform assigning row number

res = {idx: val for idx, val in enumerate(test_list, start =
1)}

 

# printing result 

print("The constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[5, 6, 7], [8, 3, 2], [8, 2, 1]]
    The constructed dictionary : {1: [5, 6, 7], 2: [8, 3, 2], 3: [8, 2, 1]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

