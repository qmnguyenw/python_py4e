Python | Remove unordered duplicate elements from a list



Given a list, the task is to remove the duplicate elements. All the elements
which are not in same order but made of same characters/numbers are considered
as duplicates.

 **Examples:**

    
    
     **Input :** ['gfg', 'ggf', 'fgg', 'for', 'orf',
                    'ofr', 'rfo', 'rof', 'fro']
    **Output :** ['for', 'fgg']
    
    **Input:** ['110', '101', '001', '010', '100']
    **Output:** ['001', '011']

  
**Method #1 :** Using _set_

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove duplicate

# unordered elements from a list

from collections import Counter

 

# List initialisation

Input = ['1213','1231','1123','1132','2113',

 '2311','0007', '0016', '0025', '0034',

 '0043', '0052', '0061', '0070','0304',

 '0313', '0322','0098','9800', '0331',

 '0340', '0403', '0412', '0421', '0430',

 '0502','8900','8009' ,'0511', '0520',

 '0601', '0610', '0700', '1006', '1015']

 

# Set initialisation

s = set()

 

# Output list initialisation

output =[]

 

for i in Input:

 if tuple(Counter(sorted(i, key = int)).items()) in s:

 pass

 

 else:

 s.add(tuple(Counter(sorted(i, key = int)).items()))

 output.append(i)

 

# Printing output

print(output)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['1213', '0007', '0016', '0025', '0034', 
     '0313', '0322', '0098', '0412', '0511']
    

  
**Method #2 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to remove duplicate

# unordered elements from a list

# List initialisation

Input = ['gfg', 'ggf', 'fgg', 'for', 'orf',

 'ofr', 'rfo', 'rof', 'fro']

 

# Getting unique nos

Output = list({''.join(sorted(n)) for n in Input})

 

# Printing Output

print(Output)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['for', 'fgg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

