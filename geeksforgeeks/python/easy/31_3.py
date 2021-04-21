Output of Python Program | Set 3



 **Difficulty level :** Intermediate

Predict the output of following Python Programs.

 **Program 1:**

 __

 __  
 __

 __

 __  
 __  
 __

class Geeks:

 def __init__(self, id):

 self.id = id

 

manager = Geeks(100)

 

manager.__dict__['life'] = 49

 

print (manager.life + len(manager.__dict__))  
  
---  
  
 __

 __

Output:

    
    
    51
    

**Explanation :** In the above program we are creating a member variable
having name ‘life’ by adding it directly to the dictionary of the object
‘manager’ of class ‘Geeks’. Total numbers of items in the dictionary is 2, the
variables ‘life’ and ‘id’. Therefore the size or the length of the dictionary
is 2 and the variable ‘life’ is assigned a value ’49’. So the sum of the
variable ‘life’ and the size of the dictionary is 49 + 2 = 51.

  

  

**Program 2:**

 __

 __  
 __

 __

 __  
 __  
 __

a= "GeeksforGeeks "

 

b = 13

 

print (a + b)  
  
---  
  
 __

 __

Output:

    
    
    An error is shown.
    

**Explanation :** As you can see the variable ‘b’ is of type integer and the
variable ‘a’ is of type string. Also as Python is a strongly typed language we
cannot simply concatenate an integer with a string. We have to first convert
the integer variable to the type string to concatenate it with a string
variable. So, trying to concatenate an integer variable to a string variable,
an exception of type “TypeError” is occurred.

**Program 3:**

 __

 __  
 __

 __

 __  
 __  
 __

dictionary= {}

dictionary[1] = 1

dictionary['1'] = 2

dictionary[1] += 1

 

sum = 0

for k in dictionary:

 sum += dictionary[k]

 

print (sum)  
  
---  
  
 __

 __

Output:

    
    
    4
    

**Explanation:** In the above dictionary, key 1 enclosed between single quotes
and only 1 represents two different keys as one of them is an integer and the
other is a string. So, the output of the program is 4.

  

  

**Program 4:**

 __

 __  
 __

 __

 __  
 __  
 __

dictionary= {1:'1', 2:'2', 3:'3'}

del dictionary[1]

dictionary[1] = '10'

del dictionary[2]

print (len(dictionary))  
  
---  
  
 __

 __

Output:

    
    
    2
    

**Explanation :** The task of the ‘del’ function is to remove key-value pairs
from a dictionary. Initially the size of the given dictionary was 3. Then the
key value pair for key 1 is first removed and then added back with a new
value. Then the key value pair for key 2 is removed. So, finally the size of
the dictionary is 2.

This article is contributed by **Pratik Agarwal**. If you like GeeksforGeeks
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

