replace() in Python to replace a substring



Given a string str that may contain one more occurrences of “AB”. Replace all
occurrences of “AB” with “C” in str.

Examples:

    
    
    Input  : str = "helloABworld"
    Output : str = "helloCworld"
    
    Input  : str = "fghABsdfABysu"
    Output : str = "fghCsdfCysu"
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Replace all occurrences of
string AB with C without using extra space link. We solve this problem in
python quickly using **replace()** method of string data type.

 **How does replace() function works ?**  
 **str.replace(pattern,replaceWith,maxCount)** takes minimum two parameters
and replaces all occurrences of **pattern** with specified sub-string
**replaceWith**. Third parameter **maxCount** is optional, if we do not pass
this parameter then replace function will do it for all occurrences of pattern
otherwise it will replace only **maxCount** times occurrences of pattern.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Function to replace all occurrences of AB with C

 

def replaceABwithC(input, pattern, replaceWith):

 return input.replace(pattern, replaceWith)

 

# Driver program

if __name__ == "__main__":

 input = 'helloABworld'

 pattern = 'AB'

 replaceWith = 'C'

 print (replaceABwithC(input,pattern,replaceWith))  
  
---  
  
 __

 __

Output:

    
    
    'helloCworld'
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

