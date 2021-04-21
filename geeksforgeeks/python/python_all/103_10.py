Python – String concatenation in Heterogenous list



Sometimes, while working with Python, we can come across a problem in which we
require to find the concatenation of strings. This problem is easier to solve.
But this can get complex in case we have mixture of data types to go along
with it. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop + conditions**  
We can employ a brute force method to type caste check each element, if its a
string we concatenate it. This can ensure that only strings are concatenated
and hence can solve the problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String concatenation in Heterogenous list

# using loop + conditions

 

# initializing list

test_list = [5, 6, "gfg ", 8, (5, 7), ' is',
9, ' best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# String concatenation in Heterogenous list

# using loop + conditions

res = ''

for ele in test_list:

 if type(ele) == str:

 res += ele 

 

# printing result 

print("Concatenation of strings in list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 'gfg ', 8, (5, 7), ' is', 9, ' best']
    Concatenation of strings in list : gfg  is best
    

**Method #2 : Using join() + isinstance()**  
This problem can also be solved using the inbuilt function of join() and it
also supports the instance filter using isinstance() which can be feeded with
strings and hence solve the problem.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String concatenation in Heterogenous list

# using join() + isinstance()

 

# initializing list

test_list = [5, 6, "gfg ", 8, (5, 7), ' is',
9, ' best']

 

# printing original list

print("The original list is : " + str(test_list))

 

# String concatenation in Heterogenous list

# using join() + isinstance()

res = "".join(filter(lambda i: isinstance(i, str),
test_list))

 

# printing result 

print("Concatenation of strings in list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 'gfg ', 8, (5, 7), ' is', 9, ' best']
    Concatenation of strings in list : gfg  is best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

