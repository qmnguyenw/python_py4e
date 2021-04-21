Python | Count and display vowels in a string



In this program, we need to count the number of vowels present in a string and
display those vowels. This can be done using various methods. In this article,
we will go through few of the popular methods to do this in an efficient
manner.

Examples:

    
    
    In a simple way
    Input : Geeks for Geeks
    Output :
    5
    ['e', 'e', 'o', 'e', 'e']
    
    This is in a different way
    Input : Geeks for Geeks
    Output : {'u': 0, 'o': 1, 'e': 4, 'a': 0, 'i': 0}
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Counting vowels: String Way**

In this method, we will store all the vowels in a string and then pick every
character from the enquired string and check whether it is in the vowel string
or not. The vowel string consists of all the vowels with both cases since we
are not ignoring the cases here. If the vowel is encountered then count gets
incremented and stored in a list and finally printed.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to count and display number of vowels

# Simply using for and comparing it with a 

# string containg all vowels

def Check_Vow(string, vowels):

 final = [each for each in string if each in vowels]

 print(len(final))

 print(final)

 

# Driver Code

string = "Geeks for Geeks"

vowels = "AaEeIiOoUu"

Check_Vow(string, vowels);  
  
---  
  
 __

 __

Output:

  

  

    
    
    5
    ['e', 'e', 'o', 'e', 'e']
    

**Counting vowels: Dictionary Way**

This also performs the same task but in a different way. In this method, we
form a dictionary with the vowels and increment them when a vowel is
encountered. In this method, we use the case fold method to ignore the cases,
following which we form a dictionary of vowels with the key as a vowel. This
is a better and efficient way to check and find the number of each vowel
present in a string.

 __

 __  
 __

 __

 __  
 __  
 __

# Count vowels in a different way

# Using dictionary

def Check_Vow(string, vowels):

 

 # casefold has been used to ignore cases

 string = string.casefold()

 

 # Forms a dictionary with key as a vowel

 # and the value as 0

 count = {}.fromkeys(vowels, 0)

 

 # To count the vowels

 for character in string:

 if character in count:

 count[character] += 1

 return count

 

# Driver Code

vowels = 'aeiou'

string = "Geeks for Geeks"

print (Check_Vow(string, vowels))  
  
---  
  
 __

 __

Output:

    
    
    {'u': 0, 'o': 1, 'e': 4, 'a': 0, 'i': 0}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

