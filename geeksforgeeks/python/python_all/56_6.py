Python – Extract Preceding Record from list values



Sometimes, while working with Tuple records, we can have a problem in which we
need to extract the record, which is preceeding to particular key provided.
This kind of problem can have application in domains such as web development
and day-day programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [(‘Gfg’, 3), (‘is’, 4), (‘best’, 1), (‘for’, 10),
> (‘geeks’, 11)], key = ‘geeks’  
>  **Output** : (‘for’, 10)
>
>  **Input** : test_list = [(‘Gfg’, 3), (‘is’, 4), (‘best’, 1), (‘for’, 10),
> (‘geeks’, 11)], key = ‘is’  
>  **Output** : (‘Gfg’, 3)

 **Method #1 : Usingzip() + enumerate() \+ loop**  
The combination of above functions can be used to perform this particular
task. In this, we create 2 lists, one with starting with next index. The
zip(), helps to connect them and return the desired result using enumerate()
for extracting index.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Preceeding Record

# Using zip() + enumerate() + loop

 

# initializing list

test_list = [('Gfg', 3), ('is', 4), ('best', 1),
('for', 10), ('geeks', 11)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing Key

key = 'for'

 

# Extract Preceding Record

# Using zip() + enumerate() + loop

for idx, (a, b) in enumerate(zip(test_list, test_list[1:])):

 if b[0] == key:

 res = (a[0], a[1])

 

# printing result 

print("The Preceeding record : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [('Gfg', 3), ('is', 4), ('best', 1), ('for', 10), ('geeks', 11)]
    The Preceeding record : ('best', 1)
    

