Python – Add Phrase in middle of String



Given a String, add a phrase in the middle of it.

>  **Input** : test_str = ‘geekforgeeks is for geeks’, mid_str = “good”  
> **Output** : geekforgeeks is good for geeks  
> **Explanation** : Added just in middle, after 2 words.
>
>  **Input** : test_str = ‘geekforgeeks best’, mid_str = “is”  
> **Output** : geekforgeeks is best  
> **Explanation** : Added just in middle, after 1 word.

**Method #1 : Using** **split()** **+** **slicing** **+** **join()**

In this, Strings are converted to a list of words, then the middle position is
extracted to append a new phrase. After addition, the string is back converted
using join().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add Phrase in middle of String

# Using split() + slicing + join()

 

# initializing string

test_str = 'geekforgeeks is for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing mid string

mid_str = "best"

 

# splitting string to list

temp = test_str.split()

mid_pos = len(temp) // 2

 

# appending in mid

res = temp[:mid_pos] + [mid_str] + temp[mid_pos:]

 

# conversion back

res = ' '.join(res)

 

# printing result

print("Formulated String : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geekforgeeks is for geeks
    Formulated String : geekforgeeks is best for geeks
    

**Method #2 : Using split() + slicing + join() [ more compact]**

Similar to the above method, just one-liner way to solve this problem, for
more compact.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add Phrase in middle of String

# Using split() + slicing + join()

 

# initializing string

test_str = 'geekforgeeks is for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing mid string

mid_str = "best"

 

# splitting string to list

temp = test_str.split()

mid_pos = len(temp) // 2

 

# joining and construction using single line

res = ' '.join(temp[:mid_pos] + [mid_str] + temp[mid_pos:])

 

# printing result

print("Formulated String : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original string is : geekforgeeks is for geeks
    Formulated String : geekforgeeks is best for geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

