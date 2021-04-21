Python | List of tuples to String



Many times we can have a problem in which we need to perform interconversion
between strings and in those cases, we can have a problem in which we need to
convert a tuple list to raw, comma separated string. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingstr() + strip()**  
The combination of above functions can be used to solve this problem. In this,
we just convert a list into string and strip the opening, closing square
brackets of list to present a string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List of tuples to String

# using str() + strip()

 

# initialize list

test_list = [(1, 4), (5, 6), (8, 9), (3,
6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# List of tuples to String

# using str() + strip()

res = str(test_list).strip('[]')

 

# printing result

print("Resultant string from list of tuple : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 4), (5, 6), (8, 9), (3, 6)]
    Resultant string from list of tuple : (1, 4), (5, 6), (8, 9), (3, 6)
    

**Method #2 : Usingmap() + join()**  
This is yet another way in which this task can be performed. In this, we apply
the string conversion function to each element and then join the tuples using
join().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List of tuples to String

# using map() + join()

 

# initialize list

test_list = [(1, 4), (5, 6), (8, 9), (3,
6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# List of tuples to String

# using map() + join()

res = ", ".join(map(str, test_list))

 

# printing result

print("Resultant string from list of tuple : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(1, 4), (5, 6), (8, 9), (3, 6)]
    Resultant string from list of tuple : (1, 4), (5, 6), (8, 9), (3, 6)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

