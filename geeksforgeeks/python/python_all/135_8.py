Operations on Python Counter



The counter can be used to calculate the frequency in a list or in a string
because as any list or string is passed as input, it returns output as a
dictionary having keys are the unique elements of the list and values are the
corresponding frequencies of the elements.  
In the code given below, Counter from Collection Python library is imported to
find the frequency of every unique character occurring in this string, By
using Counter on the list, the frequency of each unique elements present in
the list can also be found.

 __

 __  
 __

 __

 __  
 __  
 __

# Write Python3 code here

# Counter used in string to find frequencies of all its unique Characters

 

from collections import Counter

s1 ='aabbbcccdeff'

c1 = Counter(s1)

print("c1 :", c1)

 

# Counter used in List to find frequencies of all its unique elements of
list

L1 =[1, 2, 1, 1, 4, 4, 4, 5, 6,
6, 3, 3, 0, 0]

t1 = Counter(L1)

 

print("t1 :", t1)  
  
---  
  
 __

 __

 **Output:**

    
    
    c1 : Counter({'b': 3, 'c': 3, 'a': 2, 'f': 2, 'e': 1, 'd': 1})
    t1 : Counter({1: 3, 4: 3, 0: 2, 3: 2, 6: 2, 2: 1, 5: 1})
    

  
Performing certain operations on returned output dictionary if **d** is output
dictionary then like **d.items(), d.keys(), d.values()**

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

d ='aabbbcccdeff'

d = Counter(d)

 

# To print Counter value 

print("d :", d) 

 

# To access the values corresponds to each keys of the returned dictionary 

print("d.values() : ", d.values()) 

 

# To get the keys and values both of dictionary

print("d.items() :", d.items())

 

# To get only the keys

print("d.keys() :", d.keys())

 

# To sort the values of dictionary 

print("sorted(d) :", sorted(d))  
  
---  
  
 __

 __

 **Output:**

    
    
    d : Counter({'b': 3, 'c': 3, 'a': 2, 'f': 2, 'e': 1, 'd': 1})
    d.values() :  dict_values([2, 3, 3, 2, 1, 1])
    d.items() : dict_items([('a', 2), ('b', 3), ('c', 3), ('f', 2), ('e', 1), ('d', 1)])
    d.keys() : dict_keys(['a', 'b', 'c', 'f', 'e', 'd'])
    sorted(d) : ['a', 'b', 'c', 'd', 'e', 'f']
    

  
**Addition of two Counters**  
Adition of two counter creates the additions of values corresponds to each
keys, and if a key that is present in one counter and not in other, in that
case this key value also get into final output.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

t1 = Counter('aabbddffggjik')

t2 = Counter('aaabbbssshhhggdkkll')

 

print("t1:", t1)

print("t2:", t2)

print("t1 + t2 :", t1 + t2)  
  
---  
  
 __

 __

 **Output:**

    
    
    t1: Counter({'g': 2, 'a': 2, 'b': 2, 'f': 2, 'd': 2, 'k': 1, 'j': 1, 'i': 1})
    t2: Counter({'a': 3, 'b': 3, 'h': 3, 's': 3, 'l': 2, 'g': 2, 'k': 2, 'd': 1})
    t1+t2 : Counter({'a': 5, 'b': 5, 'g': 4, 'k': 3, 'h': 3, 'd': 3, 's': 3, 'l': 2, 'f': 2, 'j': 1, 'i': 1})
    

  
**Substraction of two Counters**  
Counts of common elements are subtracted from each other and (keeps only
positive counts)

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

t1 = Counter('aabbddffggjik')

t2 = Counter('aaabbbssshhhggdkkll')

 

print("t1:", t1)

print("t2:", t2)

print("t1-t2 :", t1-t2)

print("t2-t1 :", t2-t1)  
  
---  
  
 __

 __

 **Output:**

    
    
    t1: Counter({'f': 2, 'd': 2, 'b': 2, 'a': 2, 'g': 2, 'k': 1, 'i': 1, 'j': 1})
    t2: Counter({'h': 3, 'b': 3, 'a': 3, 's': 3, 'l': 2, 'k': 2, 'g': 2, 'd': 1})
    t1-t2 : Counter({'f': 2, 'i': 1, 'j': 1, 'd': 1})
    t2-t1 : Counter({'h': 3, 's': 3, 'l': 2, 'k': 1, 'b': 1, 'a': 1})
    

  
**Intersections( &) of two Counters**  
Intersaction(&) will keep only the minimum of corresponding counts: min(t1[x],
t2[x]):

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

t1 = Counter('aaabbbbccdeeee')

t2 = Counter('aabbccccdddee')

 

print("t1 :", t1)

print("t2 :", t2)

print("t1&t2; :", t1&t2;)  
  
---  
  
 __

 __

 **Output:**

    
    
    t1 : Counter({'e': 4, 'b': 4, 'a': 3, 'c': 2, 'd': 1})
    t2 : Counter({'c': 4, 'd': 3, 'a': 2, 'e': 2, 'b': 2})
    t1&t2 : Counter({'c': 2, 'a': 2, 'e': 2, 'b': 2, 'd': 1})
    

  
**Union(|) of two Counters**  
Union(|) will keep only the maximum of corresponding counts: max(c[x], d[x]):

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

t1 = Counter('aaabbbbccdeeee')

t2 = Counter('aabbccccdddee')

 

print("t1 :", t1)

print("t2 :", t2)

print("t1|t2 :", t1|t2)  
  
---  
  
 __

 __

 **Output:**

    
    
    t1 : Counter({'b': 4, 'e': 4, 'a': 3, 'c': 2, 'd': 1})
    t2 : Counter({'c': 4, 'd': 3, 'a': 2, 'b': 2, 'e': 2})
    t1|t2 : Counter({'b': 4, 'e': 4, 'c': 4, 'a': 3, 'd': 3})
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

