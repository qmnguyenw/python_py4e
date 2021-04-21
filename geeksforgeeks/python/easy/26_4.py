String slicing in Python to check if a string can become empty by recursive
deletion



Given a string “str” and another string “sub_str”. We are allowed to delete
“sub_str” from “str” any number of times. It is also given that the “sub_str”
appears only once at a time. The task is to find if “str” can become empty by
removing “sub_str” again and again.

Examples:

    
    
    Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
    Output : Yes
    Explanation : In the string GEEGEEKSKS, we can first 
                  delete the substring GEEKS from position 4.
                  The new string now becomes GEEKS. We can 
                  again delete sub-string GEEKS from position 1. 
                  Now the string becomes empty.
    
    
    Input  : str = "GEEGEEKSSGEK", sub_str = "GEEKS"
    Output : No
    Explanation : In the string it is not possible to make the
                  string empty in any possible manner.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Check if a string can
become empty by recursively deleting a given sub-string link. We will solve
this problem in python using String Slicing. Approach is very simple,

  1. Use find() method of string to search given pattern sub-string.
  2. If sub-string lies in main string then find function will return index of it’s first occurrence.
  3. Now slice string in two parts, (i) from start of string till index-1 of founded sub-string, (ii) (start from first index of founded sub-string + length of sub-string) till end of string.
  4. Concatenate these two sliced part and repeat from step 1 until original string becomes empty or we don’t find sub-string anymore.

 __

 __  
 __

 __

 __  
 __  
 __

def checkEmpty(input, pattern): 

 

 # If both are empty 

 if len(input)== 0 and len(pattern)== 0: 

 return 'true'

 

 # If only pattern is empty 

 if len(pattern)== 0: 

 return 'true'

 

 while (len(input) != 0): 

 

 # find sub-string in main string 

 index = input.find(pattern) 

 

 # check if sub-string founded or not 

 if (index ==(-1)): 

 return 'false'

 

 # slice input string in two parts and concatenate 

 input = input[0:index] + input[index +
len(pattern):] 

 

 return 'true'

 

# Driver program 

if __name__ == "__main__": 

 input ='GEEGEEKSKS'

 pattern ='GEEKS'

 print (checkEmpty(input, pattern))  
  
---  
  
 __

 __

Output:

    
    
    true
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

