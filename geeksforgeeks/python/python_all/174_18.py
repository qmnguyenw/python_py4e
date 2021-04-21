Python program to print odd numbers in a List



Given a list of numbers, write a Python program to print all odd numbers in
given list.

 **Example:**

    
    
     **Input:** list1 = [2, 7, 5, 64, 14]
    **Output:** [7, 5]
    
    **Input:** list2 = [12, 14, 95, 3, 73]
    **Output:** [95, 3, 73]

  1.  **Using for loop :** Iterate each element in the list using for loop and check if num % 2 != 0. If the condition satisfies, then only print the number.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print odd Numbers in a List

 

# list of numbers

list1 = [10, 21, 4, 45, 66, 93]

 

# iterating each number in list

for num in list1:

 

 # checking condition

 if num % 2 != 0:

 print(num, end = " ")  
  
---  
  
 __

 __

 **Output:**

    
        21 45 93 

  2. **Using while loop :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print odd Numbers in a List

 

# list of numbers

list1 = [10, 21, 4, 45, 66, 93]

i = 0

 

# using while loop 

while(i < len(list1)):

 

 # checking condition

 if list1[i] % 2 != 0:

 print(list1[i], end = " ")

 

 # increment i 

 i += 1

   
  
---  
  
__

__

**Output:**

    
        21 45 93 

  3. **Using list comprehension :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print odd Numbers in a List

 

# list of numbers

list1 = [10, 21, 4, 45, 66, 93]

 

only_odd = [num for num in list1 if num % 2 ==
1]

 

print(only_odd)  
  
---  
  
 __

 __

 **Output:**

  

  

    
        21 45 93 

  4. **Using lambda expressions :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print odd numbers in a List

 

# list of numbers 

list1 = [10, 21, 4, 45, 66, 93, 11] 

 

 

# we can also print odd no's using lambda exp. 

odd_nos = list(filter(lambda x: (x % 2 != 0),
list1))

 

print("Odd numbers in the list: ", odd_nos)   
  
---  
  
__

__

**Output:**

    
        Odd numbers in the list:  [21, 45, 93, 11]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

