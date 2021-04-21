Dictionary Methods in Python | Set 1 (cmp(), len(), items()…)



Python Dictionary Basics have been discussed in the article below

Dictionary

Some dictionary methods are discussed in this article.

 **1\. str(dic)** :- This method is used to **return the string** , denoting
all the dictionary keys with their values.

 **2\. items()** :- This method is used to **return the list** with all
dictionary keys with values.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# str() and items()

 

# Initializing dictionary

dic = { 'Name' : 'Nandini', 'Age' : 19 }

 

# using str() to display dic as string

print ("The constituents of dictionary as string are : ")

print (str(dic))

 

# using str() to display dic as list

print ("The constituents of dictionary as list are : ")

print (dic.items())  
  
---  
  
 __

 __

Output:

    
    
    The constituents of dictionary as string are : 
    {'Name': 'Nandini', 'Age': 19}
    The constituents of dictionary as list are : 
    dict_items([('Name', 'Nandini'), ('Age', 19)])
    

**3\. len()** :- It returns the **count of key entities** of the dictionary
elements.

 **4\. type()** :- This function **returns the data type** of the argument.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# len() and type()

 

# Initializing dictionary

dic = { 'Name' : 'Nandini', 'Age' : 19, 'ID' :
2541997 }

 

# Initializing list

li = [ 1, 3, 5, 6 ]

 

# using len() to display dic size

print ("The size of dic is : ",end="")

print (len(dic))

 

# using type() to display data type

print ("The data type of dic is : ",end="")

print (type(dic))

 

# using type() to display data type

print ("The data type of li is : ",end="")

print (type(li))  
  
---  
  
 __

 __

Output:

    
    
    The size of dic is : 3
    The data type of dic is : 
    The data type of li is : 
    

**5\. copy()** :- This function creates the **shallow copy of the dictionary**
into other dictionary.

 **6\. clear()** :- This function is used to **clear the dictionary**
contents.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# clear() and copy()

 

# Initializing dictionary

dic1 = { 'Name' : 'Nandini', 'Age' : 19 }

 

# Initializing dictionary 

dic3 = {}

 

# using copy() to make shallow copy of dictionary

dic3 = dic1.copy()

 

# printing new dictionary

print ("The new copied dictionary is : ")

print (dic3.items())

 

# clearing the dictionary

dic1.clear()

 

# printing cleared dictionary

print ("The contents of deleted dictionary is : ",end="")

print (dic1.items())  
  
---  
  
 __

 __

Output:

    
    
    The new copied dictionary is : 
    dict_items([('Age', 19), ('Name', 'Nandini')])
    The contents of deleted dictionary is : dict_items([])
    

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

