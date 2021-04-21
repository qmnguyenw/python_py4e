Python | Convert String to bytes



Inter conversions are as usual quite popular, but conversion between a string
to bytes is more common these days due to the fact that for handling files or
Machine Learning ( Pickle File ), we extensively require the strings to be
converted to bytes. Let’s discuss certain ways in which this can be performed.

 **Method #1 : Usingbytes(str, enc)**

String can be converted to bytes using the generic bytes function. This
function internally points to CPython Library which implicitly calls the
encode function for converting the string to specified encoding.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# convert string to byte 

# Using bytes(str, enc)

 

# initializing string 

test_string = "GFG is best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# Using bytes(str, enc)

# convert string to byte 

res = bytes(test_string, 'utf-8')

 

# print result

print("The byte converted string is : " + str(res) + ", type :
" + str(type(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GFG is best
    The byte converted string is  : b'GFG is best', type : <class 'bytes'>
    

  

  

**Method #2 : Usingencode(enc)**

The most recommended method to perform this particular task, using the encode
function to get the conversion done, as it reduces one extra linking to a
particular library, this function directly calls it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# convert string to byte 

# Using encode(enc)

 

# initializing string 

test_string = "GFG is best"

 

# printing original string 

print("The original string : " + str(test_string))

 

# Using encode(enc)

# convert string to byte 

res = test_string.encode('utf-8')

 

# print result

print("The byte converted string is : " + str(res) + ", type :
" + str(type(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GFG is best
    The byte converted string is  : b'GFG is best', type : <class 'bytes'>
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

