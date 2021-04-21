Python program to find the Decreasing point in List



Given a list, get the index of element where the list shows the first negative
trend, i.e first point where the next element < current element. If not found
return -1.

>  **Input** : test_list = [3, 6, 8, 9, 12, 5, 18, 1]  
> **Output** : 4  
> **Explanation** : At 12 -> 5, first decreasing point occurs.
>
>  **Input** : test_list = [3, 9, 12, 5, 18, 1]  
> **Output** : 2  
> **Explanation** : At 12 -> 5, first decreasing point occurs.

**Method #1 : Using loop**

In this, we check for the next element to be less than the current element, at
a point where it is first found, we break the loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Decreasing point in List

# Using loop

 

# initializing list

test_list = [3, 6, 8, 9, 12, 5, 18, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = -1

for idx in range(0, len(test_list) - 1):

 

 # checking for 1st decreasing element

 if test_list[idx + 1] < test_list[idx]:

 res = idx

 break

 

# printing result 

print("Decreasing Point : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [3, 6, 8, 9, 12, 5, 18, 1]
    Decreasing Point : 4

 **Method #2 : Using** **enumerate()** **\+ loop**

In this, we check for index and value simultaneously using enumerate, a
similar method to above, the difference being separate index element access.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Decreasing point in List

# Using enumerate() + loop

 

# initializing list

test_list = [3, 6, 8, 9, 12, 5, 18, 1]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = -1

for idx, ele in enumerate(test_list):

 

 # checking for 1st decreasing element

 if test_list[idx + 1] < ele:

 res = idx

 break

 

# printing result 

print("Decreasing Point : " + str(res))  
  
---  
  
 __

 __

  
**Output:**

    
    
    The original list is : [3, 6, 8, 9, 12, 5, 18, 1]
    Decreasing Point : 4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

