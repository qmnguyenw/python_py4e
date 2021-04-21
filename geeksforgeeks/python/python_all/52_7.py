Python – Remove alternate consecutive duplicates



Given list of elements, remove alternate consecutive duplicates of elements.

>  **Input** : test_list = [5, 5, 5, 5, 6, 6]  
>  **Output** : [5, 5, 6]  
>  **Explanation** : Alternate occ. of 5 and 6 are removed.
>
>  **Input** : test_list = [5, 5, 5, 5]  
>  **Output** : [5, 5]  
>  **Explanation** : Alternate occ. of 5 are removed.

 **Method : Using loop + remove()**

The combination of above functions can be used to solve this problem. In this,
we iterate each element and use additional previous element variable to keep
track of alternate criteria. The removal is performed using remove().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove alternate consecutive duplicates

# Using loop + remove()

 

# initializing lists

test_list = [5, 5, 5, 5, 6, 6, 8, 3,
3, 8]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using loop to iterate through elements

# element to keep track

temp = test_list[0]

count = 0

org_list = test_list

idx = 0

while(1):

 

 # break when idx greater than size

 if idx >= len(org_list):

 break

 

 # check for alternates 

 if count % 2 and temp == test_list[idx]:

 test_list.remove(test_list[idx])

 idx = idx - 1

 count += 1

 temp = test_list[idx]

 else:

 

 # keeping track of alternate index increment

 # and assignment

 if temp != test_list[idx]:

 count = 1

 temp = test_list[idx]

 else :

 count += 1

 idx = idx + 1

 

# printing result 

print("List after alternate duplicates removal : " +
str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 5, 5, 5, 6, 6, 8, 3, 3, 8]
    List after alternate duplicates removal : [5, 5, 6, 8, 3, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

