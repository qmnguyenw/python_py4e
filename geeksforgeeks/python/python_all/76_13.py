Python – Extract target key from other key values



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to extract particular key on basis of other matching record keys
when there is exact match. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop + conditions**  
This is one of the ways in which this task can be performed. In this, we
iterate for the dictionary keys and check for each keys for matching values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract target key from other key values

# Using loop + condition

 

# initializing list

test_list = [{ 'name' : 'Manjeet', 'English' : 14,
'Maths' : 2}, 

 { 'name' : 'Akshat', 'English' : 7, 'Maths' :
13},

 { 'name' : 'Akash', 'English' : 1, 'Maths' : 17},

 { 'name' : 'Nikhil', 'English' : 10, 'Maths' :
18}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing filter items 

filt_key = {'English' : 7, 'Maths' : 13}

 

# Extract target key from other key values

# Using loop + condition

res = []

for sub in test_list:

 if sub["English"] == filt_key["English"] and
sub["Maths"] == filt_key["Maths"]:

 res.append(sub['name'])

 

# printing result 

print("The filtered result : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘name’: ‘Manjeet’, ‘English’: 14, ‘Maths’: 2},
> {‘name’: ‘Akshat’, ‘English’: 7, ‘Maths’: 13}, {‘name’: ‘Akash’, ‘English’:
> 1, ‘Maths’: 17}, {‘name’: ‘Nikhil’, ‘English’: 10, ‘Maths’: 18}]  
> The filtered result : [‘Akshat’]

  

  

**Method #2 : Using loop + conditions ( for multiple/unknown keys )**  
This performs the task in similar way in which above method does. The
advantage of using this method is that one doesn’t need to feed all keys
manually in conditions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract target key from other key values

# Using loop + conditions ( for multiple / unknown keys )

 

def hlper_func(test_keys, filt_key):

 for key in test_keys.keys():

 if key in filt_key:

 if test_keys[key] != int(filt_key[key]):

 return False

 return True

 

# initializing list

test_list = [{ 'name' : 'Manjeet', 'English' : 14,
'Maths' : 2}, 

 { 'name' : 'Akshat', 'English' : 7, 'Maths' :
13},

 { 'name' : 'Akash', 'English' : 1, 'Maths' : 17},

 { 'name' : 'Nikhil', 'English' : 10, 'Maths' :
18}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing filter items 

filt_key = {'English' : 7, 'Maths' : 13}

 

# Extract target key from other key values

# Using loop + conditions ( for multiple / unknown keys )

res = []

for sub in test_list:

 if hlper_func(sub, filt_key):

 res.append(sub['name'])

 

# printing result 

print("The filtered result : " + str(res))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘name’: ‘Manjeet’, ‘English’: 14, ‘Maths’: 2},
> {‘name’: ‘Akshat’, ‘English’: 7, ‘Maths’: 13}, {‘name’: ‘Akash’, ‘English’:
> 1, ‘Maths’: 17}, {‘name’: ‘Nikhil’, ‘English’: 10, ‘Maths’: 18}]  
> The filtered result : [‘Akshat’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

