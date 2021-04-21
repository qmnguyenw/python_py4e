Python – Expand Character Frequency String



Given a string, which character followed by its frequency, create the
appropriate string.

 **Examples:**

>  **Input** : test_str = ‘g7f2g3i2s2b3e4’  
> **Output** : gggggggffgggiissbbbeeee  
> **Explanation** : g is succeeded by 7 and repeated 7 times.
>
>  **Input** : test_str = ‘g1f1g1’  
> **Output** : gfg  
> **Explanation** : f is succeeded by 1 and repeated 1 time.

**Method #1: Using** **zip()** **+** **join()**

  

  

This is one of the ways in which this task can be performed. In this, the task
of joining appropriate characters is done using join() and zip() is used to
convert different frequency and character strings. The drawback is that
frequency of character is restricted to a 1-digit number in this.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Expand Character Frequency String 

# Using join() + zip()

import re

 

# initializing string

test_str = 'g7f2g3i2s2b3e4s5t6'

 

# printing original string

print("The original string is : " + str(test_str))

 

# using zip() to pair up numbers and characters 

# seperately

res = "".join(a *int(b) for a, b in
zip(test_str[0::2], test_str[1::2]))

 

# printing result 

print("The expanded string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : g7f2g3i2s2b3e4s5t6
    The expanded string : gggggggffgggiissbbbeeeessssstttttt
    

**Method #2: Using regex() + join()**

This is yet another way in which this task can be performed. In this task of
pairing numbers and characters to different strings is performed using regex()
and the advantage is that it can take numbers with digits more than 2.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Expand Character Frequency String 

# Using regex() + join()

import re

 

# initializing string

test_str = 'g7f2g3i2s2b3e4s5t10'

 

# printing original string

print("The original string is : " + str(test_str))

 

# using findall to pair up numbers and characters 

# seperately, can include longer digit strings

res = ''.join(chr * int(num or 1) 

 for chr, num in re.findall(r'(\w)(\d+)?', test_str))

 

# printing result 

print("The expanded string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : g7f2g3i2s2b3e4s5t10
    The expanded string : gggggggffgggiissbbbeeeessssstttttttttt
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

