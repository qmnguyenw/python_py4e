Find the number in a range having maximum product of the digits



Given a range represented by two positive integers L and R. Find the number
lying in the range having the maximum product of the digits.  
 **Examples:**

    
    
    **Input :** L = 1, R = 10
    **Output :** 9
    
    **Input :** L = 51, R = 62
    **Output :** 59

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach :** The key idea here is to iterate over the digits of the number
R starting from the most significant digit. Going from left to right, i.e.
from most sigificant digit to the least significant digit, replace the current
digit with one less than current digit and replace all the digits after
current digit in the number with 9, since the number has already become
smaller than R at the current position so we can safely put any number in the
following digits to maximize the product of digits. Also, check if the
resulting number is greater than L to remain in the range and update the
maximum product.  
Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP Program to find the number in a

// range having maximum product of the

// digits

#include <bits/stdc++.h>

using namespace std;

// Returns the product of digits of number x

int product(int x)

{

 int prod = 1;

 while (x) {

 prod *= (x % 10);

 x /= 10;

 }

 return prod;

}

// This function returns the number having

// maximum product of the digits

int findNumber(int l, int r)

{

 // Converting both integers to strings

 string a = to_string(l);

 string b = to_string(r);

 // Let the current answer be r

 int ans = r;

 for (int i = 0; i < b.size(); i++) {

 if (b[i] == '0')

 continue;

 // Stores the current number having

 // current digit one less than current

 // digit in b

 string curr = b;

 curr[i] = ((curr[i] - '0') - 1) + '0';

 // Replace all following digits with 9

 // to maximise the product

 for (int j = i + 1; j < curr.size(); j++)

 curr[j] = '9';

 // Convert string to number

 int num = 0;

 for (auto c : curr)

 num = num * 10 + (c - '0');

 // Check if it lies in range and its product

 // is greater than max product

 if (num >= l && product(ans) < product(num))

 ans = num;

 }

 return ans;

}

// Driver Code

int main()

