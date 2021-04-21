Sorted() function in Python



Sorting any sequence is very easy in Python using built-in method sorted()
which does all the hard work for you.  
Sorted() sorts any sequence (list, tuple) and always returns a list with the
elements in sorted manner, without modifying the original sequence.

 **Syntax :** sorted(iterable, key, reverse)

 **Parameters :** sorted takes three parameters from which two are optional.

  *  _Iterable :_ sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted.
  *  _Key_ (optional) : A function that would server as a key or a basis of sort comparison.
  *  _Reverse_ (optional) : If set true, then the iterable would be sorted in reverse (descending) order, by default it is set as false.

 **Example 1**

 __

 __  
 __

 __

 __  
 __  
 __

x= [2, 8, 1, 4, 6, 3, 7] 

 

print ("Sorted List returned :"), 

print (sorted(x)) 

 

print ("\nReverse sort :"), 

print (sorted(x, reverse = True))

 

print ("\nOriginal list not modified :"), 

print (x)   
  
---  
  
__

__

    
    
    **Output :**
    Sorted List returned : [1, 2, 3, 4, 6, 7, 8]
    
    Reverse sort : [8, 7, 6, 4, 3, 2, 1]
    
    Original list not modified : [2, 8, 1, 4, 6, 3, 7]
    

**Example 2 : Sorting different data types**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# List

x = ['q', 'w', 'r', 'e', 't', 'y']

print (sorted(x))

 

# Tuple

x = ('q', 'w', 'e', 'r', 't', 'y')

print (sorted(x))

 

# String-sorted based on ASCII translations

x = "python"

print (sorted(x))

 

# Dictionary

x = {'q':1, 'w':2, 'e':3, 'r':4,
't':5, 'y':6}

print (sorted(x))

 

# Set

x = {'q', 'w', 'e', 'r', 't', 'y'}

print (sorted(x))

 

# Frozen Set

x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))

print (sorted(x))  
  
---  
  
 __

 __

    
    
     **Output :**
    ['e', 'q', 'r', 't', 'w', 'y']
    ['e', 'q', 'r', 't', 'w', 'y']
    ['h', 'n', 'o', 'p', 't', 'y']
    ['e', 'q', 'r', 't', 'w', 'y']
    ['e', 'q', 'r', 't', 'w', 'y']
    ['e', 'q', 'r', 't', 'w', 'y']
    

**Custom Sorting using the key parameter**  
sorted() function has an optional parameter called ‘key’ which takes a
function as its value. This key function transforms each element before
sorting, it takes the value and returns 1 value which is then used within sort
instead of the original value.

For example, if we pass a list of strings in sorted(), it gets sorted
alphabetically . But if we specify key = len, i.e. give len function as key,
then the strings would be passed to len, and the value it returns, i.e. the
length of strings will be sorted. Which means that the strings would be sorted
based on their lengths instead

 __

 __  
 __

 __

 __  
 __  
 __

L= ["cccc", "b", "dd", "aaa"]

 

print ("Normal sort :", sorted(L))

 

print ("Sort with len :", sorted(L, key = len))  
  
---  
  
 __

 __

    
    
     **Output :**
    Normal sort : ['aaa', 'b', 'cccc', 'dd']
    Sort with len : ['b', 'dd', 'aaa', 'cccc']
    

**Key also takes user-defined functions as its value for the basis of
sorting.**

 __

 __  
 __

 __

 __  
 __  
 __

# Sort a list of integers based on

# their remainder on dividing from 7

 

def func(x):

 return x % 7

 

L = [15, 3, 11, 7]

 

print ("Normal sort :", sorted(L))

print ("Sorted with key:", sorted(L, key = func))  
  
---  
  
 __

 __

    
    
     **Output :**
    Normal sort : [3, 7, 11, 15]
    Sorted with key: [7, 15, 3, 11]
    

This article is contributed by **Harshit Agrawal**. If you like GeeksforGeeks
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

