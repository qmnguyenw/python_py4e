Maximum number of unique values in the array after performing given operations



Given an array **arr[]** of size **N** and every element in the array
**arr[]** is in the range **[1, N]** and the array may contain duplicates. The
task is to find the maximum number of unique values that can be obtained such
that the value at any index i can either be:

  * Increased by 1.
  * Decreased by 1.
  * Left as it is.

 **Note:** The operation can be performed only once with each index and have
to be performed for all the indices in the array arr[].

 **Examples:**

>  **Input:** arr[] = {1, 2, 4, 4}  
>  **Output:** 4  
>  **Explanation:**  
>  One way is to perform the following operations for the index:  
> 1: Leave the value at the first index(1) as it is.  
> 2: Leave the value at the second index(2) as it is.  
> 3: Leave the value at the third index(4) as it is.  
> 4: Increment the value at the fourth index(4) by 1.  
> Then the array becomes {1, 2, 4, 5} and there are 4 unique values.
>
>  **Input:** arr[]={3, 3, 3, 3}  
>  **Output:** 3  
>  **Explanation:**  
>  One way is to perform the following operations for the index:  
> 1: Leave the value at the first index(3) as it is.  
> 2: Decrement the value at the second index(3) by 1.  
> 3: Leave the value at the third index(3) as it is.  
> 4: Increment the value at the fourth index(3) by 1.  
> Then the array becomes {3, 2, 3, 4} and there are 3 unique values.
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * For some arbitrary element **X** present in the array at index **i** , we decide what operation to perform on it by taking the following things into consideration:
    1. We **decrement** the value **X** by 1 if the value ( **X – 1** ) is not present in the array and there are one or more other X’s present in the array at different indices.
    2. We **don’t change** the value **X** if the value **X** is present only once on the array.
    3. We **increment** the value **X** by 1 if the value ( **X + 1** ) is not present in the array and there are one or more other X’s present in the array at different indices.
  * By taking the above decisions for every element, we can be sure that the final count of unique elements which we get is the maximum.
  * However, to perform the above steps for every index and count the occurrences of the element X and continuously update the array arr[], the time taken would be quadratic which is not feasible for large-sized arrays.
  * One alternative to reduce the time complexity is to initially sort the array. By sorting, all the elements in the array are grouped and all the repeated values come together.
  * After sorting the array, since the range of the numbers is already given and it is fixed, a hash map can be used where the keys of the hash are the numbers in the range **[1, N]** and the value for each key is boolean which is used to determine if the key is present in the array or not.
  * In this problem, since the indices themselves are the keys of the hash, an array **freq[]** of size ( **N + 2** ) is used to implement the hash.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the maximum number of

// unique values in the array

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the maximum number of

// unique values in the array

int uniqueNumbers(int arr[], int n)

{

 // Sorting the given array

 sort(arr, arr + n);

 

 // This array will store the frequency

 // of each number in the array

 // after performing the given operation

 int freq[n + 2];

 

 // Initialising the array with all zeroes

 memset(freq, 0, sizeof(freq));

 

 // Loop to apply operation on

 // each element of the array

 for (int x = 0; x < n; x++) {

 

 // Incrementing the value at index x

 // if the value arr[x] - 1 is

 // not present in the array

 if (freq[arr[x] - 1] == 0) {

 freq[arr[x] - 1]++;

 }

 

 // If arr[x] itself is not present, then it

 // is left as it is

 else if (freq[arr[x]] == 0) {

 freq[arr[x]]++;

 }

 

 // If both arr[x] - 1 and arr[x] are present

 // then the value is incremented by 1

 else {

 freq[arr[x] + 1]++;

 }

 }

 

 // Variable to store the number of unique values

 int unique = 0;

 

 // Finding the unique values

 for (int x = 0; x <= n + 1; x++) {

 if (freq[x]) {

 unique++;

 }

 }

 

 // Returning the number of unique values

 return unique;

}

 

// Driver Code

int main()

{

 int arr[] = { 3, 3, 3, 3 };

 

 // Size of the array

 int n = 4;

 

 int ans = uniqueNumbers(arr, n);

 cout << ans;

 return 0;

}  
  
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

// Java program to find the maximum number of

// unique values in the array 

import java.util.*;

 

class GFG {

 

 // Function to find the maximum number of 

 // unique values in the array 

 static int uniqueNumbers(int arr[], int n) 

