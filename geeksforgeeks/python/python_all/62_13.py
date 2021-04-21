Python – Character coordinates in Matrix



Sometimes, while working with Python data, we can have a problem in which we
need to extract all the coordinates in Matrix, which are characters. This kind
of problem can have potential application in domains such as web development
and day-day programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [‘1G’, ’12F’, ‘231G’]  
>  **Output** : [(0, 1), (1, 2), (2, 3)]
>
>  **Input** : test_list = [‘G’, ‘F’, ‘G’]  
>  **Output** : [(0, 0), (1, 0), (2, 0)]

 **Method #1 : Usingenumerate() + list comprehension + isalpha()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of working with indices using enumerate and characters
filtering is done using isalpha().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Character coordinates in Matrix

# Using enumerate() + list comprehension + isalpha()

 

# initializing list

test_list = ['23f45.;4d', '5678d56d', '789', '5678g']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Character coordinates in Matrix

# Using enumerate() + list comprehension + isalpha()

res = [(x, y) for x, val in enumerate(test_list) 

 for y, chr in enumerate(val) if chr.isalpha()] 

 

# printing result 

print("Character indices : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : ['23f45.;4d', '5678d56d', '789', '5678g']
    Character indices : [(0, 2), (0, 8), (1, 4), (1, 7), (3, 4)]
    

