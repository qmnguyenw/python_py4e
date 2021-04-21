Python Program to reverses alternate strings and then concatenates all
elements



Given a String List, the following program returns a concatenated list of all
its string elements with its alternate elements reversed.

>  **Input** : test_str = ‘geeksgeeks best for geeks’  
> **Output** : skeegskeeg best rof geeks  
> **Explanation** : Alternate words reversed.  
>  **Input** : test_str = ‘geeksgeeks best geeks’  
> **Output** : skeegskeeg best skeeg  
> **Explanation** : Alternate words reversed.

**Method 1 :** _Using_ _reversed()_ _and_ _loop_

In this, we perform the task of reversing strings using reversed() and then
check for alternates using % operator and concatenate accordingly.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geeksgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# spliting string 

temp = test_str.split()

 

res = []

for idx in range(len(temp)):

 

 # reversing if alternate

 if idx % 2 == 0:

 res.append(''.join(list(reversed(temp[idx]))))

 else :

 res.append(temp[idx])

 

res = ' '.join(res)

 

# printing result 

print("Transformed String : " + str(res))   
  
---  
  
__

__

**Output:**

  

  

> The original string is : geeksgeeks is best for geeks
>
> Transformed String : skeegskeeg is tseb for skeeg

 **Method 2 :** _Using_ _slicing_ _and_ _list comprehension_

In this, we perform task fo reversal using slicing and then list comprehension
is used to perform the task done by loop, in shorthand.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing string

test_str = 'geeksgeeks is best for geeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# spliting string 

temp = test_str.split()

 

# list comprehension to solve problem in 1 liner

res = ' '.join([''.join(list(reversed(temp[idx]))) if idx
% 2 == 0 else temp[idx] for idx in
range(len(temp))])

 

# printing result 

print("Transformed String : " + str(res))   
  
---  
  
__

__

**Output:**

> The original string is : geeksgeeks is best for geeks
>
> Transformed String : skeegskeeg is tseb for skeeg

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

