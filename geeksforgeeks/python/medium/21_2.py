Distribution of candies according to ages of students



Given two integer arrays ages and packs where ages store the ages of different
students and an element of pack stores the number of candies that packet has
(complete array represent the number of packets). The candies can be
distributed among students such that:

  1. Every student must get only one pack of candies.
  2. All students of the same age must get equal number of candies.
  3. A student which is older must get more candies than all the student who are younger than him.

The task is to determine whether it is possible to distribute candies in the
described manner. If possible then print Yes else print No.

 **Examples:**

> **Input:** ages[] = {5, 15, 10}, packs[] = {2, 2, 2, 3, 3, 4}  
> **Output:** YES  
> There are 3 students with age 5, 15 and 10.And there are 6 packets of
> candies containing 2, 2, 2, 3, 3, 4 candies respectively.  
> We will give one packet containing 2 candies to the student of age 5, one
> packet containing 3 candies to student with age 10 and give the packet
> containing 4 candies to student age 15
>
>  **Input:** ages[] = {5, 5, 6, 7}, packs[] = {5, 4, 6, 6}  
> **Output:** NO
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:**

  * Make 2 frequency arrays, one which will store the number of students with a particular age and one which will store the number of packets with a particular amount of candies.
  * Then traverse the frequency array for ages starting from the youngest age and for every age in ascending try to find the candy packets that are greater than or equal to the number of students for the selected age (starting from the least number of candies a packet has)
  * If the above case fails then the answer is No else repeat the above steps until all the student have got the candies and print Yes in the end.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <bits/stdc++.h>

using namespace std;

// Function to check The validity of distribution

void check_distribution(int n, int k,

 int age[], int candy[])

{

 

 // Stroring the max age of all

 // students + 1

 int mxage = *(std::max_element(

 age, age + n)) + 1;

 

 // Stroring the max candy + 1

 int mxcandy = *(std::max_element(

 candy, candy + k)) + 1;

 

 int fr1[mxage] = {0};

 int fr2[mxcandy] = {0};

 

 // Creating the frequency array of

 // the age of students

 for(int j = 0; j < n; j++)

 {

 fr1[age[j]] += 1;

 }

 

 // Creating the frequency array of the 

 // packets of candies

 for(int j = 0; j < k; j++)

 {

 fr2[candy[j]] += 1;

 }

 

 // Pointer to tell whether we have reached 

 // the end of candy frequency array

 k = 0;

 

 // Flag to tell if distribution

 // is possible or not

 bool Tf = true;

 for(int j = 0; j < mxage; j++)

 {

 if (fr1[j] == 0)

 continue;

 

 // Flag to tell if we can choose

 // some candy packets for the

 // students with age j

 bool flag = false;

 

 while (k < mxcandy)

 {

 

 // If the quantity of packets is

 // greater than or equal to the

 // number of students of age j,

 // then we can choose these 

 // packets for the students

 if (fr1[j] <= fr2[k])

 {

 flag = true;

 break;

 }

 k += 1;

 }

 

 // Start searching from k + 1

 // in next operation

 k = k + 1;

 

 // If we cannot choose any packets 

 // then the answer is NO

 if (flag == false)

 {

 Tf = false;

 break;

 }

 }

 

 if (Tf)

 cout << "YES" << endl;

 else

 cout << "NO" << endl;

}

// Driver code 

int main()

{

 int age[] = { 5, 15, 10 };

 int candy[] = { 2, 2, 2, 3, 3, 4 };

 

 int n = sizeof(age) / sizeof(age[0]);

 int k = sizeof(candy) / sizeof(candy[0]);

 

 check_distribution(n, k, age, candy);

 return 0;

}

// This code is contributed by divyeshrabadiya07  
  
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

// Java implementation of the approach

import java.util.*;

class Main

{

 // Function to check The validity of distribution

 public static void check_distribution(int n, int k,

 int age[], int candy[])