 { 

 // Sorting the given array 

 Arrays.sort(arr); 

 

 // This array will store the frequency 

 // of each number in the array 

 // after performing the given operation 

 int freq[] = new int[n + 2]; 

 

 // Initialising the array with all zeroes 

 for(int i = 0; i < n + 2; i++)

 freq[i] = 0;

 

 // Loop to apply operation on 

 // each element of the array 

 for (int x = 0; x < n; x++) { 

 

 // Incrementing the value at index x 

 // if the value arr[x] - 1 is 

 // not present in the array 

 if (freq[arr[x] - 1] == 0) { 

 freq[arr[x] - 1]++; 

 } 

 

 // If arr[x] itself is not present, then it 

 // is left as it is 

 else if (freq[arr[x]] == 0) { 

 freq[arr[x]]++; 

 } 

 

 // If both arr[x] - 1 and arr[x] are present 

 // then the value is incremented by 1 

 else { 

 freq[arr[x] + 1]++; 

 } 

 } 

 

 // Variable to store the number of unique values 

 int unique = 0; 

 

 // Finding the unique values 

 for (int x = 0; x <= n + 1; x++) { 

 if (freq[x] != 0) { 

 unique++; 

 } 

 } 

 

 // Returning the number of unique values 

 return unique; 

 } 

 

 // Driver Code 

 public static void main (String[] args)

 { 

 int []arr = { 3, 3, 3, 3 }; 

 

 // Size of the array 

 int n = 4; 

 

 int ans = uniqueNumbers(arr, n); 

 System.out.println(ans); 

 } 

}

 

// This code is contributed by Yash_R  
  
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

# Python program to find the maximum number of

# unique values in the array

 

# Function to find the maximum number of

# unique values in the array

def uniqueNumbers(arr, n):

 

 # Sorting the given array

 arr.sort()

 

 # This array will store the frequency

 # of each number in the array

 # after performing the given operation

 freq =[0]*(n + 2)

 

 # Loop to apply the operation on 

 # each element of the array

 for val in arr:

 

 # Incrementing the value at index x

 # if the value arr[x] - 1 is

 # not present in the array

 if(freq[val-1]== 0):

 freq[val-1]+= 1

 

 # If arr[x] itself is not present, then it

 # is left as it is

 elif(freq[val]== 0):

 freq[val]+= 1

 

 # If both arr[x] - 1 and arr[x] are present

 # then the value is incremented by 1

 else:

 freq[val + 1]+= 1

 

 # Variable to store the 

 # number of unique values

 unique = 0

 

 # Finding the number of unique values

 for val in freq:

 if(val>0):

 unique+= 1

 

 return unique

 

# Driver code

if __name__ == "__main__":

 arr =[3, 3, 3, 3]

 n = 4

 print(uniqueNumbers(arr, n))  
  
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

// C# program to find the maximum number of

// unique values in the array 

using System;

 

class GFG {

 

 // Function to find the maximum number of 

 // unique values in the array 

 static int uniqueNumbers(int []arr, int n) 

 { 

 // Sorting the given array 

 Array.Sort(arr); 

 

 // This array will store the frequency 

 // of each number in the array 

 // after performing the given operation 

 int []freq = new int[n + 2]; 

 

 // Initialising the array with all zeroes 

 for(int i = 0; i < n + 2; i++)

 freq[i] = 0;

 

 // Loop to apply operation on 

 // each element of the array 

 for (int x = 0; x < n; x++) { 

 

 // Incrementing the value at index x 

 // if the value arr[x] - 1 is 

 // not present in the array 

 if (freq[arr[x] - 1] == 0) { 

 freq[arr[x] - 1]++; 

 } 

 

 // If arr[x] itself is not present, then it 

 // is left as it is 

 else if (freq[arr[x]] == 0) { 

 freq[arr[x]]++; 

 } 

 

 // If both arr[x] - 1 and arr[x] are present 

 // then the value is incremented by 1 

 else { 

 freq[arr[x] + 1]++; 

 } 

 } 

 

 // Variable to store the number of unique values 

 int unique = 0; 

 

 // Finding the unique values 

 for (int x = 0; x <= n + 1; x++) { 

 if (freq[x] != 0) { 

 unique++; 

 } 

 } 

 

 // Returning the number of unique values 

 return unique; 

 } 

 

 // Driver Code 

 public static void Main (string[] args)

 { 

 int []arr = { 3, 3, 3, 3 }; 

 

 // Size of the array 

 int n = 4; 

 

 int ans = uniqueNumbers(arr, n); 

 Console.WriteLine(ans); 

 } 

}

 

// This code is contributed by Yash_R  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time Complexity Analysis:**

  * The time taken to sort the given array is **O(N * log(N))** where N is the size of the array.
  * The time taken to run a loop over the sorted array to perform the operations is **O(N)**.
  * The time taken to run a loop over the hash to count the unique values is **O(N)**.
  * Therefore, the overall time complexity is **O(N * log(N)) + O(N) + O(N)**. Since N * log(N) is greater, the final time complexity of the above approach is **O(N * log(N))**.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

