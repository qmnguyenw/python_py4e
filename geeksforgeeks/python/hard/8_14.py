Program to generate all possible valid IP addresses from given string



Given a string containing only digits, restore it by returning all possible
valid IP address combinations.  
A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are
numbers from 0-255. The numbers cannot be 0 prefixed unless they are 0.

 **Examples :**

    
    
     **Input:** 25525511135
    **Output:** [“255.255.11.135”, “255.255.111.35”]
    **Explanation:**
    These are the only valid possible
    IP addresses.
    
    **Input:** "25505011535"
    **Output:** []
    **Explanation:**
    We cannot generate a valid IP
    address with this string.

First, we will place 3 dots in the given string and then try out all the
possible combinations for the 3 dots.  
Corner case for validity:

    
    
    For string "25011255255"
    25.011.255.255 is not valid as 011 is not valid.
    25.11.255.255 is not valid either as you are not
    allowed to change the string.
    250.11.255.255 is valid.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Split the string with ‘ . ‘ and then check for all corner
cases. Before entering the loop, check the size of the string. Generate all
the possible combinations using looping through the string. If IP is found to
be valid then return the IP address, else simply return the empty list.  
Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to generate all possible

// valid IP addresses from given string

#include <bits/stdc++.h>

using namespace std;

// Function checks whether IP digits

// are valid or not.

int is_valid(string ip)

{

 // Splitting by "."

 vector<string> ips;

 string ex = "";

 for (int i = 0; i < ip.size(); i++) {

 if (ip[i] == '.') {

 ips.push_back(ex);

 ex = "";

 }

 else {

 ex = ex + ip[i];

 }

 }

 ips.push_back(ex);

 // Checking for the corner cases

 // cout << ip << endl;

 for (int i = 0; i < ips.size(); i++) {

 // cout << ips[i] <<endl;

 if (ips[i].length() > 3

 || stoi(ips[i]) < 0

 || stoi(ips[i]) > 255)

 return 0;

 if (ips[i].length() > 1

 && stoi(ips[i]) == 0)

 return 0;

 if (ips[i].length() > 1

 && stoi(ips[i]) != 0

 && ips[i][0] == '0')

 return 0;

 }

 return 1;

}

// Function converts string to IP address

void convert(string ip)

{

 int l = ip.length();

 // Check for string size

 if (l > 12 || l < 4) {

 cout << "Not Valid IP Address";

 }

 string check = ip;

 vector<string> ans;

 // Generating different combinations.

 for (int i = 1; i < l - 2; i++) {

 for (int j = i + 1; j < l - 1; j++) {

 for (int k = j + 1; k < l; k++) {

 check = check.substr(0, k) + "."

 + check.substr(k, l - k + 2);

 check

 = check.substr(0, j) + "."

 + check.substr(j, l - j + 3);

 check

 = check.substr(0, i) + "."

 + check.substr(i, l - i + 4);

 // cout<< check <<endl;

 // Check for the validity of combination

 if (is_valid(check)) {

 ans.push_back(check);

 std::cout << check << '\n';

 }

 check = ip;

 }

 }

 }

}

// Driver code

int main()

{

 string A = "25525511135";

 string B = "25505011535";

 convert(A);

 convert(B);

 return 0;

}

// This code is contributed by Harshit  
  
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

// Java Program to generate all possible

// valid IP addresses from given string

import java.util.*;

class GFG {

 // Function to restore Ip Addresses

 public static ArrayList<String>

 restoreIpAddresses(String A)

 {

 if (A.length() < 3 || A.length() > 12)

 return new ArrayList<>();

 return convert(A);

 }

 private static ArrayList<String>

 convert(String s)

 {

 ArrayList<String> l = new ArrayList<>();

 int size = s.length();

 String snew = s;

 for (int i = 1; i < size - 2;

 i++) {

 for (int j = i + 1;

 j < size - 1; j++) {

 for (int k = j + 1;

 k < size; k++) {

 snew

 = snew.substring(0, k) + "."

 + snew.substring(k);

 snew

 = snew.substring(0, j) + "."

 + snew.substring(j);

 snew

 = snew.substring(0, i) + "."

 + snew.substring(i);

 if (isValid(snew)) {

 l.add(snew);

 }

 snew = s;

 }

 }

 }

 Collections.sort(l, new Comparator<String>() {

 public int compare(String o1, String o2)

 {

 String a1[] = o1.split("[.]");

 String a2[] = o2.split("[.]");

 int result = -1;

 for (int i = 0; i < 4

 && result != 0;

 i++) {

 result = a1[i].compareTo(a2[i]);

 }

 return result;

 }

 });

 return l;

 }

 private static boolean isValid(String ip)

 {

 String a[] = ip.split("[.]");

 for (String s : a) {

 int i = Integer.parseInt(s);

 if (s.length() > 3 || i < 0 || i > 255) {

 return false;

 }

 if (s.length() > 1 && i == 0)

 return false;

 if (s.length() > 1 && i != 0

 && s.charAt(0) == '0')

 return false;

 }

 return true;

 }

 // Driver Code

 public static void main(String[] args)

 {

 System.out.println(

 restoreIpAddresses(

 "25525511135")

 .toString());

 }

}

