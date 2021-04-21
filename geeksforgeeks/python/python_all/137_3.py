Python | Insert character after every character pair



Sometimes, we can have a problem in which we need to insert a specific
character after pair(second) character. This kind of problem can occur while
working with data, that require insertion of commas or any other special
character mainly in Machine Learning domain. Let’s discuss certain ways in
which this problem can be solved.

 **Method #1 : Usingjoin() \+ list comprehension**  
The combination of above method can be used to perform this particular task.
List comprehension along with slicing can be used to convert string to list
and join function can be used to rejoin them inserting required character
between them.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Insert character after every character pair

# Using join() + list comprehension

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using join() + list comprehension

# Insert character after every character pair

res = ', '.join(test_str[i:i + 2] for i in range(0,
len(test_str), 2))

 

# printing result 

print("The string after inserting comma after every character pair : "
+ res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The string after inserting comma after every character pair : Ge, ek, sf, or, Ge, ek, s
    

**Method #2 : Usingzip() + join()**  
The combination of above functions can be used to perform this particular
task. In this, zip function converts the characters to iterable tuples, split
function is used to separate odd and even characters. Then list comprehension
is responsible to convert the tuples to list of strings and at last result is
joined using the join function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Insert character after every character pair

# Using zip() + join()

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using zip() + join()

# Insert character after every character pair

res = ', '.join(a + b for a, b in zip(test_str[::2],
test_str[1::2]))

 

# printing result 

print("The string after inserting comma after every character pair : "
+ res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The string after inserting comma after every character pair : Ge, ek, sf, or, Ge, ek
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

