Python Program that filters out non-empty rows of a matrix



Given Matrix, the following article shows how to filter all the Non-Empty rows
of a matrix. In simpler terms, the codes provided below return a matrix after
removing empty rows from it.

> **Input** : test_list = [[4, 5, 6, 7], [], [], [9, 8, 1], []]  
> **Output** : [[4, 5, 6, 7], [9, 8, 1]]  
> **Explanation** : All empty rows are removed.  
>  **Input** : test_list = [[4, 5, 6, 7], [], [9, 8, 1], []]  
> **Output** : [[4, 5, 6, 7], [9, 8, 1]]  
> **Explanation** : All empty rows are removed.

**Method 1 :** _Using_ _list comprehension_ _and_ _len()_

In this we check each row for its length, if its length is greater than 0 then
that row is added to result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[4, 5, 6, 7], [], [], [9, 8, 1],
[]]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# checking for row lengths using len()

res = [row for row in test_list if len(row) > 0]

 

# printing result

print("Filtered Matrix " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [[4, 5, 6, 7], [], [], [9, 8, 1], []]
>
> Filtered Matrix [[4, 5, 6, 7], [9, 8, 1]]

 **Method 2 :** _Using_ _filter(),_ ___lambda_ _and_ _len()_

In this, we filter rows w.r.t lengths using filter() and lambda function. The
len() is used to get the length.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[4, 5, 6, 7], [], [], [9, 8, 1],
[]]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# checking for row lengths using len()

# filtering using filter() + lambda

res = list(filter(lambda row: len(row) > 0,
test_list))

 

# printing result

print("Filtered Matrix " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[4, 5, 6, 7], [], [], [9, 8, 1], []]
>
> Filtered Matrix [[4, 5, 6, 7], [9, 8, 1]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

