Python | Group List on K character



Sometimes, we may face an issue in which we require to split a list to list of
list on the K character sent as deliminator. This kind of problem can be used
to send messages or can be used in cases where it is desired to have list of
list of native list. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingindex() and list slicing**  
The list slicing can be used to get the sublists from the native list and
index function can be used to check for the K character which can potentially
act as a separator. The drawback of this is that it only works for a single
split i.e can only divide a list to 2 sublist.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Group List on K character

# using index() + list slicing 

 

# initializing list 

test_list = ['Geeks', 'for', 'M', 'Geeks', 1, 2]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 'M'

 

# using index() + list slicing

# Group List on K character

temp_idx = test_list.index(K)

res = [test_list[: temp_idx], test_list[temp_idx + 1: ]]

 

# print result

print("The list of sublist after separation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Geeks', 'for', 'M', 'Geeks', 1, 2]
    The list of sublist after separation : [['Geeks', 'for'], ['Geeks', 1, 2]]
    

**Method #2 : Using loops**  
The problem of the above proposed method can be solved using general loops and
using brute force, in this we just look for K character and make a new list
after that.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Group List on K character

# using loop

 

# initializing list 

test_list = ['Geeks', 'M', 'for', 'M', 4, 5,
'M', 'Geeks', 'CS', 'M', 'Portal']

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing K 

K = 'M'

 

# using loop

# Group List on K character

temp = []

res = []

for ele in test_list:

 if ele == K:

 res.append(temp)

 temp = []

 else:

 temp.append(ele)

res.append(temp)

 

# print result

print("The list of sublist after separation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Geeks', 'for', 'M', 'Geeks', 1, 2]
    The list of sublist after separation : [['Geeks', 'for'], ['Geeks', 1, 2]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

