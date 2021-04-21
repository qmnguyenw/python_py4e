Python Program to Convert Matrix to String



Given a matrix, our task is to write a Python program to convert to the
matrix, with different delimiters for element and row separation.

 **Examples:**

>  **Input :** test_list = test_list = [[1, 3, “gfg”], [2, “is”, 4], [“best”,
> 9, 5]], in_del, out_del = “,”, ” “
>
>  **Output :** 1,3,gfg 2,is,4 best,9,5
>
>  **Explanation :** Element in list separated by “,”, and lists separated by
> ” “.
>
>  
>
>
>  
>
>
>  **Input :** test_list = test_list = [[1, 3, “gfg”], [2, “is”, 4], [“best”,
> 9, 5]], in_del, out_del = “,”, “-“
>
>  **Output :** 1,3,gfg-2,is,4-best,9,5
>
>  **Explanation :** Element in list separated by “,”, and lists separated by
> “-“.

 **Method #1 : Using** **join()** **+** **list comprehension**

In this, we perform task of iterating each element of each row using list
comprehension. The inner and outer join for element and row with different
delimiters using join().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to String

# Using list comprehension + join()

 

# initializing list

test_list = [[1, 3, "gfg"], [2, "is", 4],
["best", 9, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing delims

in_del, out_del = ",", " "

 

# nested join using join()

res = out_del.join([in_del.join([str(ele) for ele in sub])
for sub in test_list])

 

# printing result

print("Conversion to String : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[1, 3, ‘gfg’], [2, ‘is’, 4], [‘best’, 9, 5]]
>
> Conversion to String : 1,3,gfg 2,is,4 best,9,5
>
>  
>
>
>  
>

 **Method #2 : Using** **map()** **+** **join()**

In this, task of inner joining of elements is extending to each character
using map(). Rest all the functionalities are similar to upper method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Matrix to String

# Using map() + join()

 

# initializing list

test_list = [[1, 3, "gfg"], [2, "is", 4],
["best", 9, 5]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing delims

in_del, out_del = ",", " "

 

# nested join using join()

# map() for joining inner elements

res = out_del.join(in_del.join(map(str, sub)) for sub in
test_list)

 

# printing result

print("Conversion to String : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[1, 3, ‘gfg’], [2, ‘is’, 4], [‘best’, 9, 5]]
>
> Conversion to String : 1,3,gfg 2,is,4 best,9,5

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

