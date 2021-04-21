Python Program to Filter Rows with a specific Pair Sum



Given Matrix, the following program shows how to extract all rows which have a
pair such that their sum is equal to a specific number, here denoted as K.

>  **Input** : test_list = [[1, 5, 3, 6], [4, 3, 2, 1], [7, 2, 4, 5], [6, 9,
> 3, 2]], k = 8  
> **Output** : [[1, 5, 3, 6], [6, 9, 3, 2]]  
> **Explanation** : 5 + 3 = 8 and 6 + 2 = 8.  
> **Input** : test_list = [[1, 5, 4, 6], [4, 3, 2, 1], [7, 2, 4, 5], [6, 9, 3,
> 7]], k = 8  
> **Output** : []  
> **Explanation** : No list with 8 as pair summation.

**Method 1 :** _Using_ _loop_ _and_ _list comprehension_

In this we perform the task of getting all the pair whose sum is equal to a
given value using external function and filtering of lists is done using list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# get pair sum

def pair_sum(x, k):

 

 # checking pair sum

 for idx in range(len(x)):

 for ix in range(idx + 1, len(x)):

 if x[idx] + x[ix] == k:

 return True

 return False

 

 

# initializing list

test_list = [[1, 5, 3, 6], [4, 3, 2, 1],
[7, 2, 4, 5], [6, 9, 3, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

k = 8

 

# checking for pair sum

res = [ele for ele in test_list if pair_sum(ele, k)]

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [[1, 5, 3, 6], [4, 3, 2, 1], [7, 2, 4, 5], [6, 9, 3,
> 2]]
>
> Filtered Rows : [[1, 5, 3, 6], [6, 9, 3, 2]]

 **Method 2 :** _Using_ _filter()_ _and_ _lambda_

In this, we perform task of filtering using filter() and lambda function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# get pair sum

def pair_sum(x, k):

 

 # checking pair sum

 for idx in range(len(x)):

 for ix in range(idx + 1, len(x)):

 if x[idx] + x[ix] == k:

 return True

 return False

 

 

# initializing list

test_list = [[1, 5, 3, 6], [4, 3, 2, 1],
[7, 2, 4, 5], [6, 9, 3, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

k = 8

 

# checking for pair sum

# filtering using filter() and lambda

res = list(filter(lambda ele: pair_sum(ele, k), test_list))

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[1, 5, 3, 6], [4, 3, 2, 1], [7, 2, 4, 5], [6, 9, 3,
> 2]]
>
> Filtered Rows : [[1, 5, 3, 6], [6, 9, 3, 2]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

