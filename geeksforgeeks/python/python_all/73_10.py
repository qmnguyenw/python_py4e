Find if array can be sorted by swaps limited to multiples of k



Given an array and a number k, the task is to check if the given array can be
sorted or not with limited swap operations. We can swap arr[i] only with
arr[i] or arr[i + k] or arr[i + 2*k] or arr[i + 3*k] and so on. In general an
element at index i can be swapped with elements at indexes i + j*k where j =
0, 1, 2, 3, …  
Note : Any number of swaps can be performed on the array.

 **Examples:**

>  **Input:** arr[8] = [1, 5, 6, 9, 2, 3, 5, 9], k = 3  
> **Output:** Possible to sort  
> **Explanation:** 1 5 6 9 2 3 5 9  
> 0 1 2 3 4 5 6 7 here k is 3  
> 0 can swap with 0 + 3 = (3) element  
> 1 can swap with 1 + 3 = (4) element  
> 2 can swap with 2 + 3 = (5) element  
> 3 can swap with 3 + 3 = (6) element  
> 4 can swap with 4 + 3 = (7) element  
> we can see that element at index 0, 3, 6 can swap with each other  
> we can see that element at index 1, 4, 7 can swap with each other  
> we can see that element at index 2, 5 can swap with each other  
> element 0 can never swap with 7, 1, 4, 2, 5  
> swap element at index (1, 4) 1 2 6 9 5 3 5 9  
> because sortarr[1] = 2  
> swap element at index (2, 5) 1 2 3 9 5 6 5 9  
> because sortarr[2] = 3  
> swap element at index (3, 6) 1 2 3 5 5 6 9 9  
> because sortarr[3] = 5  
> by swapping in this case we are able to reach 1 2 3 5 5 6 9 9
>
>  **Input :** arr=[1, 4, 2, 3], k = 2  
> **Output :** Not possible to sort  
> **Explanation:** 1 4 2 3  
> 0 1 2 3 where k is 2  
> 0 can swap with 0 + 2 = (2) element.  
> 1 can swap with 1 + 2 = (3) element.  
> we can see that element at index 0, 2 can swap with each other.  
> we can see that element at index 1, 3 can swap with each other.  
> no need to swap element at index (0, 2) 1 4 2 3  
> 0 1 2 3  
> at index 1 of sorted array is 2  
> 2 is not present in 1 + j * 2, where j = {0, 1}  
> so since 2 can never come at index 1 of array,  
> array can not be sort.  
> array is not sorted after swapping.
>
>  **Input :** arr[] = [1, 4, 2, 3], k = 1  
> **Output :** Possible to sort  
> **Explanation:** 1 4 2 3  
> 0 1 2 3 where k is 1  
> when k is 1 it is always possible to sort  
> because swap take place between adjacent element.  
>
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
1) Create sortArr[] as sorted version of given arr.  
2) Compare this array with sorted array.  
3) Iterate over for loop, to compare index i.  
4) Now index i, element is compared with  
index = i + j * k  
where j = 0, 1, 2…..  
5) if for particular i element of sortArr[i] match with sequence arr[index],
then flag is 1 and  
swap arr[i], arr[index]  
6) if no swap then flag is 0 and that means no element is found in sequence  
7) if flag is 0 break for loop and print Not possible  
8) else print Possible

## C++14

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

// CheckSort function

// To check if array can be sorted

void CheckSort(vector<int> arr,int k,int n){

 // sortarr is sorted array of arr

 vector<int> sortarr(arr.begin(),arr.end());

 sort(sortarr.begin(),sortarr.end());

 // if k = 1 then (always possible to sort)

 // swapping can easily give sorted

 // array

 if (k == 1)

 printf("yes");

 else

 {

 int flag = 0;

 

 // comparing sortarray with array

 for (int i = 0; i < n; i++)

 {

 flag = 0;

 // element at index j

 // must be in j = i + l * k form

 // where i = 0, 1, 2, 3...

 // where l = 0, 1, 2, 3, ..n-1

 for (int j = i; j < n; j += k)

 {

 //if element is present

 //then swapped

 if (sortarr[i] == arr[j]){

 swap(arr[i], arr[j]);

 flag = 1;

 break;

 }

 if (j + k >= n)

 break;

 }

 // if element of sorted array

 // does not found in its sequence

 // then flag remain zero

 // that means arr can not be

 // sort after swapping

 if (flag == 0)

 break;

 }

 // if flag is 0

 // Not possible

 // else Possible

 if (flag == 0)

 printf("Not possible to sort");

 else

 printf("Possible to sort");

 }

}

// Driver code

int main()

{

 // size of step

 int k = 3;

 // array initialized

 vector<int> arr ={1, 5, 6, 9, 2, 3, 5, 9};

 // length of arr

 int n =arr.size();

 // calling function

 CheckSort(arr, k, n);

 return 0;

}

// This code is contributed by mohit kumar 29  
  
---  
  
 __

 __

## Java

 __

 __  
 __

 __

 __  
 __  
 __

import java.util.*;

