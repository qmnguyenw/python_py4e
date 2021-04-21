Python | Sort list containing alphanumeric values



Given a list containing both alphanumeric values, write a Python program to
sort the given list in such a way that the alphabetical values always comes
after numeric values.

 **Examples:**

    
    
    **Input :** ['k', 5, 'e', 3, 'g', 7, 0, 't']
    **Output :** [0, 3, 5, 7, 'e', 'g', 'k', 't']
    
    **Input :** [1, 'c', 3, 2, 'a', 'b']
    **Output :** [1, 2, 3, 'a', 'b', 'c']
    

**Approach 1 :** Using _sort()_ method

To use Python sort() method we need to convert all list values to _str_ type
first. Now there are two methods to convert values to string.

  *  **Method #1 :** List comprehension  
Python list comprehension can be simply used to convert each element of list
to string type. We sort it and since all values are now str type, we change
the final list to back to its original form.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Sort list

# containing alpha and numeric values

 

def sort(lst):

 lst = [str(i) for i in lst]

 lst.sort()

 lst = [int(i) if i.isdigit() else i for i in lst
]

 return lst

 

# Driver code

lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']

print(sort(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 3, 5, 7, 'e', 'g', 'k', 't']
    

* **Method #2 :** Using key function

Key function serves as a key for the sort comparison, which is equal to _str_
in our case.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Sort list

# containing alpha and numeric values

def sort(lst):

 

 lst.sort(key = str)

 return lst

 

# Driver code

lst = ['k', 5, 'e', 3, 'g', 7, 0, 't']

print(sort(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 3, 5, 7, 'e', 'g', 'k', 't']
    

