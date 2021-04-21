Password validation in Python



Let’s take a password as a combination of alphanumeric characters along with
special characters, and check whether the password is valid or not with the
help of few conditions.

 **Conditions for a valid password are:**

  1. Should have at least one number.
  2. Should have at least one uppercase and one lowercase character.
  3. Should have at least one special symbol.
  4. Should be between 6 to 20 characters long.

    
    
    **Input :**  Geek12#
    **Output :** Password is valid.
    
    **Input :**  asd123
    **Output :** Invalid Password !!

We can check if a given string is eligible to be a password or not using
multiple ways.

 **Method #1:** Naive Method (Without using Regex).

 __

 __  
 __

 __

 __  
 __  
 __

# Password validation in Python

# using naive method

 

# Function to validate the password

def password_check(passwd):

 

 SpecialSym =['$', '@', '#', '%']

 val = True

 

 if len(passwd) < 6:

 print('length should be at least 6')

 val = False

 

 if len(passwd) > 20:

 print('length should be not be greater than 8')

 val = False

 

 if not any(char.isdigit() for char in passwd):

 print('Password should have at least one numeral')

 val = False

 

 if not any(char.isupper() for char in passwd):

 print('Password should have at least one uppercase letter')

 val = False

 

 if not any(char.islower() for char in passwd):

 print('Password should have at least one lowercase letter')

 val = False

 

 if not any(char in SpecialSym for char in passwd):

 print('Password should have at least one of the symbols $@#')

 val = False

 if val:

 return val

 

# Main method

def main():

 passwd = 'Geek12@'

 

 if (password_check(passwd)):

 print("Password is valid")

 else:

 print("Invalid Password !!")

 

# Driver Code 

if __name__ == '__main__':

 main()  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Password is valid
    

