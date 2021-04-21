Python | Insert a number in string



Sometimes, while dealing with strings, we may encounter a problem in which we
might have a numeric variable whose value keeps changing and we need to print
the string including that number. Strings and numbers being different data
types have to be solved in different ways. Let’s discuss certain ways in which
this problem can be solved.

 **Method #1 : Using Type conversion**  
The simplest way in which this task can be performed is by converting the
integer explicitly into string datatype using the basic type conversion and
adding it to appropriate position.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Inserting a number in string 

# Using type conversion

 

# initializing string 

test_str = "Geeks"

 

# initializing number

test_int = 4

 

# printing original string 

print("The original string is : " + test_str)

 

# printing number

print("The original number : " + str(test_int))

 

# using type conversion

# Inserting number in string 

res = test_str + str(test_int) + test_str

 

# printing result 

print("The string after adding number is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks
    The original number : 4
    The string after adding number is  : Geeks4Geeks
    

**Method #2 : Using%d operator**  
This operator can be used to format the string to add the integer. The “d”
represents that the datatype to be inserted to string is an integer. This can
be changed according to the requirements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Inserting a number in string 

# Using % d operator

 

# initializing string 

test_str = "Geeks"

 

# initializing number

test_int = 4

 

# printing original string 

print("The original string is : " + test_str)

 

# printing number

print("The original number : " + str(test_int))

 

# using % d operator

# Inserting number in string 

res = (test_str + "% d" + test_str) % test_int

 

# printing result 

print("The string after adding number is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks
    The original number : 4
    The string after adding number is  : Geeks4Geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

