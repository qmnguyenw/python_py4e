Python | Get first element with maximum value in list of tuples



In Python, we can bind structural information in form of tuples and then can
retrieve the same. But sometimes we require the information of tuple
corresponding to maximum value of other tuple indexes. This functionality has
many applications such as ranking. Let’s discuss certain ways in which this
can be achieved.

 **Method #1 : Usingmax() + operator.itemgetter()**  
We can get the maximum of corresponding tuple index from a list using the key
itemgetter index provided and then mention the index information required
using index specification at the end.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to get tuple info. of maximum value tuple

# using max() + itemgetter()

from operator import itemgetter

 

# initializing list 

test_list = [('Rash', 143), ('Manjeet', 200),
('Varsha', 100)]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using max() + itemgetter()

# to get tuple info. of maximum value tuple

res = max(test_list, key = itemgetter(1))[0]

 

# printing result

print ("The name with maximum score is : " + res)  
  
---  
  
 __

 __

 **Output:**

    
    
    Original list : [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]
    The name with maximum score is : Manjeet
    

  
**Method #2 : Using max() + lambda**  
This method is almost similar to the method discussed above, just the
difference is the specification and processing of target tuple index for
maximum is done by lambda function. This improved readability of code.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to get tuple info. of maximum value tuple

# using max() + lambda

 

# initializing list 

test_list = [('Rash', 143), ('Manjeet', 200),
('Varsha', 100)]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using max() + lambda

# to get tuple info. of maximum value tuple

res = max(test_list, key = lambda i : i[1])[0]

 

# printing result

print ("The name with maximum score is : " + res)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Original list : [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]
    The name with maximum score is : Manjeet
    

