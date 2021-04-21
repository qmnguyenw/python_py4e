Binary Search (bisect) in Python



Binary Search is a technique used to search element in a sorted list. In this
article, we will looking at library functions to do Binary Search.

 **Finding first occurrence of an element.**

> bisect.bisect_left(a, x, lo=0, hi=len(a)) : Returns leftmost insertion point
> of x in a sorted list. Last two parameters are optional, they are used to
> search in sublist.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working

# of binary search in library

from bisect import bisect_left

 

def BinarySearch(a, x):

 i = bisect_left(a, x)

 if i != len(a) and a[i] == x:

 return i

 else:

 return -1

 

a = [1, 2, 4, 4, 8]

x = int(4)

res = BinarySearch(a, x)

if res == -1:

 print(x, "is absent")

else:

 print("First occurrence of", x, "is present at", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    First occurrence of 4 is present at 2
    

**Finding greatest value smaller than x.**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working

# of binary search in library

from bisect import bisect_left

 

def BinarySearch(a, x):

 i = bisect_left(a, x)

 if i:

 return (i-1)

 else:

 return -1

 

# Driver code

a = [1, 2, 4, 4, 8]

x = int(7)

res = BinarySearch(a, x)

if res == -1:

 print("No value smaller than ", x)

else:

 print("Largest value smaller than ", x, " is at index ", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    Largest value smaller than  7  is at index  3
    

**Finding rightmost occurrence**

> bisect.bisect_right(a, x, lo=0, hi=len(a)) Returns rightmost insertion point
> of x in a sorted list a. Last two parameters are optional, they are used to
> search in sublist.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working

# of binary search in library

from bisect import bisect_right

 

def BinarySearch(a, x):

 i = bisect_right(a, x)

 if i != len(a)+1 and a[i-1] == x:

 return (i-1)

 else:

 return -1

 

a = [1, 2, 4, 4]

x = int(4)

res = BinarySearch(a, x)

if res == -1:

 print(x, "is absent")

else:

 print("Last occurrence of", x, "is present at", res)  
  
---  
  
 __

 __

 **Output:**

    
    
    Last occurrence of 4 is present at 3
    

Please refer Binary Search for writing your own Binary Search code.

 **Reference :**  
https://docs.python.org/3/library/bisect.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

