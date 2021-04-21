Python | Avoiding quotes while printing strings



We often come across small issues that turns out to be big. While coding, the
small small tasks become sometimes tedious when not handled well. One among
those tasks is output formatting in which we require to omit the quotes while
printing any list elements. Let’s discuss certain ways in which this can be
performed.

 **Method #1 : Usingjoin()**  
We can simplify this task by using the join method in which we join the
strings in the list together by the separator being passed ( in this case
comma ) and hence solve the issue.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# avoiding printing last comma

# using join()

 

# initializing list

test_list = ['Geeks', 'For', 'Geeks']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using join()

# avoiding printing last comma

print ("The formatted output is : ")

print (', '.join(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Geeks', 'For', 'Geeks']
    The formatted output is : 
    Geeks, For, Geeks
    

**Method #2 : Usingprint() + sep**  
The print function can be used by passing the required container containing
the strings and * operator performs the task of joining each string in this
case. The separator being used is defined using the sep keyword passed as
second argument in print.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# avoiding printing last comma

# using print() + sep

 

# initializing list

test_list = ['Geeks', 'For', 'Geeks']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using print() + sep

# avoiding printing last comma

print ("The formatted output is : ")

print(*test_list, sep =', ')  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['Geeks', 'For', 'Geeks']
    The formatted output is : 
    Geeks, For, Geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

