Ways to sort list of dictionaries by values in Python – Using itemgetter



Previous article of this segment dealt with sorting list of dictionaries by
values using lambda function.  
  
Ways to sort list of dictionaries by values in Python – Using lambda function  
  
This article aims at performing this functionality using itemgetter and
showing visible differences.  

Itemgetter can be used instead of lambda function to achieve the similar
functionality. Outputs in same way as sorted() and lambda, but has different
internal implementation. It takes keys of dictionaries and converts them into
tuples. It reduces overhead and is **faster** and more efficient. The “
**operator** ” module has to be imported for its working. The code is
explained below

 __

 __  
 __

 __

 __  
 __  
 __

# Python code demonstrate the working of sorted()

# and itemgetter

 

# importing "operator" for implementing itemgetter

from operator import itemgetter

 

# Initializing list of dictionaries

lis = [{ "name" : "Nandini", "age" : 20}, 

{ "name" : "Manjeet", "age" : 20 },

{ "name" : "Nikhil" , "age" : 19 }]

 

# using sorted and itemgetter to print list sorted by age 

print "The list printed sorting by age: "

print sorted(lis, key=itemgetter('age'))

 

print ("\r")

 

# using sorted and itemgetter to print list sorted by both age and name

# notice that "Manjeet" now comes before "Nandini"

print "The list printed sorting by age and name: "

print sorted(lis, key=itemgetter('age', 'name'))

 

print ("\r")

 

# using sorted and itemgetter to print list sorted by age in descending
order

print "The list printed sorting by age in descending order: "

print sorted(lis, key=itemgetter('age'),reverse = True)  
  
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
    

**Advantages of itemgetter over lambda**

*  **Performance** : itemgetter performs better than lambda functions in the context of time.
*  **Concise :** : itemgetter looks more concise when accessing multiple values than lambda functions.
    
    
    
    itemgetter(1,3,4,5)  ---> Looks more concise
    key(s[1], s[2], s[3], s[4]) ---> Looks less concise
    

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

