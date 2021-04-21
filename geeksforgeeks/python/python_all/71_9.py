Python – Check List elements from Dictionary List



Sometimes, while working with data, we can have a problem in which we need to
check for list element presence as a particular key in list of records. This
kind of problem can occur in domains in which data are involved like web
development and Machine Learning. Lets discuss certain ways in which this task
can be solved.

>  **Input** : test_list = [{‘Price’: 20, ‘Color’: ‘Orange’}, {‘Price’: 25,
> ‘Color’: ‘Yellow’}]  
>  **Output** : [True, False, True, False]
>
>  **Input** : test_list = [{‘Color’: ‘Pink’, ‘Price’: 50}]  
>  **Output** : [False, False, False, False]

 **Method #1 : Using loop**  
This is brute way to solve this problem. In this, we iterate will all the
dictionaries for each value from list and compare with the desired key and
return True for records that possess it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check List elements from Dictionary List

# Using loop

 

# helpr_func

def check_ele(ele, test_list):

 

 for sub in test_list:

 for item in sub.values():

 if ele == item:

 return True

 return False

 

# initializing list

test_list = [{'Name' : 'Apple', 'Price' : 18, 'Color'
: 'Red'},

 {'Name' : 'Mango', 'Price' : 20, 'Color' :
'Yellow'},

 {'Name' : 'Orange', 'Price' : 24, 'Color' :
'Orange'},

 {'Name' : 'Plum', 'Price' : 28, 'Color' : 'Red'}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Values list 

val_list = ['Yellow', 'Red', 'Orange', 'Green']

 

# Check List elements from Dictionary List

# Using loop

res = []

for ele in val_list:

 res.append(check_ele(ele, test_list))

 

# printing result 

print("The Association list in Order : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘Name’: ‘Apple’, ‘Color’: ‘Red’, ‘Price’: 18},
> {‘Name’: ‘Mango’, ‘Color’: ‘Yellow’, ‘Price’: 20}, {‘Name’: ‘Orange’,
> ‘Color’: ‘Orange’, ‘Price’: 24}, {‘Name’: ‘Plum’, ‘Color’: ‘Red’, ‘Price’:
> 28}]
>
> The Association list in Order : [True, True, True, False]

