Python | Padding a string upto fixed length



Given a string, the task is to pad string up to given specific length with
whitespaces. Let’s discuss few methods to solve the given task.

 **Method #1: Usingljust()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# pad spaces in string

# upto fixed length

 

# initialising string

ini_string = "123abcjw"

padding_size = 15

 

# printing string and its length

print ("initial string : ", ini_string, len(ini_string))

 

# code to pad spaces in string

res = ini_string.ljust(padding_size)

 

# printing string and its length

print ("final string : ", res, len(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial string :  123abcjw 8
    final string :  123abcjw        15
    

  
**Method #2: Using format**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# pad spaces in string

# upto fixed length

 

# initialising string

ini_string = "123abcjw"

 

# printing string and its length

print ("initial string : ", ini_string, len(ini_string))

 

# code to pad spaces in string

res = "{:<15}".format(ini_string)

 

# printing string and its length

print ("final string : ", res, len(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial string :  123abcjw 8
    final string :  123abcjw        15
    

