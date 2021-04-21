Python Program that prints rows from the matrix that have same element at a
given index



Given a Matrix, the following article shows how rows which has similar digit
at the specified index will be extracted and returned as output.

>  **Input** : test_list = [[3345, 6355, 83, 938], [323, 923, 845], [192, 993,
> 49], [98, 34, 23]], K = 1  
> **Output** : [[3345, 6355, 83, 938], [192, 993, 49]]  
> **Explanation** : 3 and 9 [ same ] in 1st column.  
>  **Input** : test_list = [[3445, 6355, 83, 938], [323, 923, 845], [192, 993,
> 49], [98, 34, 23]], K = 1  
> **Output** : [[192, 993, 49]]  
> **Explanation** : 9 in 1st column.

**Method 1 :** _Using all() and_ _list comprehension_

In this, we check for all the digits at a specified index using all() and list
comprehension is used for iterating each row.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [[3345, 6355, 83, 938], [

 323, 923, 845], [192, 993, 49], [98, 34,
23]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 1

 

# checking for all elements match using all()

res = [row for row in test_list if all(

 str(i)[K] == str(row[0])[K] for i in row)]

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

