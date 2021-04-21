Python | Calculate difference between adjacent elements in given list



Given a list, the task is to create a new list containing difference of
adjacent elements in the given list.

 **Method #1: Usingzip()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to calculate difference

# between adjacent elements in list

 

 

# initialising _list

ini_list = [5, 4, 89, 12, 32, 45]

 

# printing iniial_list

print("intial_list", str(ini_list))

 

# Calculating difference list

diff_list = []

for x, y in zip(ini_list[0::], ini_list[1::]):

 diff_list.append(y-x)

 

# printing difference list

print ("difference list: ", str(diff_list))

   
  
---  
  
__

__

**Output:**

    
    
    intial_list [5, 4, 89, 12, 32, 45]
    difference list:  [-1, 85, -77, 20, 13]
    

  
**Method #2: Using Naive approach**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# to calculate difference

# between adjacent elements in list

 

 

# initialising _list

ini_list = [5, 4, 89, 12, 32, 45]

 

# printing iniial_list

print("intial_list", str(ini_list))

 

# Calculating difference list

diff_list = []

 

for i in range(1, len(ini_list)):

 diff_list.append(ini_list[i] - ini_list[i-1])

 

# printing difference list

print ("difference list: ", str(diff_list))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    intial_list [5, 4, 89, 12, 32, 45]
    difference list:  [-1, 85, -77, 20, 13]
    

