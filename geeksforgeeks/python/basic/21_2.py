Python list | pop()



 ** _pop()_** is an inbuilt function in Python that removes and returns last
value from the list or the given index value.

 **Syntax :**

    
    
    list_name.pop(index)

 **Parameter :**

    
    
     **index** ( _optional_ ) - The value at index is 
    popped out and removed.
    
    If the index is not given, then the last
    element is popped out and removed.

 **Returns :**

    
    
    The last value or the given index value from the list

 **Exception :**

  

  

    
    
    When index is out of range, it returns IndexError

  
**Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for pop() method

 

list1 = [ 1, 2, 3, 4, 5, 6 ]

 

# Pops and removes the last element from the list

print(list1.pop())

 

# Print list after removing last element

print("New List after pop : ", list1, "\n")

 

list2 = [1, 2, 3, ('cat', 'bat'), 4]

 

# Pop last three element

print(list2.pop())

print(list2.pop())

print(list2.pop())

 

# Print list

print("New List after pop : ", list2, "\n")  
  
---  
  
 __

 __

Output :

    
    
    6
    New List after pop :  [1, 2, 3, 4, 5] 
    
    4
    ('cat', 'bat')
    3
    New List after pop :  [1, 2] 

  
**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program showing pop() method

# and remaining list after each pop

 

list1 = [ 1, 2, 3, 4, 5, 6 ]

 

# Pops and removes the last 

# element from the list

print(list1.pop(), list1)

 

# Pops and removes the 0th index

# element from the list

print(list1.pop(0), list1)  
  
---  
  
 __

 __

 **Output :**

    
    
    6 [1, 2, 3, 4, 5]
    1 [2, 3, 4, 5]
    

  
**Code #3 :** IndexError

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for error in pop() method

 

list1 = [ 1, 2, 3, 4, 5, 6 ]

print(list1.pop(8))  
  
---  
  
 __

 __

 **Output :**

    
    
    Traceback (most recent call last):
      File "/home/1875538d94d5aecde6edea47b57a2212.py", line 5, in 
        print(list1.pop(8))
    IndexError: pop index out of range
    

  
**Practical Example :**  
A list fruit contains _fruit_name_ and _property_ saying its fruit. Another
list consume has two items _juice_ and _eat_. With the help of pop() and
append() we can do something interesting.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program demonstrating

# practical use of list pop()

 

fruit = [['Orange','Fruit'],['Banana','Fruit'],
['Mango', 'Fruit']]

consume = ['Juice', 'Eat']

possible = []

 

# Iterating item in list fruit

for item in fruit :

 

 # Inerating use in list consume

 for use in consume :

 

 item.append(use)

 possible.append(item[:])

 item.pop(-1)

print(possible)  
  
---  
  
 __

 __

Output :

    
    
    [['Orange', 'Fruit', 'Juice'], ['Orange', 'Fruit', 'Eat'],
     ['Banana', 'Fruit', 'Juice'], ['Banana', 'Fruit', 'Eat'],
     ['Mango', 'Fruit', 'Juice'], ['Mango', 'Fruit', 'Eat']]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

