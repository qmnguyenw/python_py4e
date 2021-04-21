Count numbers whose maximum sum of distinct digit-sum is less than or equals M



Given an array of integers **arr[]** and a number **M** , the task is to find
the maximum count of the numbers whose sum of distinct digit-sum is less than
or equal to the given number **M**.

 **Examples:**

>  **Input:** arr[] = {1, 45, 16, 17, 219, 32, 22}, M = 10  
>  **Output:** 3  
>  **Explanation:**  
>  Digit-sum of the Array is – {1, 9, 7, 8, 12, 5, 4}  
> Max sum of distinct digit-sum whose sum less than M is {1 + 5 + 4}  
> Hence, the count of the such numbers is 3.
>
>  **Input:** arr[] = {32, 45}, M = 2  
>  **Output:** 0  
>  **Explanation:**  
>  Digit-sum of the Array is – {5, 9}  
> Max sum of distinct digit-sum less than M is 0  
> Hence, the count of the such numbers is 0.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**  
The idea is to find the digit-sum of every element in the array and then sort
the digit-sum array.

  

  

Now the problem boils down to count number of elements from the sorted
distinct digit sum array, with sum less than or equal to M.

To do this, take the minimum distinct digit-sums until the sum of such numbers
is less than or equal to the given number **M** and return the count of such
numbers.

 **Explanation with Example:**

    
    
    Given Array be - arr[] = {1, 45, 17, 32, 22}, M = 10
    
    Then Digit-sum of each number in the array - 
    Digit-sum(1) = 1
    Digit-sum(45) = 4 + 5 = 9
    Digit-sum(17) = 1 + 7 = 8
    Digit-sum(32) = 3 + 2 = 5
    Digit-sum(22) = 2 + 2 = 4
    
    After sorting the digit-sum array - 
    Digit-sum[] = {1, 4, 5, 8, 9}
    
    Then there are three numbers such that, 
    there sum is less than or equal to M = 10
    which is {1, 4, 5} 
    Sum = 1 + 4 + 5 = 10 &leq; M
    

**Algorithm:**

  * Find the digit-sum of every element of the array and store it in another array(say **digit-sum[]** )
  * Sort the **digit-sum[]** array in increasing order.
  * Remove Duplicate elements from the sorted digit-sum[] array such that there are only unqiue digit-sum.
  * Intialize a variable **sum** to 0 to store the current sum.
  * Iterate over the digit-sum[] array and add the elements to the **sum** untill the value of the **sum** is less than equal to **M** and increment the count.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find the

// Maximum count of numbers whose

// sum of distinct digit-sum less

// than or equal to the given number

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the 

// digit-sum of a number 

int SumofDigits(int digit)

{

 int sum = 0;

 

 // Loop to iterate the number

 // digit-wise to find digit-sum

 while (digit != 0) {

 

 // variable to store last digit

 int rem = digit % 10;

 sum += rem;

 digit /= 10;

 }

 return sum;

}

 

// Function to find the count of number

int findCountofNumbers(int arr[], 

 int n, int M){

 

 // Vector to store the Sum of Digits

 vector<int> SumDigits;

 

 // Sum of digits for each

 // element in vector

 for (int i = 0; i < n; i++) {

 int s = SumofDigits(arr[i]);

 SumDigits.push_back(s);

 }

 

 // Sorting the digitSum vector

 sort(SumDigits.begin(), SumDigits.end());

 

 // Removing the duplicate elements

 vector<int>::iterator ip;

 ip = unique(SumDigits.begin(), 

 SumDigits.end());

 SumDigits.resize(distance(

 SumDigits.begin(), ip)

 );

 

 // Count variable to store the Count

 int count = 0;

 int sum = 0;

 // Finding the Count of Numbers

 for (int i = 0; i < SumDigits.size(); i++) {

 if (sum > M)

 break;

 sum += SumDigits[i];

 if (sum <= M)

 count++;

 }

 return count;

}

 

// Driver Code

int main()

{

 

 int arr[] = { 1, 45, 16, 17, 

 219, 32, 22 }, M = 10;

 int n = sizeof(arr) / sizeof(arr[0]);

 

 // Function Call

 cout << findCountofNumbers(arr, n, M);

 return 0;

}  
  
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

# Python 3 implementation to find the

# Maximum count of numbers whose

# sum of distinct digit-sum less

# than or equal to the given number

 

# Function to find the 

# digit-sum of a number 

def SumofDigits( digit):

 

 sum = 0

 

 # Loop to iterate the number

 # digit-wise to find digit-sum

 while (digit != 0):

 

 # variable to store last digit

 rem = digit % 10

 sum += rem

 digit //= 10

 

 return sum

 

# Function to find the count of number

def findCountofNumbers(arr, n, M):

 

 # Vector to store the Sum of Digits

 SumDigits = []

 

 # Sum of digits for each

 # element in vector

 for i in range( n ):

 s = SumofDigits(arr[i])

 SumDigits.append(s)

 

 # Sorting the digitSum vector

 SumDigits.sort()

 

 # Removing the duplicate elements

 ip = list(set(SumDigits))

 

 # Count variable to store the Count

 count = 0

 sum = 0

 

 # Finding the Count of Numbers

 for i in range(len(SumDigits)):

 if (sum > M):

 break

 sum += SumDigits[i]

 if (sum <= M):

 count+=1

 

 return count

 

# Driver Code

if __name__ == "__main__":

 

 arr = [ 1, 45, 16, 17, 

 219, 32, 22 ]

 M = 10

 n = len(arr)

 

 # Function Call

 print( findCountofNumbers(arr, n, M))

 

# This ccode is contributed by chitranayal  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Performance Analysis:**

  *  **Time Complexity:** As in the given approach, we are using sorting which takes O(NlogN) in worst-case and the to find the digit-sum of every element takes O(N*K) where K is the maximum number of digits, Hence the time complexity will be **O(NlogN + N*k)**.
  *  **Auxiliary Space:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

