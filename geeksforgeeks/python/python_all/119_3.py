Python | Convert String to N chunks tuple



Sometimes, while working with Python Strings, we can have a problem in which
we need to break a string to N sized chunks to a tuple. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using list comprehension + tuple**  
This is one approach in which this task can be performed. In this, we just
iterate the String and break the chunks of string and construct the tuple
using tuple() in one liner.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to N chunks tuple

# Using list comprehension + tuple()

 

# initialize string

test_string = "ggggffffgggg"

 

# printing original string

print("The original string : " + str(test_string))

 

# initialize N 

N = 4

 

# Convert String to N chunks tuple

# Using list comprehension + tuple()

res = tuple(test_string[ i : i + N] for i in range(0,
len(test_string), N))

 

# printing result

print("Chunked String into tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : ggggffffgggg
    Chunked String into tuple : ('gggg', 'ffff', 'gggg')
    

**Method #2 : Usingzip() + iter() + join() \+ list comprehension**  
The combination of above functions can also be used to perform this task. In
this, we perform the act of making chunks using zip() + iter(). And cummulate
the result using join().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to N chunks tuple

# Using zip() + iter() + join()+ list comprehension

 

# initialize string

test_string = "ggggffffgggg"

 

# printing original string

print("The original string : " + str(test_string))

 

# initialize N 

N = 4

 

# Convert String to N chunks tuple

# Using zip() + iter() + join() + list comprehension

res = tuple([''.join(ele) for ele in
zip(*[iter(test_string)] * N)])

 

# printing result

print("Chunked String into tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : ggggffffgggg
    Chunked String into tuple : ('gggg', 'ffff', 'gggg')
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

