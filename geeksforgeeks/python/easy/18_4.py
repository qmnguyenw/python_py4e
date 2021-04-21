Python | Frequency of each character in String



Given a string, the task is to find the frequencies of all the characters in
that string and return a dictionary with key as the character and its value
as its frequency in the given string.

 **Method #1 :** Naive method

Simply iterate through the string and form a key in dictionary of newly
occurred element or if element is already occurred, increase its value by 1.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# each occurrence frequency using 

# naive method 

 

# initializing string 

test_str = "GeeksforGeeks"

 

# using naive method to get count 

# of each element in string 

all_freq = {}

 

for i in test_str:

 if i in all_freq:

 all_freq[i] += 1

 else:

 all_freq[i] = 1

 

# printing result 

print ("Count of all characters in GeeksforGeeks is :\n "

 + str(all_freq))  
  
---  
  
 __

 __

 **Output :**

    
    
    Count of all characters in GeeksforGeeks is :
     {'r': 1, 'e': 4, 'k': 2, 'G': 2, 's': 2, 'f': 1, 'o': 1}
    

  

  

**Method #2 :** Using collections.Counter()

The most suggested method that could be used to find all occurrences is this
method, this actually gets all element frequency and could also be used to
print single element frequency if required.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# each occurrence frequency using 

# collections.Counter()

from collections import Counter

 

# initializing string 

test_str = "GeeksforGeeks"

 

# using collections.Counter() to get 

# count of each element in string 

res = Counter(test_str)

 

# printing result 

print ("Count of all characters in GeeksforGeeks is :\n "

 + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Count of all characters in GeeksforGeeks is : 
    Counter({'e': 4, 's': 2, 'k': 2, 'G': 2, 'o': 1, 'r': 1, 'f': 1})
    

**Method #3 :** Using dict.get()

get() method is used to check the previously occurring character in string,
if its new, it assigns 0 as initial and appends 1 to it, else appends 1 to
previously holded value of that element in dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# each occurrence frequency using 

# dict.get()

 

# initializing string 

test_str = "GeeksforGeeks"

 

# using dict.get() to get count 

# of each element in string 

res = {}

 

for keys in test_str:

 res[keys] = res.get(keys, 0) + 1

 

# printing result 

print ("Count of all characters in GeeksforGeeks is : \n"

 + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Count of all characters in GeeksforGeeks is :
     {'k': 2, 'e': 4, 's': 2, 'G': 2, 'f': 1, 'r': 1, 'o': 1}
    

**Method #4 :** Using set() + count()

count() coupled with set() can also achieve this task, in this we just
iterate over the set converted string and get the count of each character in
original string and assign that element with that value counted using
count().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# each occurrence frequency using 

# set() + count()

 

# initializing string 

test_str = "GeeksforGeeks"

 

# using set() + count() to get count 

# of each element in string 

res = {i : test_str.count(i) for i in set(test_str)}

 

# printing result 

print ("The count of all characters in GeeksforGeeks is :\n "

 + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    Count of all characters in GeeksforGeeks is :
     {'G': 2, 's': 2, 'k': 2, 'e': 4, 'o': 1, 'r': 1, 'f': 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

