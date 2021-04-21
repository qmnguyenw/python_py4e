Python | Check if list is strictly increasing



The test for monotonic sequence is a utility that has manifold applications in
mathematics and hence every sphere related to mathematics. As mathematics and
Computer Science generally go parallel, mathematical operations such as
checking for strictly increasing sequence can be useful to gather knowledge
of. Same argument can be extended for strictly decreasing lists also. Lets
discuss certain ways to perform this test.

 **Method #1 : Usingall() + zip()**  
The all() generally checks for all the elements fed to it. The task of zip()
is to link list beginning from beginning and list beginning from first
element, so that a check can be performed on all elements.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to check for strictly increasing list

# using zip() + all()

 

# initializing list

test_list = [1, 4, 5, 7, 8, 10]

 

# printing original lists

print ("Original list : " + str(test_list))

 

# using zip() + all()

# to check for strictly increasing list

res = all(i < j for i, j in zip(test_list,
test_list[1:]))

 

# printing result

print ("Is list strictly increasing ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list : [1, 4, 5, 7, 8, 10]
    Is list strictly increasing ? : True
    

  
**Method #2 : Usingreduce() \+ lambda**  
reduce() coupled with lambda can also perform this task of checking for
monotonicity. reduce function is used to cumulate the result as True or False,
lambda function checks for each index value with next index value.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to check for strictly increasing list

# using reduce() + lambda

 

# initializing list

test_list = [1, 4, 5, 7, 8, 10]

 

# printing original lists

print ("Original list : " + str(test_list))

 

# using reduce() + lambda

# to check for strictly increasing list

res = bool(lambda test_list: reduce(lambda i, j: j if

 i < j else 9999, test_list) != 9999)

 

# printing result

print ("Is list strictly increasing ? : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Original list : [1, 4, 5, 7, 8, 10]
    Is list strictly increasing ? : True
    

