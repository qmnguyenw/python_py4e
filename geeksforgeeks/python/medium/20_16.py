Python | Removing duplicate dicts in list



Removal of duplicates is essential in many applications. List of dictionaries
are quite common and sometimes we require to duplicate the duplicated. Lets
discuss certain ways in which this can be achieved.  

 **Method #1 : Naive method**  
The basic method that comes to mind while performing this operation is the
naive method of iterating the list of dictionaries and manually removing the
duplicate dictionary and append in new list.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# remove duplicate dictionary

# using naive method 

 

# initializing list

test_list = [{"Akash" : 1}, {"Kil" : 2}, {"Akshat" :
3}, {"Kil" : 2}, {"Akshat" : 3}]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using naive method to 

# remove duplicates 

res_list = []

for i in range(len(test_list)):

 if test_list[i] not in test_list[i + 1:]:

 res_list.append(test_list[i])

 

# printing resultant list

print ("Resultant list is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [{'Akash': 1}, {'Kil': 2}, {'Akshat': 3}, {'Kil': 2}, {'Akshat': 3}]
    Resultant list is : [{'Akash': 1}, {'Kil': 2}, {'Akshat': 3}]
    

**Method #2 : Using list comprehension**  
The use of list comprehension and enumerate can possibly allow to achieve this
particular task in a single line and hence is of a good utility.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# remove duplicate dictionary

# using list comprehension

 

# initializing list

test_list = [{"Akash" : 1}, {"Kil" : 2}, {"Akshat" :
3}, {"Kil" : 2}, {"Akshat" : 3}]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using list comprehension to 

# remove duplicates 

res_list = [i for n, i in enumerate(test_list) if i not
in test_list[n + 1:]]

 

# printing resultant list

print ("Resultant list is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    Original list : [{'Akash': 1}, {'Kil': 2}, {'Akshat': 3}, {'Kil': 2}, {'Akshat': 3}]
    Resultant list is : [{'Akash': 1}, {'Kil': 2}, {'Akshat': 3}]
    

**Method #3 : Using frozenset**  
frozenset is used to assign a value to key in dictionary as a set. The
repeated entries of dictionary are hence ignored and hence solving this
particular task.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# remove duplicate dictionary

# using frozenset

 

# initializing list

test_list = [{"Akash" : 1}, {"Kil" : 2}, {"Akshat" :
3}, {"Kil" : 2}, {"Akshat" : 3}]

 

# printing original list 

print ("Original list : " + str(test_list))

 

# using frozenset to 

# remove duplicates 

res_list = {frozenset(item.items()) : item for item in
test_list}.values()

 

# printing resultant list

print ("Resultant list is : " + str(res_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original list : [{'Akash': 1}, {'Kil': 2}, {'Akshat': 3}, {'Kil': 2}, {'Akshat': 3}]
    Resultant list is : [{'Kil': 2}, {'Akshat': 3}, {'Akash': 1}]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

