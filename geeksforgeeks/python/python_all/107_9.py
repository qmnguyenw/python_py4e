Python program to sort a list of tuples alphabetically



Given a list of tuples, write a Python program to sort the tuples
alphabetically by the first item of each tuple.

 **Examples:**

    
    
    **Input:** [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]
    **Output:** [('Amana', 28), ('Abhishek', 29), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]
    
    **Input:** [("aaaa", 28), ("aa", 30), ("bab", 29), ("bb", 21), ("csa", "C")]
    **Output:** [('aa', 30), ('aaaa', 28), ('bab', 29), ('bb', 21), ('csa', 'C')]
    

**Method 1:** Using Bubble sort  
Using the technique of Bubble Sort to we can perform the sorting. Note that
each tuple is an element in the given list. Access the first element of each
tuple using the nested loops. This performs the in-place method of sorting.
The time complexity is similar to the Bubble Sort i.e. O(n^2).

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort a

# list of tuples alphabetically

 

 

# Function to sort the list of

# tuples

 

def SortTuple(tup):

 

 # Getting the length of list 

 # of tuples

 n = len(tup)

 

 for i in range(n):

 for j in range(n-i-1):

 

 if tup[j][0] > tup[j + 1][0]:

 tup[j], tup[j + 1] = tup[j + 1], tup[j]

 

 return tup

 

# Driver's code

 

tup = [("Amana", 28), ("Zenat", 30), ("Abhishek",
29),

 ("Nikhil", 21), ("B", "C")]

 

print(SortTuple(tup))  
  
---  
  
 __

 __

 **Output:**

    
    
    [('Abhishek', 29), ('Amana', 28), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]
    

**Method 2:** Using sort() method  
While sorting via this method the actual content of the tuple is changed, and
just like the previous method, the in-place method of the sort is performed.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort a list of

# tuples using sort() 

 

# Function to sort the list

def SortTuple(tup): 

 

 # reverse = None (Sorts in Ascending order) 

 # key is set to sort using first element of 

 # sublist lambda has been used 

 tup.sort(key = lambda x: x[0]) 

 return tup 

 

# Driver's code

 

tup = [("Amana", 28), ("Zenat", 30), ("Abhishek",
29),

 ("Nikhil", 21), ("B", "C")]

 

print(SortTuple(tup))  
  
---  
  
 __

 __

 **Output:**

    
    
    [('Abhishek', 29), ('Amana', 28), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]
    

**Method 3:** Using sorted() method

sorted() method is a method of list class that returns the sorted list
without making any changes to the original list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort a list of

# tuples using sorted() 

 

# Function to sort the list

def Sort_Tuple(tup): 

 

 # reverse = None (Sorts in Ascending order) 

 # key is set to sort using first element of 

 # sublist lambda has been used 

 return(sorted(tup, key = lambda x: x[0])) 

 

# Driver Code 

tup = [("Amana", 28), ("Zenat", 30), ("Abhishek",
29),

 ("Nikhil", 21), ("B", "C")]

 

# printing the sorted list of tuples 

print(Sort_Tuple(tup))   
  
---  
  
__

__

**Output:**

    
    
    [('Abhishek', 29), ('Amana', 28), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

