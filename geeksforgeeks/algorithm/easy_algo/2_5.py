Dividing Sticks Problem



Given a list of integer each representing the length of each stick and an
integer which tells how many times we can break a stick into half parts, we
have to find maximum desired length sticks can be obtained from the group of
sticks.  
_**Note 1:** When we break a stick it gets converted into two half parts for
example for a stick of length 10 two sticks can be obtained of both 5 in
length and for a stick of length 5 two sticks will be obtained of length 2 and
3 respectively._  
 _ **Note 2:** Discarded part can’t be used again for making sticks such that
if a stick of length 11 is given we can break it into 5 and 6 of length pieces
then we have to discard one of the pieces which can’t be used further._  
 **Examples:**

>  **Input:**  
> list = [2, 3, 4, 11]  
> n = 2  
> desired_length = 3  
> **Output :**  
> Maximum sticks of desired length that can be obtained are : 3  
>  **Explanation :**  
> We already have one stick of length 3 and two more sticks can be obtained  
> by breaking stick of length 11 into [5, 3, 3] pieces therefore total sticks
> will be 3.
>
>  **Input:**  
> list = [2, 1, 4, 5]  
> n = 2  
> desired_length = 4  
> **Output :**  
> Maximum sticks of desired length that can be obtained are : 1  
>  **Explanation :**  
> We already have one stick of length 4 and no more sticks can be obtained  
> by breaking any stick therefore total sticks will be 1

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
To solve the problem mentioned above we will first do a linear search
operation to find all the sticks which have exact same length as of the
desired stick length and count them. We will then store the count in the
variable. Obviously we have to discard all the sticks which have a length less
than the desired length as with them we can’t make any desired length stick.
Then pass the value of sticks that have length more than the desired length to
a function which calculate how many sticks can be obtained by breaking them.
With the help of recursion find number of ways in which sticks can be
obtained.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

 

// Method to find number of sticks by breaking them 

int sticks_break(int stick_length,int n, 

 int desired_length)

{

 

 // If stick cant be break any more 

 if (n < 1)

 return 0;

 

 // Check if stick length became 

 // smaller than the desired length 

 if (stick_length < desired_length)

 return 0;

 

 // Check if stick length is even number 

 if (stick_length % 2 == 0)

 

 // Check if half of stick 

 // length is equal to desired length 

 if (stick_length / 2 == desired_length) 

 return 2;

 

 // Check if half of stick length 

 // is greater than the desired length 

 else if (stick_length / 2 > desired_length)

 return (sticks_break(stick_length / 2,

 n - 1, desired_length));

 

 // Check if stick length is odd number 

 if (stick_length % 2 != 0)

 

 // For odd number two halves will be 

 // generated checking if first half 

 // is equal to desired length 

 if (stick_length / 2 == desired_length) 

 return 1;

 

 // Checking if second half 

 // is equal to desired length 

 if (stick_length / 2 + 1 == desired_length)

 return 1;

 

 // Check if half of stick length 

 // is greater than the desired length 

 if (stick_length/2 > desired_length)

 return (max (sticks_break(

 stick_length / 2, n - 1,

 desired_length),

 sticks_break(

 stick_length / 2 + 1,

 n - 1, desired_length))); 

 

 return 0;

} 

 

// Method to find number of sticks 

int numberOfSticks(vector<int>list_length,

 int n, int desired_length)

{

 int count = 0;

 

 for(auto stick_lenght : list_length)

 {

 

 // Check if desired length is found 

 if (desired_length == stick_lenght)

 

 // Incrementing the count 

 count = count + 1;

 

 // Check if stick length is 

 // greater than desired length 

 else if (stick_lenght> desired_length) 

 

 // Incrementing count 

 // after break the sticks 

 count = count + sticks_break(

 stick_lenght, n,

 desired_length);

 } 

 

 // Return count 

 return count;

}

 

// Driver code

int main()

{

 

 // List of integers 

 vector<int>list_length = { 1, 2, 3, 21 };

 

 // Number of ways stick can be break 

 int n = 3;

 

 // Desired length

 int desired_length = 3;

 

 int count = numberOfSticks(list_length, n, 

 desired_length);

 

 // Print result

 cout << count << endl;

}

 

// This code is contributed by Stream_Cipher  
  
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

 

// Method to find number of sticks by breaking them 

static int sticks_break(int stick_length,

 int n, int desired_length)

{

 

 // If stick cant be break any more 

 if (n < 1)

 return 0;

 

 // Check if stick length became 

 // smaller than the desired length 

 if (stick_length < desired_length)

 return 0;

 

 // Check if stick length is even number 

 if (stick_length % 2 == 0)

 

 // Check if half of stick 

 // length is equal to desired length 

 if (stick_length / 2 == desired_length) 

 return 2;

 

 // Check if half of stick length 

 // is greater than the desired length 

 else if (stick_length / 2 > desired_length)

 return (sticks_break(stick_length / 2,

 n - 1, desired_length));

 

 // Check if stick length is odd number 

 if (stick_length % 2 != 0)

 

 // For odd number two halves will be 

 // generated checking if first half

 // is equal to desired length 

 if (stick_length / 2 == desired_length) 

 return 1;

 

 // Checking if second half 

 // is equal to desired length 

 if (stick_length / 2 + 1 == desired_length)

 return 1;

 

 // Check if half of stick length 

 // is greater than the desired length 

 if (stick_length/2 > desired_length)

 return (Math.max (sticks_break(

 stick_length / 2,

 n - 1, desired_length),

 sticks_break(

 stick_length / 2 + 1, 

 n - 1, desired_length))); 

 

 return 0;

} 

 

