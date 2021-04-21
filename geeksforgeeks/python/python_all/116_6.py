Convert String float to float list in Python



Sometimes, while working with data, we could be dealing with numbers, that are
in decimal and not integers. This is general case in data science domain.
Let’s discuss how to resolve a problem in which we may have a comma separated
float numbers and we need to convert to float list.

 **Method #1 : Using list comprehension +split() + float()**  
The combination of above methods can be used to perform this task. In this, we
convert the String to string list using split and then convert the string to
float using float().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String float to float list

# using list comprehension + split() + float()

 

# initializing string 

test_str = "3.44, 7.8, 9.12, 100.2, 6.50"

 

# printing original string 

print("The original string is : " + test_str)

 

# Convert String float to float list

# using list comprehension + split() + float()

res = [float(idx) for idx in test_str.split(', ')]

 

# printing result

print("The float list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 3.44, 7.8, 9.12, 100.2, 6.50
    The float list is : [3.44, 7.8, 9.12, 100.2, 6.5]
    

**Method #2 : Usingmap() + split() + float()**  
The combination of above functions can also be used to solve this problem. In
this, we perform the task of extending logic to entire list usin map(), rest
all the functionalities are performed as above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String float to float list

# using map() + split() + float()

 

# initializing string 

test_str = "3.44, 7.8, 9.12, 100.2, 6.50"

 

# printing original string 

print("The original string is : " + test_str)

 

# Convert String float to float list

# using map() + split() + float()

res = list(map(float, test_str.split(', ')))

 

# printing result

print("The float list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 3.44, 7.8, 9.12, 100.2, 6.50
    The float list is : [3.44, 7.8, 9.12, 100.2, 6.5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

