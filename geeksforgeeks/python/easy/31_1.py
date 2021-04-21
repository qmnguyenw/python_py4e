List methods in Python



This article is extension of below articles :  
Python List  
List Methods in Python | Set 1 (in, not in, len(), min(), max()…)  
List Methods in Python | Set 2 (del, remove(), sort(), insert(), pop(),
extend()…)

 **Adding and Appending**

  *  **append():** Used for appending and adding elements to List.It is used to add elements to the last position of List.  
 **Syntax:**

    
         list.append (element)

 __

 __  
 __

 __

 __  
 __  
 __

# Adds List Element as value of List.

List = ['Mathematics', 'chemistry', 1997, 2000]

List.append(20544)

print(List)  
  
---  
  
 __

 __

Output:

    
        ['Mathematics', 'chemistry', 1997, 2000, 20544]
    

  * **insert():** Inserts an elements at specified position.  
 **Syntax:**

  

  

    
         list.insert(<position, element)

Note: Position mentioned should be within the range of List, as in this case
between 0 and 4, elsewise would throw IndexError.

 __

 __  
 __

 __

 __  
 __  
 __

List = ['Mathematics', 'chemistry', 1997, 2000]

# Insert at index 2 value 10087

List.insert(2,10087) 

print(List)   
  
---  
  
__

__

Output:

    
        ['Mathematics', 'chemistry', 10087, 1997, 2000, 20544]
    

  * **extend():** Adds contents to List2 to the end of List1.  
 **Syntax:**

    
        List1.extend(List2)

 __

 __  
 __

 __

 __  
 __  
 __

List1= [1, 2, 3]

List2 = [2, 3, 4, 5]

 

# Add List2 to List1

List1.extend(List2) 

print(List1)

 

# Add List1 to List2 now

List2.extend(List1) 

print(List2)  
  
---  
  
 __

 __

Output:

    
        [1, 2, 3, 2, 3, 4, 5]
    [2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]

 **sum(), count(), index(), min() and max() functions of List**

  *  **sum() :** Calculates sum of all the elements of List.  
 **Syntax:**

    
         sum(List)

 __

 __  
 __

 __

 __  
 __  
 __

List = [1, 2, 3, 4, 5]

print(sum(List))  
  
---  
  
 __

 __

Output:

    
        15
    

**What happens if numeric value is not used a parameter?**  
Sum is calculated only for Numeric values, elsewise throws TypeError.  
See example:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

List = ['gfg', 'abc', 3]

print(sum(List))  
  
---  
  
 __

 __

Output:

    
        Traceback (most recent call last):
      File "", line 1, in 
        sum(List)
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    

  * **count():** Calculates total occurrence of given element of List.  
 **Syntax:**

    
        List.count(element)

 __

 __  
 __

 __

 __  
 __  
 __

List = [1, 2, 3, 1, 2, 1, 2, 3, 2,
1]

print(List.count(1))  
  
---  
  
 __

 __

Output:

    
        4
    

  * **length:** Calculates total length of List.  
 **Syntax:**

    
        len(list_name)

 __

 __  
 __

 __

 __  
 __  
 __

List = [1, 2, 3, 1, 2, 1, 2, 3, 2,
1]

print(len(List))  
  
---  
  
 __

 __

Output:

    
        10
    

  * **index():** Returns the index of first occurrence. Start and End index are not necessary parameters.  
 **Syntax:**

    
        List.index(element[,start[,end]])

 __

 __  
 __

 __

 __  
 __  
 __

List = [1, 2, 3, 1, 2, 1, 2, 3, 2,
1]

print(List.index(2))  
  
---  
  
 __

 __

Output:

    
        1
    

Another example:

 __

 __  
 __

 __

 __  
 __  
 __

List = [1, 2, 3, 1, 2, 1, 2, 3, 2,
1]

print(List.index(2,2))  
  
---  
  
 __

 __

Output:

    
        4
    

__

__  
__

__

__  
__  
__

List = [1, 2, 3, 1, 2, 1, 2, 3, 2,
1]

 

"""index(element, start, end) : It will calculate till index end-1. """

 

# will check from index 2 to 4.

print("After checking in index range 2 to 4")

print(List.index(2,2,5))

 

# will check from index 2 to 3.

print("After checking in index range 2 to 3")

print(List.index(2,2,4))

   
  
---  
  
__

__

Output:

    
    
    After checking in index range 2 to 4
    4
    After checking in index range 2 to 3
    Traceback (most recent call last):
      File "", line 1, in 
        List.index(2,2,4)
    ValueError: tuple.index(x): x not in tuple
    

  * **min() :** Calculates minimum of all the elements of List.  
 **Syntax:**

    
        min(List)

 __

 __  
 __

 __

 __  
 __  
 __

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

print(min(List))  
  
---  
  
 __

 __

Output:

    
        1.054
    

  * **max():** Calculates maximum of all the elements of List.  
 **Syntax:**

    
        max(List)

 __

 __  
 __

 __

 __  
 __  
 __

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

print(max(List))  
  
---  
  
 __

 __

Output:

    
        5.33
    

**sort() and reverse() functions**

  *  **reverse():** Sort the given data structure (both tuple and list) in ascending order. Key and reverse_flag are not necessary parameter and reverse_flag is set to False, if nothing is passed through sorted().  
 **Syntax:**

    
        sorted([list[,key[,Reverse_Flag]]])
     list.sort([key,[Reverse_flag]])

 __

 __  
 __

 __

 __  
 __  
 __

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

 

#Reverse flag is set True

List.sort(reverse=True) 

 

#List.sort().reverse(), reverses the sorted list 

print(List)   
  
---  
  
__

__

Output:

    
        [5.33, 4.445, 3, 2.5, 2.3, 1.054]
    

__

__  
__

__

__  
__  
__

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

sorted(List)

print(List)  
  
---  
  
 __

 __

Output:

    
        [1.054, 2.3, 2.5, 3, 4.445, 5.33]
    

**Deletion of List Elements**

To Delete one or more elements, i.e. remove an element, many built in
functions can be used, such as pop() & remove() and keywords such as del.

  *  **pop():** Index is not a necessary parameter, if not mentioned takes the last index.  
 **Syntax:**

    
         list.pop([index])

Note: Index must be in range of the List, elsewise IndexErrors occurs.

 __

 __  
 __

 __

 __  
 __  
 __

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

print(List.pop())  
  
---  
  
 __

 __

Output:

    
        2.5
    

__

__  
__

__

__  
__  
__

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

print(List.pop(0))  
  
---  
  
 __

 __

Output:

    
        2.3
    

  * **del() :** Element to be deleted is mentioned using list name and index.  
 **Syntax:**

    
        del list.[index]

 __

 __  
 __

 __

 __  
 __  
 __

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

del List[0]

print(List)  
  
---  
  
 __

 __

Output:

    
        [4.445, 3, 5.33, 1.054, 2.5]

  *  **remove():** Element to be deleted is mentioned using list name and element.  
 **Syntax:**

    
         list.remove(element)

 __

 __  
 __

 __

 __  
 __  
 __

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]

List.remove(3)

print(List)  
  
---  
  
 __

 __

Output:

    
        [2.3, 4.445, 5.33, 1.054, 2.5]
    

This article is contributed by **Piyush Doorwar**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

