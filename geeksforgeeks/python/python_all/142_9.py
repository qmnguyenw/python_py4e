Python | Get the starting index for all occurrences of given substring



Given a string and a substring, the task to find out the starting index for
all the occurrences of a given substring in a string. Let’s discuss a few
methods to solve the given task.

 **Method #1: Using Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to find all occurrences of substring in

# a string

 

# Initialising string

ini_string = 'xbzefdgstbzefzexezef'

 

# Initialising sub-string

sub_string = 'zef'

 

# Printing initial string and sub-string

print ("initial_strings : ", ini_string, "\nsubstring : ",
sub_string)

 

res = []

flag = 0

k = 0

 

# Finding all occurrences of substring

# in a string using Naive method

for i in range(0, len(ini_string)):

 k = i

 flag = 0

 for j in range(0, len(sub_string)):

 if ini_string[k] != sub_string[j]:

 flag = 1

 if flag:

 break

 k = k + 1

 if flag == 0:

 res.append(i)

 

 

# printing result(

print ("resultant positions", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial_strings :  xbzefdgstbzefzexezef 
    substring :  zef
    resultant positions [2, 10, 17]
    

&nsbp;  
 **Method #2: Using list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to find all occurrences of substring in

# a string

 

# Initialising string

ini_string = 'xbzefdgstbzefzexezef'

 

# Initialising sub-string

sub_string = 'zef'

 

# Printing initial string and sub-string

print ("initial_strings : ", ini_string, "\nsubstring : ",
sub_string)

 

res = []

# Finding all occurrences of substring

# in a string using list comprehension

res = [i for i in range(len(ini_string)) 

 if ini_string.startswith(sub_string, i)]

 

# printing result(

print ("resultant positions", str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial_strings :  xbzefdgstbzefzexezef 
    substring :  zef
    resultant positions [2, 10, 17]
    

