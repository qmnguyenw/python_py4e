Python – Maximum occurring Substring from list



Sometimes, while working with Python strings, we can have a problem in which
we need to check for maximum occurring subtring from strings list. This can
have application in DNA sequencing in Biology and other application. Lets
discuss certain way in which this task can be performed.

 **Method : Usingregex() + groupby() + max() \+ lambda**  
The combination of above functionalities can be used to solve this particular
problem. In this, we first extract the sequences using regex function. Then
the counter grouping is performed using groupby(). The last step is extracting
maximum which is done using max() along with lambda function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum occurring Substring from list

# Using regex() + groupby() + max() + lambda

import re 

import itertools

 

# initializing string

test_str =
"gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"

test_list = ['gfg', 'is', 'best']

 

# printing original string and list

print("The original string is : " + test_str)

print("The original list is : " + str(test_list))

 

# Maximum occurring Substring from list

# Using regex() + groupby() + max() + lambda

seqs = re.findall(str.join('|', test_list), test_str)

grps = [(key, len(list(j))) for key, j in
itertools.groupby(seqs)]

res = max(grps, key = lambda ele : ele[1])

 

# printing result 

print("Maximum frequency substring : " + str(res[0]))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb
    The original list is : ['gfg', 'is', 'best']
    Maximum frequency substring : gfg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

