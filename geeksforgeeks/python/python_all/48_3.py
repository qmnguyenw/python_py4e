Python program for arranging the students according to their marks in
descending order



Consider a class of 20 students whose names and marks are given to you. The
task is to arrange the students according to their marks in decreasing order.
Write a python program to perform the task.

 **Examples:**

    
    
     **Input:**
    Arun: 78%
    Geeta: 86%
    Shilpi: 65%
    
    **Output:** 
    Geeta: 86%
    Arun: 78%
    Shilpi: 65%
    
    
    

**Approach:** Since problem states that we need to collect student name and
their marks first so for this we will take inputs one by one in the list data
structure then sort them in reverse order using sorted() built-in function
based on the student’s percentage and in the last we will print the value
accordingly.

Below is the implementation:

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

print("-----Program for printing student name with marks using
list-----")

 

# create an empty dictionary

D = {}

 

n = int(input('How many student record you want to store?? '))

 

# create an empty list

# Add student information to the list

ls = []

 

for i in range(0, n):

 

 # Take combined input name and 

 # percentage and split values 

 # using split function.

 x,y = input("Enter the student name and it's percentage:
").split()

 

 # Add name and marks stored in x, y

 # respectively using tuple to the list

 ls.append((y,x))

 

# sort the elements of list

# based on marks

ls = sorted(ls, reverse = True)

 

print('Sorted list of students according to their marks in descending
order')

 

for i in ls:

 

 # print name and marks stored in 

 # second and first position 

 # respectively in list of tuples.

 print(i[1], i[0])  
  
---  
  
 __

 __

