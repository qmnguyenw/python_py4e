Ways to sort list of dictionaries by values in Python – Using lambda function



Sorting has always been a useful utility in day-to-day programming. Dictionary
in Python is widely used in many applications ranging from competitive domain
to developer domain(e.g. handling JSON data). Having the knowledge to sort
dictionaries according to its values can prove useful in such cases.  
There are 2 ways to achieve this sorting:

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201006145715/ways.jpg)

1.) **_Using lambda function:-_**

This article deals with sorting using the lambda function and using “
**sorted()** ” inbuilt function. Various variations can also be achieved for
sorting the dictionaries.  

  * **For descending order :** Use “ **reverse = True** ” in addition to the sorted() function.
  *  **For sorting w.r.t multiple values:** Separate by “ **comma** ” mentioning the correct order in which sorting has to be performed.

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code demonstrate the working of

# sorted() with lambda

# Initializing list of dictionaries

lis = [{ "name" : "Nandini", "age" : 20},

{ "name" : "Manjeet", "age" : 20 },

{ "name" : "Nikhil" , "age" : 19 }]

# using sorted and lambda to print list sorted

# by age

print "The list printed sorting by age: "

print sorted(lis, key = lambda i: i['age'])

print ("\r")

# using sorted and lambda to print list sorted

# by both age and name. Notice that "Manjeet"

# now comes before "Nandini"

print "The list printed sorting by age and name: "

print sorted(lis, key = lambda i: (i['age'], i['name']))

print ("\r")

# using sorted and lambda to print list sorted

# by age in descending order

print "The list printed sorting by age in descending order: "

print sorted(lis, key = lambda i: i['age'],reverse=True)  
  
---  
  
 __

 __

Output:  

    
    
    The list printed sorting by age: 
    [{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}]
    
    The list printed sorting by age and name: 
    [{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Manjeet'}, {'age': 20, 'name': 'Nandini'}]
    
    The list printed sorting by age in descending order: 
    [{'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}, {'age': 19, 'name': 'Nikhil'}]
    
    
    

**Next Article - >** Ways to sort list of dictionaries by values in Python –
Using itemgetter  
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