{

 int l = 1, r = 10;

 cout << findNumber(l, r) << endl;

 l = 51, r = 62;

 cout << findNumber(l, r) << endl;

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

// Java Program to find the number in a

// range having maximum product of the

// digits

class GFG

{

 

// Returns the product of digits of number x

static int product(int x)

{

 int prod = 1;

 while (x > 0)

 {

 prod *= (x % 10);

 x /= 10;

 }

 return prod;

}

// This function returns the number having

// maximum product of the digits

static int findNumber(int l, int r)

{

 // Converting both integers to strings

 //string a = l.ToString();

 String b = Integer.toString(r);

 // Let the current answer be r

 int ans = r;

 for (int i = 0; i < b.length(); i++)

 {

 if (b.charAt(i) == '0')

 continue;

 // Stores the current number having

 // current digit one less than current

 // digit in b

 char[] curr = b.toCharArray();

 curr[i] = (char)(((int)(curr[i] -

 (int)'0') - 1) + (int)('0'));

 // Replace all following digits with 9

 // to maximise the product

 for (int j = i + 1; j < curr.length; j++)

 curr[j] = '9';

 // Convert string to number

 int num = 0;

 for (int j = 0; j < curr.length; j++)

 num = num * 10 + (curr[j] - '0');

 // Check if it lies in range and its product

 // is greater than max product

 if (num >= l && product(ans) < product(num))

 ans = num;

 }

 return ans;

}

// Driver Code

public static void main (String[] args)

{

 int l = 1, r = 10;

 System.out.println(findNumber(l, r));

 l = 51;

 r = 62;

 System.out.println(findNumber(l, r));

}

}

// This code is contributed by chandan_jnu  
  
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

# Python3 Program to find the number

# in a range having maximum product

# of the digits

# Returns the product of digits

# of number x

def product(x) :

 

 prod = 1

 while (x) :

 prod *= (x % 10)

 x //= 10;

 

 return prod

# This function returns the number having

# maximum product of the digits

def findNumber(l, r) :

 

 # Converting both integers to strings

 a = str(l);

 b = str(r);

 # Let the current answer be r

 ans = r

 

 for i in range(len(b)) :

 if (b[i] == '0') :

 continue

 # Stores the current number having

 # current digit one less than current

 # digit in b

 curr = list(b)

 curr[i] = str(((ord(curr[i]) -

 ord('0')) - 1) + ord('0'))

 # Replace all following digits with 9

 # to maximise the product

 for j in range(i + 1, len(curr)) :

 curr[j] = str(ord('9'))

 

 # Convert string to number

 num = 0

 for c in curr :

 num = num * 10 + (int(c) - ord('0'))

 # Check if it lies in range and its

 # product is greater than max product

 if (num >= l and product(ans) < product(num)) :

 ans = num

 return ans

# Driver Code

if __name__ == "__main__" :

 

 l, r = 1, 10

 print(findNumber(l, r))

 l, r = 51, 62

 print(findNumber(l, r))

# This code is contributed by Ryuga  
  
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

// C# Program to find the number in a

// range having maximum product of the

// digits

using System;

class GFG

{

 

// Returns the product of digits of number x

static int product(int x)

{

 int prod = 1;

 while (x > 0)

 {

 prod *= (x % 10);

 x /= 10;

 }

 return prod;

}

// This function returns the number having

// maximum product of the digits

static int findNumber(int l, int r)

{

 // Converting both integers to strings

 //string a = l.ToString();

 string b = r.ToString();

 // Let the current answer be r

 int ans = r;

 for (int i = 0; i < b.Length; i++)

 {

 if (b[i] == '0')

 continue;

 // Stores the current number having

 // current digit one less than current

 // digit in b

 char[] curr = b.ToCharArray();

 curr[i] = (char)(((int)(curr[i] -

 (int)'0') - 1) + (int)('0'));

 // Replace all following digits with 9

 // to maximise the product

 for (int j = i + 1; j < curr.Length; j++)

 curr[j] = '9';

 // Convert string to number

 int num = 0;

 for (int j = 0; j < curr.Length; j++)

 num = num * 10 + (curr[j] - '0');

 // Check if it lies in range and its product

 // is greater than max product

 if (num >= l && product(ans) < product(num))

 ans = num;

 }

 return ans;

}

// Driver Code

static void Main()

{

 int l = 1, r = 10;

 Console.WriteLine(findNumber(l, r));

 l = 51;

 r = 62;

 Console.WriteLine(findNumber(l, r));

}

}

// This code is contributed by chandan_jnu  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP Program to find the number

// in a range having maximum product

// of the digits

// Returns the product of digits

// of number x

function product($x)

{

 $prod = 1;

 while ($x)

 {

 $prod *= ($x % 10);

 $x = (int)($x / 10);

 }

 

 return $prod;

}

// This function returns the number

// having maximum product of the digits

function findNumber($l, $r)

{

 // Let the current answer be r

 $ans = $r;

 

 // Converting both integers

 // to strings

 $a = strval($l);

 $b = strval($r);

 for ($i = 0; $i < strlen($b); $i++)

 {

 if ($b[$i] == '0')

 continue;

 // Stores the current number having

 // current digit one less than

 // current digit in b

 $curr = $b;

 $curr[$i] = chr(((ord($curr[$i]) -

 ord('0')) - 1) +

 ord('0'));

 // Replace all following digits

 // with 9 to maximise the product

 for ($j = $i + 1; $j < strlen($curr); $j++)

 $curr[$j] = '9';

 

 // Convert string to number

 $num = 0;

 for ($c = 0; $c < strlen($curr); $c++)

 $num = $num * 10 + (ord($curr[$c]) -

 ord('0'));

 // Check if it lies in range and its

 // product is greater than max product

 if ($num >= $l and

 product($ans) < product($num))

 $ans = $num;

 }

 return $ans;

}

// Driver Code

$l = 1;

$r = 10;

print(findNumber($l, $r) . "\n");

$l = 51;

$r = 62;

print(findNumber($l, $r));

// This code is contributed

// by chandan_jnu

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    9
    59

**Time Complexity** : O(18 * 18), if we are dealing with the numbers upto
1018.

 **Another Approach:** It can be solved using Digit Dp

  

  

 **Key Points of Observation:-**

 **1.** As we know we use **tight** in digit dp to check whether the range for
this digit is restricted or not,same here we will use **tight ta** and **tight
tb** ( **basically two tight conditions** ) ,where ta will tell us

the **lower_bound** of the digit and tb will tell us the **upper_bound** of
the digit and reason to use two tight values is that we have to calculate the
maximum product,it may be the case as:-

 **max(l,r) ≠ max(r) – max(l-1)** and our integer should lie in a range from l
to r.

 **2.** Let suppose the range values as, l=5 and r=15 , so to make size equal
we should append the zeroes in front of number after converting to string and
taking care of leading zeroes while calculating the answer,

 **Dp states include:-**

 **1) pos**

  * it will tell the position of index from left in the integer

 **2) ta**

  

  

  * it represents the lower_bound of a digit,we have to make sure number should be greater than or equal to { l }
  * Let suppose we are building a number greater than equal to 0055 and we have created a sequence like 005, so at the 4th place, we can’t put digit less than 5,that will only have digits between 5 to 9. So for checking this bound, we need ta.

    
    
    Example : Consider the value of  l = 005
    Index   : 0 1 2
    digits  : 0 0 5
    valid numbers like: 005,006,007,008...
    invalid numbers like: ...001,002,003,004

 **3) tb**

  * the upper_bound of a digit,we have to make sure number should be lesser than or equal to { r }
  * Again let suppose we are building a number lesser than equal to 526 and we have created a sequence like 52, so at the 3rd place, we can’t put digit greater than 6,there we can only place between 0 to 6. So for checking this bound, we need tb

    
    
    Example : Consider the value of  r = 150
    Index   : 0 1 2
    digits  : 1 5 0
    valid numbers like: ...148,149,150
    invalid numbers like: 151,152,153...

 **4) st**

  * used to check for leading zeroes( as 005 ~ 5)

 **3\. Constraints: l and r (1 ≤ l ≤ r ≤ 10^18)**

 **Algorithm:**

  * We will traverse i from start to end on the basis of **tight ta** and **tight tb** as:

    
    
    start = ta == 1 ? l[ pos ] - '0' : 0;
    end = tb ==1 ? r[ pos ] -'0'  : 9;

  * Firstly we will check for **leading zeroes** as :

    
    
    if ( st == 0 and i = 0) then multiply with 1,else multiply with i

  * For every position we will calculate the product of sequence and check whether it is the maximum product or not and store the corresponding number

    
    
    int ans = 0;
    for(int i = start; i <= end; i++){
      int val = i;
      if (st==0 and i==0) val = 1;
      ans = max (ans, val * solve (pos+1, ta&(i==start),tb&(i==end) ,st|i>0);
    }

 **C++ implementation:**

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP program for the above approach

#include <bits/stdc++.h>

using namespace std;

#define int long long int

// pair of array to store product and number

// dp[pos][tight1][tight2][start]

pair<int, string> dp[20][2][2][2];

pair<int, string> recur(string l, string r, int pos, int ta,

 int tb, int st)

{

 // Base case if pos is equal

 // to l or r size return

 // pair{1,""}

 if (pos == l.size()) {

 return { 1, "" };

 }

 // look up condition

 if (dp[pos][ta][tb][st].first != -1)

 return dp[pos][ta][tb][st];

 // Lower bound condition

 int start = ta ? l[pos] - '0' : 0;

 // Upper bound condition

 int end = tb ? r[pos] - '0' : 9;

 // To store the maximum product

 // initially its is set to -1

 int ans = -1;

 // To store the corresponding

 // number as number is large

 // so store it as a string

 string s = "";

 for (int i = start; i <= end; i++) {

 // Multiply with this val

 int val = i;

 // check for leading zeroes as 00005

 if (st == 0 and i == 0) {

 val = 1;

 }

 // Recursive call for next

 // position and store it in

 // a pair pair first gives

 // maximum product pair

 // second gives number which

 // gave maximum product

 pair<int, string> temp

 = recur(l, r, pos + 1, ta & (i == start),

 tb & (i == end), st | i > 0);

 // check if calculated product is greater than

 // previous calculated ans

 if (temp.first * val > ans) {

 ans = temp.first * val;

 // update string only if no leading zeroes

 // becoz no use to append the leading zeroes

 if (i == 0 and st == 0) {

 s = temp.second;

 }

 else {

 s = temp.second;

 s.push_back('0' + i);

 }

 }

 }

 // while returning memoize the ans

 return dp[pos][ta][tb][st] = { ans, s };

}

pair<int, string> solve(int a, int b)

{

 // convert int l to sting L and int r to string R ,

 // as integer value should be large

 string L = to_string(a);

 string R = to_string(b);

 // to make the size of strings

 // equal append zeroes in

 // front of string L

 if (L.size() < R.size()) {

 reverse(L.begin(), L.end());

 while (L.size() < R.size()) {

 L.push_back('0');

 }

 reverse(L.begin(), L.end());

 }

 // initialize dp

 // as it is pair of array so memset will not work

 for (int i = 0; i < 20; i++) {

 for (int j = 0; j < 2; j++) {

 for (int k = 0; k < 2; k++) {

 for (int l = 0; l < 2; l++) {

 dp[i][j][k][l].first = -1;

 }

 }

 }

 }

 // as we have to return pair second value

 // it's that number which gaves mximum product

 // initally pos=0,ta=1,tb=1,start=0(becoz number is not

 // started yet)

 pair<int, string> ans = recur(L, R, 0, 1, 1, 0);

 // reverse it becoz we were appending from right to left

 // in recursive call

 reverse(ans.second.begin(), ans.second.end());

 return { ans.first, ans.second };

}

signed main()

{

 // take l and r as input

 int l = 52, r = 62;

 cout << "l= " << l << "\n";

 cout << "r= " << r << "\n";

 pair<int, string> ans = solve(l, r);

 cout << "Maximum Product: " << ans.first << "\n";

 cout << "Number which gave maximum product: "

 << ans.second;

 return 0;

}  
  
---  
  
 __

 __

 **Output**

    
    
    l= 52
    r= 62
    Maximum Product: 45
    Number which gave maximum product: 59

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

