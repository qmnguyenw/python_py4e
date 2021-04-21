Python | Add leading K character



Sometimes, during the string manipulation, we are into a problem where we need
to pad or add leading K to the string as per the requirements. This problem
can occur in web development. Having shorthands to solve this problem turns to
be handy in many situations. Let’s discuss certain ways in which this problem
can be solved.

 **Method #1 : Usingrjust()**  
rjust function offers a single line way to perform this particular task. Hence
can easily be employed to any string whose padding we need to be done. We can
specify the amount of padding required.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Add leading K character

# using rjust() 

 

# initializing string 

test_string = 'GFG'

 

# printing original string 

print("The original string : " + str(test_string)) 

 

# No. of zeros required 

N = 4

 

# initializing K 

K = 'M'

 

# using rjust() 

# Add leading K character

res = test_string.rjust(N + len(test_string), K) 

 

# print result 

print("The string after adding leading K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string : GFG
    The string after adding leading K : MMMMGFG
    

**Method #2 : Usingformat()**  
String formatting using the format function can be used to perform this task
easily, we just mention the number of elements total, element needed to pad,
and direction of padding, in this case left.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Add leading K character

# using format() 

 

# initializing string 

test_string = 'GFG'

 

# printing original string 

print("The original string : " + str(test_string)) 

 

# No. of zeros required 

N = 4

 

# initializing K 

K = '0'

 

# using format() 

# Add leading K character 

# N for number of elememts and '>' for leading 

temp = '{:>' + K + '7}'

res = temp.format(test_string) 

 

# print result 

print("The string after adding leading K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string : GFG
    The string after adding leading K : 0000GFG
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

