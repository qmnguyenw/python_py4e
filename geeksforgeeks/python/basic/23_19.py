Find the k most frequent words from data set in Python



Given the data set, we can find k number of most frequent words.

The solution of this problem already present as Find the k most frequent words
from a file. But we can solve this problem very efficiently in Python with the
help of some high performance modules.

In order to do this, we’ll use a high performance data type module, which is
**collections**. This module got some specialized container datatypes and we
will use **counter** class from this module.  
  
Examples :

    
    
    Input : "John is the son of John second. 
             Second son of John second is William second."
    Output : [('second', 4), ('John', 3), ('son', 2), ('is', 2)]
    
    **Explanation :**
    1. The string will converted into list like this :
        ['John', 'is', 'the', 'son', 'of', 'John', 
         'second', 'Second', 'son', 'of', 'John', 
         'second', 'is', 'William', 'second']
    2. Now 'most_common(4)' will return four most 
       frequent words and its count in tuple. 
    
    
    Input : "geeks for geeks is for geeks. By geeks
             and for the geeks."
    Output : [('geeks', 5), ('for', 3)]
    
    **Explanation :**
    most_common(2) will return two most frequent words and their count.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach :**

    
          1.  Import Counter class from collections module.
      2. Split the string into list using split(), it will
    return the lists of words. 
      3. Now pass the list to the instance of Counter class
      4. The function 'most-common()' inside Counter will return
    the list of most frequent words from list and its count.
    
    

Below is Python implementation of above approach :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the k most frequent words

# from data set

from collections import Counter

 

data_set = "Welcome to the world of Geeks " \

"This portal has been created to provide well written well" \

"thought and well explained solutions for selected questions " \

"If you like Geeks for Geeks and would like to contribute " \

"here is your chance You can write article and mail your article " \

" to contribute at geeksforgeeks org See your article appearing on " \

"the Geeks for Geeks main page and help thousands of other Geeks. " \

 

# split() returns list of all the words in the string

split_it = data_set.split()

 

# Pass the split_it list to instance of Counter class.

Counter = Counter(split_it)

 

# most_common() produces k frequently encountered

# input values and their respective counts.

most_occur = Counter.most_common(4)

 

print(most_occur)  
  
---  
  
 __

 __

Output :

    
    
    [('Geeks', 5), ('to', 4), ('and', 4), ('article', 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

