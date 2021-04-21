Python program to Concatenate all Elements of a List into a String



Given a list, the task is to write a Python program to concatenate all
elements in a list into a string.

 **Examples:**

    
    
     **Input:** ['hello', 'geek', 'have', 'a', 'geeky', 'day']
    **Output:** hello geek have a geeky day
    
    **Input:** ['did', 'u', 'like', 'my', 'article', '?']
    **Output:** did u like my article ?

 **Method 1:** Using join() method

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

l = ['hello', 'geek', 'have',

 'a', '1', 'day']

 

# this will join all the 

# elements of the list with ' '

l = ' '.join(l) 

print(l)  
  
---  
  
 __

 __

 **Output:**

    
    
    hello geek have a 1 day

 **Method 2:** Naive approach

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

l= [ 'hello', 'geek', 'have', 

 'a', 'geeky', 'day']

 

ans = ' '

for i in l: 

 

 # concatenating the strings

 # using + operator

 ans = ans+ ' '+i

 

print(ans)  
  
---  
  
 __

 __

 **Output:**

    
    
    hello geek have a geeky day

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

