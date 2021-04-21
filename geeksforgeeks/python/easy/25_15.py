Concatenated string with uncommon characters in Python



Two strings are given and you have to modify 1st string such that all the
common characters of the 2nd string have to be removed and the uncommon
characters of the 2nd string have to be concatenated with uncommon characters
of the 1st string.

 **Examples:**

    
    
    Input : S1 = "aacdb"
            S2 = "gafd"
    Output : "cbgf"
    
    Input : S1 = "abcs";
            S2 = "cxzca";
    Output : "bsxz"
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has existing solution please refer Concatenated string with
uncommon characters of two strings link. We can solve this problem quickly in
Python using Set and List Comprehension. Approach is simple,

  1. Convert both strings into set so that they could have only unique characters. Now take intersection of two sets to get common character both strings have.
  2. Now separate out those characters in each string which are not common in both of them and concatenate the characters.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to concatenated string with uncommon

# characters of two strings 

 

def uncommonConcat(str1, str2): 

 

 # convert both strings into set 

 set1 = set(str1) 

 set2 = set(str2) 

 

 # take intersection of two sets to get list of 

 # common characters 

 common = list(set1 & set2) 

 

 # separate out characters in each string 

 # which are not common in both strings 

 result = [ch for ch in str1 if ch not in common]
+ [ch for ch in str2 if ch not in common] 

 

 # join each character without space to get 

 # final string 

 print( ''.join(result) )

 

# Driver program 

if __name__ == "__main__": 

 str1 = 'aacdb'

 str2 = 'gafd'

 uncommonConcat(str1,str2)   
  
---  
  
__

__

Output:

    
    
    cbgf
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

