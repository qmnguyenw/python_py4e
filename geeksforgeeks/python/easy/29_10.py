Fraction module in Python



This module provides support for rational number arithmetic. It allows to
create a Fraction instance from integers, floats, numbers, decimals and
strings.

 **Fraction Instances :** A Fraction instance can be constructed from a pair
of integers, from another rational number, or from a string. Fraction
instances are hashable, and should be treated as immutable.

  1.  **class fractions.Fraction(numerator=0, denominator=1) :** This requires that numerator and denominator are instances of **numbers. Rational** and a fraction instance with value = (numerator/denominator) is returned. A zerodivision error is raised if denominator = 0.

 __

 __  
 __

 __

 __  
 __  
 __

from fractions import Fraction

 

print (Fraction(11, 35))

# returns Fraction(11, 35)

 

print (Fraction(10, 18))

# returns Fraction(5, 9)

 

print (Fraction())

# returns Fraction(0, 1)  
  
---  
  
 __

 __

 **Output :**

    
    
    11/35
    5/9
    0
    

  2. **class fractions.Fraction(other_fraction) :** This requires that other_fraction is instance of **numbers.Rational** and a fraction instance with same value is returned.
  3.  **class fractions.Fraction(float) :** This requires the **float** instance and a fraction instance with same value is returned.

 __

 __  
 __

 __

 __  
 __  
 __

from fractions import Fraction

 

print (Fraction(1.13))

# returns Fraction(1272266894732165, 1125899906842624)  
  
---  
  
 __

 __

 **Output :**

    
    
    1272266894732165/1125899906842624
    

  4. **class fractions.Fraction(decimal) :** This requires the **decimal** instance and a fraction instance with same value is returned.

 __

 __  
 __

 __

 __  
 __  
 __

from fractions import Fraction

 

print (Fraction('1.13'))

# returns Fraction(113, 100)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    113/100
    

  5. **class fractions.Fraction(string) :** This requires the **string or unicode** instance instance and a fraction instance with same value is returned.

 **Form for this instance :** [sign] numerator [‘/’ denominator]  
Here, sign represents ‘+’ or ‘-’ and numerator and denominator are strings of
single digits.

 __

 __  
 __

 __

 __  
 __  
 __

from fractions import Fraction

 

print (Fraction('8/25'))

# returns Fraction(8, 25)

 

print (Fraction('1.13'))

# returns Fraction(113, 100)

 

print (Fraction('3/7'))

# returns Fraction(3, 7)

 

print (Fraction('1.414213 \t\n'))

# returns Fraction(1414213, 1000000)  
  
---  
  
 __

 __

 **Output :**

    
    
    8/25
    113/100
    3/7
    1414213/1000000
    

  6. **limit_denominator(max_denominator=1000000) :**
    * This method is useful for finding rational approximations to a given floating-point number.
    * This module finds and returns the closest Fraction to self that has denominator at most max_denominator.
    * This module can also be used to return the numerator of a given fraction in the lowest term by using the **numerator** property and the denominator by using the **denominator** property.

 __

 __  
 __

 __

 __  
 __  
 __

from fractions import Fraction

 

print (Fraction('3.14159265358979323846'))

# returns Fraction(157079632679489661923, 50000000000000000000)

 

print
(Fraction('3.14159265358979323846').limit_denominator(10000))

# returns Fraction(355, 113)

 

print (Fraction('3.14159265358979323846').limit_denominator(100))

# returns Fraction(311, 99)

 

print (Fraction('3.14159265358979323846').limit_denominator(10))

# returns Fraction(22, 7)

 

print (Fraction(125, 50).numerator)

# returns 5

 

print (Fraction(125, 50).denominator)

# returns 2  
  
---  
  
 __

 __

 **Output :**

    
    
    157079632679489661923/50000000000000000000
    355/113
    311/99
    22/7
    5
    2
    

**Performing Mathematical operations on fractions**

 __

 __  
 __

 __

 __  
 __  
 __

from fractions import Fraction

 

print (Fraction(113, 100) + Fraction(25, 18))

# returns Fraction(2267, 900)

 

print (Fraction(18, 5) / Fraction(18, 10))

# returns Fraction(2, 1)

 

print (Fraction(18, 5) * Fraction(16, 19))

# returns Fraction(288, 95)

 

print (Fraction(18, 5) * Fraction(15, 36))

# returns Fraction(3, 2)

 

print (Fraction(12, 5) ** Fraction(12, 10))

# returns 2.8592589556010197  
  
---  
  
 __

 __

 **Output :**

    
    
    2267/900
    2
    288/95
    3/2
    2.8592589556
    

**Fraction-based calculations using various functions of math module**

 __

 __  
 __

 __

 __  
 __  
 __

import math

from fractions import Fraction

 

print (math.sqrt(Fraction(25, 4)))

# returns 2.5

 

print (math.sqrt(Fraction(28,3)))

# returns 3.0550504633038935

 

print (math.floor(Fraction(3558, 1213)))

# returns 2

 

print (Fraction(math.sin(math.pi/3)))

# returns Fraction(3900231685776981, 4503599627370496)

 

print (Fraction(math.sin(math.pi/3)).limit_denominator(10))

# returns Fraction(6, 7)  
  
---  
  
 __

 __

 **Output :**

    
    
    2.5
    3.0550504633
    2.0
    3900231685776981/4503599627370496
    6/7
    

This article is contributed by **Aditi Gupta**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

