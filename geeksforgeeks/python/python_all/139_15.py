Python | Convert String to Binary



Data conversion have always been widely used utility and one among them can be
conversion of a string to it’s binary equivalent. Let’s discuss certain ways
in which this can be done.

 **Method #1 : Usingjoin() + ord() + format()**  
The combination of above functions can be used to perform this particular
task. The ord function converts the character to it’s ASCII equivalent, format
converts this to binary number and join is used to join each converted
character to form a string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Converting String to binary

# Using join() + ord() + format()

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# using join() + ord() + format()

# Converting String to binary

res = ''.join(format(ord(i), '08b') for i in test_str)

 

# printing result 

print("The string after binary conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The string after binary conversion : 01000111011001010110010101101011011100110110011001101111011100100100011101100101011001010110101101110011

**Method #2 : Usingjoin() + bytearray() + format()**  
This method is almost similar to the above function. The difference here is
that rather than converting the character to it’s ASCII using ord function,
the conversion at once of string is done by bytearray function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Converting String to binary

# Using join() + bytearray() + format()

 

# initializing string 

test_str = "GeeksforGeeks"

 

# printing original string 

print("The original string is : " + str(test_str))

 

# using join() + bytearray() + format()

# Converting String to binary

res = ''.join(format(i, '08b') for i in bytearray(test_str,
encoding ='utf-8'))

 

# printing result 

print("The string after binary conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : GeeksforGeeks
    The string after binary conversion : 01000111011001010110010101101011011100110110011001101111011100100100011101100101011001010110101101110011
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

