Python | Sort list of lists by the size of sublists



Given a list of lists, the task is to sort a list on the basis of size of
sublists. Let’s discuss a few methods to do the same.

 **Method #1: Using sort**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort list of list

# on the basis of size of sublist

 

ini_list = [[1, 2, 3], [1, 2], [1, 2, 3,
4],

 [1, 2, 3, 4, 5], [2, 4, 6]]

 

# printing initial ini_list

print ("initial list", str(ini_list))

 

# sorting on bais of size of list

ini_list.sort(key = len)

 

# printing final result

print("final list", str(ini_list))  
  
---  
  
 __

 __

 **Output:**

> initial list [[1, 2, 3], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 4, 6]]  
> final list [[1, 2], [1, 2, 3], [2, 4, 6], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

  
**Method #2: Using lambda**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort list of list

# on the basis of size of sublist

 

ini_list = [[1, 2, 3], [1, 2], [1, 2, 3,
4],

 [1, 2, 3, 4, 5], [2, 4, 6]]

 

# printing initial ini_list

print ("initial list", str(ini_list))

 

# sorting on bais of size of list

ini_list.sort(key = lambda x:len(x))

 

# printing final result

print("final list", str(ini_list))  
  
---  
  
 __

 __

 **Output:**

> initial list [[1, 2, 3], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 4, 6]]  
> final list [[1, 2], [1, 2, 3], [2, 4, 6], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

  
**Method #3: Using sorted**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort list of list

# on the basis of size of sublist

 

ini_list = [[1, 2, 3], [1, 2], [1, 2, 3,
4],

 [1, 2, 3, 4, 5], [2, 4, 6]]

 

# printing initial ini_list

print ("initial list", str(ini_list))

 

# sorting on bais of size of list

result = sorted(ini_list, key = len)

 

# printing final result

print("final list", str(result))  
  
---  
  
 __

 __

 **Output:**

> initial list [[1, 2, 3], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 4, 6]]  
> final list [[1, 2], [1, 2, 3], [2, 4, 6], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

