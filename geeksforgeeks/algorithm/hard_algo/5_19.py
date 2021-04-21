Program to generate all possible valid IP addresses from given string | Set 2



Given a string containing only digits, restore it by returning all possible
valid IP address combinations.  
A valid IP address must be in the form of **A.B.C.D** , where **A** , **B** ,
**C** and **D** are numbers from **0 – 255**. The numbers cannot be **0**
prefixed unless they are **0**.

 **Examples:**

>  **Input:** str = “25525511135”  
>  **Output:**  
>  255.255.11.135  
> 255.255.111.35
>
>  **Input:** str = “11111011111”  
>  **Output:**  
>  111.110.11.111  
> 111.110.111.11

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This problem can be solved using backtracking. In each call we
have three options to create a single block of numbers of a valid ip address:

  

  

  1. Either select only a single digit, add a dot and move onto selecting other blocks (further function calls).
  2. Or select two digits at the same time, add a dot and move further.
  3. Or select three consecutive digits and move for the next block.

At the end of the fourth block, if all the digits have been used and the
address generated is a valid ip-address then add it to the results and then
backtrack by removing the digits selected in the previous call.

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

#include <iostream>

#include <vector>

using namespace std;

 

// Function to get all the valid ip-addresses

void GetAllValidIpAddress(vector<string>& result,

 string givenString, int index,

 int count, string ipAddress)

{

 

 // If index greater than givenString size

 // and we have four block

 if (givenString.size() == index && count == 4) {

 

 // Remove the last dot

 ipAddress.pop_back();

 

 // Add ip-address to the results

 result.push_back(ipAddress);

 return;

 }

 

 // To add one index to ip-address

 if (givenString.size() < index + 1)

 return;

 

 // Select one digit and call the

 // same function for other blocks

 ipAddress = ipAddress

 + givenString.substr(index, 1) + '.';

 GetAllValidIpAddress(result, givenString, index + 1,

 count + 1, ipAddress);

 

 // Backtrack to generate another poosible ip address

 // So we remove two index (one for the digit

 // and other for the dot) from the end

 ipAddress.erase(ipAddress.end() - 2, ipAddress.end());

 

 // Select two consecutive digits and call

 // the same function for other blocks

 if (givenString.size() < index + 2

 || givenString[index] == '0')

 return;

 ipAddress = ipAddress + givenString.substr(index, 2) + '.';

 GetAllValidIpAddress(result, givenString, index + 2,

 count + 1, ipAddress);

 

 // Backtrack to generate another poosible ip address

 // So we remove three index from the end

 ipAddress.erase(ipAddress.end() - 3, ipAddress.end());

 

 // Select three consecutive digits and call

 // the same function for other blocks

 if (givenString.size() < index + 3

 || stoi(givenString.substr(index, 3)) > 255)

 return;

 ipAddress += givenString.substr(index, 3) + '.';

 GetAllValidIpAddress(result, givenString, index + 3,

 count + 1, ipAddress);

 

 // Backtrack to generate another poosible ip address

 // So we remove four index from the end

 ipAddress.erase(ipAddress.end() - 4, ipAddress.end());

}

 

// Driver code

int main()

{

 string givenString = "25525511135";

 

 // Fill result vector with all valid ip-addresses

 vector<string> result;

 GetAllValidIpAddress(result, givenString, 0, 0, "");

 

 // Print all the generated ip-addresses

 for (int i = 0; i < result.size(); i++) {

 cout << result[i] << "\n";

 }

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

# Python3 implementation of the approach

 

# Function to get all the valid ip-addresses 

def GetAllValidIpAddress(result, givenString,

 index, count, ipAddress) :

 

 # If index greater than givenString size 

 # and we have four block 

 if (len(givenString) == index and count == 4) :

 

 # Remove the last dot 

 ipAddress.pop(); 

 

 # Add ip-address to the results 

 result.append(ipAddress); 

 return; 

 

 # To add one index to ip-address 

 if (len(givenString) < index + 1) :

 return; 

 

 # Select one digit and call the 

 # same function for other blocks 

 ipAddress = (ipAddress +

 givenString[index : index + 1] + ['.']); 

 

 GetAllValidIpAddress(result, givenString, index + 1,

 count + 1, ipAddress); 

 

 # Backtrack to generate another poosible ip address 

 # So we remove two index (one for the digit 

 # and other for the dot) from the end 

 ipAddress = ipAddress[:-2];

 

 # Select two consecutive digits and call 

 # the same function for other blocks 

 if (len(givenString) < index + 2 or

 givenString[index] == '0') :

 return; 

 

 ipAddress = ipAddress + givenString[index:index + 2] +
['.']; 

 GetAllValidIpAddress(result, givenString, index + 2, 

 count + 1, ipAddress); 

 

 # Backtrack to generate another poosible ip address 

 # So we remove three index from the end 

 ipAddress = ipAddress[:-3]; 

 

 # Select three consecutive digits and call 

 # the same function for other blocks 

 if (len(givenString)< index + 3 or

 int("".join(givenString[index:index + 3])) > 255) :

 return; 

 ipAddress += givenString[index:index + 3] + ['.']; 

 GetAllValidIpAddress(result, givenString, 

 index + 3, count + 1, ipAddress); 

 

 # Backtrack to generate another poosible ip address 

 # So we remove four index from the end 

 ipAddress = ipAddress[:-4]; 

 

# Driver code 

if __name__ == "__main__" : 

 givenString = list("25525511135"); 

 

 # Fill result vector with all valid ip-addresses 

 result = [] ; 

 GetAllValidIpAddress(result, givenString, 0, 0, []); 

 

 # Print all the generated ip-addresses 

 for i in range(len(result)) :

 print("".join(result[i])); 

 

# This code is contributed by Ankitrai01  
  
---  
  
 __

 __

 **Output:**

    
    
    255.255.11.135
    255.255.111.35
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

