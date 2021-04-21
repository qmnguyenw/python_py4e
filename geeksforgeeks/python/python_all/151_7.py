Python | Split nested list into two lists



Given a nested 2D list, the task is to split the nested list into two lists
such that first list contains first elements of each sublists and second list
contains second element of each sublists.

 **Method #1: Usingmap, zip()**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# splitting nested list

# into 2 lists

 

# initialising nested lists

ini_list = [[1, 2], [4, 3], [45, 65], [223,
2]]

 

# printing initial lists

print ("initial list", str(ini_list))

 

# code to split it into 2 lists

res1, res2 = map(list, zip(*ini_list))

 

# printing result

print("final lists", res1, "\n", res2)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list [[1, 2], [4, 3], [45, 65], [223, 2]]
    final lists [1, 4, 45, 223] 
     [2, 3, 65, 2]
    

  
**Method #2: Using list comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# python code to demonstrate

# splitting nested list

# into 2 lists

 

# initialising nested lists

ini_list = [[1, 2], [4, 3], [45, 65], [223,
2]]

 

# printing initial lists

print ("initial list", str(ini_list))

 

# code to split it into 2 lists

res1 = [i[1] for i in ini_list]

res2 = [i[0] for i in ini_list]

 

# printing result

print("final lists", str(res1), "\n", str(res2))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial list [[1, 2], [4, 3], [45, 65], [223, 2]]
    final lists [2, 3, 65, 2] 
     [1, 4, 45, 223]
    

