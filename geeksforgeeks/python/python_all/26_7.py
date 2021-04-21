Python – Row with Minimum difference in extreme values



Given a Matrix, extract the rows with a minimum difference in extreme values.

 **Examples:**

>  **Input** : test_list = [[4, 10, 18], [5, 0], [1, 4, 6], [19, 2]]  
> **Output** : [[1, 4, 6], [5, 0]]  
> **Explanation** : 6 – 1 = 5, 5 – 0 = 5, is minimum difference between
> extreme values.  
>
>
> **Input** : test_list = [[4, 10, 18], [5, 0], [2, 4, 6], [19, 2]]  
> **Output** : [[2, 4, 6]]  
> **Explanation** : 6 – 2 = 4, is min diff.  
>

**Method #1 : Using** **list comprehension** **+** **min()**

  

  

In this, we compute minimum difference between extreme values, and then use
list comprehension to get particular row with that value difference between
extreme values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Matrix Minimum difference in extreme values row

# Using min() + list comprehension

 

# initializing list

test_list = [[4, 10, 18], [5, 3, 10], [1,
4, 6], [19, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting min value 

min_val = min([max(sub) - min(sub) for sub in
test_list])

 

# using list comprehension to filter 

res = [sub for sub in test_list if max(sub) -
min(sub) == min_val]

 

# printing result 

print("Rows with Minimum difference in extreme values : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 10, 18], [5, 3, 10], [1, 4, 6], [19, 2]]  
> Rows with Minimum difference in extreme values : [[1, 4, 6]]

 **Method #2 : Using** **min()** **+** **list comprehension** **+**
**filter()** **+** **lambda**

In this, we perform task of filtering comparing with minimum value using
filter() + lambda.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Matrix Minimum difference in extreme values row

# Using min() + list comprehension + filter() + lambda

 

# initializing list

test_list = [[4, 10, 18], [5, 3, 10], [1,
4, 6], [19, 2]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting min value 

min_val = min([max(sub) - min(sub) for sub in
test_list])

 

# using filter() + lambda to filter 

res = list(filter(lambda sub : max(sub) - min(sub)
== min_val, test_list))

 

# printing result 

print("Rows with Minimum difference in extreme values : " +
str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 10, 18], [5, 3, 10], [1, 4, 6], [19, 2]]  
> Rows with Minimum difference in extreme values : [[1, 4, 6]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

