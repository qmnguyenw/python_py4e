Find all the co binary numbers in the given range.



Find the number of co-binary palindromes existing between m and n. A co-binary
palindrome is a number in which both, the decimal number and its binary
conversion are a palindrome.

 **Examples:**

    
    
    **Input:** starting number : 300, last number: 315
    
    **Output : 313**
    

**Code: Python code to find all the co binary numbers in the given range**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code for co-binary palindromes

 

def convert_into_binary(number):

 return bin(number).replace("0b","")

 

def reverse_it(number):

 number = str(number)

 return number[::-1]

 

def is_palindrome(number):

 if number == int(reverse_it(number)) :

 return True

 else:

 return False

 

# starting number

m = 300

 

# ending number

n = 1000

bin_pals = []

 

for i in range(m,n+1):

 if is_palindrome(i) == True and is_palindrome(

 int(convert_into_binary(i))):

 

 bin_pals.append(i)

 

print(bin_pals)  
  
---  
  
 __

 __

 **Output :**

    
    
    [313, 585, 717]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

