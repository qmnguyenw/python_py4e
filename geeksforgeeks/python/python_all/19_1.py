Python Program that prints the rows of a given length from a matrix



Given a Matrix, the following articles shows how to extract all the rows with
a specified length.

>  **Input** : test_list = [[3, 4, 5, 6], [1, 4, 6], [2], [2, 3, 4, 5, 6], [7,
> 3, 1]], K = 3  
> **Output** : [[1, 4, 6], [7, 3, 1]]  
> **Explanation** : Extracted lists have length of 3.  
>  **Input** : test_list = [[3, 4, 5, 6], [1, 4, 6], [2], [2, 3, 4, 5, 6], [7,
> 3, 1]], K = 4  
> **Output** : [[3, 4, 5, 6]]  
> **Explanation** : Extracted lists have length of 4.

**Method 1 :** _Using_ _list comprehension_ _and_ _len()_

In this, we perform the task of getting length using len() and list
comprehension does the task of filtering all the rows which have a specified
length.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[3, 4, 5, 6], [1, 4, 6],
[2], [2, 3, 4, 5, 6], [7, 3, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# list comprehension is used for extracting K len rows

res = [sub for sub in test_list if len(sub) == K]

 

# printing result

print("The filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [[3, 4, 5, 6], [1, 4, 6], [2], [2, 3, 4, 5, 6], [7,
> 3, 1]]
>
> The filtered rows : [[1, 4, 6], [7, 3, 1]]

 **Method 2 :** _Using_ _filter()_ _,_ _lambda_ _and_ _len()_

In this, we perform the task of filtering using filter() and lambda. len() is
used for finding length of rows.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[3, 4, 5, 6], [1, 4, 6],
[2], [2, 3, 4, 5, 6], [7, 3, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# filter() + lambda to filter out rows of len K

res = list(filter(lambda sub: len(sub) == K,
test_list))

 

# printing result

print("The filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 4, 5, 6], [1, 4, 6], [2], [2, 3, 4, 5, 6], [7,
> 3, 1]]
>
> The filtered rows : [[1, 4, 6], [7, 3, 1]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

