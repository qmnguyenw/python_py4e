Python | Integrity Sorting in two lists



Often during the problem solving we come across to many problems where we need
to sort the list. But sometimes we would also want to sort the another list so
that the elements of are automatically shifted and remain at same index as the
first list even after first list get sorted. Let’s discuss certain ways in
which this can be done.  

 **Method #1 : Usingsorted() + zip() + itemgetter()**  
Combining the three functions we can possibly achieve the task. The zip
functions binds the two list together, sorted function sorts the list and
itemgetter function is used to define the metrics against which we need second
list to shift, in this case first list.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# integrity sorting in two list 

# using sorted() + zip() + itemgetter()

from operator import itemgetter

 

# initializing lists

test_list1 = [3, 4, 9, 1, 6]

test_list2 = [1, 5, 3, 6, 7]

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using sorted() + zip() + itemgetter()

# integrity sorting in two list 

res = [list(x) for x in
zip(*sorted(zip(test_list1, test_list2),

 key = itemgetter(0)))]

 

# printing result 

print ("The lists after integrity sort : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [3, 4, 9, 1, 6]
    The original list 2 is : [1, 5, 3, 6, 7]
    The lists after integrity sort : [[1, 3, 4, 6, 9], [6, 1, 5, 7, 3]]
    

  
**Method #2 : Usingsorted() + zip() + lambda function**  
This method performs the similar task, each function performing the similar
function, the difference is just the instead of itemgetter function, lambda
function performs the task of assigning a base to sort the list, i.e the first
list in this case.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# integrity sorting in two list 

# using sorted() + zip() + lambda function

from operator import itemgetter

 

# initializing lists

test_list1 = [3, 4, 9, 1, 6]

test_list2 = [1, 5, 3, 6, 7]

 

# printing original lists

print ("The original list 1 is : " + str(test_list1))

print ("The original list 2 is : " + str(test_list2))

 

# using sorted() + zip() + lambda function

# integrity sorting in two list 

res = [list(i) for i in
zip(*sorted(zip(test_list1, test_list2),

 key = lambda dual: dual[0]))]

 

# printing result 

print ("The lists after integrity sort : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list 1 is : [3, 4, 9, 1, 6]
    The original list 2 is : [1, 5, 3, 6, 7]
    The lists after integrity sort : [[1, 3, 4, 6, 9], [6, 1, 5, 7, 3]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

