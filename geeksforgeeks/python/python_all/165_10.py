Python | Convert byteString key:value pair of dictionary to String



Given a dictionary having key:value pairs as byteString, the task is to
convert the key:value pair to string.

 **Examples:**

    
    
    **Input:** {b'EmplId': b'12345', b'Name': b'Paras', b'Company': b'Cyware' }
    **Output:** {'EmplId': '12345', 'Name': 'Paras', 'Company': 'Cyware'}
    
    **Input:** {b'Key1': b'Geeks', b'Key2': b'For', b'Key3': b'Geek' }
    **Output:** {'Key1':'Geeks', 'Key2':'For', 'Key3':'Geek' }
    

  
**Method #1:** By dictionary comprehension

 __

 __  
 __

 __

 __  
 __  
 __

# Python Code to convert ByteString key:value

# pair of dictionary to String.

 

# Initialising dictionary 

x = {b'EmplId': b'12345', b'Name': b'Paras',
b'Company': b'Cyware'}

 

# Converting

x = { y.decode('ascii'): x.get(y).decode('ascii') for y in
x.keys() }

 

# printing converted dictionary

print(x)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'Name': 'Paras', 'EmplId': '12345', 'Company': 'Cyware'}
    

  
**Method #2:** By iterating key and values

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python Code to convert ByteString key:value

# pair of dictionary to String.

 

# Initialising dictionary 

x = {b'EmplId': b'12345', b'Name': b'Paras',
b'Company': b'Cyware'}

 

# Initialising empty dictionary 

y = {}

 

# Converting

for key, value in x.items():

 y[key.decode("utf-8")] = value.decode("utf-8")

 

# printing converted dictionary

print(y)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'Company': 'Cyware', 'Name': 'Paras', 'EmplId': '12345'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

