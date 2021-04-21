Dictionary Methods in Python | Set 2 (update(), has_key(), fromkeys()…)



Some of the Dictionary methods are discussed in set 1 below

Dictionary Methods in Python | Set 1 (cmp(), len(), items()…)

More methods are discussed in this article.

 **1\. fromkeys(seq,value)** :- This method is used to declare a **new
dictionary from the sequence** mentioned in its arguments. This function can
also **initialize the declared dictionary with “value” argument**.

 **2\. update(dic)** :- This function is used to **update the dictionary to
add other dictionary keys**.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# fromkeys() and update()

 

# Initializing dictionary 1

dic1 = { 'Name' : 'Nandini', 'Age' : 19 }

 

# Initializing dictionary 2

dic2 = { 'ID' : 2541997 }

 

# Initializing sequence

sequ = ('Name', 'Age', 'ID')

 

# using update to add dic2 values in dic 1

dic1.update(dic2)

 

# printing updated dictionary values

print ("The updated dictionary is : ")

print (str(dic1))

 

# using fromkeys() to transform sequence into dictionary

dict = dict.fromkeys(sequ,5)

 

# printing new dictionary values

print ("The new dictionary values are : ")

print (str(dict))  
  
---  
  
 __

 __

Output:

    
    
    The updated dictionary is : 
    {'Age': 19, 'Name': 'Nandini', 'ID': 2541997}
    The new dictionary values are : 
    {'Age': 5, 'Name': 5, 'ID': 5}
    

**3\. has_key()** :- This function returns true if **specified key is
present** in the dictionary, else returns false.

 **4\. get(key, def_val)** :- This function return the **key value associated
with the key** mentioned in arguments. If key is not present, the default
value is returned.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# has_key() and get()

 

# Initializing dictionary

dict = { 'Name' : 'Nandini', 'Age' : 19 }

 

# using has_key() to check if dic1 has a key

if dict.has_key('Name'):

 print ("Name is a key")

else : print ("Name is not a key")

 

# using get() to print a key value

print ("The value associated with ID is : ")

print (dict.get('ID', "Not Present"))

 

# printing dictionary values

print ("The dictionary values are : ")

print (str(dict))  
  
---  
  
 __

 __

Output:

    
    
    Name is a key
    The value associated with ID is : 
    Not Present
    The dictionary values are : 
    {'Name': 'Nandini', 'Age': 19}
    

**5\. setdefault(key, def_value)** :- This function also **searches for a
key** and displays its value like get() but, it **creates new key with
def_value** if key is not present.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# setdefault()

 

# Initializing dictionary

dict = { 'Name' : 'Nandini', 'Age' : 19 }

 

# using setdefault() to print a key value

print ("The value associated with Age is : ",end="")

print (dict.setdefault('ID', "No ID"))

 

# printing dictionary values

print ("The dictionary values are : ")

print (str(dict))  
  
---  
  
 __

 __

Output:

    
    
    The value associated with Age is : No ID
    The dictionary values are : 
    {'Name': 'Nandini', 'Age': 19, 'ID': 'No ID'}
    

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

