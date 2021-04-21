List Methods in Python | Set 1 (in, not in, len(), min(), max()…)



List basics have been covered in python in the set below

Data Types-List, Tuples and Iterations

List methods are discussed in this articles.

 **1\. “in” operator** :- This operator is used to **check if an element is
present** in the list or not. Returns true if element is present in list else
returns false.

 **2\. “not in” operator** :- This operator is used to **check if an element
is not present** in the list or not. Returns true if element is not present in
list else returns false.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# "in" and "not in" 

# initializing list

lis = [1, 4, 3, 2, 5]

 

# checking if 4 is in list using "in"

if 4 in lis:

 print ("List is having element with value 4")

else : print ("List is not having element with value 4")

 

# checking if 4 is not list using "not in"

if 4 not in lis:

 print ("List is not having element with value 4")

else : print ("List is having element with value 4")  
  
---  
  
 __

 __

Output:

    
    
    List is having element with value 4
    List is having element with value 4
    

**3\. len()** :- This function returns the **length** of list.

 **4\. min()** :- This function returns the **minimum** element of list.

 **5\. max()** :- This function returns the **maximum** element of list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# len(), min() and max()

# initializing list 1

lis = [2, 1, 3, 5, 4]

 

# using len() to print length of list

print ("The length of list is : ", end="")

print (len(lis))

 

# using min() to print minimum element of list

print ("The minimum element of list is : ", end="")

print (min(lis))

 

# using max() to print maximum element of list

print ("The maximum element of list is : ", end="")

print (max(lis))  
  
---  
  
 __

 __

Output:

    
    
    The length of list is : 5
    The minimum element of list is : 1
    The maximum element of list is : 5
    

**6\. “+” operator** :- This operator is used to **concatenate** two lists
into a single list.

 **7\. “*” operator** :- This operator is used to **multiply the list “n”
times** and return the single list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# "+" and "*"

# initializing list 1

lis = [1, 2, 3]

 

# initializing list 2

lis1 = [4, 5, 6]

 

# using "+" to concatenate lists

lis2= lis + lis1

 

# priting concatenated lists

print ("list after concatenation is : ", end="")

for i in range(0,len(lis2)):

 print (lis2[i], end=" ")

 

print ("\r")

 

#using '*' to combine lists 

lis3 = lis * 3

 

# priting combined lists

print ("list after combining is : ", end="")

for i in range(0,len(lis3)):

 print (lis3[i], end=" ")  
  
---  
  
 __

 __

Output:

  

  

    
    
    list after concatenation is : 1 2 3 4 5 6 
    list after combining is : 1 2 3 1 2 3 1 2 3 
    

**8\. index(ele, beg, end)** :- This function returns the **index of first
occurrence of element** after beg and before end.

 **9\. count()** :- This function counts the **number of occurrences** of
elements in list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# index() and count()

# initializing list 1

lis = [2, 1, 3, 5, 4, 3]

 

# using index() to print first occurrence of 3

# prints 5

print ("The first occurrence of 3 after 3rd position is : ",
end="")

print (lis.index(3, 3, 6))

 

# using count() to count number of occurrence of 3

print ("The number of occurrences of 3 is : ", end="")

print (lis.count(3))  
  
---  
  
 __

 __

Output:

    
    
    The first occurrence of 3 after 3rd position is : 5
    The number of occurrences of 3 is : 2
    

**Related articles:**  
List methods in Python  
List Methods in Python | Set 2 (del, remove(), sort(), insert(), pop(),
extend()…)

This article is contributed by **Manjeet Singh** .If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

