Python | Check if substring is part of List of Strings



Many problems of substrings have been dealt with many times. There can also be
such problem in which we require to check if argument string is a part of any
of the strings coming in the input list of strings. Let’s discuss various ways
in which this can be performed.

 **Method #1 : Usingjoin()**  
The basic approach that can be employed to perform this particular task is
computing the join of all the list strings and then searching the string in
the joined string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if substring is part of List of Strings

# Using join()

 

# initializing list 

test_list = ['GeeksforGeeks', 'is', 'Best']

 

# test string 

check_str = "for"

 

# printing original string 

print("The original string is : " + str(test_list))

 

# Using join()

# Check if substring is part of List of Strings

temp = '\t'.join(test_list)

res = check_str in temp

 

# printing result 

print("Is check string part of any input list string : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : ['GeeksforGeeks', 'is', 'Best']
    Is check string part of any input list string : True
    

**Method #2 : Usingany()**  
The any function can be used to compute the presence of the test substring in
all the strings of the list and return True if it’s found in any. This is
better than above function as it doesn’t explicitly take space to create new
concatenated string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if substring is part of List of Strings

# Using any()

 

# initializing list 

test_list = ['GeeksforGeeks', 'is', 'Best']

 

# test string 

check_str = "for"

 

# printing original string 

print("The original string is : " + str(test_list))

 

# Using any()

# Check if substring is part of List of Strings

res = any(check_str in sub for sub in test_list)

 

# printing result 

print("Is check string part of any input list string : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : ['GeeksforGeeks', 'is', 'Best']
    Is check string part of any input list string : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

