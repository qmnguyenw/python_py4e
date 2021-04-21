Python | Find k longest words in given list



Given a list of words and a positive integer K, write a Python program to find
k longest words in the list in descending order of length.

 **Examples:**

    
    
    **Input :** lst  = ['am', 'watermelon', 'girl', 'boy', 'colour'], K = 3
    **Output :** ['watermelon', 'colour', 'girl']
    
    **Input :** ['see', 'I', 'geek', 'on', 'brain'], K = 4
    **Output :** ['brain', 'geek', 'see', 'on']
    

  
**Method #1 :** Using _count()_ from _itertools_

First, sort the ‘lst’ based on length of the words and then based on a counter
variable, so that words occurring later gets higher priority and thus, extract
k variables.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find

# longest K words in a list

from itertools import count

 

def longest_word(lst, K):

 cnt = count()

 return sorted(lst, key = lambda w : (len(w), next(cnt)),


 reverse = True)[:K]

 

# Driver code

lst = ['am', 'watermelon', 'girl', 'boy', 'colour']

K = 3

print(longest_word(lst, K))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    ['watermelon', 'colour', 'girl']
    

