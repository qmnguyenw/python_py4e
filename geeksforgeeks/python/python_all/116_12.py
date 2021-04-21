Python | Convert String to tuple list



Sometimes, while working with Python strings, we can have a problem in which
we receive a tuple, list in the comma-separated string format, and have to
convert to the tuple list. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Using loop +split() + replace()**  
This is a brute force method to perform this task. In this, we perform the
task of extracting and remaking the tuples to list in a loop using split() and
replace() functionalities.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to tuple list

# using loop + replace() + split()

 

# initializing string 

test_str = "(1, 3, 4), (5, 6, 4), (1, 3, 6)"

 

# printing original string 

print("The original string is : " + test_str)

 

# Convert String to tuple list

# using loop + replace() + split()

res = []

temp = []

for token in test_str.split(", "):

 num = int(token.replace("(", "").replace(")", ""))

 temp.append(num)

 if ")" in token:

 res.append(tuple(temp))

 temp = []

 

# printing result

print("List after conversion from string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : (1, 3, 4), (5, 6, 4), (1, 3, 6)
    List after conversion from string : [(1, 3, 4), (5, 6, 4), (1, 3, 6)]
    

**Method #2: Usingeval()**  
This inbuilt function can also be used to perform this task. This function
internally evaluates the string and returns the converted list of tuples as
desired.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to tuple list

# using eval()

 

# initializing string 

test_str = "(1, 3, 4), (5, 6, 4), (1, 3, 6)"

 

# printing original string 

print("The original string is : " + test_str)

 

# Convert String to tuple list

# using eval()

res = list(eval(test_str))

 

# printing result

print("List after conversion from string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : (1, 3, 4), (5, 6, 4), (1, 3, 6)
    List after conversion from string : [(1, 3, 4), (5, 6, 4), (1, 3, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

