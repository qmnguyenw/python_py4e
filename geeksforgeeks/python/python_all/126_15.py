Python | Remove trailing/leading special characters from strings list



Sometimes, while working with String lists, we can have a problem in which we
need to perform the deletion of extra characters that can be termed as
unwanted and occur at end of each string. Let’s discuss a way in which this
task can be performed.

 **Method : Usingmap() + str.strip()**  
Combination of the above two functionalities can help us achieve this
particular task. In this, we employ strip(), which has the ability to remove
the trailing and leading special unwanted characters from string list. The
map(), is used to extend the logic to each element in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove trailing / leading special characters from strings list

# Using map() + str.strip()

 

# initializing list

test_list = ['\rgfg\t\n', 'is\n', '\t\tbest\r']

 

# printing list

print("The original list : " + str(test_list))

 

# Remove trailing / leading special characters from strings list

# Using map() + str.strip()

res = list(map(str.strip, test_list))

 

# Printing result

print("List after removal of special characters : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : ['\rgfg\t\n', 'is\n', '\t\tbest\r']
    List after removal of special characters : ['gfg', 'is', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

