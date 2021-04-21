Python Program to print a specific number of rows with Maximum Sum



Given a Matrix, the following article extracts a specifies number of rows that
has a maximum sum.

>  **Input** : test_list = [[3, 4, 5, 6], [1, 4, 6], [199], [2, 3, 4, 5, 6],
> [7, 3, 1]], K = 3  
> **Output** : [[199], [2, 3, 4, 5, 6], [3, 4, 5, 6]]  
> **Explanation** : 199 > 20 > 18, 3 maximum elements rows are extracted.  
>  **Input** : test_list = [[3, 4, 5, 6], [1, 4, 6], [199], [2, 3, 4, 5, 6],
> [7, 3, 1]], K = 2  
> **Output** : [[199], [2, 3, 4, 5, 6]]  
> **Explanation** : 199 > 20, 2 maximum elements rows are extracted.

**Method 1 :** _Using_ _sorted(),_ ___reverse,_ ___slice_ _and_ _sum()_

In this, we perform the task of sorting using sorted() and getting sum using
sum(). Reverse key is used to perform reversal of rows for getting maximum
summation rows at top and then top K(specific number of rows) rows are sliced.

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
[199], [2, 3, 4, 5, 6], [7, 3, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# sorted gets reverse sorted matrix by sum

# K rows extracted using slicing

res = sorted(test_list, key=lambda row: sum(row),
reverse=True)[:K]

 

# printing result

print("The filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

> The original list is : [[3, 4, 5, 6], [1, 4, 6], [199], [2, 3, 4, 5, 6], [7,
> 3, 1]]
>
> The filtered rows : [[199], [2, 3, 4, 5, 6], [3, 4, 5, 6]]

 **Method 2 :** _Using_ _sort()_ _,_ _reverse_ _,_ _slicing_ _and_ _sum()_

In this, we perform the task of in place sorting using sort(), using reverse
as key. Slicing is done using slice operation. The sum(), is used to take
summation and an external function is called to compute sum of rows of the
list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# row sum util.

def row_sum(row):

 return sum(row)

 

 

# initializing list

test_list = [[3, 4, 5, 6], [1, 4, 6],
[199], [2, 3, 4, 5, 6], [7, 3, 1]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 3

 

# sort() used to sort

# K rows extracted using slicing

test_list.sort(key=row_sum, reverse=True)

res = test_list[:K]

 

# printing result

print("The filtered rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[3, 4, 5, 6], [1, 4, 6], [199], [2, 3, 4, 5, 6], [7,
> 3, 1]]
>
> The filtered rows : [[199], [2, 3, 4, 5, 6], [3, 4, 5, 6]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