// This code is contributed by Nidhi Hooda.  
  
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

# Python3 code to check valid possible IP

# Function checks whether IP digits

# are valid or not.

def is_valid(ip):

 # Splitting by "."

 ip = ip.split(".")

 

 # Checking for the corner cases

 for i in ip:

 if (len(i) > 3 or int(i) < 0 or

 int(i) > 255):

 return False

 if len(i) > 1 and int(i) == 0:

 return False

 if (len(i) > 1 and int(i) != 0 and

 i[0] == '0'):

 return False

 

 return True

# Function converts string to IP address

def convert(s):

 

 sz = len(s)

 # Check for string size

 if sz > 12:

 return []

 snew = s

 l = []

 # Generating different combinations.

 for i in range(1, sz - 2):

 for j in range(i + 1, sz - 1):

 for k in range(j + 1, sz):

 snew = snew[:k] + "." + snew[k:]

 snew = snew[:j] + "." + snew[j:]

 snew = snew[:i] + "." + snew[i:]

 

 # Check for the validity of combination

 if is_valid(snew):

 l.append(snew)

 

 snew = s

 

 return l

# Driver code 

A = "25525511135"

B = "25505011535"

print(convert(A))

print(convert(B))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    ['255.255.11.135', '255.255.111.35']

 **Complexity Analysis:**

  *  **Time Complexity:** O(n^3), where n is the length of the string   
Three nested traversal of the string is needed, where n is always less than
12.

  *  **Auxiliary Space:** O(n).   
As as extra space is needed.

 **Another Efficient Approach (Dynamic Programming):** There is a dp approach
exist for this problem and can be solved in time complexity
O(n*4*3)=O(12n)=O(n) and space complexity O(4n).

**Approach:** We know that there are only 4 parts of the IP. We start
iterating from the end of string and goes to the start of string. We create a
dp 2D-array of size (4 x N). There can be only 2 values in the dp array i.e.
1(true) or 0(false). dp[0][i] tells if we can create 1 part of IP from the
substring starting from i to end of string. Similarly, dp[1][i] tells if we
can create 2 parts of IP from the substring starting from i to end of string.

After creating the dp array, we start creating the valid IP addresses. We
start from the bottom left corner of the 2D dp array. We only iterate 12
times(worst case) but those also will be the valid IP addresses because we
only form valid IP addresses.

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java Program to generate all possible

// valid IP addresses from given string

import java.util.*;

class GFG

{

 public static ArrayList<String> list;

 

 // Function to restore Ip Addresses

 public static ArrayList<String>

 restoreIpAddresses(String s)

 {

 int n = s.length();

 list = new ArrayList<>();

 if (n < 4 || n > 12)

 return list;

 

 // initialize the dp array

 int dp[][] = new int[4][n];

 for (int i = 0; i < 4; i++)

 {

 for (int j = n - 1; j >= 0; j--)

 {

 if (i == 0)

 {

 // take the substring

 String sub = s.substring(j);

 if (isValid(sub))

 {

 dp[i][j] = 1;

 }

 else if (j < n - 3)

 {

 break;

 }

 }

 else

 {

 if (j <= n - i)

 {

 for (int k = 1;

 k <= 3 && j + k <= n;

 k++)

 {

 String temp

 = s.substring(j, j + k);

 if (isValid(temp))

 {

 if (j + k < n

 && dp[i - 1][j + k]

 == 1)

 {

 dp[i][j] = 1;

 break;

 }

 }

 }

 }

 }

 }

 }

 

 if (dp[3][0] == 0)

 return list;

 

 

 // Call function createfromDp

 createIpFromDp(dp, 3, 0, s, "");

 return list;

 }

 

 public static void createIpFromDp(int dp[][],

 int r,

 int c, String s,

 String ans)

 {

 if (r == 0)

 {

 ans += s.substring(c);

 list.add(ans);

 return;

 }

 for (int i = 1;

 i <= 3 && c + i < s.length();

 i++)

 {

 if (isValid(s.substring(c, c + i))

 && dp[r - 1] == 1)

 {

 createIpFromDp(dp, r - 1, c + i, s,

 ans +

 s.substring(c, c + i)

 + ".");

 }

 }

 }

 

 

 private static boolean isValid(String ip)

 {

 String a[] = ip.split("[.]");

 for (String s : a)

 {

 int i = Integer.parseInt(s);

 if (s.length() > 3 || i < 0 || i > 255)

 {

 return false;

 }

 if (s.length() > 1 && i == 0)

 return false;

 if (s.length() > 1 && i != 0

 && s.charAt(0) == '0')

 return false;

 }

 return true;

 }

 // Driver Code

 public static void main(String[] args)

 {

 // Function call

 System.out.println(

 restoreIpAddresses("25525511135").toString());

 }

}

// This code is contributed by Nidhi Hooda.  
  
---  
  
 __

 __

 **Output**

    
    
    [255.255.11.135, 255.255.111.35]
    

**Complexity Analysis:**

  *  **Time Complexity** : O(n), where n is the length of the string. The dp array creation would take O(4*n*3) = O(12n) = O(n). Valid IP creation from dp array would take O(n).
  *  **Auxiliary Space** : O(n). As dp array has extra space of size (4 x n). It means O(4n).

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

