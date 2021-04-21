Python | Add leading Zeros to string



Sometimes, during the string manipulation, we are into a problem where we need
to pad or add leading zeroes to the string as per the requirements. This
problem can occur in web development. Having shorthands to solve this problem
turns to be handy in many situations. Let’s discuss certain ways in which this
problem can be solved.

 **Method #1 : Usingrjust()**

 **rjust** function offers a single line way to perform this particular
task. Hence can easily be employed to any string whose padding we need to be
done. We can specify the amount of padding required.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# adding leading zeros

# using rjust()

 

# initializing string 

test_string = 'GFG'

 

# printing original string 

print("The original string : " + str(test_string))

 

# No. of zeros required

N = 4

 

# using rjust()

# adding leading zero

res = test_string.rjust(N + len(test_string), '0')

 

# print result

print("The string after adding leading zeros : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GFG
    The string after adding leading zeros : 0000GFG
    

  

  

**Method #2 : Usingzfill()**

This is yet another way to perform this particular task, in this function we
don’t need to specify the letter that we need to pad, this function is
exclusively made to pad zeros internally and hence recommended.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# adding leading zeros

# using zfill()

 

# initializing string 

test_string = 'GFG'

 

# printing original string 

print("The original string : " + str(test_string))

 

# No. of zeros required

N = 4

 

# using zfill()

# adding leading zero

res = test_string.zfill(N + len(test_string))

 

# print result

print("The string after adding leading zeros : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GFG
    The string after adding leading zeros : 0000GFG
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

