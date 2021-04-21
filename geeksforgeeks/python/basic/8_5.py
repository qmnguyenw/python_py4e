Python – Remove empty List from List



Sometimes, while working with python data, we can have a problem in which we
need to filter out certain empty data. These can be None, empty string etc.
This can have application in many domains. Let’s discuss certain ways in which
removal of empty lists can be performed.

 **Method #1 : Using list comprehension**  
This is one of the way in which this problem can be solved. In this, we
iterate through the list and don’t include the list which is empty.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove empty List from List

# using list comprehension

 

# Initializing list 

test_list = [5, 6, [], 3, [], [], 9]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Remove empty List from List

# using list comprehension

res = [ele for ele in test_list if ele != []]

 

# printing result 

print ("List after empty list removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, [], 3, [], [], 9]
    List after empty list removal : [5, 6, 3, 9]
    

**Method #2 : Usingfilter()**  
This is yet another way in which this task can be performed. In this we filter
None values. The none values include empty lists as well and hence these get
removed.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove empty List from List

# using filter()

 

# Initializing list 

test_list = [5, 6, [], 3, [], [], 9]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Remove empty List from List

# using filter

res = list(filter(None, test_list))

 

# printing result 

print ("List after empty list removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, [], 3, [], [], 9]
    List after empty list removal : [5, 6, 3, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

