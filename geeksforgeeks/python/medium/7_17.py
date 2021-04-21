Methods of Ordered Dictionary in Python



An **OrderedDict** **** is a dict that remembers the order that keys were
first inserted. If a new entry overwrites an existing entry, the original
insertion position is left unchanged. Deleting an entry and reinserting it
will move it to the end. Ordered dictionary somehow can be used in the place
where there is a use of hash Map and queue. It has characteristics of both
into one. Like queue, it **remembers the order** and it also allows insertion
and deletion at both ends. And like dictionary is also behaves as a **hash
map.**

 **Note:** From Python 3.6 onwards, order is retained for keyword arguments
passed to the OrderedDict constructor, refer PEP-468.

## Methods of ordered Dictionary

Let’s look at various methods offered by the ordered dictionary.

  *  **popitem():**

This method is used to delete a key from the beginning.

 **Syntax:**

  

  

    
        popitem(last = True)                      
    

If the last is False then this method would delete a key from the beginning of
the dictionary. This serves as FIFO(First In First Out) in the queue otherwise
it method would delete the key from the end of the dictionary.

 **Time Complexity :** O(1).

For Better Understanding have a look at the code.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections import OrderedDict

 

 

ord_dict = OrderedDict().fromkeys('GeeksForGeeks')

print("Original Dictionary")

print(ord_dict)

 

# Pop the key from last

ord_dict.popitem()

print("\nAfter Deleting Last item :")

print(ord_dict)

 

# Pop the key from beginning

ord_dict.popitem(last = False)

print("\nAfter Deleting Key from Beginning :")

print(ord_dict)  
  
---  
  
 __

 __

 **Output:**

> Original Dictionary  
> OrderedDict([(‘G’, None), (‘e’, None), (‘k’, None), (‘s’, None), (‘F’,
> None), (‘o’, None), (‘r’, None)])
>
> After Deleting Last item :  
> OrderedDict([(‘G’, None), (‘e’, None), (‘k’, None), (‘s’, None), (‘F’,
> None), (‘o’, None)])
>
> After Deleting Key from Beginning :  
> OrderedDict([(‘e’, None), (‘k’, None), (‘s’, None), (‘F’, None), (‘o’,
> None)])

  *  **move_to_end():**

This method is used to move an existing key of the dictionary either to end or
to the begining. There are two versions of this function –

  

  

 **Syntax:**

    
        move_to_end(key, last = True)
    

If last is True then this method would move an existing key of the dictionary
in the end otherwise it would move an existing key of dictionary in the
beginning. If the key is moved at the beginning then it serves as FIFO ( First
In First Out ) in queue.

 **Time Complexity :** O(1)

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections import OrderedDict

 

 

ord_dict = OrderedDict().fromkeys('GeeksForGeeks')

print("Original Dictionary")

print(ord_dict)

 

# Move the key to end

ord_dict.move_to_end('G')

print("\nAfter moving key 'G' to end of dictionary :")

print(ord_dict)

 

# Move the key to beginning

ord_dict.move_to_end('k', last = False)

print("\nAfter moving Key in the Beginning :")

print(ord_dict)  
  
---  
  
 __

 __

 **Output:**

> Original Dictionary  
> OrderedDict([(‘G’, None), (‘e’, None), (‘k’, None), (‘s’, None), (‘F’,
> None), (‘o’, None), (‘r’, None)])
>
> After moving key ‘G’ to end of dictionary :  
> OrderedDict([(‘e’, None), (‘k’, None), (‘s’, None), (‘F’, None), (‘o’,
> None), (‘r’, None), (‘G’, None)])
>
> After moving Key in the Beginning :  
> OrderedDict([(‘k’, None), (‘e’, None), (‘s’, None), (‘F’, None), (‘o’,
> None), (‘r’, None), (‘G’, None)])

 **Working of move_to_end() function**

Basically, this method looks up a link in a linked list in a dictionary
self.__map and updates the previous and next pointers for the link and its
neighbours. It deletes that element from it’s position and add it to end or
beginning depending upon parameter value. Since all of the operations below
take constant time, the complexity of _OrderedDict.move_to_end()_ is constant
as well.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

