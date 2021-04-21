Python – Sort by range inclusion



Given a range, sort tuple Matrix by total range covered in a given range.
[Considering tuples which completely lie within range].

>  **Input** : test_list = [[(1, 5), (6, 10), (10, 15)], [(3, 16)], [(2, 4),
> (6, 8), (9, 14)], [(1, 3), (9, 13)]], i, j = 2, 15  
> **Output** : [[(3, 16)], [(1, 5), (6, 10), (10, 15)], [(1, 3), (9, 13)],
> [(2, 4), (6, 8), (9, 14)]]  
> **Explanation** : 0 < 4 < 4 < 9, is the magnitude of range covered in tuples
> lists.
>
>  **Input** : test_list = [[(1, 5), (6, 10), (10, 15)], [(3, 16)], [(2, 4),
> (6, 8), (9, 14)]], i, j = 2, 15  
> **Output** : [[(3, 16)], [(1, 5), (6, 10), (10, 15)], [(2, 4), (6, 8), (9,
> 14)]]  
> **Explanation** : 0 < 4 < 9, is the magnitude of range covered in tuples
> lists.

**Method #1 : Using sort() +** **sum()**

In this, inplace sorting is performed using sort(), and summation of ranges in
the given range is performed using sum() and list comprehension with
conditions.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by range inclusion

# Using sort() + sum()

 

 

def range_sum(row):

 

 # summing in range element

 return sum([abs(sub[1] - sub[0]) for sub in
row if sub[0] > i and sub[0] < j and sub[1] > i
and sub[1] < j])

 

 

# initializing list

test_list = [[(1, 5), (6, 10), (10, 15)],
[(3, 16)], [

 (2, 4), (6, 8), (9, 14)], [(1, 3), (9,
13)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range

i, j = 2, 15

 

# inplace sorting using sort()

test_list.sort(key=range_sum)

 

# printing result

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[(1, 5), (6, 10), (10, 15)], [(3, 16)], [(2, 4), (6,
> 8), (9, 14)], [(1, 3), (9, 13)]]  
> Sorted List : [[(3, 16)], [(1, 5), (6, 10), (10, 15)], [(1, 3), (9, 13)],
> [(2, 4), (6, 8), (9, 14)]]

 **Method #2 : Using** **sorted()** **+** **lambda** **\+ sum()**

In this, we perform task of sorting using sorted() and utility injection using
lambda function, the summation is performed using sum().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by range inclusion

# Using sorted() + lambda + sum()

 

# initializing list

test_list = [[(1, 5), (6, 10), (10, 15)],
[(3, 16)], [

 (2, 4), (6, 8), (9, 14)], [(1, 3), (9,
13)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing range

i, j = 2, 15

 

# sorting using sorted() + lambda

res = sorted(test_list, key=lambda row: sum(

 [abs(sub[1] - sub[0]) for sub in row if
sub[0] > i and sub[0] < j and sub[1] > i and
sub[1] < j]))

 

# printing result

print("Sorted List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[(1, 5), (6, 10), (10, 15)], [(3, 16)], [(2, 4), (6,
> 8), (9, 14)], [(1, 3), (9, 13)]]  
> Sorted List : [[(3, 16)], [(1, 5), (6, 10), (10, 15)], [(1, 3), (9, 13)],
> [(2, 4), (6, 8), (9, 14)]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

