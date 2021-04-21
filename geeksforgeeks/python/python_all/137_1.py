Python | Convert Stream of numbers to list



Sometimes, we can be stuck with a problem in which we are given a stream of
space separated numbers with a goal to convert them into a list of numbers.
This type of problem can occur in common day-day programming or competitive
programming while taking inputs. Let’s discuss certain ways in which this
problem can be solved.

 **Method #1 : Usinglist() + split()**  
The space separated numbers can be converted to list by using a simple split
function that would convert the string to list of numbers and hence solve our
problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Stream of numbers to list

# Using list() + split()

 

# initializing string 

test_str = "10 12 3 54 6 777 443"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using list() + split()

# Convert Stream of numbers to list

res = list(test_str.split())

 

# printing result 

print("The list of stream of numbers : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 10 12 3 54 6 777 443
    The list of stream of numbers : ['10', '12', '3', '54', '6', '777', '443']
    

**Method #2 : Usingmap() + split() + list()**  
Since the drawback of above method is that the conversion doesn’t change the
datatype of the unit numbers, so if it’s desired to change the data type of
number as well, it is suggested to additionally use map() to have list of
strings as integers.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Stream of numbers to list

# Using map() + split() + list()

 

# initializing string 

test_str = "10 12 3 54 6 777 443"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using map() + split() + list()

# Convert Stream of numbers to list

res = list(map(int, test_str.split()))

 

# printing result 

print("The list of stream of numbers : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : 10 12 3 54 6 777 443
    The list of stream of numbers : [10, 12, 3, 54, 6, 777, 443]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

