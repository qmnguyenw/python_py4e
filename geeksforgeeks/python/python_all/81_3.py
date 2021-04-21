Python | Convert Joint Float string to Numbers



Sometimes, while working with Legacy languages, we can have certain problems.
One such can be working with FORTRAN which can give text output (without
spaces, which are required) '12.4567.23' . In this, there are actually two
floating point separate numbers but concatenated. We can have problem in which
we need to separate them. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usnig loop +float()**  
This is brute force method in which this task can be performed. In this, we
iterate for each element and break in chunks of 4 and skip to every 5th
element and perform split and store in list. The converstion from string to
float is done using float().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Joint Float string to Numbers

# Using loop + float()

 

# initializing string

test_str = "45.6778.4524.45"

 

# printing original string

print("The original string is : " + test_str)

 

# Convert Joint Float string to Numbers

# Using loop + float()

res = []

for idx in range(0, len(test_str), 5):

 res.append(float(test_str[idx : idx + 5]))

 

# printing result 

print("The float list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : 45.6778.4524.45
    The float list is : [45.67, 78.45, 24.45]
    

**Method #2 : Using list comprehension +float()**  
This is shorthand way to solve this problem. This is similar to above
function. The difference is that we perform all loop task in single line using
list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Joint Float string to Numbers

# Using list comprehension + float()

 

# initializing string

test_str = "45.6778.4524.45"

 

# printing original string

print("The original string is : " + test_str)

 

# Convert Joint Float string to Numbers

# Using list comprehension + float()

res = [float(test_str[idx : idx + 5]) for idx in
range(0, len(test_str), 5)]

 

# printing result 

print("The float list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : 45.6778.4524.45
    The float list is : [45.67, 78.45, 24.45]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

