Python | Program to accept the strings which contains all vowels



Given a string, the task is to check if every vowel is present or not. We
consider a vowel to be present if it is present in upper case or lower case.
i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ .  
**Examples :**

    
    
    **Input :** geeksforgeeks
    **Output :** Not Accepted
    All vowels except 'o' are not present
    
    **Input :** ABeeIghiObhkUul
    **Output :** Accepted
    All vowels are present

 **Approach :** Firstly, create set of vowels using set() function. Check for
each character of the string is vowel or not, if vowel then add into the set
s. After coming out of the loop, check length of the set s, if length of set s
is equal to the length of the vowels set then string is accepted otherwise
not.  
Below is the implementation :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to accept the strings

# which contains all the vowels

# Function for check if string

# is accepted or not

def check(string) :

 string = string.lower()

 # set() function convert "aeiou"

 # string into set of characters

 # i.e.vowels = {'a', 'e', 'i', 'o', 'u'}

 vowels = set("aeiou")

 # set() function convert empty

 # dictionary into empty set

 s = set({})

 # looping through each

 # character of the string

 for char in string :

 # Check for the character is present inside

 # the vowels set or not. If present, then

 # add into the set s by using add method

 if char in vowels :

 s.add(char)

 else:

 pass

 

 # check the length of set s equal to length

 # of vowels set or not. If equal, string is 

 # accepted otherwise not

 if len(s) == len(vowels) :

 print("Accepted")

 else :

 print("Not Accepted")

# Driver code

if __name__ == "__main__" :

 

 string = "SEEquoiaL"

 # calling function

 check(string)  
  
---  
  
 __

 __

 **Output:**

    
    
    Accepted

**Alternate Implementation :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def check(string):

 string = string.replace(' ', '')

 string = string.lower()

 vowel = [string.count('a'), string.count('e'), string.count(

 'i'), string.count('o'), string.count('u')]

 # If 0 is present int vowel count array

 if vowel.count(0) > 0:

 return('not accepted')

 else:

 return('accepted')

# Driver code

if __name__ == "__main__":

 string = "SEEquoiaL"

 print(check(string))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    accepted

