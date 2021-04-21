Python – Alternate Strings Concatenation



The problem of getting concatenation of a list is quite generic and we might
some day face the issue of getting the concatenation of alternate elements and
get the list of 2 elements containing concatenation of alternate elements.
Let’s discuss certain ways in which this can be performed.

 **Method #1 : Using list comprehension + list slicing +join()**  
List slicing clubbed with list comprehension can be used to perform this
particular task. We can have list comprehension to get run the logic and list
slicing can slice out the alternate character, concat by the join() function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Alternate Strings Concatenation

# using list comprehension + list slicing

 

# initializing list 

test_list = ["GFG", "is", "for", "Computer",
"Science", "learning"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + list slicing

# Alternate Strings Concatenation

res = [" ".join(test_list[i : : 2]) for i in
range(len(test_list) //

 (len(test_list)//2))]

 

# print result

print("The alternate elements concatenation list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['GFG', 'is', 'for', 'Computer', 'Science', 'learning']
    The alternate elements concatenation list : ['GFG for Science', 'is Computer learning']
    

**Method #2 : Using loop**  
This is the brute method to perform this particular task in which we have the
concatenation of alternate elements in different element indices and then
return the output list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Alternate Strings Concatenation

# using loop

 

# initializing list 

test_list = ["GFG", "is", " for", " Computer", "
Science", " learning"]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using loop

# Alternate Strings Concatenation

res = ["", ""]

for i in range(0, len(test_list)):

 if(i % 2):

 res[1] += test_list[i]

 else :

 res[0] += test_list[i]

 

# print result

print("The alternate elements concatenation list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['GFG', 'is', 'for', 'Computer', 'Science', 'learning']
    The alternate elements concatenation list : ['GFG for Science', 'is Computer learning']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