// Method to find number of sticks 

static int numberOfSticks(int list_length[],

 int n, int desired_length)

{

 int count = 0;

 

 for(int i = 0; i < list_length.length; i++)

 {

 

 // Check if desired length is found 

 if (desired_length == list_length[i])

 

 // Incrementing the count 

 count = count + 1;

 

 // Check if stick length is 

 // greater than desired length 

 else if (list_length[i]> desired_length)

 

 // Incrementing count 

 // after break the sticks 

 count = count + sticks_break(list_length[i],

 n, desired_length);

 } 

 

 // Return count 

 return count;

}

 

// Driver code

public static void main(String args[]) 

{ 

 

 // List of integers 

 int[] list_length = new int[]{ 1, 2, 3, 21 }; 

 

 // Number of ways stick can be break 

 int n = 3;

 

 // Desired length

 int desired_length = 3;

 

 int count = numberOfSticks(list_length, n,

 desired_length);

 

 // Print result

 System.out.println(count);

}

}

 

// This code is contributed by Stream_Cipher  
  
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

# method to find number of sticks by breaking them

def sticks_break(stick_length, n, desired_length): 

 

 # if stick cant be break any more 

 if n < 1: 

 

 return 0

 

 # check if stick length became 

 # smaller than the desired length 

 if stick_length < desired_length: 

 

 return 0

 

 # check if stick length is even number 

 if stick_length % 2 == 0: 

 

 # check if half of stick 

 # length is equal to desired length 

 if stick_length / 2 == desired_length: 

 

 return 2

 

 # check if half of stick length 

 # is greater than the desired length 

 elif stick_length / 2 > desired_length: 

 

 return sticks_break(stick_length / 2, n-1, desired_length) 

 

 # check if stick length is odd number 

 if stick_length % 2 != 0: 

 

 # for odd number two halves will be generated 

 # checking if first half is equal to desired length 

 if stick_length // 2 == desired_length: 

 

 return 1

 

 # checking if second half 

 # is equal to desired length 

 if stick_length // 2 + 1 == desired_length: 

 

 return 1

 

 # check if half of stick length 

 # is greater than the desired length 

 if stick_length//2 > desired_length: 

 

 return max (sticks_break(stick_length//2, n-1,
desired_length), sticks_break(stick_length//2 + 1, n-1,
desired_length)) 

 

 

 return 0

 

 

# method to find number of sticks 

def numberOfSticks(list_length, n, desired_length): 

 

 count = 0

 

 for stick_length in list_length: 

 

 # check if desired length is found 

 if desired_length == stick_length: 

 

 # incrementing the count 

 count = count + 1

 

 # check if stick length is 

 # greater than desired length 

 elif stick_length > desired_length: 

 

 # incrementing count 

 # after break the sticks 

 count = count + sticks_break(stick_length, n, desired_length) 

 

 # return count 

 return count 

 

# driver code 

if __name__ == "__main__": 

 

 # list of integers 

 list_length =[1, 2, 3, 21] 

 

 # number of ways stick can be break 

 n = 3

 

 # desired length 

 desired_length = 3

 

 count = numberOfSticks(list_length, n, desired_length) 

 

 # print result 

 print(str(count))   
  
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

class GFG{

 

// Method to find number of sticks by breaking them 

static int sticks_break(int stick_length,

 int n, int desired_length)

{

 

 // If stick cant be break any more 

 if (n < 1 )

 return 0;

 

 // Check if stick length became 

 // smaller than the desired length 

 if (stick_length < desired_length)

 return 0;

 

 // Check if stick length is even number 

 if (stick_length % 2 == 0)

 

 // Check if half of stick 

 // length is equal to desired length 

 if (stick_length / 2 == desired_length) 

 return 2;

 

 // Check if half of stick length 

 // is greater than the desired length 

 else if (stick_length / 2 > desired_length)

 return (sticks_break(stick_length / 2,

 n - 1, desired_length));

 

 // Check if stick length is odd number 

 if (stick_length % 2 != 0)

 

 // For odd number two halves will be

 // generated checking if first half 

 // is equal to desired length 

 if (stick_length / 2 == desired_length) 

 return 1;

 

 // Checking if second half 

 // is equal to desired length 

 if (stick_length / 2 + 1 == desired_length)

 return 1;

 

 // Check if half of stick length 

 // is greater than the desired length 

 if (stick_length/2 > desired_length)

 return (Math.Max(sticks_break(

 stick_length / 2,

 n - 1, desired_length),

 sticks_break(

 stick_length / 2 + 1, 

 n - 1, desired_length))); 

 

 return 0;

} 

 

// Method to find number of sticks 

static int numberOfSticks(int []list_length,

 int n, int desired_length)

{

 int count = 0;

 for(int i = 0; i < list_length.Length; i++)

 {

 

 // Check if desired length is found 

 if (desired_length == list_length[i])

 

 // Incrementing the count 

 count = count + 1;

 

 // Check if stick length is 

 // greater than desired length 

 else if (list_length[i]> desired_length) 

 

 // Incrementing count 

 // after break the sticks 

 count = count + sticks_break(list_length[i],

 n, desired_length);

 } 

 

 // Return count 

 return count;

}

 

// Driver code

public static void Main() 

{ 

 

 // list of integers 

 int []list_length = { 1, 2, 3, 21 };

 

 // Number of ways stick can be break 

 int n = 3;

 

 // Desired length

 int desired_length = 3;

 int count = numberOfSticks(list_length,

 n, desired_length);

 

 // Print result

 Console.WriteLine(count); 

}

}

 

// This code is contributed by Stream_Cipher  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