class GFG{

 

// CheckSort function

// To check if array can be sorted

public static void CheckSort(Vector<Integer> arr,

 int k, int n)

{

 

 // sortarr is sorted array of arr

 Vector<Integer> sortarr = new Vector<Integer>();

 for(int i = 0; i < arr.size(); i++)

 {

 sortarr.add(arr.get(i));

 }

 

 Collections.sort(sortarr);

 

 // If k = 1 then (always possible to sort)

 // swapping can easily give sorted

 // array

 if (k == 1)

 System.out.println("yes");

 else

 {

 int flag = 0;

 

 // Comparing sortarray with array

 for(int i = 0; i < n; i++)

 {

 flag = 0;

 

 // Element at index j

 // must be in j = i + l * k form

 // where i = 0, 1, 2, 3...

 // where l = 0, 1, 2, 3, ..n-1

 for(int j = i; j < n; j += k)

 {

 

 // If element is present

 //then swapped

 if (sortarr.get(i) == arr.get(j))

 {

 Collections.swap(arr, i, j);

 flag = 1;

 break;

 }

 if (j + k >= n)

 break;

 }

 

 // If element of sorted array

 // does not found in its sequence

 // then flag remain zero

 // that means arr can not be

 // sort after swapping

 if (flag == 0)

 break;

 }

 

 // If flag is 0

 // Not possible

 // else Possible

 if (flag == 0)

 System.out.println("Not possible to sort");

 else

 System.out.println("Possible to sort");

 }

}

// Driver code

public static void main(String[] args)

{

 

 // Size of step

 int k = 3;

 

 // Array initialized

 Vector<Integer> arr = new Vector<Integer>();

 arr.add(1);

 arr.add(5);

 arr.add(6);

 arr.add(9);

 arr.add(2);

 arr.add(3);

 arr.add(5);

 arr.add(9);

 

 // Length of arr

 int n = arr.size();

 

 // Calling function

 CheckSort(arr, k, n);

}

}

// This code is contributed by divyeshrabadiya07  
  
---  
  
 __

 __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# CheckSort function

# To check if array can be sorted

def CheckSort(arr, k, n):

 

 # sortarr is sorted array of arr

 sortarr = sorted(arr)

 

 # if k = 1 then (always possible to sort)

 # swapping can easily give sorted

 # array

 if (k == 1):

 print("yes")

 else:

 

 # comparing sortarray with array

 for i in range(0, n):

 flag = 0

 

 # element at index j

 # must be in j = i + l * k form

 # where i = 0, 1, 2, 3...

 # where l = 0, 1, 2, 3, ..n-1

 for j in range(i, n, k):

 # if element is present

 # then swapped

 if (sortarr[i] == arr[j]):

 arr[i], arr[j] = arr[j], arr[i]

 flag = 1

 break

 if (j + k >= n):

 break

 # if element of sorted array

 # does not found in its sequence

 # then flag remain zero

 # that means arr can not be

 # sort after swapping

 if (flag == 0):

 break

 

 # if flag is 0

 # Not possible

 # else Possible

 if (flag == 0):

 print("Not possible to sort")

 else:

 print("Possible to sort")

# Driver code

if __name__ == "__main__":

 # size of step

 k = 3

 # array initialized

 arr =[1, 5, 6, 9, 2, 3, 5, 9]

 # length of arr

 n = len(arr)

 # calling function

 CheckSort(arr, k, n)   
  
---  
  
__

__

## C#

 __

 __  
 __

 __

 __  
 __  
 __

using System;

using System.Collections;

using System.Collections.Generic;

class GFG{

 

// CheckSort function

// To check if array can be sorted

static void CheckSort(ArrayList arr, int k, int n)

{

 

 // sortarr is sorted array of arr

 ArrayList sortarr = new ArrayList(arr);

 sortarr.Sort();

 

 // If k = 1 then (always possible to sort)

 // swapping can easily give sorted

 // array

 if (k == 1)

 Console.Write("yes");

 else

 {

 int flag = 0;

 

 // Comparing sortarray with array

 for(int i = 0; i < n; i++)

 {

 flag = 0;

 

 // Element at index j

 // must be in j = i + l * k form

 // where i = 0, 1, 2, 3...

 // where l = 0, 1, 2, 3, ..n-1

 for(int j = i; j < n; j += k)

 {

 

 // If element is present

 // then swapped

 if ((int)sortarr[i] == (int)arr[j])

 {

 int tmp = (int)arr[i];

 arr[i] = (int)arr[j];

 arr[j] = tmp;

 flag = 1;

 break;

 }

 

 if (j + k >= n)

 {

 break;

 }

 }

 // If element of sorted array

 // does not found in its sequence

 // then flag remain zero

 // that means arr can not be

 // sort after swapping

 if (flag == 0)

 {

 break;

 }

 }

 

 // If flag is 0

 // Not possible

 // else Possible

 if (flag == 0)

 Console.Write("Not possible to sort");

 else

 Console.Write("Possible to sort");

 }

}

// Driver code

public static void Main(string[] args)

{

 

 // Size of step

 int k = 3;

 

 // Array initialized

 ArrayList arr = new ArrayList(){ 1, 5, 6, 9,

 2, 3, 5, 9 };

 

 // Length of arr

 int n = arr.Count;

 

 // Calling function

 CheckSort(arr, k, n);

}

}

// This code is contributed by rutvik_56  
  
---  
  
 __

 __

 **Output:**

    
    
    Possible to sort
    
    
    

**Performance Analysis:**  
**Time complexity:** O(N^2) Where N is size of array. worst case  
 **Auxiliary Space:** O(N) where N is size of array.  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

