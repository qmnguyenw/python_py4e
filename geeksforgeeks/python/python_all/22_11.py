Python Program to Removes Every Element From A String List Except For a
Specified letter



Given a List that contains only string elements, the following program shows
methods how every other alphabet can be removed from elements except for a
specific one and then returns the output.

>  **Input** : test_list = [“google”, “is”, “good”, “goggled”, “god”], K = ‘g’  
> **Output** : [‘gg’, ”, ‘g’, ‘ggg’, ‘g’]  
> **Explanation** : All characters other than “g” removed.  
>  **Input** : test_list = [“google”, “is”, “good”, “goggled”, “god”], K = ‘o’  
> **Output** : [‘oo’, ”, ‘oo’, ‘o’, ‘o’]  
> **Explanation** : All characters other than “o” removed.

**Method 1 :** _Using_ _loop_

In this, we remake the string, by appending only K, and avoiding all other
strings from result.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = ["google", "is", "good", "goggled",
"god"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 'g'

 

res = []

for sub in test_list:

 

 # joining only K characters

 res.append(''.join([ele for ele in sub if ele == K]))

 

# printing result

print("Modified List : " + str(res))  
  
---  
  
 __

 __

