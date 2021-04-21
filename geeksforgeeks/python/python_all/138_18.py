Python | Ways to check string contain all same characters



Given a list of strings, write a Python program to check whether each string
has all the characters same or not. Given below are a few methods to check the
same.

 **Method #1: Using Naive Method** [Inefficient]

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to check whether string contains

# all characters same or not

 

# Initialising string list

ini_list = ["aaaaaaaaaaa", "aaaaaaabaa"]

 

# Printing initial string

print ("Initial Strings list", ini_list)

 

# Using Naive Method:

flag = True

for i in ini_list:

 for j in range(0, len(i)-1):

 if i[j]!= i[j + 1]:

 print ("String {} don't have all characters same".format(i))

 flag = False

 break

 if flag == True:

 print ("String {} don't have all characters same".format(i))

   
  
---  
  
__

__

**Output:**

    
    
    Initial Strings list ['aaaaaaaaaaa', 'aaaaaaabaa']
    String aaaaaaaaaaa don't have all characters same
    String aaaaaaabaa don't have all characters same
    

  
**Method #2: Using String Comparisons**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to check whether string contains

# all characters same or not

 

# Initialising string list

ini_list = ["aaaaaaaaaaa", "aaaaaaabaa"]

 

# Printing initial string

print ("Initial Strings list", ini_list)

 

# Using String comparison

for i in ini_list:

 if i == len(i)*i[0]:

 print ("String {} have all characters same".format(i))

 else:

 print ("String {} don't have all characters same".format(i))

   
  
---  
  
__

__

**Output:**

  

  

    
    
    Initial Strings list ['aaaaaaaaaaa', 'aaaaaaabaa']
    String aaaaaaaaaaa have all characters same
    String aaaaaaabaa don't have all characters same
    

