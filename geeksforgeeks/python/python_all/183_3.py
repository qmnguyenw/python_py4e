Python Program for Cocktail Sort



Cocktail Sort is a variation of Bubble sort. The Bubble sort algorithm always
traverses elements from left and moves the largest element to its correct
position in first iteration and second largest in second iteration and so on.
Cocktail Sort traverses through a given array in both directions
alternatively.

 **  
Algorithm:**  
Each iteration of the algorithm is broken up into 2 stages:

  1. The first stage loops through the array from left to right, just like the Bubble Sort. During the loop, adjacent items are compared and if value on the left is greater than the value on the right, then values are swapped. At the end of first iteration, largest number will reside at the end of the array.
  2. The second stage loops through the array in opposite direction- starting from the item just before the most recently sorted item, and moving back to the start of the array. Here also, adjacent items are compared and are swapped if required.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for implementation of Cocktail Sort

 

def cocktailSort(a):

 n = len(a)

 swapped = True

 start = 0

 end = n-1

 while (swapped==True):

 

 # reset the swapped flag on entering the loop,

 # because it might be true from a previous

 # iteration.

 swapped = False

 

 # loop from left to right same as the bubble

 # sort

 for i in range (start, end):

 if (a[i] > a[i+1]) :

 a[i], a[i+1]= a[i+1], a[i]

 swapped=True

 

 # if nothing moved, then array is sorted.

 if (swapped==False):

 break

 

 # otherwise, reset the swapped flag so that it

 # can be used in the next stage

 swapped = False

 

 # move the end point back by one, because

 # item at the end is in its rightful spot

 end = end-1

 

 # from right to left, doing the same

 # comparison as in the previous stage

 for i in range(end-1, start-1,-1):

 if (a[i] > a[i+1]):

 a[i], a[i+1] = a[i+1], a[i]

 swapped = True

 

 # increase the starting point, because

 # the last stage would have moved the next

 # smallest number to its rightful spot.

 start = start+1

 

# Driver code to test above

a = [5, 1, 4, 2, 8, 0, 2]

cocktailSort(a)

print("Sorted array is:")

for i in range(len(a)):

 print ("%d" %a[i]),  
  
---  
  
 __

 __

 **Output:**

    
    
    Sorted array is:
    0 1 2 2 4 5 8
    

Please refer complete article on Cocktail Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

