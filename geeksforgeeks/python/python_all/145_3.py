Python program to find occurrence to each character in given string



Given a string, the task is to write a program in Python which prints the
number of occurrences of each character in a string.

There are multiple ways in Python, we can do this task. Let’s discuss a few of
them.

 **Method #1:** Using set() \+ count()

Iterate over the set converted string and get the count of each character in
original string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to program to find occurrence

# to each character in given string

 

# initializing string 

inp_str = "GeeksforGeeks"

 

# using set() + count() to get count 

# of each element in string 

out = {x : inp_str.count(x) for x in set(inp_str )} 

 

# printing result 

print ("Occurrence of all characters in GeeksforGeeks is :\n "+
str(out))   
  
---  
  
__

__

**Output:**

  

  

    
    
    Occurrence of all characters in GeeksforGeeks is :
     {'o': 1, 'r': 1, 'e': 4, 's': 2, 'f': 1, 'G': 2, 'k': 2}
    

