Binary Search In JavaScript



Binary Search is searching technique which works on Divide and Conquer
approach. It used to search any element in a sorted array.

As compared to linear, binary search is much faster with Time Complexity of
O(logN) whereas linear search algorithm works in O(N) time complexity.

In this article, implement of Binary Search in Javascript using both iterative
and recursive ways are discussed.

Given a sorted array of numbers. The task is to search a given element
![x](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-4fdd037713ae07c442e4e7d7e059e818_l3.png) in the array
using Binary search.

 **Examples** :

  

  

    
    
    Input : arr[] = {1, 3, 5, 7, 8, 9}
            x = 5
    Output : Element found!
    
    Input : arr[] = {1, 3, 5, 7, 8, 9}
            x = 6
    Output : Element not found!
    

**Note:** Assuming the array is sorted.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Recursive Approach :**

  1.  _BASE CONDITION:_ If starting index is greater than ending index return false.
  2. Compute the middle index.
  3. Compare the middle element with number x. If equal return true.
  4. If greater, call the same function with ending index = middle-1 and repeat step 1.
  5. If smaller, call the same function with starting index = middle+1 and repeat step 1.

Below is the implementation of Binary Search(Recursive Approach) in
JavaScript:

 __

 __  
 __

 __

 __  
 __  
 __

<script>

let recursiveFunction = function (arr, x, start, end) {

 

 // Base Condition

 if (start > end) return false;

 

 // Find the middle index

 let mid=Math.floor((start + end)/2);

 

 // Compare mid with given key x

 if (arr[mid]===x) return true;

 

 // If element at mid is greater than x,

 // search in the left half of mid

 if(arr[mid] > x) 

 return recursiveFunction(arr, x, start, mid-1);

 else

 

 // If element at mid is smaller than x,

 // search in the right half of mid

 return recursiveFunction(arr, x, mid+1, end);

}

 

// Driver code

let arr = [1, 3, 5, 7, 8, 9];

let x = 5;

 

if (recursiveFunction(arr, x, 0, arr.length-1))

 document.write("Element found!<br>");

else document.write("Element not found!<br>");

 

x = 6;

 

if (recursiveFunction(arr, x, 0, arr.length-1))

 document.write("Element found!<br>");

else document.write("Element not found!<br>");

</script>   
  
---  
  
__

__

**Output** :

    
    
    Element found!
    Element not found!
    

**Time Complexity:** O(logN).

 **Iterative Approach :** In this iterative approach instead of recursion, we
will use a while loop and the loop will run until it hits the base condition
i.e start becomes greater than end.

Below is the implementation of Binary Search(Iterative Approach) in
JavaScript:

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// Iterative function to implement Binary Search

let iterativeFunction = function (arr, x) {

 

 let start=0, end=arr.length-1;

 

 // Iterate while start not meets end

 while (start<=end){

 

 // Find the mid index

 let mid=Math.floor((start + end)/2);

 

 // If element is present at mid, return True

 if (arr[mid]===x) return true;

 

 // Else look in left or right half accordingly

 else if (arr[mid] < x) 

 start = mid + 1;

 else

 end = mid - 1;

 }

 

 return false;

}

 

// Driver code

let arr = [1, 3, 5, 7, 8, 9];

let x = 5;

 

if (iterativeFunction(arr, x, 0, arr.length-1))

 document.write("Element found!<br>");

else document.write("Element not found!<br>");

 

x = 6;

 

if (iterativeFunction(arr, x, 0, arr.length-1))

 document.write("Element found!<br>");

else document.write("Element not found!<br>");

</script>   
  
---  
  
__

__

**Output** :

    
    
    Element found!
    Element not found!
    

**Time Complexity:** O(logN).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

