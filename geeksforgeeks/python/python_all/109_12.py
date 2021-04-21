Python – Truth values deletion in List



Due to the upcoming of Machine Learning, focus has now moved on handling the
values than ever before, the reason behind this is that it is the essential
step of data preprocessing before it is fed into further techniques to
perform. Hence removal of values in essential, be it None, or sometimes Truth,
and knowledge of it is a must. Lets discuss certain ways in which this is
achieved.

 **Method #1 : Naive Method**  
In naive method, we iterate through whole list and append all the filtered,
None values into a new list, hence ready to be performed with subsequent
operations.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Truth values deletion in List

# using naive method 

 

# initializing list

test_list = [1, None, 4, None, False, 5, 8,
False]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using naive method 

# Truth values deletion in List

res = []

for val in test_list:

 if not val:

 res.append(val)

 

# printing result

print ("List after removal of Truth values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, None, 4, None, False, 5, 8, False]
    List after removal of Truth values : [None, None, False, False]
    

**Method #2 : Using list comprehension**  
The longer task of using the naive method and increasing line of codes can be
done in compact way using this method. We just check for None values and
construct the new filtered list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Truth values deletion in List

# using list comprehension

 

# initializing list

test_list = [1, None, 4, None, False, 5, 8,
False]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list comprehension

# Truth values deletion in List

res = [i for i in test_list if not i]

 

# printing result

print ("List after removal of Truth values : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, None, 4, None, False, 5, 8, False]
    List after removal of Truth values : [None, None, False, False]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

