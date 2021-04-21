Python program to Sort a List of Tuples in Increasing Order by the Last
Element in Each Tuple



The task is to write a Python Program to sort a list of tuples in increasing
order by the last element in each tuple.

    
    
     **Input:** [(1, 3), (3, 2), (2, 1)]
    **Output:** [(2, 1), (3, 2), (1, 3)]
    **Explanation:** sort tuple based on the last digit of each tuple.
    

**Methods #1:** Using sorted().

Sorted() method sorts a list and always returns a list with the elements in a
sorted manner, without modifying the original sequence.

 **Approach:**

  * Take a list of tuples from the user.
  * Define a function that returns the last element of each tuple in the list of tuples.
  * Define another function with the previous function as the key and sort the list.
  * Print the sorted list.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

def last(n):

 return n[-1] 

 

def sort(tuples):

 return sorted(tuples, key=last)

 

a=[(1, 3), (3, 2), (2, 1)]

print("Sorted:")

print(sort(a))  
  
---  
  
 __

 __

