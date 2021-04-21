Python program to sort and find the data in the student records



Consider a software for maintaining records of the students in a class.
Consider the following functions which are required to be performed:

  1. Sorting of names according to First Name of the students.
  2. Finding the Minimum marks among all the marks
  3. Finding contact number of student using his/her First Name.

The task is to write a Python program to implement the software having these
three functionalities.

 **Approach:** For the above problem we should use a dictionary that either
takes a name as a whole to key and other data as value to it or vice versa.
Here I have taken the name as a key and contact number, marks as the value
associated with the name. So at first the user needs to enter the details of
the students and these details will be stored in dictionary as {[‘first name’,
‘second name’]:(‘contact number’, ‘marks’)}. Then we create a new list of
tuples that store data according to the function requirement. In the program
four user-defined functions have been created:

  1.  **sort(** ) function that sorts the record based on the first name.
  2.  **minmarks( )** function that finds the minimum marks from all records.
  3.  **searchdetail( )** function that takes first name as an input and fetch student contact number from the corresponding record.
  4.  **option()** function for showing the options.

Below is the implementation:

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

print("-----Program for Student Information-----")

 

D = dict()

 

n = int(input('How many student record you want to store?? '))

 

# Add student information 

# to the dictionary

for i in range(0,n):

 x, y = input("Enter the complete name (First and last name) of
student: ").split()

 z = input("Enter contact number: ")

 m = input('Enter Marks: ')

 D[x, y] = (z, m)

 

# define a function for shorting 

# names based on first name

def sort():

 ls = list()

 # fetch key and value using 

 # items() method

 for sname,details in D.items(): 

 

 # store key parts as an tuple

 tup = (sname[0],sname[1]) 

 

 # add tuple to the list

 ls.append(tup) 

 

 # sort the final list of tuples

 ls = sorted(ls) 

 for i in ls:

 

 # print first name and second name

 print(i[0],i[1]) 

 return

 

# define a function for 

# finding the minimum marks 

# in stored data

def minmarks():

 ls = list()

 # fetch key and value using

 # items() methods

 for sname,details in D.items(): 

 # add details second element

 # (marks) to the list

 ls.append(details[1]) 

 

 # sort the list elemnts 

 ls = sorted(ls) 

 print("Minimum marks: ", min(ls))

 

 return

 

# define a function for searching

# student contact number

def searchdetail(fname):

 ls = list()

 

 for sname,details in D.items():

 

 tup=(sname,details)

 ls.append(tup)

 

 for i in ls: 

 if i[0][0] == fname:

 print(i[1][0])

 return

 

# define a funtion for

# asking the options

def option():

 

 choice = int(input('Enter the operation detail: \n \

 1: Sorting using first name \n \

 2: Finding Minimum marks \n \

 3: Search contact number using first name: \n \

 4: Exit\n \

 Option: '))

 

 if choice == 1:

 # finction call

 sort()

 print('Want to perform some other operation??? Y or N: ')

 inp = input()

 if inp == 'Y':

 option()

 

 # exit finction call 

 exit()

 

 elif choice == 2:

 minmarks()

 print('Want to perform some other operation??? Y or N: ')

 

 inp = input()

 if inp == 'Y':

 option()

 exit() 

 

 elif choice == 3:

 first = input('Enter first name of student: ')

 searchdetail(first)

 

 print('Want to perform some other operation??? Y or N: ')

 inp = input()

 if inp == 'Y':

 option()

 

 exit()

 else:

 print('Thanks for executing me!!!!')

 exit()

 

option()  
  
---  
  
 __

 __

