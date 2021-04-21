Python program to Reverse a range in list



Given a List, our task is to write a Python program to reverse a range in the
list.

 **Example:**

>  **Input :** test_list = [6, 3, 1, 8, 9, 2, 10, 12, 7, 4, 11], str, end = 3,
> 9
>
>  **Output :** [6, 3, 1, 7, 12, 10, 2, 9, 8, 4, 11]
>
>  **Explanation :** 8, 9, 2, 10, 12, 7 are reversed in list to 7, 12, 10, 2,
> 9, 8.
>
>  
>
>
>  
>
>
>  **Input :** test_list = [6, 3, 1, 8, 9, 2, 10, 12, 7, 4, 11], str, end = 8,
> 9
>
>  **Output :** [6, 3, 1, 8, 9, 2, 10, 7, 12, 4, 11]
>
>  **Explanation :** 12, 7 are reversed in list to 7, 12.

 **Method #1 : Using** **reverse()** **+** **loop**

In this example, sublist is extracted and reversed using reverse(). The loop
is used next to replace range elements with reversed elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reversing a range

# Using reverse() + loop

 

# initializing list

test_list = [6, 3, 1, 8, 9, 2, 10, 12,
7, 4, 11]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range 

strt, end = 3, 9

 

# reversing list and assigning the range

temp = test_list[strt:end]

temp.reverse()

for idx in range(strt, end):

 test_list[idx] = temp[idx - strt]

 

# printing result

print("Range reversed range list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [6, 3, 1, 8, 9, 2, 10, 12, 7, 4, 11]
    Range reversed range list : [6, 3, 1, 7, 12, 10, 2, 9, 8, 4, 11]

 **Method #2 : Using list** **split()** **+** **slicing**

The compact approach to solve this problem is to perform a reversal of range
list using list split way of reversing slicing only the required range.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reversing a range

# Using list split + slicing

 

# initializing list

test_list = [6, 3, 1, 8, 9, 2, 10, 12,
7, 4, 11]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range 

strt, end = 3, 9

 

# Third arg. of split with -1 performs reverse 

test_list[strt:end] = test_list[strt:end][::-1]

 

# printing result

print("Range reversed range list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [6, 3, 1, 8, 9, 2, 10, 12, 7, 4, 11]
    Range reversed range list : [6, 3, 1, 7, 12, 10, 2, 9, 8, 4, 11]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

