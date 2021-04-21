Validating Roman Numerals Using Regular expression



Given a **String** , and You have to validate whether the given String is
Valid Roman Numeral or not. If it is valid print True else False.

 **Note** : Numerals are lying between 1 to 3999.

 **Examples:**

    
    
    **Input:** String = IX  
    **Output:** True 
    
    **Input:** String = 54IVC 
    **Output:** False
    

## Recommended: Please solve it on “ ** _ _PRACTICE__** ” first, before moving
on to the solution.

Roman numerals are based on below symbols.

    
    
    **SYMBOL**       **VALUE**
    I             1
    IV            4
    V             5
    IX            9
    X             10
    XL            40
    L             50
    XC            90
    C             100
    CD            400
    D             500
    CM            900 
    M             1000       
    

A number in Roman Numerals is a string of these symbols written in descending
order(e.g. M’s first, followed by D’s, etc.). However, in a few specific
cases, to avoid four characters being repeated in succession (such as IIII or
XXXX), **subtractive notation** is often used as follows:

  

  

  *  **I** placed before **V** or **X** indicates one less, so four is **IV** (one less than 5) and 9 is IX (one less than 10).
  *  **X** placed before **L** or **C** indicates ten less, so forty is **XL** (10 less than 50) and 90 is **XC** (ten less than a hundred).
  *  **C** placed before **D** or **M** indicates a hundred less, so four hundred is **CD** (a hundred less than five hundred) and nine hundred is **CM** (a hundred less than a thousand).

 **Approach:**

  * The Regular Expression to check if a string is Valid Roman Numeral or not is this:
    
    
     ^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$
    

In which,

    1.  **M{0,4}** specifies the thousands section and basically restrains it to between 0 and 4000
    2.  **(CM|CD|D?C{0,3})** is for the hundreds section.
    3.  **(XC|XL|L?X{0,3})** is for the tens place.
    4. Finally, **(IX|IV|V?I{0,3})** is the units section.
  * Import regular expression and search the input string in the expression if the string exists return True else return False

Below is the implementation of the above approach.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Validate the Roman numeral

 

# Function to Validate the Roman numeral

def ValidationOfRomanNumerals(string):

 

 # Importing regular expression

 import re

 

 # Serching the input string in expression and 

 # returning the boolean value


print(bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",string)))

 

# Driver code

 

# Given string

string="XI"

 

# Function call

ValidationOfRomanNumerals(string)  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

