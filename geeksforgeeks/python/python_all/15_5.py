Python – Sort Matrix by K Sized Subarray Maximum Sum



Given Matrix, write a Python program to sort rows by maximum of K sized
subarray sum.

 **Examples:**

>  **Input** : test_list = [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1], [4, 3, 9, 3, 9],
> [5, 4, 3, 2, 1]], K = 3  
> **Output** : [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1], [5, 4, 3, 2, 1], [4, 3, 9,
> 3, 9]]  
> **Explanation** : 12 = 12 = 12 < 21, is order of maximum sum 3 length
> substring.  
>
>
> **Input** : test_list = [[4, 3, 5, 2, 3], [4, 3, 9, 3, 9], [5, 4, 3, 2, 1]],
> K = 3  
> **Output** : [[4, 3, 5, 2, 3], [5, 4, 3, 2, 1], [4, 3, 9, 3, 9]]  
> **Explanation** : 12 = 12 < 21, is order of maximum sum 3 length substring.

**Method #1 : Using** **max()** **+** **sum()** **+** **slicing** **\+
sort()**

  

  

In this, maximum of K length subarray is computed using max(), sum() and
slicing using external function and inplace sorting is done using sort().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by K Sized Subarray Maximum Sum

# Using max() + sum() + slicing + sort()

 

 

def max_ksub(row):

 

 # getting maximum K length sum

 return max(sum(row[idx: idx + K]) for idx in
range(len(row) - K))

 

 

# initializing list

test_list = [[4, 3, 5, 2, 3], [6, 4, 2,
1, 1],

 [4, 3, 9, 3, 9], [5, 4, 3, 2, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# performing inplace sorting

test_list.sort(key=max_ksub)

 

# printing result

print("The sorted result : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1], [4, 3, 9, 3, 9],
> [5, 4, 3, 2, 1]]  
> The sorted result : [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1], [5, 4, 3, 2, 1], [4,
> 3, 9, 3, 9]]

 **Method #2 : Using** **sorted()** **+** **lambda** **\+ max() + sum() +
slicing**

In this, we perform task of sorting using sorted() + lambda function which
injects comparator logic and avoids calling external function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Matrix by K Sized Subarray Maximum Sum

# Using sorted() + lambda + max() + sum() + slicing

 

# initializing list

test_list = [[4, 3, 5, 2, 3], [6, 4, 2,
1, 1],

 [4, 3, 9, 3, 9], [5, 4, 3, 2, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# sorted() performs inplace sort

# lambda function injects comparison logic

res = sorted(test_list, key=lambda row: max(

 sum(row[idx: idx + K]) for idx in range(len(row) -
K)))

 

# printing result

print("The sorted result : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1], [4, 3, 9, 3, 9],
> [5, 4, 3, 2, 1]]  
> The sorted result : [[4, 3, 5, 2, 3], [6, 4, 2, 1, 1], [5, 4, 3, 2, 1], [4,
> 3, 9, 3, 9]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

