Python – Index Frequency Alphabet List



Create a String list with each character repeated as much as its position
number.

 **Method #1 : Using ascii_lowercase + ord() + loop**

In this, task of getting index is done using ord(), and ascii lowecase() is
used for extracting alphabets. Loop is used to perform task for each letter.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Frequency Alphabet List

# Using ascii_lowercase + ord() + loop

from string import ascii_lowercase

 

# extracting start index

strt_idx = ord('a') - 1

 

res = []

for ele in ascii_lowercase:

 

 # multiplying Frequency

 res.append(ele * (ord(ele) - strt_idx))

 

# printing result 

print("The constructed list : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The constructed list : ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg', 'hhhhhhhh', 'iiiiiiiii', 'jjjjjjjjjj', 'kkkkkkkkkkk', 'llllllllllll', 'mmmmmmmmmmmmm', 'nnnnnnnnnnnnnn', 'ooooooooooooooo', 'pppppppppppppppp', 'qqqqqqqqqqqqqqqqq', 'rrrrrrrrrrrrrrrrrr', 'sssssssssssssssssss', 'tttttttttttttttttttt', 'uuuuuuuuuuuuuuuuuuuuu', 'vvvvvvvvvvvvvvvvvvvvvv', 'wwwwwwwwwwwwwwwwwwwwwww', 'xxxxxxxxxxxxxxxxxxxxxxxx', 'yyyyyyyyyyyyyyyyyyyyyyyyy', 'zzzzzzzzzzzzzzzzzzzzzzzzzz']
    

**Method #2 : Using list comprehension + ascii_lowercase + ord()**

  

  

In this, list comprehension is used to solve this problem. This is shorthand
of above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Frequency Alphabet List

# Using list comprehension + ascii_lowercase + ord()

from string import ascii_lowercase

 

# extracting start index

strt_idx = ord('a') - 1

 

# list comprehension to solve as one liner

res = [ele * (ord(ele) - strt_idx) for ele in
ascii_lowercase]

 

# printing result 

print("The constructed list : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The constructed list : ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', 'ggggggg', 'hhhhhhhh', 'iiiiiiiii', 'jjjjjjjjjj', 'kkkkkkkkkkk', 'llllllllllll', 'mmmmmmmmmmmmm', 'nnnnnnnnnnnnnn', 'ooooooooooooooo', 'pppppppppppppppp', 'qqqqqqqqqqqqqqqqq', 'rrrrrrrrrrrrrrrrrr', 'sssssssssssssssssss', 'tttttttttttttttttttt', 'uuuuuuuuuuuuuuuuuuuuu', 'vvvvvvvvvvvvvvvvvvvvvv', 'wwwwwwwwwwwwwwwwwwwwwww', 'xxxxxxxxxxxxxxxxxxxxxxxx', 'yyyyyyyyyyyyyyyyyyyyyyyyy', 'zzzzzzzzzzzzzzzzzzzzzzzzzz']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

