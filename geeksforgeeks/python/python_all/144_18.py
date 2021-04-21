Python | Add trailing Zeros to string



Sometimes, we wish to manipulate a string in such a way in which we might need
to add additional zeros at the end of string; in case of filling the missing
bits or any other specific requirement. The solution to this kind of problems
is always handy and is good if one has knowledge of it. Let’s discuss certain
ways in which this can be solved.

 **Method #1 : Usingljust()**

This task can be performed using the simple inbuilt string function of _ljust_
in which we just need to pass no. of zeros required and the element to right
pad, in this case being zero.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# adding trailing zeros

# using ljust()

 

# initializing string 

test_string = 'GFG'

 

# printing original string 

print("The original string : " + str(test_string))

 

# No. of zeros required

N = 4

 

# using ljust()

# adding trailing zero

res = test_string.ljust(N + len(test_string), '0')

 

# print result

print("The string after adding trailing zeros : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GFG
    The string after adding trailing zeros : GFG0000
    

  

  

**Method #2 : Usingformat()**

String formatting using the format function can be used to perform this task
easily, we just mention the number of elements total, element needed to pad,
and direction of padding, in this case right.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# adding trailing zeros

# using format()

 

# initializing string 

test_string = 'GFG'

 

# printing original string 

print("The original string : " + str(test_string))

 

# No. of zeros required

N = 4

 

# using format()

# adding trailing zero

# N for number of elememts, '0' for Zero, and '<' for trailing

temp = '{:<07}'

res = temp.format(test_string)

 

# print result

print("The string after adding trailing zeros : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GFG
    The string after adding trailing zeros : GFG0000
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

