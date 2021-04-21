Python – Difference between Uni length slicing and Access Notation



There are various ways to extract elements, Uni length slicing and Access
Notations are among them. Let’s check difference between them.

 **Difference #1 : Different behaviour with Different Containers**

The access notation return element in both List and Strings, but return 1
length strings while slicing using uni length slice and element in case of
strings.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Difference between Uni length slicing and Access Notation

# In different containers

 

# initializing lists

test_list = [5, 7, 2, 6, 8, 1]

 

# initializing string 

test_str = "572681"

 

# printing original list

print("The original list : " + str(test_list))

 

# printing string

print("The original string : " + str(test_str))

print("\r")

 

# access Notation results 

acc_list = test_list[3]

acc_str = test_str[3]

 

# unilength slicing results 

slc_list = test_list[3 : 4]

slc_str = test_str[3 : 4]

 

# printing results 

print("The access notation result for list : " + str(acc_list))

print("The access notation result for string : " + str(acc_str))

print("\r")

print("The slicing result for list : " + str(slc_list))

print("The slicing result for string : " + str(slc_str))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 7, 2, 6, 8, 1]
    The original string : 572681
    
    The access notation result for list : 6
    The access notation result for string : 6
    
    The slicing result for list : [6]
    The slicing result for string : 6
    

**Difference #2 : No Index out of bounds Exception in case of Slice
operation**

  

  

There is no out of bounds exception in case of Slice Operation, but there is,
in case of access notation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Difference between Uni length slicing and Access Notation

# No Index out of bounds Exception in case of Slice operation

 

# initializing lists

test_list = [5, 7, 2, 6, 8, 1]

 

# printing string

print("The original list : " + str(test_list))

 

# access Notation results 

try :

 acc_list = test_list[17]

except Exception as e:

 acc_list = str(e)

 

# unilength slicing results 

slc_list = test_list[17 : 18]

 

# printing results 

print("The access notation result for list : " + str(acc_list))

print("The slicing result for list : " + str(slc_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 7, 2, 6, 8, 1]
    The access notation result for list : list index out of range
    The slicing result for list : []
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

