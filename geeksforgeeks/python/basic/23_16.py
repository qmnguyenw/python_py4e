zip() in Python



The purpose of zip() is to **map the similar index of multiple containers** so
that they can be used just using as single entity.

>  **Syntax :**  
>  zip(*iterators)  
>  **Parameters :**  
>  Python iterables or containers ( list, string etc )  
>  **Return Value :**  
>  Returns a single iterator object, having mapped values from all the  
> containers.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# zip()

 

# initializing lists

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]

roll_no = [ 4, 1, 3, 2 ]

marks = [ 40, 50, 60, 70 ]

 

# using zip() to map values

mapped = zip(name, roll_no, marks)

 

# converting values to print as set

mapped = set(mapped)

 

# printing resultant values 

print ("The zipped result is : ",end="")

print (mapped)  
  
---  
  
 __

 __

Output:

    
    
    The zipped result is : {('Shambhavi', 3, 60), ('Astha', 2, 70),
    ('Manjeet', 4, 40), ('Nikhil', 1, 50)}
    

**How to unzip?**  
Unzipping means converting the zipped values back to the individual self as
they were. This is done with the help of “ ***** ” operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# unzip

 

# initializing lists

 

name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]

roll_no = [ 4, 1, 3, 2 ]

marks = [ 40, 50, 60, 70 ]

 

# using zip() to map values

mapped = zip(name, roll_no, marks)

 

# converting values to print as list

mapped = list(mapped)

 

# printing resultant values 

print ("The zipped result is : ",end="")

print (mapped)

 

print("\n")

 

# unzipping values

namz, roll_noz, marksz = zip(*mapped)

 

print ("The unzipped result: \n",end="")

 

# printing initial lists

print ("The name list is : ",end="")

print (namz)

 

print ("The roll_no list is : ",end="")

print (roll_noz)

 

print ("The marks list is : ",end="")

print (marksz)  
  
---  
  
 __

 __

Output:

  

  

    
    
    The zipped result is : [('Manjeet', 4, 40), ('Nikhil', 1, 50), 
    ('Shambhavi', 3, 60), ('Astha', 2, 70)]
    
    
    The unzipped result: 
    The name list is : ('Manjeet', 'Nikhil', 'Shambhavi', 'Astha')
    The roll_no list is : (4, 1, 3, 2)
    The marks list is : (40, 50, 60, 70)
    

**Practical Applications :** There are many possible applications that can be
said to be exected using zip, be it **student database or scorecard** or any
other utility that requires mapping of groups. A small example of scorecard is
demonstrated below.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the application of

# zip()

 

# initializing list of players.

players = [ "Sachin", "Sehwag", "Gambhir", "Dravid",
"Raina" ]

 

# initializing their scores

scores = [100, 15, 17, 28, 43 ]

 

# printing players and scores.

for pl, sc in zip(players, scores):

 print ("Player : %s Score : %d" %(pl, sc))  
  
---  
  
 __

 __

Output:

    
    
    Player :  Sachin     Score : 100
    Player :  Sehwag     Score : 15
    Player :  Gambhir     Score : 17
    Player :  Dravid     Score : 28
    Player :  Raina     Score : 43
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

