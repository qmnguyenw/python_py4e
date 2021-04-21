Python Program to Sort Matrix Rows by summation of consecutive difference of
elements



Given a Matrix, the following article depicts how to sort rows of a matrix on
the basis of summation of difference between consecutive elements of a row.

>  **Input** : test_list = [[1, 5, 3, 6], [4, 3, 2, 1], [7, 2, 4, 5], [6, 9,
> 3, 2]],  
> **Output** : [[4, 3, 2, 1], [7, 2, 4, 5], [1, 5, 3, 6], [6, 9, 3, 2]]  
> **Explanation** : 4 < 8 < 9 < 10 is consecutive difference summation.  
>  **Input** : test_list = [[1, 5, 3, 6], [7, 2, 4, 5], [6, 9, 3, 2]],  
> **Output** : [[7, 2, 4, 5], [1, 5, 3, 6], [6, 9, 3, 2]]  
> **Explanation** : 8 < 9 < 10 is consecutive difference summation.

**Method 1 :** _Using_ _sort()_ _and_ _abs()_

In this, we perform task of in-place sorting using sort() and abs() is used to
get the absolute value of the summation of consecutive difference.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# get abs summation

def diff_sum(row):

 return sum([abs(row[idx + 1] - row[idx]) for idx
in range(0, len(row) - 1)])

 

 

# initializing list

test_list = [[1, 5, 3, 6], [4, 3, 2, 1],
[7, 2, 4, 5], [6, 9, 3, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing inplace sort

test_list.sort(key=diff_sum)

 

# printing result

print("Sorted Rows : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [[1, 5, 3, 6], [4, 3, 2, 1], [7, 2, 4, 5], [6, 9, 3,
> 2]]
>
> Sorted Rows : [[4, 3, 2, 1], [7, 2, 4, 5], [1, 5, 3, 6], [6, 9, 3, 2]]

 **Method 2 :** _Using_ _sorted()_ _,_ _lambda_ _,_ _abs()_ _and_ _sum()_

In this, the sorting is done using sorted() and lambda function is used to
inject conditional statement in sorted().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[1, 5, 3, 6], [4, 3, 2, 1],
[7, 2, 4, 5], [6, 9, 3, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# performing sort

res = sorted(test_list, key=lambda row: sum(

 [abs(row[idx + 1] - row[idx]) for idx in
range(0, len(row) - 1)]))

 

# printing result

print("Sorted Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[1, 5, 3, 6], [4, 3, 2, 1], [7, 2, 4, 5], [6, 9, 3,
> 2]]
>
> Sorted Rows : [[4, 3, 2, 1], [7, 2, 4, 5], [1, 5, 3, 6], [6, 9, 3, 2]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

