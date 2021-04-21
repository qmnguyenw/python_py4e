Python | Sort list of lists by lexicographic value and then length



There are many times different types of sorting has been discussed in python
lists. The sorting of python list of lists has also been discussed. But
sometimes, we have two parameters upon which we need to sort. First one being
the _list sum_ and next being its _length_. Let’s discuss how this type of
problem can be solved.

 **Method #1 : Usingsort() twice**  
The first approach that comes into the mind is the generic way that is to use
the sort function twice, firstly on basis of the value and then on basis of
size of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort list of lists by value and length

# using sort() twice 

 

# initializing list 

test_list = [[1, 4, 3, 2], [5, 4, 1], [1,
4, 6, 7]]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using sort() twice 

# sort list of lists by value and length

test_list.sort()

test_list.sort(key = len)

 

# printing result

print ("The list after sorting by value and length " +
str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[1, 4, 3, 2], [5, 4, 1], [1, 4, 6, 7]]  
> The list after sorting by value and length [[5, 4, 1], [1, 4, 3, 2], [1, 4,
> 6, 7]]

  
**Method #2 : Using lambda function**  
The above method calls a single sort function twice but as an improvement to
it, this method calls the sort function just once and uses lambda function to
perform both sorts in one go.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort list of lists by value and length

# using lambda function

 

# initializing list 

test_list = [[1, 4, 3, 2], [5, 4, 1], [1,
4, 6, 7]]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# using lambda function 

# sort list of lists by value and length

res = sorted(test_list, key = lambda i: (len(i), i))

 

# printing result

print ("The list after sorting by value and length " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[1, 4, 3, 2], [5, 4, 1], [1, 4, 6, 7]]  
> The list after sorting by value and length [[5, 4, 1], [1, 4, 3, 2], [1, 4,
> 6, 7]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

