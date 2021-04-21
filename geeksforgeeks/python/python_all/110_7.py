Python | Maximize alternate element List



The problem of getting maximum of a list is quite generic and we might some
day face the issue of getting the maximum of alternate elements and get the
list of 2 elements containing maximum of alternate elements. Let’s discuss
certain ways in which this can be performed.

 **Method #1 : Using list comprehension + list slicing +max()**  
List slicing clubbed with list comprehension can be used to perform this
particular task. We can have list comprehension to get run the logic and list
slicing can slice out the alternate character, maximize by the max function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximize alternate element List

# using list comprehension + list slicing + max()

 

# initializing list 

test_list = [2, 1, 5, 6, 8, 10]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + list slicing + max()

# Maximize alternate element List

res = [max(test_list[i : : 2]) for i in
range(len(test_list) // (len(test_list)//2))]

 

# print result

print("The alternate elements maximum list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [2, 1, 5, 6, 8, 10]
    The alternate elements maximum list : [8, 10]
    

**Method #2 : Using loop**  
This is the brute method to perform this particular task in which we have the
maximum of alternate elements in different element indices and then return the
output list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Maximize alternate element List

# using loop

 

# initializing list 

test_list = [2, 1, 5, 6, 8, 10]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using loop

# Maximize alternate element List

res = [0, 0]

for i in range(0, len(test_list)):

 if(i % 2):

 res[1] = max(res[1], test_list[i])

 else :

 res[0] = max(res[0], test_list[i])

 

# print result

print("The alternate elements maximum list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [2, 1, 5, 6, 8, 10]
    The alternate elements maximum list : [8, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

