Python | Find Min/Max in heterogeneous list



The lists in Python can handle different type of datatypes in it. The
manipulation of such lists is complicated. Let’s say we have a problem in
which we need to find the min/max integer value in which the list can contain
string as a data type i.e heterogenous. Let’s discuss certain ways in which
this can be performed.

 **Method #1 : Using list comprehension +min()/max() + isinstance()**  
This particular problem can be solved by filtering our search of min/max using
the isinstance method, we can filter out the integer value and then can use
min/max function to get required min/max value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Min / Max in heterogenous list

# using list comprehension + min()/max() + isinstance()

 

# initializing list

test_list = [3, 'computer', 5, 'geeks', 6, 7]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list comprehension + min()/max() + isinstance()

# Min / Max in heterogenous list

res = min(i for i in test_list if isinstance(i,
int))

 

# printing result

print ("The minimum value in list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 'computer', 5, 'geeks', 6, 7]
    The minimum value in list is : 3
    

**Method #2 : Usinglambda + key + max()/min() + isinstance()**  
The above problem can also be solved using the lambda function as a key in the
min()/max() along with the isinstance method which performs the task of
checking for integer values.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Min / Max in heterogenous list

# using lambda + key + max()/min() + isinstance()

 

# initializing list

test_list = [3, 'computer', 5, 'geeks', 6, 7]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using lambda + key + max()/min() + isinstance()

# Min / Max in heterogenous list

res = max(test_list, key = lambda i: (isinstance(i, int),
i))

 

# printing result

print ("The maximum value in list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [3, 'computer', 5, 'geeks', 6, 7]
    The maximum value in list is : 7
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

