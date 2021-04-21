Python | Remove duplicates in Matrix



While working with Python Matrix, we can face a problem in which we need to
perform the removal of duplicates from Matrix. This problem can occur in
Machine Learning domain because of extensive usage of matrices. Let’s discuss
certain way in which this task can be performed.

 **Method : Using loop**  
This task can be performed in brute force manner using loops. In this, we just
iterate the list of list using loop and check for the already presence of
element, and append in case it’s new element, and construct a non-duplicate
matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing duplicates in Matrix

# using loop

 

# initialize list 

test_list = [[5, 6, 8], [8, 5, 3], [9,
10, 3]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Removing duplicates in Matrix

# using loop

res = []

track = []

count = 0

 

for sub in test_list:

 res.append([]);

 for ele in sub:

 if ele not in track:

 res[count].append(ele)

 track.append(ele)

 count += 1

 

# printing result

print("The Matrix after duplicates removal is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[5, 6, 8], [8, 5, 3], [9, 10, 3]]
    The Matrix after duplicates removal is : [[5, 6, 8], [3], [9, 10]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

