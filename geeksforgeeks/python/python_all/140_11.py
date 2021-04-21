Python | Check possible bijection between sequence of characters and digits



Given a string ‘char_seq'(sequence of characters) and a positive integer
‘dig_seq'(sequence of digits), Write a Python program to find possible
bijection or one-one onto relationship between ‘char_seq’ and ‘dig_seq’ such
that each character matches to one and only one digit.

 **Examples:**

    
    
    **Input :** char_seq = 'bxdyxb'
            dig_seq = 123421
    **Output :** True
    
    **Input :** char_seq = 'bxdyxb'
            dig_seq = 123321
    **Output :** False
    

  
**Method #1 :** Using _zip_ method

This method simply zips the ‘char_seq’ and ‘dig_seq’ and checks if
corresponding digits and characters matches or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Check possible bijection

# between sequence of characters and digits

 

def is_bijection(char_seq, dig_seq):

 z = zip(str(char_seq), str(dig_seq))

 res = all(

 (z1[0] == z2[0]) == (z1[1] == z2[1])
for z1 in z for z2 in z)

 

 return res

 

# Driver code

char_seq = 'bxdyxb'

dig_seq = 123421

print(is_bijection(char_seq, dig_seq))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    True
    

