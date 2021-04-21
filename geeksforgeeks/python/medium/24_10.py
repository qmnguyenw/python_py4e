Output of Python Programs | Set 24 (Dictionary)



Prerequisite : Python-Dictionary

 **1\. What will be the output?**

 __

 __  
 __

 __

 __  
 __  
 __

dictionary= {"geek":10, "for":45, "geeks": 90}

print("geek" in dictionary)  
  
---  
  
 __

 __

Options:

  1. 10
  2. False
  3. True
  4. Error

    
    
    Output:
    3. True

 **Explanation:** **_in_** is used to check the key exist in dictionary or
not.

 **2\. What will be the output?**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

dictionary={1:"geek", 2:"for", 3:"geeks"}

del dictionary  
  
---  
  
 __

 __

Options:

  1. del deletes the entire dictionary
  2. del doesn’t exist for the dictionary
  3. del deletes the keys in the dictionary
  4. del deletes the values in the dictionary

    
    
    Output:
    1. del deletes the entire dictionary

 **Explanation:** **_del_** deletes the entire dictionary and any further
attempt to access it will throw an error.

 **3\. What will be the output?**

 __

 __  
 __

 __

 __  
 __  
 __

a= {}

a[1] = 1

a['1'] = 2

a[1]= a[1]+1

count = 0

for i in a:

 count += a[i]

print(count)  
  
---  
  
 __

 __

Options:

  1. 4
  2. 2
  3. 1
  4. Error

    
    
    Output:
    1. 4

 **Explanation:** The above piece of code basically finds the sum of the
values of keys.

 **4\. What will be the output?**

 __

 __  
 __

 __

 __  
 __  
 __

test= {1:'A', 2:'B', 3:'C'}

del test[1]

test[1] = 'D'

del test[2]

print(len(test))  
  
---  
  
 __

 __

Options:

  1. 2
  2. 1
  3. 0
  4. Error

    
    
    Output:
    1. 2

 **Explanation:** After the key-value pair of 1:’A’ is deleted, the key-value
pair of 1:’D’ is added.

 **5\. What will be the output?**

 __

 __  
 __

 __

 __  
 __  
 __

a={}

a['a']= 1

a['b']=[2, 3, 4]

print(a)  
  
---  
  
 __

 __

Options:

  1. {‘b’: [2], ‘a’: 1}
  2. {‘a’: 1, ‘b’: [2, 3, 4]}
  3. {‘b’: [2], ‘a’: [3]}
  4. Error

    
    
    Output:
    2. {'a': 1, 'b': [2, 3, 4]}

 **Explanation:** Mutable members can be used as the values of the dictionary
but they cannot be used as the keys of the dictionary.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

