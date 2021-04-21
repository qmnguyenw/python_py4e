cmp(list) method in Python



cmp(list) is a method specified in Number in Python 2.  

The comparison of integral numbers have been discussed using cmp(). But many a
times, there is a need to compare the entire list that can be composed of
similar or different data types. In this case, different case scenarios occur
and having knowledge of them can at times prove to be quite handy.  
  
This function takes 2 lists as input and checks if the first argument list is
greater, equal or smaller than the second argument list.

> Syntax : **cmp(list1, list2)**
>
>  **Parameters :**  
>  **list1 :** The first argument list to be compared.  
>  **list2 :** The second argument list to be compared.
>
>  **Returns :** This function returns 1, if first list is “greater” than
> second list, -1 if first list is smaller than the second list else it
> returns 0 if both the lists are equal.
>
>  
>
>
>  
>

There are certain case scenarios when we need to decide whether one list is
smaller or greater or equal to the other list.

 **Case 1 :** When list contains just integers.

This is the case when all the elements in the list are of type integers and
hence when comparison is made, the number by number comparison is done left to
right, if we get a larger number at any particular index, we term it to be
greater and stop the further comparisons. If all the elements in both the list
are similar and one list is larger(in size) than the other list, larger list
is considered to be greater.

  
**Code #1 :** Demonstrating cmp() using only integers.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# the working of cmp()

# only integer case.

 

# initializing argument lists

list1 = [ 1, 2, 4, 3]

list2 = [ 1, 2, 5, 8]

list3 = [ 1, 2, 5, 8, 10]

list4 = [ 1, 2, 4, 3]

 

# Comparing lists 

print "Comparison of list2 with list1 : ",

print cmp(list2, list1)

 

# prints -1, because list3 has larger size than list2

print "Comparison of list2 with list3(larger size) : ",

print cmp(list2, list3)

 

# prints 0 as list1 and list4 are equal

print "Comparison of list4 with list1(equal) : ",

print cmp(list4, list1)  
  
---  
  
 __

 __

Output:

    
    
    Comparison of list2 with list1 :  1
    Comparison of list2 with list3(larger size) :  -1
    Comparison of list4 with list1(equal) :  0
    

**Case 2 :** When list contains multiple datatypes.  
The case when more than one datatypes, eg. string is contained in the string,
string is considered to be greater than integer, by this way, all datatypes
are alphabetically sorted in case of comparison. Size rule remains intact in
this case.

  
**Code #2 :** Demonstrating cmp() using multiple data types.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# the working of cmp()

# multiple data types

 

# initializing argument lists

list1 = [ 1, 2, 4, 10]

list2 = [ 1, 2, 4, 'a']

list3 = [ 'a', 'b', 'c']

list4 = [ 'a', 'c', 'b']

 

 

# Comparing lists 

# prints 1 because string

# at end compared to number

# string is greater

print "Comparison of list2 with list1 : ",

print cmp(list2, list1)

 

# prints -1, because list3

# has an alphabet at beginning

# even though size of list2

# is greater, Comparison

# is terminated at 1st

# element itself.

print "Comparison of list2 with list3(larger size) : ",

print cmp(list2, list3)

 

# prints -1 as list4 is greater than

# list3

print "Comparison of list3 with list4 : ",

print cmp(list3, list4)  
  
---  
  
 __

 __

Output:

    
    
    Comparison of list2 with list1 :  1
    Comparison of list2 with list3(larger size) :  -1
    Comparison of list3 with list4 :  -1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

