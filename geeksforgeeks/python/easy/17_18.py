Python | Removing unwanted characters from string



The generic problem faced by the programmers is removing a character from the
entire string. But sometimes the requirement is way above and demands the
removal of more than 1 character, but a list of such malicious characters.
These can be in the form of special characters for reconstructing valid
passwords and many other applications possible. Let’s discuss certain ways to
perform this particular task.  
 **Method #1 : Using replace()**  
One can use replace() inside a loop to check for a bad_char and then replace
it with the empty string hence removing it. This is the most basic approach
and inefficient on a performance point of view.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removal of bad_chars

# using replace()

# initializing bad_chars_list

bad_chars = [';', ':', '!', "*"]

# initializing test string

test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"

# printing original string

print ("Original String : " + test_string)

# using replace() to

# remove bad_chars

for i in bad_chars :

 test_string = test_string.replace(i, '')

# printing resultant string

print ("Resultant list is : " + str(test_string))  
  
---  
  
 __

 __

 **Output :**  

    
    
    Original String : Ge;ek*s:fo!r;Ge*e*k:s!
    Resultant list is : GeeksforGeeks
    
    
    
    

**Method #2 : Using join() + generator**  
By using join() we remake the string. In generator function, we specify the
logic to ignore the characters in bad_chars and hence constructing new string
free from bad characters.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removal of bad_chars

# using join() + generator

# initializing bad_chars_list

bad_chars = [';', ':', '!', "*"]

# initializing test string

test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"

# printing original string

print ("Original String : " + test_string)

# using join() + generator to

# remove bad_chars

test_string = ''.join(i for i in test_string if not i in
bad_chars)

# printing resultant string

print ("Resultant list is : " + str(test_string))  
  
---  
  
 __

 __

 **Output :**  

    
    
    Original String : Ge;ek*s:fo!r;Ge*e*k:s!
    Resultant list is : GeeksforGeeks
    
    
    
    

**Method #3 : Using translate()**  
The most elegant way to perform this particular task, this method is basically
used for achieving the solution to these kind of problems itself, we can
translate each bad_char to empty string and get filtered string.  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removal of bad_chars

# using translate()

import string

# initializing bad_chars_list

bad_chars = [';', ':', '!', "*"]

# initializing test string

test_string = "Ge;ek * s:fo ! r;Ge * e*k:s !"

# printing original string

print ("Original String : " + test_string)

# using translate() to

# remove bad_chars

delete_dict = {sp_character: '' for sp_character in
string.punctuation}

delete_dict[' '] = ''

table = str.maketrans(delete_dict)

test_string = test_string.translate(table)

# printing resultant string

print ("Resultant list is : " + str(test_string))  
  
---  
  
 __

 __

 **Output :**  

    
    
    Original String : Ge;ek*s:fo!r;Ge*e*k:s!
    Resultant list is : GeeksforGeeks
    
    
    
    

**Method #4 : Using filter()**  
This is yet another solution to perform this task. Using the lambda function,
filter function can remove all the bad_chars and return the wanted refined
string.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# removal of bad_chars

# using filter()

# initializing bad_chars_list

bad_chars = [';', ':', '!', "*"]

# initializing test string

test_string = "Ge;ek*s:fo!r;Ge*e*k:s!"

# printing original string

print("Original String : " + test_string)

# using filter() to

# remove bad_chars

test_string = ''.join((filter(lambda i: i not in bad_chars,
test_string)))

# printing resultant string

print("Resultant list is : " + str(test_string))  
  
---  
  
 __

 __

 **Output :**  

    
    
    Original String : Ge;ek*s:fo!r;Ge*e*k:s!
    Resultant list is : GeeksforGeeks
    
    
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

