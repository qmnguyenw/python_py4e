Python program for most frequent word in Strings List



Given Strings List, write a Python program to get word with most number of
occurrences.

 **Example:**

>  **Input** : test_list = [“gfg is best for geeks”, “geeks love gfg”, “gfg is
> best”]  
> **Output** : gfg  
> **Explanation** : gfg occurs 3 times, most in strings in total.
>
>  **Input** : test_list = [“geeks love gfg”, “geeks are best”]  
> **Output** : geeks  
> **Explanation** : geeks occurs 2 times, most in strings in total.

**Method #1 : Using loop +** **max()** **+** **split()** **+**
**defaultdict()**

  

  

In this, we perform task of getting each word using split(), and increase its
frequency by memorizing it using defauldict(). At last, max(), is used with
parameter to get count of maximum frequency string.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Most frequent word in Strings List

# Using loop + max() + split() + defaultdict()

from collections import defaultdict

# initializing Matrix

test_list = ["gfg is best for geeks", "geeks love gfg", "gfg is
best"]

# printing original list

print("The original list is : " + str(test_list))

temp = defaultdict(int)

# memoizing count

for sub in test_list:

 for wrd in sub.split():

 temp[wrd] += 1

# getting max frequency

res = max(temp, key=temp.get)

# printing result

print("Word with maximum frequency : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['gfg is best for geeks', 'geeks love gfg', 'gfg is best']
    Word with maximum frequency : gfg

 **Method #2 : Using list comprehension +** **mode()**

In this, we get all the words using list comprehension and get maximum
frequency using mode().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Most frequent word in Strings List

# Using list comprehension + mode()

from statistics import mode

# initializing Matrix

test_list = ["gfg is best for geeks", "geeks love gfg", "gfg is
best"]

# printing original list

print("The original list is : " + str(test_list))

# getting all words

temp = [wrd for sub in test_list for wrd in sub.split()]

# getting frequency

res = mode(temp)

# printing result

print("Word with maximum frequency : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['gfg is best for geeks', 'geeks love gfg', 'gfg is best']
    Word with maximum frequency : gfg

#### Method #3: Using list() and Counter()

  * Append all words to empty list and calculate frequency of all words using **Counter()**function.
  * Find max count and print that key.

Below is the implementation:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Most frequent word in Strings List

from collections import Counter

# function which returns

# most frequeent word

def mostFrequentWord(words):

 

 # Takig empty list

 lis = []

 for i in words:

 

 # Getting all words

 for j in i.split():

 lis.append(j)

 

 # Calculating frequency of all words

 freq = Counter(lis)

 

 # find max count and print that key

 max = 0

 for i in freq:

 if(freq[i] > max):

 max = freq[i]

 word = i

 return word

# Driver code

# initializing strings list

words = ["gfg is best for geeks", "geeks love gfg", "gfg is
best"]

# printing original list

print("The original list is : " + str(words))

# passing this words to mostFrequencyWord function

# printing result

print("Word with maximum frequency : " + mostFrequentWord(words))

# This code is contributed by vikkycirus  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['gfg is best for geeks', 'geeks love gfg', 'gfg is best']
    Word with maximum frequency : gfg

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

