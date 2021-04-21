Python – Remove records if Key not present



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to remove all the dictionaries in which particular key is not
present. This kind of problem can have application in many domains such as
day-day programming and data domain. Let’s discuss certain ways in which this
task can be performed.

>  **Input** : test_list = [{‘Gfg’ : 1, ‘Best’ : 3}, {‘Gfg’ : 3, ‘Best’ : 5},
> {‘Best’ : 3}] , K = ‘Best’  
>  **Output** : [{‘Gfg’ : 1, ‘Best’ : 3}, {‘Gfg’ : 3, ‘Best’ : 5}, {‘Best’ :
> 3}]
>
>  **Input** : test_list = [{‘Gfg’ : 1, ‘Best’ : 3}, {‘Gfg’ : 3, ‘Best’ : 5},
> {‘Best’ : 3}], K = ‘good’  
>  **Output** : []

 **Method #1 : Using list comprehension**  
This is one of the ways in which this task can be performed. In this, we
iterate and test for key presence using list comprehension and conditional
statement.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove records if Key not present

# Using list comprehension

 

# initializing list

test_list = [{'Gfg' : 1, 'Best' : 3},

 {'Gfg' : 3, 'Best' : 5}, 

 {'Best' : 3}]

 

# printing original list 

print("The original list : " + str(test_list))

 

# initializing K Key

K = 'Gfg'

 

# Remove records if Key not present

# Using list comprehension

res = [ele for ele in test_list if K in ele]

 

# printing result 

print("List after filteration : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [{'Gfg': 1, 'Best': 3}, {'Gfg': 3, 'Best': 5}, {'Best': 3}]
    List after filteration : [{'Gfg': 1, 'Best': 3}, {'Gfg': 3, 'Best': 5}]
    

