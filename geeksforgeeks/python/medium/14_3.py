Student management system in Python



 **Prerequisite:** Classes and objects in python

 **Problem Statement:**  
Write a program to build a simple Student Management System using Python which
can perform following operations:

  1. Accept
  2. Display
  3. Search
  4. Delete
  5. Update

 **Approach:** Below is the approach to do the above operations:

  1.  **Accept** – This method takes details from the user like name, roll number, and marks for two different subjects.
    
    
    # Method to enter new student details
    def accept(self, Name, Rollno, marks1, marks2 ):
        # Creates a new class constructor
        # and pass the details
        ob = Student(Name, Rollno, marks1, marks2 )
    
        # list containing objects of student class
        ls.append(ob)
    

  2. **Display** – This method displays the details of every student.
    
    
    # Function to display student details     
    def display(self, ob):
        print("Name   : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")    
    

  3. **Search** – This method searches for a particular student from the list of students.  
This method will ask the user for roll number and then search according to the
roll number

    
    
    # Search Function    
    def search(self, rn):
        for i in range(ls.__len__()):
            # iterate through the list containing
            # student object and checks through
            # roll no of each object
            if(ls[i].rollno == rn):
                # returns the object with matching 
                # roll number
                return i 
    

  4. **Delete** – This method deletes the record of a particular student with a matching roll number.
    
    
    # Delete Function                                  
    def delete(self, rn):
        # Calls the search function 
        # created above
        i = obj.search(rn)  
        del ls[i]
    

  5. **Update** – This method updates the roll number of the student.  
This method will ask for the old roll number and new roll number. It will
replace the old roll number with new roll number.

  

  

    
    
    # Update Function   
    def update(self, rn, No):
        # calling the search function
        # of student class
        i = obj.search(rn)
        ls[i].rollno = No
    

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# This is simplest Student data management program in python

# Create class "Student"

class Student:

 # Constructor

 def __init__(self, name, rollno, m1, m2):

 self.name = name

 self.rollno = rollno

 self.m1 = m1

 self.m2 = m2

 

 # Function to create and append new student 

 def accept(self, Name, Rollno, marks1, marks2 ):

 # use ' int(input()) ' method to take input from user

 ob = Student(Name, Rollno, marks1, marks2 )

 ls.append(ob)

 

 # Function to display student details 

 def display(self, ob):

 print("Name : ", ob.name)

 print("RollNo : ", ob.rollno)

 print("Marks1 : ", ob.m1)

 print("Marks2 : ", ob.m2)

 print("\n") 

 

 # Search Function 

 def search(self, rn):

 for i in range(ls.__len__()):

 if(ls[i].rollno == rn):

 return i 

 

 # Delete Function 

 def delete(self, rn):

 i = obj.search(rn) 

 del ls[i]

 

 # Update Function 

 def update(self, rn, No):

 i = obj.search(rn)

 roll = No

 ls[i].rollno = roll;

 

# Create a list to add Students

ls =[]

# an object of Student class

obj = Student('', 0, 0, 0)

 

print("\nOperations used, ")

print("\n1.Accept Student details\n2.Display Student Details\n" /

 / "3.Search Details of a Student\n4.Delete Details of Student" /

 / "\n5.Update Student Details\n6.Exit")

 

# ch = int(input("Enter choice:"))

# if(ch == 1):

obj.accept("A", 1, 100, 100)

obj.accept("B", 2, 90, 90)

obj.accept("C", 3, 80, 80)

 

# elif(ch == 2):

print("\n")

print("\nList of Students\n")

for i in range(ls.__len__()): 

 obj.display(ls[i])

 

# elif(ch == 3):

print("\n Student Found, ")

s = obj.search(2)

obj.display(ls[s])

 

# elif(ch == 4):

obj.delete(2)

print(ls.__len__())

print("List after deletion")

for i in range(ls.__len__()): 

 obj.display(ls[i])

 

# elif(ch == 5):

obj.update(3, 2)

print(ls.__len__())

print("List after updation")

for i in range(ls.__len__()): 

 obj.display(ls[i])

 

# else:

print("Thank You !")

   
  
---  
  
__

__

**Output:**

    
    
    Operations used,
    
    1.Accept Student details
    2.Display Student Details
    3.Search Details of a Student
    4.Delete Details of Student
    5.Update Student Details
    6.Exit
    
    
    
    List of Students
    
    Name   :  A
    RollNo :  1
    Marks1 :  100
    Marks2 :  100
    
    
    Name   :  B
    RollNo :  2
    Marks1 :  90
    Marks2 :  90
    
    
    Name   :  C
    RollNo :  3
    Marks1 :  80
    Marks2 :  80
    
    
    
     Student Found,
    Name   :  B
    RollNo :  2
    Marks1 :  90
    Marks2 :  90
    
    
    2
    List after deletion
    Name   :  A
    RollNo :  1
    Marks1 :  100
    Marks2 :  100
    
    
    Name   :  C
    RollNo :  3
    Marks1 :  80
    Marks2 :  80
    
    
    2
    List after updation
    Name   :  A
    RollNo :  1
    Marks1 :  100
    Marks2 :  100
    
    
    Name   :  C
    RollNo :  2
    Marks1 :  80
    Marks2 :  80
    
    
    Thank You !
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

