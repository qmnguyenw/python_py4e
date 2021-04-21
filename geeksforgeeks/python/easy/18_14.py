Ways to remove i’th character from string in Python



In Python it is all known that string is immutable and hence sometimes poses
visible restrictions while coding the constructs that are required in day-day
programming. This article presents one such problem of removing i’th character
from string and talks about possible solutions that can be employed in
achieving them.

 **Method 1 : Naive Method**

In this method, one just has to run a loop and append the characters as they
come and build a new string from the existing one except when the index is i.

 **Code #1 :** Demonstrating Naive method to remove i’th char from string.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# method to remove i'th character

# Naive Method

 

# Initializing String 

test_str = "GeeksForGeeks"

 

# Printing original string 

print ("The original string is : " + test_str)

 

# Removing char at pos 3

# using loop

new_str = ""

 

for i in range(len(test_str)):

 if i != 2:

 new_str = new_str + test_str[i]

 

# Printing string after removal 

print ("The string after removal of i'th character : " + new_str)  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : GeeksForGeeks
    The string after removal of i'th character : GeksForGeeks
    

**Note:** This solution is much slower (has O(n^2) time complexity) than the
other methods. If speed is needed, method #3 is similar in logic and is faster
(it has O(n) time complexity).  

  

  

 **Method 2 : Usingstr.replace()**

