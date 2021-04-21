Python | Transcribing dictionary key



While working with data, we can come across various data interconversions that
we wish to perform. These can be of transcribing a key inside a list of
dictionary to the outer part for generalizations. This type of utility is
quite useful to know. Let’s discuss certain ways in which this can be
performed.

 **Method #1 : Using dictionary comprehension**

This particular task can be performed using the method of dictionary
comprehension in which we assign the keys and values from the desired lists
and remake the dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Dictionary key transcription

# dictionary comprehension

 

# initializing list

test_list = [{'state' : 'Haryana', 'capital' :
'Chandigarh', 'area' : 'North'},

 {'state' : 'Karnataka', 'capital' : 'Bengaluru', 'area'
: 'South'}]

 

# printing original list

print("The original list : " + str(test_list))

 

# using Dictionary comprehension

# Dictionary key transcription

res = { sub["state"]: {"capital": sub["capital"], "area":
sub["area"] }

 for sub in test_list }

 

# print result

print("The Dictionary after transcription of key : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [{‘capital’: ‘Chandigarh’, ‘state’: ‘Haryana’, ‘area’:
> ‘North’}, {‘capital’: ‘Bengaluru’, ‘state’: ‘Karnataka’, ‘area’: ‘South’}]
>
>  
>
>
>  
>
>
> The Dictionary after transcription of key : {‘Haryana’: {‘capital’:
> ‘Chandigarh’, ‘area’: ‘North’}, ‘Karnataka’: {‘capital’: ‘Bengaluru’,
> ‘area’: ‘South’}}

**Method #2 : Using dictionary comprehension +items() + get()**

This task can also be performed using a set of functions as well. This method
allows the flexibility of adding any key of choice. This is useful in cases
where keys are not known in advance.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Dictionary key transcription

# dictionary comprehension + items() + get()

 

# initializing list

test_list = [{'state' : 'Haryana', 'capital' :
'Chandigarh', 'area' : 'North'},

 {'state' : 'Karnataka', 'capital' : 'Bengaluru', 'area'
: 'South'}]

 

# printing original list

print("The original list : " + str(test_list))

 

# using dictionary comprehension + items() + get()

# Dictionary key transcription

res = {sub.get('state'): {key: val for key, val in
sub.items()

 if key != 'state'} for sub in test_list}

 

# print result

print("The Dictionary after transcription of key : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [{‘capital’: ‘Chandigarh’, ‘state’: ‘Haryana’, ‘area’:
> ‘North’}, {‘capital’: ‘Bengaluru’, ‘state’: ‘Karnataka’, ‘area’: ‘South’}]
>
> The Dictionary after transcription of key : {‘Haryana’: {‘capital’:
> ‘Chandigarh’, ‘area’: ‘North’}, ‘Karnataka’: {‘capital’: ‘Bengaluru’,
> ‘area’: ‘South’}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

