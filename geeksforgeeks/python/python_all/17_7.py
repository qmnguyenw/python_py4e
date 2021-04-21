Python Program that Displays Letters that are not common in two strings



Given two strings. write a Python program is to find which letters are in the
two strings but not in both.

 **Example** :

    
    
     **Input:**
    india
    australia
    
    **Output:**
    s
    t
    r
    n
    d
    u
    l
    

**Steps to be performed:**

  * Take two string input and store them in different variables.
  * Convert them into set and look for letters inside in two strings but not in both.
  * Store those letters in different list.
  * Print that list.

 **Below is the implementation.**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# taking string inputs

string_1 = "hi"

string_2 = "virat"

 

# letters which are present in the two strings

# but not in both are found using the ‘^’ operator

e = list(set(string_1) ^ set(string_2))

 

# printing finale list

print("The letters are:")

for i in e:

 print(i)  
  
---  
  
 __

 __

