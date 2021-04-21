Ways to concatenate two lists in Python



Let’s see how to concatenate two lists using different methods in Python. This
operation is useful when we have numbers of lists of elements which needs to
be processed in a similar manner.

 **Method #1 :** Using Naive Method

In this method, we traverse the second list and keep appending elements in the
first list, so that first list would have all the elements in both lists and
hence would perform the append.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate list

# concatenation using naive method 

 

# Initializing lists

test_list1 = [1, 4, 5, 6, 5]

test_list2 = [3, 5, 7, 2, 5]

 

# using naive method to concat

for i in test_list2 :

 test_list1.append(i)

 

# Printing concatenated list

print ("Concatenated list using naive method : "

 + str(test_list1))  
  
---  
  
 __

 __

 **Output:**

    
    
    Concatenated list using naive method : [1, 4, 5, 6, 5, 3, 5, 7, 2, 5]
    

  
**Method #2 :** Using + operator

  

  

The most conventional method to perform the list concatenation, the use of “+”
operator can easily add the whole of one list behind the other list and hence
perform the concatenation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate list

# concatenation using + operator 

 

# Initializing lists

test_list3 = [1, 4, 5, 6, 5]

test_list4 = [3, 5, 7, 2, 5]

 

# using + operator to concat

test_list3 = test_list3 + test_list4

 

# Printing concatenated list

print ("Concatenated list using + : "

 + str(test_list3))  
  
---  
  
 __

 __

 **Output:**

    
    
    Concatenated list using + : [1, 4, 5, 6, 5, 3, 5, 7, 2, 5]
    

**Method #3 :** Using list comprehension

List comprehension can also accomplish this task of list concatenation. In
this case, a new list is created, but this method is a one liner alternative
to the loop method discussed above.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate list

# concatenation using list comprehension 

 

# Initializing lists

test_list1 = [1, 4, 5, 6, 5]

test_list2 = [3, 5, 7, 2, 5]

 

# using list comprehension to concat

res_list = [y for x in [test_list1, test_list2] for y in
x]

 

# Printing concatenated list

print ("Concatenated list using list comprehension: "

 + str(res_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Concatenated list using list comprehension: [1, 4, 5, 6, 5, 3, 5, 7, 2, 5]
    

  
**Method #4 :** Using extend()

extend() is the function extended by lists in Python and hence can be used
to perform this task. This function performs the inplace extension of first
list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate list

# concatenation using list.extend()

 

# Initializing lists

test_list3 = [1, 4, 5, 6, 5]

test_list4 = [3, 5, 7, 2, 5]

 

# using list.extend() to concat

test_list3.extend(test_list4)

 

# Printing concatenated list

print ("Concatenated list using list.extend() : "

 + str(test_list3))  
  
---  
  
 __

 __

 **Output:**

    
    
    Concatenated list using list.extend() : [1, 4, 5, 6, 5, 3, 5, 7, 2, 5]
    

  
**Method #5 :** Using * operator

Using * operator, this method is the new addition to list concatenation and
works only in Python 3.6+. Any no. of lists can be concatenated and returned
in a new list using this operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate list

# concatenation using * operator

 

# Initializing lists

test_list1 = [1, 4, 5, 6, 5]

test_list2 = [3, 5, 7, 2, 5]

 

# using * operator to concat

res_list = [*test_list1, *test_list2]

 

# Printing concatenated list

print ("Concatenated list using * operator : "

 + str(res_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Concatenated list using * operator : [1, 4, 5, 6, 5, 3, 5, 7, 2, 5]
    

  
**Method #6 :** Using itertools.chain()

itertools.chain() returns the iterable after chaining its arguments in one
and hence does not require to store the concatenated list if only its initial
iteration is required. This is useful when concatenated list has to be used
just once.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate list

# concatenation using itertools.chain()

import itertools

 

# Initializing lists

test_list1 = [1, 4, 5, 6, 5]

test_list2 = [3, 5, 7, 2, 5]

 

# using itertools.chain() to concat

res_list = list(itertools.chain(test_list1, test_list2))

 

# Printing concatenated list

print ("Concatenated list using itertools.chain() : "

 + str(res_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    Concatenated list using itertools.chain() : [1, 4, 5, 6, 5, 3, 5, 7, 2, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

