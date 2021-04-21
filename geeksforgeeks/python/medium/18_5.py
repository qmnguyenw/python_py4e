Python | Sort list of tuples by specific ordering



The normal sorting of tuples has been dealt previously. This article aims at
sorting the given list of tuples by the second element, based on the order
provided in some list.

 **Method #1 : Using list comprehension +filter() \+ lambda**  
Above three functions can be combined to perform the particular task in which
list comprehension performs the iteration, lambda function is used as helper
function for filtering to sort according to second element of tuple.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# sort list of tuples according to second

# using list comprehension + filter() + lambda

 

# initializing list of tuples

test_list = [('a', 2), ('c', 3), ('d', 4)]

 

# initializing sort order 

sort_order = [4, 2, 3]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# printing sort order list 

print ("The sort order list is : " + str(sort_order))

 

# using list comprehension + filter() + lambda

# sort list of tuples according to second

res = [i for j in sort_order 

 for i in filter(lambda k: k[1] == j, test_list)]

 

# printing result

print ("The list after appropriate sorting : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [('a', 2), ('c', 3), ('d', 4)]
    The sort order list is : [4, 2, 3]
    The list after appropriate sorting : [('d', 4), ('a', 2), ('c', 3)]
    

  
**Method #2 : Usingsorted() + index() \+ lambda**  
The sorted function can be used to sort according to order specified. The
index function specifies that second element of tuple has to be taken into
considerations and all are joined with help of lambda.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# sort list of tuples according to second

# using sorted() + index() + lambda

 

# initializing list of tuples

test_list = [('a', 2), ('c', 3), ('d', 4)]

 

# initializing sort order 

sort_order = [4, 2, 3]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# printing sort order list 

print ("The sort order list is : " + str(sort_order))

 

# using sorted() + index() + lambda

# sort list of tuples according to second

res = list(sorted(test_list, 

 key = lambda i: sort_order.index(i[1])))

 

# printing result

print ("The list after appropriate sorting : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [('a', 2), ('c', 3), ('d', 4)]
    The sort order list is : [4, 2, 3]
    The list after appropriate sorting : [('d', 4), ('a', 2), ('c', 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

