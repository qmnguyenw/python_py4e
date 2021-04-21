Python program to find second largest number in a list



Given a list of numbers, the task is to write a Python program to find the
second largest number in given list.  
 **Examples:**

    
    
    **Input:** list1 = [10, 20, 4]
    **Output:** 10
    
    **Input:** list2 = [70, 11, 20, 4, 100]
    **Output:** 70
    

**Method 1:** Sorting is an easier but less optimal method. Given below is an
O(n) algorithm to do the same.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find second largest

# number in a list

# list of numbers - length of

# list should be at least 2

list1 = [10, 20, 4, 45, 99]

mx=max(list1[0],list1[1])

secondmax=min(list1[0],list1[1])

n =len(list1)

for i in range(2,n):

 if list1[i]>mx:

 secondmax=mx

 mx=list1[i]

 elif list1[i]>secondmax and \

 mx != list1[i]:

 secondmax=list1[i]

print("Second highest number is : ",\

 str(secondmax))  
  
---  
  
 __

 __

 **Output**

    
    
    Second highest number is :  45
    

**Method 2:** Sort the list in ascending order and print the second last
element in the list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find largest

# number in a list

# list of numbers

list1 = [10, 20, 4, 45, 99]

# sorting the list

list1.sort()

# printing the second last element

print("Second largest element is:", list1[-2])  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    Second largest element is: 45
    

