Add custom borders to matrix in Python



Given a Matrix, the task is to write a python program to print each row having
custom borders.

    
    
     **Input :** test_list = [[4, 5, 6], [1, 4, 5], [6, 9, 1], [0, 3 ,1]], bord = "|"
    **Output :** | 4 5 6 |
             | 1 4 5 |
             | 6 9 1 |
             | 0 3 1 |
    **Explanation :** Matrix is ended using | border as required.
    
    **Input :** test_list = [[4, 5, 6], [1, 4, 5], [6, 9, 1], [0, 3 ,1]], bord = "!"
    **Output :** ! 4 5 6 !
             ! 1 4 5 !
             ! 6 9 1 !
             ! 0 3 1 !
    Explanation : Matrix is ended using ! border as required.

 **Method #1 : Using** **loop**

In this, we perform task of printing the row elements using inner loop,
separated by space. The main step of adding custom borders is concatenated
using + operator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Matrix Borders

# Using loop

 

# initializing list

test_list = [[4, 5, 6], [1, 4, 5], 

 [6, 9, 1], [0, 3, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing border

bord = "|"

 

for sub in test_list:

 temp = bord + " "

 

 # inner row

 for ele in sub:

 temp = temp + str(ele) + " "

 

 # adding border

 temp = temp + bord

 print(temp)  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [[4, 5, 6], [1, 4, 5], [6, 9, 1], [0, 3, 1]]
    | 4 5 6 |
    | 1 4 5 |
    | 6 9 1 |
    | 0 3 1 |

 **Method #2 : Using * operator +** **loop**

  

  

In this, the task of joining inner characters is performed using * operator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Matrix Borders

# Using * operator + loop

 

# initializing list

test_list = [[4, 5, 6], [1, 4, 5], 

 [6, 9, 1], [0, 3, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing border

bord = "|"

 

for sub in test_list:

 

 # * operator performs task of joining

 print(bord, *sub, bord)  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [[4, 5, 6], [1, 4, 5], [6, 9, 1], [0, 3, 1]]
    | 4 5 6 |
    | 1 4 5 |
    | 6 9 1 |
    | 0 3 1 |

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

