Python – Index Value Summation List



To access the elements of lists, there are various methods. But sometimes we
may require to access the element along with the index on which it is found
and compute its summation, and for that we may need to employ different
strategies. This article discusses some of those strategies.

 **Method 1 : Naive method**  
This is the most generic method that can be possibly employed to perform this
task of accessing the index along with the value of the list elements. This is
done using a loop. The task of performing sum is performed using external
variable to add.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Index Value Summation List

# using naive method

 

# initializing list

test_list = [1, 4, 5, 6, 7]

 

# Printing list 

print ("The original list is : " + str(test_list))

 

# using naive method to

# Index Value Summation List

res = []

for i in range(len(test_list)):

 res.append(i + test_list[i])

 

print ("The list index-value summation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 7]
    The list index-value summation is : [1, 5, 7, 9, 11]
    

**Method 2 : Using list comprehension +sum()**  
This method works in similar way as the above method but uses the list
comprehension technique for the same, this reduces the possible lines of code
to be written and hence saves time. The task of performing summation is done
by sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Index Value Summation List

# using list comprehension

 

# initializing list

test_list = [1, 4, 5, 6, 7]

 

# Printing list 

print ("The original list is : " + str(test_list))

 

# using list comprehension to

# Index Value Summation List

res = [sum(list((i, test_list[i]))) for i in
range(len(test_list))]

 

print ("The list index-value summation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 7]
    The list index-value summation is : [1, 5, 7, 9, 11]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

