List comprehension and ord() in Python to remove all characters other than
alphabets



Given a string consisting of alphabets and other characters, remove all the
characters other than alphabets and print the string so formed.  
Examples:

    
    
    Input : str = "$Gee*k;s..fo, r'Ge^eks?"
    Output : GeeksforGeeks
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Remove all characters other
than alphabets from string link.  
We will solve this problem in python quickly using List Comprehension.  
 **Approach :** is

    
    
    1. Traverse string 
    2. Select characters which lie in range of [a-z] or [A-Z]
    3. Print them together

 **How does ord() and range() function works in python ?**

  * The **ord()** method returns an integer representing the Unicode code point of the given Unicode character. **For example,
    
         ord('5') = 53 and ord('A') = 65 and ord('$') = 36

**

  * The **range(a,b,step)** function generates a list of elements which ranges from a inclusive to b exclusive with increment/decrement of given step.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove all characters

# other than alphabets from string 

 

def removeAll(input): 

 

 # Traverse complete string and separate 

 # all characters which lies between [a-z] or [A-Z] 

 sepChars = [char for char in input if

ord(char) in range(ord('a'),ord('z')+1,1)
or ord(char) in

range(ord('A'),ord('Z')+1,1)] 

 

 # join all separated characters 

 # and print them together 

 return ''.join(sepChars) 

 

# Driver program 

if __name__ == "__main__": 

 input = "$Gee*k;s..fo, r'Ge^eks?"

 print (removeAll(input))   
  
---  
  
__

__

Output:

    
    
    GeeksforGeeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

