Lucky alive person in a circle | Set – 2



Given that N person (numbered 1 to N) standing as to form a circle. They all
have the gun in their hand which is pointed to their leftmost Partner.  
Every one shoots such that 1 shoot 2, 3 shoots 4, 5 shoots 6 …. (N-1)the shoot
N (if N is even otherwise N shoots 1).  
Again on the second iteration, they shoot the rest of remains as above
mentioned logic (now for n as even, 1 will shoot to 3, 5 will shoot to 7 and
so on).

The task is to find which person is the luckiest(didn’t die)?

 **Examples** :

>  **Input:** N = 3  
>  **Output:** 3  
> As N = 3 then 1 will shoot 2, 3 will shoot 1 hence 3 is the luckiest person.
>
>  **Input:** N = 8  
>  **Output:** 1  
> Here as N = 8, 1 will shoot 1, 3 will shoot 4, 5 will shoot 6, 7 will shoot
> 8, Again 1 will shoot 3, 5 will shoot 7, Again 1 will shoot 5 and hence 1 is
> the luckiest person.
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has already been discussed in Lucky alive person in a circle |
Code Solution to sword puzzle. In this post, a different approach is
discussed.

 **Approach:**

  1. Take the Binary Equivalent of N.
  2. Find its 1’s compliment and convert its equal decimal number N.
  3. find |N – N|.

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to convert string to number

int stringToNum(string s)

{

 

 // object from the class stringstream

 stringstream geek(s);

 

 // The object has the value 12345 and stream

 // it to the integer x

 int x = 0;

 geek >> x;

 

 return x;

}

 

// Function to convert binary to decimal

int binaryToDecimal(string n)

{

 int num = stringToNum(n);

 int dec_value = 0;

 

 // Initializing base value to 1, i.e 2^0

 int base = 1;

 

 int temp = num;

 while (temp) {

 int last_digit = temp % 10;

 temp = temp / 10;

 

 dec_value += last_digit * base;

 

 base = base * 2;

 }

 

 return dec_value;

}

 

string itoa(int num, string str, int base)

{

 int i = 0;

 bool isNegative = false;

 

 /* Handle 0 explicitly, otherwise 

 empty string is printed for 0 */

 if (num == 0) {

 str[i++] = '0';

 return str;

 }

 

 // In standard itoa(), negative numbers

 // are handled only with base 10.

 // Otherwise numbers are considered unsigned.

 if (num < 0 && base == 10) {

 isNegative = true;

 num = -num;

 }

 

 // Process individual digits

 while (num != 0) {

 int rem = num % base;

 str[i++] = (rem > 9) ? (rem - 10) + 'a' : rem + '0';

 num = num / base;

 }

 

 // If the number is negative, append '-'

 if (isNegative)

 str[i++] = '-';

 

 // Reverse the string

 reverse(str.begin(), str.end());

 

 return str;

}

 

char flip(char c)

{

 return (c == '0') ? '1' : '0';

}

 

// Function to find the ones complement

string onesComplement(string bin)

{

 int n = bin.length(), i;

 

 string ones = "";

 

 // for ones complement flip every bit

 for (i = 0; i < n; i++)

 ones += flip(bin[i]);

 

 return ones;

}

 

// Driver code

int main()

{

 // Taking the number of a person

 // standing in a circle.

 int N = 3;

 string arr = "";

 

 // Storing the binary equivalent in a string.

 string ans(itoa(N, arr, 2));

 

 // taking one's compelement and

 // convert it to decimal value

 int N_dash = binaryToDecimal(onesComplement(ans));

 

 int luckiest_person = N - N_dash;

 

 cout << luckiest_person;

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**  
Alternate Shorter Implementation :**  
The approach used here is same.

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

#include <bits/stdc++.h>

using namespace std;

 

int luckiest_person(int n)

{

 // to calculate the number of bits in

 // the binary equivalent of n

 int len = log2(n) + 1; 

 

 // Finding complement by inverting the

 // bits one by one from last

 int n2 = n;

 for (int i = 0; i < len; i++) {

 

 // XOR of n2 with (1<<i) to flip 

 // the last (i+1)th bit of binary equivalent of n2

 n2 = n2 ^ (1 << i); 

 } 

 

 // n2 will be the one's complement of n

 return abs(n - n2);

}

int main()

{

 int N = 3;

 int lucky_p = luckiest_person(N);

 cout << lucky_p;

 

 return 0;

}  
  
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

