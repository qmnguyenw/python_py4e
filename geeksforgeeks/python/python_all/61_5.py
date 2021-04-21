Python – Successive Characters Frequency



Sometimes, while working with Python strings, we can have a problem in which
we need to find the frequency of next character of a particular word in
string. This is quite unique problem and has the potential for application in
day-day programming and web development. Let’s discuss certain ways in which
this task can be performed.

>  **Input** : test_str = ‘geeks are for geeksforgeeks’, que_word = “geek”  
>  **Output** : {‘s’: 3}
>
>  **Input** : test_str = ‘geek’, que_word = “geek”  
>  **Output** : {}

 **Method #1 : Using loop +count() + re.findall()**  
The combination of above methods constitute the brute force method to perform
this task. In this, we perform the task of counting using count(), and
character is searched using findall().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Successive Characters Frequency

# Using count() + loop + re.findall()

import re

 

# initializing string

test_str = 'geeksforgeeks is best for geeks. A geek should take
interest.'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing word 

que_word = "geek"

 

# Successive Characters Frequency

# Using count() + loop + re.findall()

temp = []

for sub in re.findall(que_word + '.', test_str):

 temp.append(sub[-1])

 

res = {que_word : temp.count(que_word) for que_word in temp}

 

# printing result 

print("The Characters Frequency is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original string is : geeksforgeeks is best for geeks. A geek should take interest.
    The Characters Frequency is : {'s': 3, ' ': 1}
    

