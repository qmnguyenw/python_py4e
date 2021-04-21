Python | Replace elements in second list with index of same element in first
list



Given two lists of strings, where first list contains all elements of second
list, the task is to replace every element in second list with index of
elements in first list.

 **Method #1: Using Iteration**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to replace every element

# in second list with index of first element.

 

# List Initialization

Input1 = ['cut', 'god', 'pass'] 

Input2 = ['god', 'cut', 'cut', 'cut', 

 'god', 'pass', 'cut', 'pass']

 

# List Initialization

Output = []

 

# Using iteration

for x in Input2:

 for y in Input1:

 if x == y:

 Output.append(Input1.index(y))

 

# Printing output

print("initial 2 list are")

print(Input1, "\n", Input2)

print("Second list after replacement is:", Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    initial 2 list are
    ['cut', 'god', 'pass'] 
     ['god', 'cut', 'cut', 'cut', 'god', 'pass', 'cut', 'pass']
    Second list after replacement is: [1, 0, 0, 0, 1, 2, 0, 2]
    

  
**Method #2: Using List comprehension**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to replace every element

# in second list with index of first element.

 

# List initialization

Input1 = ['cut', 'god', 'pass']

 

# using enumeate

temp = {y:x for x, y in enumerate(Input1)}

 

# List initialization

Input2 = ['god', 'cut', 'cut', 'cut', 

 'god', 'pass', 'cut', 'pass']

 

# Using list comprehension

Output = [temp.get(elem) for elem in Input2]

 

# Printing output

print("initial 2 list are")

print(Input1, "\n", Input2)

print("Second list after replacement is:", Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    initial 2 list are
    ['cut', 'god', 'pass'] 
     ['god', 'cut', 'cut', 'cut', 'god', 'pass', 'cut', 'pass']
    Second list after replacement is: [1, 0, 0, 0, 1, 2, 0, 2]
    

