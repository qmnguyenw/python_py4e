Python | Group Anagrams from given list



Anagrams are the words that are formed by similar elements but the orders in
which these characters occur differ. Sometimes, we may encounter a problem in
which we need to group the anagrams and hence solution to above problem always
helps. Let’s discuss certain ways in which this can be done.  
 **Method #1 : Using defaultdict() + sorted() + values()**  
The combination of above functions can be used to get the solution of above
problem. In this, we first get the anagrams grouped using defaultdict and use
sorted function to get each anagram root value to group anagrams.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Grouping Anagrams

# using defaultdict() + sorted() + values()

from collections import defaultdict

# initializing list

test_list = ['lump', 'eat', 'me', 'tea', 'em',
'plum']

# printing original list

print("The original list : " + str(test_list))

# using defaultdict() + sorted() + values()

# Grouping Anagrams

temp = defaultdict(list)

for ele in test_list:

 temp[str(sorted(ele))].append(ele)

res = list(temp.values())

# print result

print("The grouped Anagrams : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['lump', 'eat', 'me', 'tea', 'em', 'plum']
    The grouped Anagrams : [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]
    
    
    
    

  
**Method #2 : Using list comprehension + sorted() + lambda + groupby()**  
The combination of above function can also be used to perform this particular
task. The groupby function performs the necessary grouping together. The
lambda function helps to group alike anagrams.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Grouping Anagrams

# using list comprehension + sorted() + lambda + groupby()

from itertools import groupby

# initializing list

test_list = ['lump', 'eat', 'me', 'tea', 'em',
'plum']

# printing original list

print("The original list : " + str(test_list))

# using list comprehension + sorted() + lambda + groupby()

# Grouping Anagrams

temp = lambda test_list: sorted(test_list)

res = [list(val) for key, val in
groupby(sorted(test_list, key = temp), temp)]

# print result

print("The grouped Anagrams : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['lump', 'eat', 'me', 'tea', 'em', 'plum']
    The grouped Anagrams : [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]
    
    
    
    

**Method3: Using Simple Python Programming**

  

  

Below is the program to group anagram words together in a simple python
programming way. Without using list comprehension or lambda or imported
methods.

The method followed is simple –

1\. Sort each word and use the sorted word as a dictionary key

2\. Keep adding new word into dictionary against sorted key

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

data= ['eat', 'ate', 'tea', 'ant', 'tan',

 'bat', 'adobe', 'abode', 'listen', 'silent']

def createAnagramKey(string):

 key = ''

 for ch in sorted(string):

 key += ch

 return str(key)

def groupAnagramWords(data):

 group = dict()

 for ele in data:

 if group.get(createAnagramKey(ele)) == None:

 group[createAnagramKey(ele)] = [ele]

 else:

 group[createAnagramKey(ele)].append(ele)

 return group

anagram_grouped = groupAnagramWords(data)

# Anagram in dictonry format

print('In dictonry format')

print(anagram_grouped)

anagram_grouped_list = list()

for k, v in anagram_grouped.items():

 anagram_grouped_list.append(v)

print('In list format')

print(anagram_grouped_list)  
  
---  
  
 __

 __

 **Output:**

    
    
    In dictonry format
    {'aet': ['eat', 'ate', 'tea'], 'ant': ['ant', 'tan'], 'abt': ['bat'],
     'abdeo': ['adobe', 'abode'], 'eilnst': ['listen', 'silent']}
     
    In list format
    [['eat', 'ate', 'tea'], ['ant', 'tan'], ['bat'], ['adobe', 'abode'], ['listen', 'silent']]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

