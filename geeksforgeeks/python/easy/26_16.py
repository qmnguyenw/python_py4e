Remove all duplicates from a given string in Python



We are given a string and we need to remove all duplicates from it? What will
be the output if the order of character matters?  
Examples:

    
    
    Input : geeksforgeeks
    Output : efgkos
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Remove all duplicates from a
given string.  
 **Method 1:**

 __

 __  
 __

 __

 __  
 __  
 __

from collections import OrderedDict 

 

# Function to remove all duplicates from string 

# and order does not matter 

def removeDupWithoutOrder(str): 

 

 # set() --> A Set is an unordered collection 

 # data type that is iterable, mutable, 

 # and has no duplicate elements. 

 # "".join() --> It joins two adjacent elements in 

 # iterable with any symbol defined in 

 # "" ( double quotes ) and returns a 

 # single string 

 return "".join(set(str)) 

 

# Function to remove all duplicates from string 

# and keep the order of characters same 

def removeDupWithOrder(str): 

 return "".join(OrderedDict.fromkeys(str)) 

 

# Driver program 

if __name__ == "__main__": 

 str = "geeksforgeeks"

 print ("Without Order = ",removeDupWithoutOrder(str)) 

 print ("With Order = ",removeDupWithOrder(str))   
  
---  
  
__

__

Output:

    
    
    Without Order =  egfkosr
    With Order    =  geksfor
    

**Method 2:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

def removeDuplicate(str):

 s=set(str)

 s="".join(s)

 print("Without Order:",s)

 t=""

 for i in str:

 if(i in t):

 pass

 else:

 t=t+i

 print("With Order:",t)

 

str="geeksforgeeks"

removeDuplicate(str)  
  
---  
  
 __

 __

 **Output:**

    
    
    Without Order: rofgeks
    With Order: geksfor

 **What do OrderedDict and fromkeys() do ?**

An OrderedDict is a dictionary that remembers the order of the keys that were
inserted first. If a new entry overwrites an existing entry, the original
insertion position is left unchanged.

For example see below code snippet :

 __

 __  
 __

 __

 __  
 __  
 __

from collections import OrderedDict

 

ordinary_dictionary = {}

ordinary_dictionary['a'] = 1

ordinary_dictionary['b'] = 2

ordinary_dictionary['c'] = 3

ordinary_dictionary['d'] = 4

ordinary_dictionary['e'] = 5

 

# Output = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}

print (ordinary_dictionary) 

 

ordered_dictionary = OrderedDict()

ordered_dictionary['a'] = 1

ordered_dictionary['b'] = 2

ordered_dictionary['c'] = 3

ordered_dictionary['d'] = 4

ordered_dictionary['e'] = 5

 

# Output = {'a':1,'b':2,'c':3,'d':4,'e':5}

print (ordered_dictionary)   
  
---  
  
__

__

**fromkeys()** creates a new dictionary with keys from seq and values set to
value and returns list of keys, **fromkeys(seq[, value])** is the syntax for
fromkeys() method.

 ** _Parameters :_**

  *  **seq :** This is the list of values which would be used for dictionary keys preparation.
  *  **value :** This is optional, if provided then value would be set to this value.

For example see below code snippet :

 __

 __  
 __

 __

 __  
 __  
 __

from collections import OrderedDict

seq = ('name', 'age', 'gender')

dict = OrderedDict.fromkeys(seq)

 

# Output = {'age': None, 'name': None, 'gender': None}

print (str(dict)) 

dict = OrderedDict.fromkeys(seq, 10)

 

# Output = {'age': 10, 'name': 10, 'gender': 10}

print (str(dict))   
  
---  
  
__

__

This article is contributed by **Shashank Mishra (Gullu)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

