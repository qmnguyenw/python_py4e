Python – Concatenate consecutive elements in Tuple



Sometimes, while working with data, we can have a problem in which we need to
find cumulative result. This can be of any type, product or summation. Here we
are gonna discuss about adjacent element concatenation. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingzip() + generator expression + tuple()**  
The combination of above functionalities can be used to perform this task. In
this, we use generator expression to provide concatenation logic and
simultaneous element pairing is done by zip(). The result is converted to
tuple form using tuple().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive element concatenation in Tuple

# using zip() + generator expression + tuple

 

# initialize tuple

test_tup = ("GFG ", "IS ", "BEST ", "FOR ", "ALL ",
"GEEKS")

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Consecutive element concatenation in Tuple

# using zip() + generator expression + tuple

res = tuple(i + j for i, j in zip(test_tup,
test_tup[1:]))

 

# printing result

print("Resultant tuple after consecutive concatenation : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : ('GFG ', 'IS ', 'BEST ', 'FOR ', 'ALL ', 'GEEKS')
    Resultant tuple after consecutive concatenation : ('GFG IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL GEEKS')
    

**Method #2 : Usingtuple() + map() \+ lambda**  
The combination of above functions can also help to perform this task. In
this, we perform concatenation and binding logic using lambda function. The
map() is used to iterate to each element and at end result is converted by
tuple().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive element concatenation in Tuple

# using tuple() + map() + lambda

 

# initialize tuple

test_tup = ("GFG ", "IS ", "BEST ", "FOR ", "ALL ",
"GEEKS")

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Consecutive element concatenation in Tuple

# using tuple() + map() + lambda

res = tuple(map(lambda i, j : i + j, test_tup[: -1],
test_tup[1: ]))

 

# printing result

print("Resultant tuple after consecutive concatenation : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : ('GFG ', 'IS ', 'BEST ', 'FOR ', 'ALL ', 'GEEKS')
    Resultant tuple after consecutive concatenation : ('GFG IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL GEEKS')
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

