Counting number of unique values in a Python list



Let us see how to count the number of unique values in a Python list.  
 **Examples :**

    
    
    **Input :** 10 20 10 30 40 40
    **Output :** 2
    **Explanation :** Only 2 elements, 20 and 30 are unique in the list.
    
    **Input :** 'geeks' 'for' 'geeks'
    **Output :** 1
    

**Approach 1 :** Traversing the list and counting the frequrency of each
element using dictionary, finally counting the elements for which the
frequency is 1.

 __

 __  
 __

 __

 __  
 __  
 __

# function to count the unique elements

def count_unique(my_list):

 

 # variable to store the unique count

 count = 0

 

 # creating dictionary to count frequency

 freq = {}

 

 # traversing the list

 for x in my_list:

 if (x in freq):

 freq[x] += 1

 else:

 freq[x] = 1

 

 # traversing the dictionary

 for key, value in freq.items():

 if value == 1:

 count += 1

 

 # displaying the count of unique elements

 print(count)

 

# driver function

if __name__ == "__main__":

 

 my_list = [10, 20, 10, 30, 40, 40]

 count_unique(my_list)

 

 my_list = ['geeks', 'for', 'geeks']

 count_unique(my_list)  
  
---  
  
 __

 __

 **Output :**

    
    
    2
    1
    

**Time complexity :** O(N)  
 **Space complexity :** O(N)

 **Approach 2 :** Here we will be using the get() method of the dictionary
class to count the frequency. This makes the program shorter and demonstrates
how get() method is useful instead of if…else.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# function to count the unique elements

def count_unique(my_list):

 

 # variable to store the unique count

 count = 0

 

 # creating dictionary to count frequency

 freq = {}

 

 # traversing the list

 for x in my_list:

 freq[x] = freq.get(x, 0) + 1

 

 # traversing the dictionary

 for key, value in freq.items():

 if value == 1:

 count += 1

 

 # displaying the count of unique elements

 print(count)

 

# driver function

if __name__ == "__main__":

 

 my_list = [10, 20, 10, 30, 40, 40]

 count_unique(my_list)

 

 my_list = ['geeks', 'for', 'geeks']

 count_unique(my_list)  
  
---  
  
 __

 __

 **Output :**

    
    
    2
    1
    

**Time complexity :** O(N)  
 **Space complexity :** O(N)

 **Approach 3 :** Here we will be using the count() method of the list class
to count the frequency.

 __

 __  
 __

 __

 __  
 __  
 __

# function to count the unique elements

def count_unique(my_list):

 

 # variable to store the unique count

 count = 0

 

 # creating dictionary to count frequency

 freq = {}

 

 # traversing the list

 for x in my_list:

 freq[x] = my_list.count(x)

 

 # traversing the dictionary

 for key, value in freq.items():

 if value == 1:

 count += 1

 

 # displaying the count of unique elements

 print(count)

 

# driver function

if __name__ == "__main__":

 

 my_list = [10, 20, 10, 30, 40, 40]

 count_unique(my_list)

 

 my_list = ['geeks', 'for', 'geeks']

 count_unique(my_list)  
  
---  
  
 __

 __

 **Output :**

    
    
    2
    1
    

**Time complexity :** O(N)  
 **Space complexity :** O(N)

 **Approach 4 :** Here we will be using the Counter() method of the
collections module to count the frequency.

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import collections

 

# function to count the unique elements

def count_unique(my_list):

 

 # variable to store the unique count

 count = 0

 

 # creating dictionary to count frequency

 freq = collections.Counter(my_list)

 

 # traversing the dictionary

 for key, value in freq.items():

 if value == 1:

 count += 1

 

 # displaying the count of unique elements

 print(count)

 

# driver function

if __name__ == "__main__":

 

 my_list = [10, 20, 10, 30, 40, 40]

 count_unique(my_list)

 

 my_list = ['geeks', 'for', 'geeks']

 count_unique(my_list)  
  
---  
  
 __

 __

 **Output :**

    
    
    2
    1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

