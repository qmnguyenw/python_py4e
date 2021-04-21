Python program to calculate the number of digits and letters in a string



 **Prerequisites:** isnumeric() method – Python

Given a string, containing digits and letters, the task is to write a Python
program to calculate the number of digits and letters in a string. The
following block expresses the basic idea behind it:

    
    
     **Input:** string = "geeks2for3geeks"
    **Output:** total digits = 2 and total letters = 13
    
    **Input:** string = "python1234"
    **Output:** total digits = 4 and total letters = 6
    
    **Input:** string = "co2mpu1te10rs"
    **Output:** total digits = 4 and total letters = 9

####  **First Approach**

The idea here is to solve this problem by iterating through all characters and
check whether character is in all_digits or all_letters.

**Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# define all digits as string

all_digits = ['0', '1', '2', '3', '4', '5',
'6', '7', '8', '9']

 

# define all letters

all_letters = ['a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j', 'k', 'l',

 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']

 

# given string

string = "geeks2for3geeks"

 

# intialized value

total_digits = 0

total_letters = 0

 

# iterate through all characters

for s in string:

 

 # if character found in all_digits then increment total_digits by one

 if s in all_digits:

 total_digits += 1

 

 # if character found in all_letters then increment total_letters by one

 elif s in all_letters:

 total_letters += 1

 

print("Total letters found :-", total_letters)

print("Total digits found :-", total_digits)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Total letters found :- 13
    Total digits found :- 2

####  **Optimized Method**

Instead of checking character in all_letters, we can check:

  * if character is found in all digits, then increment total_digits value by one
  * If not it means characters is a letter, increment total_letters value by one

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# define all digits as string

all_digits = ['0', '1', '2', '3', '4', '5',
'6', '7', '8', '9']

 

# define all letters

all_letters = ['a', 'b', 'c', 'd', 'e', 'f',
'g', 'h', 'i', 'j', 'k', 'l',

 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']

 

# given string

string = "geeks2for3geeks"

 

# intialized value

total_digits = 0

total_letters = 0

 

# iterate through all characters

for s in string:

 

 # if character found in all_digits then increment total_digits by one

 if s in all_digits:

 total_digits += 1

 

 # if character not found in all_digits then increment total_letters by
one

 else:

 total_letters += 1

 

print("Total letters found :-", total_letters)

print("Total digits found :-", total_digits)  
  
---  
  
 __

 __

 **Output:**

    
    
    Total letters found :- 13
    Total digits found :- 2

####  **Second Approach (More Optimized Method)**

The idea here is to solve this problem by iterating through all characters and
check whether character is letter or digits using isnumeric() function. If
isnumeric is True, it means character is digit, else character is a letter.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# given string

string = "python1234"

 

# intialized value

total_digits = 0

total_letters = 0

 

# iterate through all characters

for s in string:

 

 # if character is digit (return True)

 if s.isnumeric():

 total_digits += 1

 

 # if character is letter (return False)

 else:

 total_letters += 1

 

print("Total letters found :-", total_letters)

print("Total digits found :-", total_digits)  
  
---  
  
 __

 __

 **Output:**

    
    
    Total letters found :- 6
    Total digits found :- 4

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

