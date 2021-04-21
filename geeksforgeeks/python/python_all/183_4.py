Python Program for Bitonic Sort



 **Bitonic Sequence**

A sequence is called Bitonic if it is first increasing, then decreasing. In
other words, an array arr[0..n-i] is Bitonic if there exists an index i where
0<=i<=n-1 such that

    
    
     ** _x_** ** _0_** ** _ <= x_** ** _1_** ** _….. <= x_** ** _i_** ** _and  x_** ** _i_** ** _> = x_** ** _i+1_** ** _….. >= x_** ** _n-1_** ** __**

  1. A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty. Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty.
  2. A rotation of Bitonic Sequence is also bitonic.

 **Bitonic Sorting**

It mainly involves two steps.

  1. Forming a bitonic sequence (discussed above in detail). After this step we reach the fourth stage in below diagram, i.e., the array becomes {3, 4, 7, 8, 6, 5, 2, 1}
  2. Creating one sorted sequence from bitonic sequence : After first step, first half is sorted in increasing order and second half in decreasing order.  
We compare first element of first half with first element of second half, then
second element of first half with second element of second and so on. We
exchange elements if an element of first half is smaller.  
After above compare and exchange steps, we get two bitonic sequences in array.
See fifth stage in below diagram. In the fifth stage, we have {3, 4, 2, 1, 6,
5, 7, 8}. If we take a closer look at the elements, we can notice that there
are two bitonic sequences of length n/2 such that all elements in first bitnic
sequence {3, 4, 2, 1} are smaller than all elements of second bitonic sequence
{6, 5, 7, 8}.  
We repeat the same process within two bitonic sequences and we get four
bitonic sequences of length n/4 such that all elements of leftmost bitonic
sequence are smaller and all elements of rightmost. See sixth stage in below
diagram, arrays is {2, 1, 3, 4, 6, 5, 7, 8}.  
If we repeat this process one more time we get 8 bitonic sequences of size n/8
which is 1. Since all these bitonic sequence are sorted and every bitonic
sequence has one element, we get the sorted array.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for Bitonic Sort. Note that this program

# works only when size of input is a power of 2.

 

# The parameter dir indicates the sorting direction, ASCENDING

# or DESCENDING; if (a[i] > a[j]) agrees with the direction,

# then a[i] and a[j] are interchanged.*/

def compAndSwap(a, i, j, dire):

 if (dire==1 and a[i] > a[j]) or (dire==0 and
a[i] > a[j]):

 a[i],a[j] = a[j],a[i]

 

# It recursively sorts a bitonic sequence in ascending order,

# if dir = 1, and in descending order otherwise (means dir=0).

# The sequence to be sorted starts at index position low,

# the parameter cnt is the number of elements to be sorted.

def bitonicMerge(a, low, cnt, dire):

 if cnt > 1:

 k = cnt/2

 for i in range(low , low+k):

 compAndSwap(a, i, i+k, dire)

 bitonicMerge(a, low, k, dire)

 bitonicMerge(a, low+k, k, dire)

 

# This funcion first produces a bitonic sequence by recursively

# sorting its two halves in opposite sorting orders, and then

# calls bitonicMerge to make them in the same order

def bitonicSort(a, low, cnt,dire):

 if cnt > 1:

 k = cnt/2

 bitonicSort(a, low, k, 1)

 bitonicSort(a, low+k, k, 0)

 bitonicMerge(a, low, cnt, dire)

 

# Caller of bitonicSort for sorting the entire array of length N

# in ASCENDING order

def sort(a,N, up):

 bitonicSort(a,0, N, up)

 

# Driver code to test above

a = [3, 7, 4, 8, 6, 2, 1, 5]

n = len(a)

up = 1

 

sort(a, n, up)

print ("\n\nSorted array is")

for i in range(n):

 print("%d" %a[i]),  
  
---  
  
 __

 __

Please refer complete article onBitonic Sort for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

