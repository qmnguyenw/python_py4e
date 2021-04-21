Python | Cloning or Copying a list



In this article we will go through various ways of copying or cloning a list
in Python. These various ways of copying takes different execution time, so we
can compare them on the basis of time.

  1.  **Using slicing technique**  
This is the easiest and the fastest way to clone a list. This method is
considered when we want to modify a list and also keep a copy of the original.
In this we make a copy of the list itself, along with the reference. This
process is also called cloning. This technique takes about 0.039 seconds and
is the fastest technique.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to copy or clone a list

# Using the Slice Operator

def Cloning(li1):

 li_copy = li1[:]

 return li_copy

 

# Driver Code

li1 = [4, 8, 2, 10, 15, 18]

li2 = Cloning(li1)

print("Original List:", li1)

print("After Cloning:", li2)  
  
---  
  
 __

 __

Output:  
Original List: [4, 8, 2, 10, 15, 18]  
After Cloning: [4, 8, 2, 10, 15, 18]

  2.  **Using the extend() method**  
The lists can be copied into a new list by using the extend() function. This
appends each element of the iterable object (e.g., anothre list) to the end of
the new list. This takes around 0.053 second to complete.  
Example:

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to clone or copy a list

# Using the in-built function extend()

def Cloning(li1):

 li_copy = []

 li_copy.extend(li1)

 return li_copy

 

# Driver Code

li1 = [4, 8, 2, 10, 15, 18]

li2 = Cloning(li1)

print("Original List:", li1)

print("After Cloning:", li2)  
  
---  
  
 __

 __

Output:

    
        Original List: [4, 8, 2, 10, 15, 18]
    After Cloning: [4, 8, 2, 10, 15, 18]

  3.  **Using the list() method**  
This is the simplest method of cloning a list by using the builtin function
list(). This takes about 0.075 seconds to complete.  
Example:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to clone or copy a list

# Using the in-built function list()

def Cloning(li1):

 li_copy = list(li1)

 return li_copy

 

# Driver Code

li1 = [4, 8, 2, 10, 15, 18]

li2 = Cloning(li1)

print("Original List:", li1)

print("After Cloning:", li2)  
  
---  
  
 __

 __

Output:

    
        Original List: [4, 8, 2, 10, 15, 18]
    After Cloning: [4, 8, 2, 10, 15, 18]

  4.  **Using the method of Shallow Copy**  
This method of copying using copy.copy is well explained in the article
Shallow Copy. This takes around 0.186 seconds to complete.

  5.  **Using list comprehension**  
The method of list comprehension can be used to copy all the elements
individually from one list to another. This takes around 0.217 seconds to
complete.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to clone or copy a list

# Using list comprehension

def Cloning(li1):

 li_copy = [i for i in li1]

 return li_copy

 

# Driver Code

li1 = [4, 8, 2, 10, 15, 18]

li2 = Cloning(li1)

print("Original List:", li1)

print("After Cloning:", li2)  
  
---  
  
 __

 __

Output:

    
        Original List: [4, 8, 2, 10, 15, 18]
    After Cloning: [4, 8, 2, 10, 15, 18]

  6.  **Using the append() method**  
This can be used for appending and adding elements to list or copying them to
a new list. It is used to add elements to the last position of list. This
takes around 0.325 seconds to complete and is the slowest method of cloning.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to clone or copy a list

# Using append()

def Cloning(li1):

 li_copy =[]

 for item in li1: li_copy.append(item)

 return li_copy

 

# Driver Code

li1 = [4, 8, 2, 10, 15, 18]

li2 = Cloning(li1)

print("Original List:", li1)

print("After Cloning:", li2)  
  
---  
  
 __

 __

Output:

    
        Original List: [4, 8, 2, 10, 15, 18]
    After Cloning: [4, 8, 2, 10, 15, 18]

  7.  **Using the copy() method**  
The inbuilt method copy is used to copy all the elements from one list to
another. This takes around 1.488 seconds to complete.  
Example:

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to clone or copy a list

# Using bilt-in method copy()

def Cloning(li1):

 li_copy =[]

 li_copy = li1.copy()

 return li_copy

 

# Driver Code

li1 = [4, 8, 2, 10, 15, 18]

li2 = Cloning(li1)

print("Original List:", li1)

print("After Cloning:", li2)  
  
---  
  
 __

 __

Output:

    
        Original List: [4, 8, 2, 10, 15, 18]
    After Cloning: [4, 8, 2, 10, 15, 18]

  8.  **Using the method of Deep Copy**  
This method of copying is well explained in the article Deep Copy. This takes
around 10.59 seconds to complete and is the slowest method of cloning.

Referred to Stack Overflow.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

