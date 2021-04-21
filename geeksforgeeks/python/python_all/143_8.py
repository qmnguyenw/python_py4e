Python | Check for ASCII string



Many times it is desirable to work with the strings that only contain
alphabets and the other special characters are undesirable and sometimes this
very task becomes the point to filter the strings and hence requires the way
to check if a string is whole ASCII. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Usingord() + all()**  
The combination of this method can be used to achieve the desirable task. In
this method, we search for all the string and check for each character, a
value in range of ASCII characters.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Check for ASCII string

# using all() + ord()

 

# initializing string 

test_string = "G4G is best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using all() + ord()

# Check for ASCII string

res = all(ord(c) < 128 for c in test_string)

 

# print result

print("Is the string full ASCII ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : G4G is best
    Is the string full ASCII ? : True
    

**Method #2 : Usinglambda + encode()**  
This task can also be achieved using the above functions. In this combination,
lambda function is used to extend the size check logic to whole string and
encode function checks if the size of original and encoded strings match.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Check for ASCII string

# using lambda + encode()

 

# initializing string 

test_string = "G4G is best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# using lambda + encode()

# Check for ASCII string

res = lambda ele: len(ele) == len(ele.encode())

 

# print result

print("Is the string full ASCII ? : " + str(res(test_string)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : G4G is best
    Is the string full ASCII ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

