Python program to find second maximum value in Dictionary



Dictionaries in Python is same as Associative arrays or Maps in other
languages. Unlike lists, dictionaries stores data in key-value pair.  
Let’s see how to find the second maximum value in a Python dictionary.  
 **Method #1:** Naive Approach:  
A general approach is to find the largest value of the dictionary and then
iterate over the dictionary maintaining the value that must be greater than
all the other values and less than the maximum value.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python naive approach to find the

# second largest element in a dictionary

# creating a new dictionary

new_dict ={"google":12, "amazon":9, "flipkart":4,
"gfg":13}

# maximum value

max = max(new_dict.values())

# iterate through the dictionary

max2 = 0

for v in new_dict.values():

 if(v>max2 and v<max):

 max2 = v

# print the second largest value

print(max2)  
  
---  
  
 __

 __

 **Output:**

    
    
    12

**Method #2:** Using sorted() method  
We can find the second largest value in a dictionary by sorting the values of
the dictionaries and then retrieving the second last element from the sorted
list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find second largest

# element from a dictionary using sorted() method

# creating a new Dictionary

example_dict = {"mark": 13, "steve": 3, "bill":
6, "linus": 11}

# now directly print the second largest

# value in the dictionary

print("Output1:", sorted(example_dict.values())[-2])

# More than 1 keys with maximum value are present

example_dict = {"fb": 20, "whatsapp": 12,
"instagram": 20, "oculus": 10}

print("Output2:", sorted(set(example_dict.values()),
reverse=True)[-2])  
  
---  
  
 __

 __

 **Output:**

    
    
    11

**Explanation:** example_dict.values() gives list of all the values in the
dictionary. sorted() method will sort the list of dict_values.
list(sorted(example_dict.values()))[-2] converts dict_values to list and
return the second last element of the sorted list, i.e. the second largest
value of dictionary.  
if more than one maximum values are present in the dictionary as shown in the
2nd example, converting the dictionary values to a set will eliminate the
duplicates.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

