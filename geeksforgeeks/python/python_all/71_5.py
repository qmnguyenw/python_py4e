Python – Convert List of Dictionaries to List of Lists



Sometimes, while working with Python data, we can have problem in which we
need to convert the list of dictionaries into list of lists, this can be
simplified by appending the keys just once if they are repetitive as mostly in
records, this saves memory space. This type of problem can have applications
in web development domain. Let’s discuss certain ways in which this task can
be performed.

>  **Input** : test_list = [{‘Gfg’: 123, ‘best’: 10}, {‘Gfg’: 51, ‘best’: 7}]  
>  **Output** : [[‘Gfg’, ‘best’], [123, 10], [51, 7]]
>
>  **Input** : test_list = [{‘Gfg’ : 12}]  
>  **Output** : [[‘Gfg’], [12]]

 **Method #1 : Using loop +enumerate()**  
The combination of above methods can be used to perform this task. In this, we
perform the task of iterating using loop and brute force with help of
enumerate() to perform appropriate append in result list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List of Dictionaries to List of Lists

# Using loop + enumerate()

 

# initializing list

test_list = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' :
20},

 {'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10},

 {'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert List of Dictionaries to List of Lists

# Using loop + enumerate()

res = []

for idx, sub in enumerate(test_list, start = 0):

 if idx == 0:

 res.append(list(sub.keys()))

 res.append(list(sub.values()))

 else:

 res.append(list(sub.values()))

 

# printing result 

print("The converted list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘Akash’: 18, ‘Nikhil’: 17, ‘Akshat’: 20}, {‘Akash’:
> 30, ‘Nikhil’: 21, ‘Akshat’: 10}, {‘Akash’: 12, ‘Nikhil’: 31, ‘Akshat’: 19}]  
> The converted list : [[‘Akash’, ‘Nikhil’, ‘Akshat’], [18, 17, 20], [30, 21,
> 10], [12, 31, 19]]

