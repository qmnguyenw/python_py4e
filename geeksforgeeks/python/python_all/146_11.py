Python | Sorting list of lists with similar list elements



Sorting has always been a key operation that is performed for many
applications and also as a subproblem to many problems. Many variations and
techniques have been discussed and it’s knowledge can be useful to have while
programming. This article discusses the sorting of lists containing a list.
Let’s discuss certain ways in which this can be performed.

 **Method #1 : Usingsorted() \+ list comprehension**  
In this method, we just use shorthand of the longer process that can be
applied. The list is iterated and subsequent sublist is sorted using the
sorted function sorting the inner list as well.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sorting list of lists with similar list elements

# using list comprehension + sorted()

 

# initializing list

test_list = [[[4, 4], [1, 1]], [[3, 3], [2,
2], [5, 5]]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + sorted()

# Sorting list of lists with similar list elements

res = [sorted(idx) for idx in test_list]

 

# print result

print("The list after performing sort operation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [[[4, 4], [1, 1]], [[3, 3], [2, 2], [5, 5]]]  
> The list after performing sort operation : [[[1, 1], [4, 4]], [[2, 2], [3,
> 3], [5, 5]]]

  

  

**Method #2 : Usingmap() + sorted()**  
The combination of above functions also perform the similar task as the above
method, just the difference being that map function is used to extend the sort
logic to whole of sublists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sorting list of lists with similar list elements

# using map() + sorted()

 

# initializing list

test_list = [[[4, 4], [1, 1]], [[3, 3], [2,
2], [5, 5]]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() + sorted()

# Sorting list of lists with similar list elements

res = list(map(sorted, test_list))

 

# print result

print("The list after performing sort operation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [[[4, 4], [1, 1]], [[3, 3], [2, 2], [5, 5]]]  
> The list after performing sort operation : [[[1, 1], [4, 4]], [[2, 2], [3,
> 3], [5, 5]]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

