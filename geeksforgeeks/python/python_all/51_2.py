Python – Elements Maximum till current index in List



Given list with elements, extract element if it’s the maximum element till
current index.

>  **Input** : test_list = [4, 6, 7, 8]
>
>  **Output** : [4, 6, 7, 8]
>
>  **Explanation** : All elements are maximum till their index.
>
>  **Input** : test_list = [6, 7, 3, 6, 8, 7]
>
>  
>
>
>  
>
>
>  **Output** : [7, 8]
>
>  **Explanation** : 7 and 8 are maximum till their index.

 **Method #1 : Using loop**

This is brute method in which this task can be performed. In this, we run
nested loop till current index and increment the counter if all elements are
lower than current element, if counter matches the current index, suggests
that current element is maximum till current index.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements Maximum till current index in List

# Using loop

 

# initializing list

test_list = [3, 5, 2, 6, 7, 9, 3]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using loop

res = []

for idx in range(1, len(test_list)):

 cnt = 0

 

 # inner loop to count element less than current

 for idx2 in range(idx):

 if test_list[idx] > test_list[idx2]:

 cnt = cnt + 1

 if cnt == idx:

 res.append(test_list[idx])

 

# printing result

print("Extracted Maximum elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [3, 5, 2, 6, 7, 9, 3]
    Extracted Maximum elements : [5, 6, 7, 9]
    
    
    

**Method #2 : Using max() + list comprehension + list slicing**

The combination of above functions can be used to solve this problem. In this,
we use max() to check if current element is greater that all previous elements
extracted using list slicing.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements Maximum till current index in List

# Using max() + list comprehension + list slicing

 

# initializing list

test_list = [3, 5, 2, 6, 7, 9, 3]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using max() + list comprehension + list slicing

# max() used to get if current is current maximum

res = [test_list[idx] for idx in range(

 1, len(test_list)) if test_list[idx] >
max(test_list[:idx])]

 

# printing result

print("Extracted Maximum elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [3, 5, 2, 6, 7, 9, 3]
    Extracted Maximum elements : [5, 6, 7, 9]
    
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