 {

 

 // Stroring the max age of all

 // students + 1

 int mxage = age[0];

 for(int i = 0; i < age.length; i++)

 {

 if(mxage < age[i])

 {

 mxage = age[i];

 }

 }

 

 // Stroring the max candy + 1

 int mxcandy = candy[0];

 for(int i = 0; i < candy.length; i++)

 {

 if(mxcandy < candy[i])

 {

 mxcandy = candy[i];

 }

 }

 

 int fr1[] = new int[mxage + 1];

 Arrays.fill(fr1, 0);

 int fr2[] = new int[mxcandy + 1];

 Arrays.fill(fr2, 0);

 

 

 // Creating the frequency array of

 // the age of students

 for(int j = 0; j < n; j++)

 {

 fr1[age[j]] += 1;

 }

 

 // Creating the frequency array of the 

 // packets of candies

 for(int j = 0; j < k; j++)

 {

 fr2[candy[j]] += 1;

 }

 

 // Pointer to tell whether we have reached 

 // the end of candy frequency array

 k = 0;

 

 // Flag to tell if distribution

 // is possible or not

 boolean Tf = true;

 for(int j = 0; j < mxage; j++)

 {

 if (fr1[j] == 0)

 continue;

 

 // Flag to tell if we can choose

 // some candy packets for the

 // students with age j

 boolean flag = false;

 

 while (k < mxcandy)

 {

 

 // If the quantity of packets is

 // greater than or equal to the

 // number of students of age j,

 // then we can choose these 

 // packets for the students

 if (fr1[j] <= fr2[k])

 {

 flag = true;

 break;

 }

 k += 1;

 }

 

 // Start searching from k + 1

 // in next operation

 k = k + 1;

 

 // If we cannot choose any packets 

 // then the answer is NO

 if (flag == false)

 {

 Tf = false;

 break;

 }

 }

 

 if (Tf)

 System.out.println("YES");

 else

 System.out.println("NO");

 }

 

 // Driver code

 public static void main(String[] args)

 {

 int age[] = { 5, 15, 10 };

 int candy[] = { 2, 2, 2, 3, 3, 4 };

 int n = age.length;

 int k = candy.length;

 

 check_distribution(n, k, age, candy);

 }

}

// This code is contributed by divyesh072019  
  
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

# Python3 implementation of the approach

# Function to check The validity of distribution

def check_distribution(n, k, age, candy):

 # Stroring the max age of all students + 1

 mxage = max(age)+1

 # Stroring the max candy + 1

 mxcandy = max(candy)+1

 fr1 = [0] * mxage

 fr2 = [0] * mxcandy

 # creating the frequency array of the

 # age of students

 for j in range(n):

 fr1[age[j]] += 1

 # Creating the frequency array of the

 # packets of candies

 for j in range(k):

 fr2[candy[j]] += 1

 # pointer to tell whether we have reached

 # the end of candy frequency array

 k = 0

 # Flag to tell if distribution is possible or not

 Tf = True

 for j in range(mxage):

 if (fr1[j] == 0):

 continue

 # Flag to tell if we can choose some

 # candy packets for the students with age j

 flag = False

 while (k < mxcandy):

 # If the quantity of packets is greater 

 # than or equal to the number of students

 # of age j, then we can choose these

 # packets for the students

 if (fr1[j] <= fr2[k]):

 flag = True

 break

 k += 1

 # Start searching from k + 1 in next operation

 k = k + 1

 # If we cannot choose any packets

 # then the answer is NO

 if (flag == False):

 Tf = False

 break

 if (Tf):

 print("YES")

 else:

 print("NO")

# Driver code

age = [5, 15, 10]

candy = [2, 2, 2, 3, 3, 4]

n = len(age)

k = len(candy)

check_distribution(n, k, age, candy)  
  
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

// C# implementation of the approach

using System.IO;

using System;

class GFG

{

 // Function to check The validity of distribution

 static void check_distribution(int n,int k,

 int[] age,int[] candy)

