Python program to count positive and negative numbers in a list



Given a list of numbers, write a Python program to count positive and negative
numbers in a List.

 **Example:**

    
    
     **Input:** list1 = [2, -7, 5, -64, -14]
    **Output:** pos = 2, neg = 3
    
    **Input:** list2 = [-12, 14, 95, 3]
    **Output:** pos = 3, neg = 1

 **Example #1:** Count positive and negative numbers from given list using for
loop

Iterate each element in the list using for loop and check if num >= 0, the
condition to check positive numbers. If the condition satisfies, then increase
pos_count else increase neg_count.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count positive and negative numbers in a List

 

# list of numbers

list1 = [10, -21, 4, -45, 66, -93, 1]

 

pos_count, neg_count = 0, 0

 

# iterating each number in list

for num in list1:

 

 # checking condition

 if num >= 0:

 pos_count += 1

 

 else:

 neg_count += 1

 

print("Positive numbers in the list: ", pos_count)

print("Negative numbers in the list: ", neg_count)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Positive numbers in the list:  4
    Negative numbers in the list:  3
    

**Example #2:** Using while loop

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count positive and negative numbers in a List

 

# list of numbers

list1 = [-10, -21, -4, -45, -66, 93,
11]

 

pos_count, neg_count = 0, 0

num = 0

 

# using while loop 

while(num < len(list1)):

 

 # checking condition

 if list1[num] >= 0:

 pos_count += 1

 else:

 neg_count += 1

 

 # increment num 

 num += 1

 

print("Positive numbers in the list: ", pos_count)

print("Negative numbers in the list: ", neg_count)  
  
---  
  
 __

 __

 **Output:**

    
    
    Positive numbers in the list:  2
    Negative numbers in the list:  5
    

**Example #3 :** Using Python Lambda Expressions

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count positive

# and negative numbers in a List

 

# list of numbers

list1 = [10, -21, -4, 45, 66, 93, -11]

 

neg_count = len(list(filter(lambda x: (x < 0),
list1)))

 

# we can also do len(list1) - neg_count

pos_count = len(list(filter(lambda x: (x >= 0),
list1)))

 

print("Positive numbers in the list: ", pos_count)

print("Negative numbers in the list: ", neg_count)  
  
---  
  
 __

 __

 **Output:**

    
    
    Positive numbers in the list:  4
    Negative numbers in the list:  3
    

**Example #4 :** Using List Comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count positive

# and negative numbers in a List

 

# list of numbers

list1 = [-10, -21, -4, -45, -66, -93,
11]

 

only_pos = [num for num in list1 if num >= 1]

pos_count = len(only_pos)

 

print("Positive numbers in the list: ", pos_count)

print("Negative numbers in the list: ", len(list1) -
pos_count)  
  
---  
  
 __

 __

 **Output:**

    
    
    Positive numbers in the list:  1
    Negative numbers in the list:  6
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

