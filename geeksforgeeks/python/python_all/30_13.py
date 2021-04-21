Python – Sort words separated by Delimiter



Given string of words separated by some delimiter. The task is to sort all the
words given in the string

    
    
     **Input** : test_str = 'gfg:is:best:for:geeks', delim = "*" 
    **Output** : best*for*geeks*gfg*is 
    **Explanation** : Words sorted after separated by delim.
    
    **Input** : test_str = 'gfg:is:best', delim = "*" 
    **Output** : best*gfg*is 
    **Explanation** : Words sorted after separated by delim. 

**Method: Using sorted() + join() + split()**

The combination of the above functions can be used to solve this problem. In
this, we segregate all the words by a particular delimiter using split(), and
convert to list, then perform the sort of words, then reconvert to string
attaching by the same delimiter.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort words seperated by Delimiter

# Using split() + join() + sorted()

 

# initializing string

test_str = 'gfg:is:best:for:geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing Delimiter

delim = ":"

 

# joining the sorted string after split

res = delim.join(sorted(test_str.split(':')))

 

# printing result 

print("The sorted words : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : gfg:is:best:for:geeks
    The sorted words : best:for:geeks:gfg:is
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

