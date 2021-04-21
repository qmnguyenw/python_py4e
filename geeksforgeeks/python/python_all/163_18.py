Python – Create a dictionary using list with none values



Sometimes you might need to convert a list to dict object for some better and
fast operation. Let’s see how to convert a list into a dictionary of none
values. Here we will find three methods of doing this.

 **Method #1:** Using zip()and dict

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# converting list into dictionary with none values

# using zip() and dictionary

 

# initializing list

ini_list = [1, 2, 3, 4, 5]

 

# printing intialized list

print ("initial list", str(ini_list))

 

# Converting list into dictionary using zip() and dictionary

res = dict(zip(ini_list, [None]*len(ini_list)))

 

# printing final result

print ("final dictionary", str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list [1, 2, 3, 4, 5]
    final dictionary {1: None, 2: None, 3: None, 4: None, 5: None}
    

  
**Method #2:** Using dict

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate converting

# list into dictionary with none values

# using dict()

 

# initializing list

ini_list = [1, 2, 3, 4, 5]

 

# printing intialized list

print ("initial list", str(ini_list))

 

# Converting list into dict()

res = dict.fromkeys(ini_list)

 

# printing final result

print ("final dictionary", str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial list [1, 2, 3, 4, 5]
    final dictionary {1: None, 2: None, 3: None, 4: None, 5: None}
    

