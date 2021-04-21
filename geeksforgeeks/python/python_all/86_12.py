Python – Merge consecutive empty Strings



Sometimes, while working with python lists we can have a problem in which we
need to perform a merge operation on string of lists. This merge is
consecutive to convert multiple spaces to one. Lets discuss certain way in
which this can be performed.

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this we find for
empty strings using loop and ignore the consecutive strings in making of new
list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Merge consecutive empty Strings

# using loop

 

# Initializing list

test_list = ['Gfg', '', '', '', 'is', '', '',
'best', '']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Merge consecutive empty Strings

# using loop

count = 0

res = []

for ele in test_list:

 if ele =='':

 count += 1

 if (count % 2)== 0:

 res.append('')

 count = 0

 else:

 res.append(ele)

 

# printing result 

print ("List after removal of consecutive empty strings : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Gfg', '', '', '', 'is', '', '', 'best', '']
    List after removal of consecutive empty strings : ['Gfg', '', 'is', '', 'best', '']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

