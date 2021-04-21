Python | Assign multiple variables with list values



We generally come through the task of getting certain index values and
assigning variables out of them. The general approach we follow is to extract
each list element by its index and then assign it to variables. This approach
requires more line of code. Let’s discuss certain ways to do this task in
compact manner to improve readability.

 **Method #1 : Using list comprehension**  
By using list comprehension one can achieve this task with ease and in one
line. We run a loop for specific indices in RHS and assign them to the
required variables.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to assign variables from list element

# using list comprehension 

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 3]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using list comprehension

# to assign variables from list element

var1, var2, var3 = [test_list[i] for i in (1, 3, 5)]

 

# printing result

print ("The variables are : " + str(var1) +

 " " + str(var2) +

 " " + str(var3))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 4, 5, 6, 7, 3]
    The variables are : 4 6 3
    

  
**Method #2 : Usingitemgetter()**  
itemgetter function can also be used to perform this particular task. This
function accepts the index values and the container it is working on and
assigns to the variables.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to assign variables from list element

# using itemgetter()

from operator import itemgetter

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 3]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using using itemgetter()

# to assign variables from list element

var1, var2, var3 = itemgetter(1, 3, 5)(test_list)

 

# printing result

print ("The variables are : " + str(var1) +

 " " + str(var2) +

 " " + str(var3))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : [1, 4, 5, 6, 7, 3]
    The variables are : 4 6 3
    

