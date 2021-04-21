Python Program for Pigeonhole Sort



Pigeonhole sorting is a sorting algorithm that is suitable for sorting lists
of elements where the number of elements and the number of possible key values
are approximately the same.  
It requires O( _n_ \+ _Range_ ) time where n is number of elements in input
array and \’Range\’ is number of possible values in array.

 **Working of Algorithm :**

  1. Find minimum and maximum values in array. Let the minimum and maximum values be \’min\’ and \’max\’ respectively. Also find range as \’max-min-1\’.
  2. Set up an array of initially empty “pigeonholes” the same size as of the range.
  3. Visit each element of the array and then put each element in its pigeonhole. An element arr[i] is put in hole at index arr[i] – min.
  4. Start the loop all over the pigeonhole array in order and put the elements from non- empty holes back into the original array.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to implement Pigeonhole Sort */

 

# source code : "https://en.wikibooks.org/wiki/

# Algorithm_Implementation/Sorting/Pigeonhole_sort"

def pigeonhole_sort(a):

 # size of range of values in the list 

 # (ie, number of pigeonholes we need)

 my_min = min(a)

 my_max = max(a)

 size = my_max - my_min + 1

 

 # our list of pigeonholes

 holes = [0] * size

 

 # Populate the pigeonholes.

 for x in a:

 assert type(x) is int, "integers only please"

 holes[x - my_min] += 1

 

 # Put the elements back into the array in order.

 i = 0

 for count in range(size):

 while holes[count] > 0:

 holes[count] -= 1

 a[i] = count + my_min

 i += 1

 

 

a = [8, 3, 2, 7, 4, 6, 8]

print("Sorted order is : ", end =" ")

 

pigeonhole_sort(a)

 

for i in range(0, len(a)):

 print(a[i], end =" ")

   
  
---  
  
__

__

**Output:**

    
    
    Sorted order is : 2 3 4 6 7 8 8 

Please refer complete article on Pigeonhole Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

