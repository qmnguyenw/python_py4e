Mathematical Functions in Python | Set 3 (Trigonometric and Angular Functions)



Some of the mathematical functions are discussed in below set 1 and set 2

Mathematical Functions in Python | Set 1 (Numeric Functions)  
Mathematical Functions in Python | Set 2 (Logarithmic and Power Functions)

Trigonometric and angular functions are discussed in this article.

 **1\. sin()** :- This function returns the **sine** of value passed as
argument. The value passed in this function should be in **radians**.

 **2\. cos()** :- This function returns the **cosine** of value passed as
argument. The value passed in this function should be in **radians**.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# sin() and cos()

 

# importing "math" for mathematical operations

import math

 

a = math.pi/6

 

# returning the value of sine of pi/6

print ("The value of sine of pi/6 is : ", end="")

print (math.sin(a))

 

# returning the value of cosine of pi/6

print ("The value of cosine of pi/6 is : ", end="")

print (math.cos(a))  
  
---  
  
 __

 __

Output:

    
    
    The value of sine of pi/6 is : 0.49999999999999994
    The value of cosine of pi/6 is : 0.8660254037844387
    

**3\. tan()** :- This function returns the **tangent** of value passed as
argument. The value passed in this function should be in **radians**.

 **4\. hypot(a, b)** :- This returns the **hypotenuse** of the values passed
in arguments. Numerically, it returns the value of **sqrt(a*a + b*b)**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# tan() and hypot()

 

# importing "math" for mathematical operations

import math

 

a = math.pi/6

b = 3

c = 4

 

# returning the value of tangent of pi/6

print ("The value of tangent of pi/6 is : ", end="")

print (math.tan(a))

 

# returning the value of hypotenuse of 3 and 4

print ("The value of hypotenuse of 3 and 4 is : ", end="")

print (math.hypot(b,c))  
  
---  
  
 __

 __

Output:

    
    
    The value of tangent of pi/6 is : 0.5773502691896257
    The value of hypotenuse of 3 and 4 is : 5.0
    

**5\. degrees()** :- This function is used to **convert argument value from
radians to degrees**.

 **6\. radians()** :- This function is used to **convert argument value from
degrees to radians**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# degrees() and radians()

 

# importing "math" for mathematical operations

import math

 

a = math.pi/6

b = 30

 

# returning the converted value from radians to degrees

print ("The converted value from radians to degrees is : ",
end="")

print (math.degrees(a))

 

# returning the converted value from degrees to radians

print ("The converted value from degrees to radians is : ",
end="")

print (math.radians(b))  
  
---  
  
 __

 __

Output:

    
    
    The converted value from radians to degrees is : 29.999999999999996
    The converted value from degrees to radians is : 0.5235987755982988
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

