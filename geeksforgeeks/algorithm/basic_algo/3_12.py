Number of groups of magnets formed from N magnets



Given N magnets kept in a row one after another, either with a negative pole
on the left and positive pole on the right (01) or positive pole on the left
and negative pole on the right (10). Considering the fact that if 2
consecutive magnets have different poles facing each other, they form a group
and attract to each other, find the total number of groups possible.

 **Examples** :

    
    
    **Input** : N = 6
            magnets = {10, 10, 10, 01, 10, 10}
    **Output** : 3
    The groups are formed by the following magnets:
    1, 2, 3
    4
    5, 6
    
    **Input** : N = 5
            magnets = {10, 10, 10, 10, 10, 01}
    **Output** : 1
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Let us consider every pair of consecutive magnets, there are 2 possible cases:

  * Both of them have the same configuration: In this case, the connecting ends will have different poles and hence they would belong to the same group.
  * Both of them have different Configuration: In this case, the connecting ends will have the same pole and hence they would repel each other to form different groups.

So a new group will only be formed in the case when two consecutive magnets
have different configuration. So traverse the array of magnets and find the
number of consecutive pairs with the different configuration.

Below is the implementation of the above approach:  

## C++

  

  

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find number of groups

// of magnets formed from N magnets

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to count number of groups of

// magnets formed from N magnets

int countGroups(int n, string m[])

{

 // Intinially only a single group

 // for the first magnet

 int count = 1;

 

 for (int i = 1; i < n; i++)

 

 // Different configuration increases

 // number of groups by 1

 if (m[i] != m[i - 1])

 count++;

 

 return count;

}

 

// Driver Code

int main()

{

 int n = 6;

 

 string m[n] = { "10", "10", "10", "01", "10", "10"
};

 

 cout << countGroups(n, m);

 

 return 0;

}  
  
---  
  
 __

 __

