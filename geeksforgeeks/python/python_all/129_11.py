Python | Percentage similarity of lists



Sometimes, while working with Python list, we have a problem in which we need
to find how much a list is similar to other list. The similarity quotient of
both the list is what is required in many scenarios we might have. Let’s
discuss a way in which this task can be performed.

 **Method : Using"|" operator + "&" operator + set()**  
The method which is formally applied to calculate the similarity among lists
is finding the distinct elements and also common elements and computing it’s
quotient. The result is then multiplied by 100, to get the percentage.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Percentage similarity of lists

# using "|" operator + "&" operator + set()

 

# initialize lists

test_list1 = [1, 4, 6, 8, 9, 10, 7]

test_list2 = [7, 11, 12, 8, 9]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Percentage similarity of lists

# using "|" operator + "&" operator + set()

res = len(set(test_list1) & set(test_list2)) /
float(len(set(test_list1) | set(test_list2))) * 100

 

# printing result

print("Percentage similarity among lists is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [1, 4, 6, 8, 9, 10, 7]
    The original list 2 is : [7, 11, 12, 8, 9]
    Percentage similarity among lists is : 33.33333333333333
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

