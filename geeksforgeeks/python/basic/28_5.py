Counters in Python | Set 1 (Initialization and Updation)



 **Counter** is a **container** included in the collections module. Now you
all must be wondering what is a container. Don’t worry first let’s discuss
about the container.

## What is Container?

Containers are objects that hold objects. They provide a way to access the
contained objects and iterate over them. Examples of built in containers are
Tuple, list, and dictionary. Others are included in Collections module.

A Counter is a subclass of dict. Therefore it is an unordered collection where
elements and their respective count are stored as a dictionary. This is
equivalent to a bag or multiset of other languages.

 **Syntax :**

    
    
    class collections.Counter([iterable-or-mapping])

 **Initialization :**  
The constructor of counter can be called in any one of the following ways :

  

  

* With sequence of items
* With dictionary containing keys and counts
* With keyword arguments mapping string names to counts

 **Example of each type of initialization :**

 __

 __  
 __

 __

 __  
 __  
 __

# A Python program to show different ways to create

# Counter

from collections import Counter

 

# With sequence of items 

print(Counter(['B','B','A','B','C','A','B','B','A','C']))

 

# with dictionary

print(Counter({'A':3, 'B':5, 'C':2}))

 

# with keyword arguments

print(Counter(A=3, B=5, C=2))  
  
---  
  
 __

 __

 **Output of all the three lines is same :**

    
    
    Counter({'B': 5, 'A': 3, 'C': 2})
    Counter({'B': 5, 'A': 3, 'C': 2})
    Counter({'B': 5, 'A': 3, 'C': 2})
    

**Updation :**  
We can also create an empty counter in the following manner :

    
    
    coun = collections.Counter()
    

And can be updated via update() method .Syntax for the same :

    
    
    coun.update(Data)
    

__

__  
__

__

__  
__  
__

# A Python program to demonstrate update()

from collections import Counter

coun = Counter()

 

coun.update([1, 2, 3, 1, 2, 1, 1, 2])

print(coun)

 

coun.update([1, 2, 4])

print(coun)  
  
---  
  
 __

 __

 **Output :**

    
    
    Counter({1: 4, 2: 3, 3: 1})
    Counter({1: 5, 2: 4, 3: 1, 4: 1})
    

  * Data can be provided in any of the three ways as mentioned in initialization and the counter’s data will be increased not replaced.
  * Counts can be zero and negative also.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate that counts in

# Counter can be 0 and negative

from collections import Counter

 

c1 = Counter(A=4, B=3, C=10)

c2 = Counter(A=10, B=3, C=4)

 

c1.subtract(c2)

print(c1)  
  
---  
  
 __

 __

 **Output :**

    
         Counter({'c': 6, 'B': 0, 'A': -6})

  * We can use Counter to count distinct elements of a list or other collections.

 __

 __  
 __

 __

 __  
 __  
 __

# An example program where different list items are

# counted using counter

from collections import Counter

 

# Create a list

z = ['blue', 'red', 'blue', 'yellow', 'blue',
'red']

 

# Count distinct elements and print Counter aboject

print(Counter(z))  
  
---  
  
 __

 __

 **Output:**

    
    
    Counter({'blue': 3, 'red': 2, 'yellow': 1})
    

This article is contributed by **Mayank Rawat** .If you like GeeksforGeeks and
would like to contribute, you can also write an article using
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

