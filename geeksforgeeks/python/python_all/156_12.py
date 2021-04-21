Python | Sort list elements by frequency



Given a list containing repeated and non-repeated elements, the task is to
sort the given list on basis of the frequency of elements. Let’s discuss few
methods for the same.

###  **Method #1: Using collections.counter()**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort list by frequency

# of elements

from collections import Counter

ini_list = [1, 2, 3, 4, 4, 5, 5, 5,
5, 7,

 1, 1, 2, 4, 7, 8, 9, 6, 6, 6]

# printing initial ini_list

print ("initial list", str(ini_list))

# sorting on bais of frequency of elements

result = [item for items, c in Counter(ini_list).most_common()

 for item in [items] * c]

# printing final result

print("final list", str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list [1, 2, 3, 4, 4, 5, 5, 5, 5, 7, 1, 1, 2, 4, 7, 8, 9, 6, 6, 6]
    final list [5, 5, 5, 5, 1, 1, 1, 4, 4, 4, 6, 6, 6, 2, 2, 7, 7, 3, 8, 9]

###  
**Method #2: Using iterables**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort list by frequency

# of elements

from collections import Counter

from itertools import repeat, chain

ini_list = [1, 2, 3, 4, 4, 5, 5, 5,
5, 7,

 1, 1, 2, 4, 7, 8, 9, 6, 6, 6]

# printing initial ini_list

print ("initial list", str(ini_list))

# sorting on bais of frequency of elements

result = list(chain.from_iterable(repeat(i, c)

 for i, c in Counter(ini_list).most_common()))

# printing final result

print("final list", str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list [1, 2, 3, 4, 4, 5, 5, 5, 5, 7, 1, 1, 2, 4, 7, 8, 9, 6, 6, 6]
    final list [5, 5, 5, 5, 1, 1, 1, 4, 4, 4, 6, 6, 6, 2, 2, 7, 7, 3, 8, 9]

###  
**Method #3: Using sorted**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort list by frequency

# of elements

ini_list = [1, 1, 2, 2, 2, 3, 3, 3,
3, 3,

 5, 5, 5, 4, 4, 4, 4, 4, 4]

# printing initial ini_list

print ("initial list", str(ini_list))

# sorting on bais of frequency of elements

result = sorted(ini_list, key = ini_list.count,

 reverse = True)

# printing final result

print("final list", str(result))  
  
---  
  
 __

 __

 **Output:**

    
    
    initial list [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5, 5, 4, 4, 4, 4, 4, 4]
    final list [4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 5, 5, 5, 1, 1]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

