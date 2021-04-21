Python – Descending Sort String Numbers



Reverse Sorting a list is easy task and has been dealt with in many
situations. With Machine Learning and Data Science emerging, sometimes we can
get the data in the format of list of numbers but with string as data type.
Generic Sort functions give erroneous result in that case, hence several other
methods have to employed to perform these particular task. Lets discuss ways
in which this is performed.

 **Method #1 : Naive Method**  
In the naive method requires the type conversion of all the elements into
integers of the list iterated through a loop. After that generic sort function
is employed to perform the task. The descending sorting is done by passing
reverse.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Descending Sort String Numbers

# using naive method 

 

# initializing list 

test_list = [ '4', '6', '7', '2', '1']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# Descending Sort String Numbers

# numeric string sorting

for i in range(0, len(test_list)) :

 test_list[i] = int(test_list[i])

test_list.sort(reverse = True)

 

# printing result

print ("The resultant reverse sorted list : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['4', '6', '7', '2', '1']
    The resultant reverse sorted list : [7, 6, 4, 2, 1]
    

**Method #2 : Usingsort() using key + reverse**  
The generic sort() can be used to perform this particular task, but has to be
specified with the key as integer to convert it to integer while performing
sort function internally. The descending sorting is done by passing reverse.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Descending Sort String Numbers

# using sort() + key

 

# initializing list 

test_list = [ '4', '6', '7', '2', '1']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using sort() + key

# Descending Sort String Numbers

test_list.sort(key = int, reverse = True)

 

# printing result

print ("The resultant reverse sorted list : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['4', '6', '7', '2', '1']
    The resultant reverse sorted list : ['7', '6', '4', '2', '1']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

