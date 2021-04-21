Counters in Python | Set 2 (Accessing Counters)



Counters in Python | Set 1 (Initialization and Updation)

Once initialized, counters are accessed just like dictionaries. Also, it does
not raise the KeyValue error (if key is not present) instead the value’s count
is shown as 0.

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate accessing of

# Counter elements

from collections import Counter

 

# Create a list

z = ['blue', 'red', 'blue', 'yellow', 'blue',
'red']

col_count = Counter(z)

print(col_count)

 

col = ['blue','red','yellow','green']

 

# Here green is not in col_count 

# so count of green will be zero

for color in col:

 print (color, col_count[color])  
  
---  
  
 __

 __

 **Output:  
**

    
    
    Counter({'blue': 3, 'red': 2, 'yellow': 1})
    blue 3
    red 2
    yellow 1
    green 0
    

**elements() :**  
The elements() method returns an iterator that produces all of the items known
to the Counter.  
Note : Elements with count <= 0 are not included.

  

  

 **Example :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python example to demonstrate elements() on

# Counter (gives back list)

from collections import Counter

 

coun = Counter(a=1, b=2, c=3)

print(coun)

 

print(list(coun.elements()))  
  
---  
  
 __

 __

 **Output :**

    
    
    Counter({'c': 3, 'b': 2, 'a': 1})
    ['a', 'b', 'b', 'c', 'c', 'c']
    

**most_common() :**  
most_common() is used to produce a sequence of the n most frequently
encountered input values and their respective counts.

 __

 __  
 __

 __

 __  
 __  
 __

# Python example to demonstrate most_elements() on

# Counter

from collections import Counter

 

coun = Counter(a=1, b=2, c=3, d=120, e=1,
f=219)

 

# This prints 3 most frequent characters

for letter, count in coun.most_common(3):

 print('%s: %d' % (letter, count))  
  
---  
  
 __

 __

 **  
Output :**

    
    
    f: 219
    d: 120
    c: 3
    

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