 {

 

 // Stroring the max age of all

 // students + 1

 int mxage = age[0];

 for(int i = 0; i < age.Length; i++)

 {

 if(mxage < age[i])

 {

 mxage = age[i];

 }

 }

 

 // Stroring the max candy + 1

 int mxcandy = candy[0];

 for(int i = 0; i < candy.Length; i++)

 {

 if(mxcandy < candy[i])

 {

 mxcandy = candy[i];

 }

 }

 

 int[] fr1 = new int[mxage + 1];

 Array.Fill(fr1, 0);

 int[] fr2 = new int[mxcandy + 1];

 Array.Fill(fr2, 0);

 

 // Creating the frequency array of

 // the age of students

 for(int j = 0; j < n; j++)

 {

 fr1[age[j]] += 1;

 }

 

 // Creating the frequency array of the 

 // packets of candies

 for(int j = 0; j < k; j++)

 {

 fr2[candy[j]] += 1;

 }

 

 // Pointer to tell whether we have reached 

 // the end of candy frequency array

 k = 0;

 

 // Flag to tell if distribution

 // is possible or not

 bool Tf = true;

 

 for(int j = 0; j < mxage; j++)

 {

 if(fr1[j] == 0)

 {

 continue;

 }

 

 // Flag to tell if we can choose

 // some candy packets for the

 // students with age j

 bool flag = false;

 

 while (k < mxcandy)

 {

 

 // If the quantity of packets is

 // greater than or equal to the

 // number of students of age j,

 // then we can choose these 

 // packets for the students

 if (fr1[j] <= fr2[k])

 {

 flag = true;

 break;

 }

 k += 1;

 }

 

 // Start searching from k + 1

 // in next operation

 k = k + 1;

 

 // If we cannot choose any packets 

 // then the answer is NO

 if (flag == false)

 {

 Tf = false;

 break;

 }

 

 }

 

 if(Tf)

 {

 Console.WriteLine("Yes");

 }

 else

 {

 Console.WriteLine("No");

 }

 

 }

 

 // Driver code

 static void Main()

 {

 int[] age = {5, 15, 10};

 int[] candy = { 2, 2, 2, 3, 3, 4 };

 int n = age.Length;

 int k = candy.Length;

 

 check_distribution(n, k, age, candy);

 }

}

// This code is contributed by avanitrachhadiya2155  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

 // Javascript implementation of the approach

 

 // Function to check The validity of distribution

 function check_distribution(n, k, age, candy)

 {

 

 // Stroring the max age of all

 // students + 1

 let mxage = age[0];

 for(let i = 0; i < age.length; i++)

 {

 if(mxage < age[i])

 {

 mxage = age[i];

 }

 }

 

 // Stroring the max candy + 1

 let mxcandy = candy[0];

 for(let i = 0; i < candy.length; i++)

 {

 if(mxcandy < candy[i])

 {

 mxcandy = candy[i];

 }

 }

 

 let fr1 = new Array(mxage + 1);

 fr1.fill(0);

 let fr2 = new Array(mxcandy + 1);

 fr2.fill(0);

 

 // Creating the frequency array of

 // the age of students

 for(let j = 0; j < n; j++)

 {

 fr1[age[j]] += 1;

 }

 

 // Creating the frequency array of the

 // packets of candies

 for(let j = 0; j < k; j++)

 {

 fr2[candy[j]] += 1;

 }

 

 // Pointer to tell whether we have reached

 // the end of candy frequency array

 k = 0;

 

 // Flag to tell if distribution

 // is possible or not

 let Tf = true;

 

 for(let j = 0; j < mxage; j++)

 {

 if(fr1[j] == 0)

 {

 continue;

 }

 

 // Flag to tell if we can choose

 // some candy packets for the

 // students with age j

 let flag = false;

 

 while (k < mxcandy)

 {

 

 // If the quantity of packets is

 // greater than or equal to the

 // number of students of age j,

 // then we can choose these

 // packets for the students

 if (fr1[j] <= fr2[k])

 {

 flag = true;

 break;

 }

 k += 1;

 }

 

 // Start searching from k + 1

 // in next operation

 k = k + 1;

 

 // If we cannot choose any packets

 // then the answer is NO

 if (flag == false)

 {

 Tf = false;

 break;

 }

 

 }

 

 if(Tf)

 {

 document.write("YES");

 }

 else

 {

 document.write("NO");

 }

 

 }

 

 let age = [5, 15, 10];

 let candy = [ 2, 2, 2, 3, 3, 4 ];

 let n = age.length;

 let k = candy.length;

 check_distribution(n, k, age, candy);

 

 // This code is contributed by suresh07.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    YES

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

