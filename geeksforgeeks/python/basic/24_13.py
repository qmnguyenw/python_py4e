chr() in Python



The **chr()** method returns a string representing a character whose Unicode
code point is an integer.  
 **Syntax:**

    
    
    **chr(num)**
    **num :** integer value
    

  * The chr() method takes only one integer as argument.
  * The range may vary from 0 to 1,1141,111(0x10FFFF in base 16).
  * The chr() method returns a character whose unicode point is num, an integer.
  * If an integer is passed that is outside the range then the method returns a ValueError.

Example: Suppose we want to print ‘G e e k s f o r G e e k s’.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# chr() builtin function

 

print(chr(71), chr(101),

chr(101), chr(107),

chr(115), chr(32),

chr(102), chr(111),

chr(114),chr(32),

chr(71), chr(101),

chr(101), chr(107), 

chr(115))  
  
---  
  
 __

 __

Output:

    
    
    G e e k s   f o r   G e e k s
    

Another example :

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# chr() builtin function

 

numbers = [17, 38, 79]

 

for number in numbers:

 

 # Convert ASCII-based number to character.

 letter = chr(number)

 print("Character of ASCII value", number, "is ", letter)  
  
---  
  
 __

 __

Output:

  

  

    
    
    Character of ASCII value 17 is  
    Character of ASCII value 38 is  &
    Character of ASCII value 79 is  O

 **What happens if we give something out of range?**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# chr() builtin function

# if value given is 

# out of range

 

# Convert ASCII-based number to character

print(chr(400))  
  
---  
  
 __

 __

Output:

    
    
    No Output
    

We wont get any output and the compiler will throw an error:

    
    
    Traceback (most recent call last):
      File "/home/484c76fb455a624cc137946a244a9aa5.py", line 1, in 
        print(chr(400))
    UnicodeEncodeError: 'ascii' codec can't encode character 
    '\u0190' in position 0: ordinal not in range(128)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

