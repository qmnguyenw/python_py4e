0/1 Knapsack Problem to print all possible solutions



Given weights and profits of **N** items, put these items in a knapsack of
capacity **W**. The task is to print all possible solutions to the problem in
such a way that there are no remaining items left whose weight is less than
the remaining capacity of the knapsack. Also, compute the maximum profit.

 **Examples:**

>  **Input:** Profits[] = {60, 100, 120, 50}  
> Weights[] = {10, 20, 30, 40}, W = 40  
>  **Output:**  
>  10: 60, 20: 100,  
> 10: 60, 30: 120,  
> Maximum Profit = 180  
>  **Explanation:**  
>  Maximum profit from all the possible solutions is 180
>
>  **Input:** Profits[] = {60, 100, 120, 50}  
> Weights[] = {10, 20, 30, 40}, W = 50  
>  **Output:**  
>  10: 60, 20: 100,  
> 10: 60, 30: 120,  
> 20: 100, 30: 120,  
> Maximum Profit = 220  
>  **Explanation:**  
>  Maximum profit from all the possible solutions is 220

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The idea is to make pairs for the weight and the profits of the
items and then try out all permutations of the array and including the weights
until their is no such item whose weight is less than the remaining capacity
of the knapsack. Meanwhile after including an item increment the profit for
that solution by the profit of that item.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to print all

// the possible solutions of the

// 0/1 Knapsack problem

 

#include <bits/stdc++.h>

 

using namespace std;

 

// Utility function to find the

// maximum of the two elements

int max(int a, int b) { 

 return (a > b) ? a : b; 

}

 

// Function to find the all the

// possible solutions of the 

// 0/1 knapSack problem

int knapSack(int W, vector<int> wt, 

 vector<int> val, int n)

{

 // Mapping weights with Profits

 map<int, int> umap;

 

 set<vector<pair<int, int>>> set_sol;

 // Making Pairs and inserting

 // into the map

 for (int i = 0; i < n; i++) {

 umap.insert({ wt[i], val[i] });

 }

 

 int result = INT_MIN;

 int remaining_weight;

 int sum = 0;

 

 // Loop to iterate over all the 

 // possible permutations of array

 do {

 sum = 0;

 

 // Initially bag will be empty

 remaining_weight = W;

 vector<pair<int, int>> possible;

 

 // Loop to fill up the bag 

 // untill there is no weight

 // such which is less than

 // remaining weight of the

 // 0-1 knapSack

 for (int i = 0; i < n; i++) {

 if (wt[i] <= remaining_weight) {

 

 remaining_weight -= wt[i];

 auto itr = umap.find(wt[i]);

 sum += (itr->second);

 possible.push_back({itr->first,

 itr->second

 });

 }

 }

 sort(possible.begin(), possible.end());

 if (sum > result) {

 result = sum;

 }

 if (set_sol.find(possible) == 

 set_sol.end()){

 for (auto sol: possible){

 cout << sol.first << ": "

 << sol.second << ", ";

 }

 cout << endl;

 set_sol.insert(possible);

 }

 

 } while (

 next_permutation(wt.begin(), 

 wt.end()));

 return result;

}

 

// Driver Code

int main()

{

 vector<int> val{ 60, 100, 120 };

 vector<int> wt{ 10, 20, 30 };

 int W = 50;

 int n = val.size();

 int maximum = knapSack(W, wt, val, n);

 cout << "Maximum Profit = ";

 cout << maximum;

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    10: 60, 20: 100, 
    10: 60, 30: 120, 
    20: 100, 30: 120, 
    Maximum Profit = 220
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

