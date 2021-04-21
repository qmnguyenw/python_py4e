fnmatch – Unix filename pattern matching in Python



This module is used for matching Unix shell-style wildcards. fnmatch()
compares a single file name against a pattern and returns TRUE if they match
else returns FALSE.  
The comparison is case-sensitive when the operating system uses a case-
sensitive file system.  
The special characters and their functions used in shell-style wildcards are :

  *  **‘*’ –** matches everything
  *  **‘?’ –** matches any single character
  *  **‘[seq]’ –** matches any character in seq
  *  **‘[!seq]’ –** matches any character not in seq

The meta-characters should be wrapped in brackets for a literal match. For
example, ‘[?]’ matches the character ‘?’.

 **Functions provided by the fnmatch module**

  1.  **fnmatch.fnmatch(filename, pattern)** : This function tests whether the given filename string matches the pattern string and returns a boolean value. If the operating system is case-insensitive, then both parameters will be normalized to all lower-case or upper-case before the comparison is performed.

 **Example:** Script to search all files starting with ‘fnmatch’ and ending in
‘.py’

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# fnmatch.fnmatch(filename, pattern) 

import fnmatch 

import os 

 

pattern = 'fnmatch_*.py'

print ('Pattern :', pattern )

print()

 

files = os.listdir('.') 

for name in files: 

 print ('Filename: %-25s %s' % (name, fnmatch.fnmatch(name,
pattern))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    $ python fnmatch_fnmatch.py
    
    Pattern : fnmatch_*.py
    
    Filename: __init__.py               False
    Filename: fnmatch_filter.py         True
    Filename: fnmatch_fnmatch.py        True
    Filename: fnmatch_fnmatchcase.py    True
    Filename: fnmatch_translate.py      True
    Filename: index.rst                 False
    

  2. **fnmatch.fnmatchcase(filename, pattern):** This function performs the case sensitive comparison and tests whether the given filename string matches the pattern string and returns a boolean value.

 **Example:** Script for a case-sensitive comparison, regardless of the
filesystem and operating system settings.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# fnmatch.fnmatchcase(filename, pattern) 

import fnmatch 

import os 

 

pattern = 'FNMATCH_*.PY'

print ('Pattern :', pattern) 

print()

 

files = os.listdir('.') 

 

for name in files: 

 (print 'Filename: %-25s %s' % (name, fnmatch.fnmatchcase(name,
pattern)))  
  
---  
  
 __

 __

 **Output :**

    
    
    $ python fnmatch_fnmatchcase.py
    
    Pattern : FNMATCH_*.PY
    
    Filename: __init__.py               False
    Filename: fnmatch_filter.py         False
    Filename: FNMATCH_FNMATCH.PY        True
    Filename: fnmatch_fnmatchcase.py    False
    Filename: fnmatch_translate.py      False
    Filename: index.rst                 False
    

  3. **fnmatch.filter(names, pattern):** This function returns the subset of the list of names passed in the function that match the given pattern.  

