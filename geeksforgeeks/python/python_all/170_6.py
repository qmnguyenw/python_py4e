Python | Get the Index of first element greater than K



Python list operations are always desired to have shorthands as they are used
in many places in development. Hence having knowledge of them always remains
quite useful.  
Let’s deals with finding one such utility of having index of first element
greater than K by one-liner. There are various ways in which this can be
achieved.

 **Method #1 : Usingnext() + enumerate()**  
Using next() returns the iterator to the element that has been using the
enumerate(). We simply put the condition for enumerate and next() picks
appropriate element index.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to find index of first element just 

# greater than K 

# using enumerate() + next()

 

# initializing list

test_list = [0.4, 0.5, 11.2, 8.4, 10.4]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using enumerate() + next() to find index of

# first element just greater than 0.6 

res = next(x for x, val in enumerate(test_list)

 if val > 0.6)

 

# printing result

print ("The index of element just greater than 0.6 : "

 + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [0.4, 0.5, 11.2, 8.4, 10.4]
    The index of element just greater than 0.6 : 2
    

  
**Method #2 : Usingfilter() \+ lambda**  
Using filter along with lambda can also help us to achieve this particular
task, subscript index value 0 is used to specify that first element greater
than value has to be taken.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to find index of first element just 

# greater than K 

# using filter() + lambda

 

# initializing list

test_list = [0.4, 0.5, 11.2, 8.4, 10.4]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using filter() + lambda

# to find index of first element just 

# greater than 0.6 

res = list(filter(lambda i: i > 0.6, test_list))[0]

 

# printing result

print ("The index of element just greater than 0.6 : "

 + str(test_list.index(res)))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : [0.4, 0.5, 11.2, 8.4, 10.4]
    The index of element just greater than 0.6 : 2
    

