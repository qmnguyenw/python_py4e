Python program to print Rows where all its Elements’ frequency is greater than
K



Given Matrix, extract all rows whose all elements have a frequency greater
than K.

>  **Input** : test_list = [[1, 1, 2, 3, 2, 3], [4, 4, 5, 6, 6], [1, 1, 1, 1],
> [4, 5, 6, 8]], K = 2  
> **Output** : [[1, 1, 1, 1]]  
> **Explanation** : Here, frequency of 1 is 4 > 2, hence row retained.
>
>  **Input** : test_list = [[1, 1, 2, 3, 2, 3], [4, 4, 5, 6, 6], [1, 3, 4, 1],
> [4, 5, 6, 8]], K = 2  
> **Output** : []  
> **Explanation** : No list filtered as result.

**Method #1 : Using** **list comprehension** **+** **all()** **+** **count()**

In this, we perform task of iterating through elements using list
comprehension and all() is used to check for each elements count(), extracted
using count().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rows with all Elements frequency greater than K

# Using list comprehension + count() + all()

 

def freq_greater_K(row, K) :

 

 # checking for all elements occurrence greater than K 

 return all(row.count(ele) > K for ele in row)

 

# initializing list

test_list = [[1, 1, 2, 3, 2, 3], [4, 4,
5, 6, 6], [1, 1, 1, 1], [4, 5, 6,
8]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

# checking for each row 

res = [ele for ele in test_list if freq_greater_K(ele, K)]

 

# printing result 

print("Filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[1, 1, 2, 3, 2, 3], [4, 4, 5, 6, 6], [1, 1, 1, 1],
> [4, 5, 6, 8]]  
> Filtered rows : [[1, 1, 2, 3, 2, 3], [1, 1, 1, 1]]

 **Method #2 : Using** **filter()** **+** **lambda** **\+ all() + count()**

In this, task of filtering is done using filter() + lambda, all() is used to
check for each element, count() to compute count.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rows with all Elements frequency greater than K

# Using filter() + lambda + all() + count()

 

def freq_greater_K(row, K) :

 

 # checking for all elements occurrence greater than K 

 return all(row.count(ele) > K for ele in row)

 

# initializing list

test_list = [[1, 1, 2, 3, 2, 3], [4, 4,
5, 6, 6], [1, 1, 1, 1], [4, 5, 6,
8]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 1

 

# checking for each row 

res = list(filter(lambda ele : freq_greater_K(ele, K),
test_list))

 

# printing result 

print("Filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[1, 1, 2, 3, 2, 3], [4, 4, 5, 6, 6], [1, 1, 1, 1],
> [4, 5, 6, 8]]  
> Filtered rows : [[1, 1, 2, 3, 2, 3], [1, 1, 1, 1]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

