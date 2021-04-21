Python | Convert location coordinates to tuple



Sometimes, while working with locations, we need a lot of data which has
location points in form of latitutes and longitudes. These can be in form of a
string and we desire to get tuple versions of same. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usingtuple() + float() + split() + map()**

The combination of above functions can be used to perform this task. In this,
we first split the two parts of coordinates into a list, apply float function
to each of them using float() and map() and lastly it is converted to
tuple using tuple().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert location coordinates to tuple

# Using tuple() + float() + split() + map()

 

# Initializing string

test_str = "44.6463, -49.583"

 

# printing original string

print("The original string is : " + str(test_str))

 

# Convert location coordinates to tuple

# Using tuple() + float() + split() + map()

res = tuple(map(float, test_str.split(', ')))

 

# printing result

print("The coordinates after conversion to tuple are : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 44.6463, -49.583
    The coordinates after conversion to tuple are : (44.6463, -49.583)
    

  

  

**Method #2 : Usingeval()**  
This is the one-liner and recommended method to perform this particular task.
In this, the eval(), internally detects the string and converts to floating
point number seperated as tuple elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert location coordinates to tuple

# Using eval()

 

# Initializing string

test_str = "44.6463, -49.583"

 

# printing original string

print("The original string is : " + str(test_str))

 

# Convert location coordinates to tuple

# Using eval()

res = eval(test_str)

 

# printing result

print("The coordinates after conversion to tuple are : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 44.6463, -49.583
    The coordinates after conversion to tuple are : (44.6463, -49.583)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

