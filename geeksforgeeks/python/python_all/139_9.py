Python | Ways to print list without quotes



Whenever we print list in Python, we generally use str(list) because of which
we have single quotes in the output list. Suppose if the problem requires to
print solution without quotes. Let’s see some ways to print list without
quotes.

 **Method #1: Usingmap()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# printing list in a proper way

 

# Initialising list

ini_list = ['a', 'b', 'c', 'd']

 

# Printing initial list with str

print ("List with str", str(ini_list))

 

# Printing list using map

print ("List in proper method", '[%s]' % ',
'.join(map(str, ini_list)))  
  
---  
  
 __

 __

 **Output:**

    
    
    List with str ['a', 'b', 'c', 'd']
    List in proper method [a, b, c, d]
    

  
**Method #2: Usingsep Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# printing list in proper way

 

# Initialising list

ini_list = ['a', 'b', 'c', 'd']

 

# Printing initial list with str

print ("List with str", str(ini_list))

 

# Printing list using sep Method

print (*ini_list, sep =', ')  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    List with str ['a', 'b', 'c', 'd']
    a, b, c, d
    

