Maximum Possible Rating of a Coding Contest



  
Given two arrays of positive integer **Point[]** , **Upvote[]** of size **N**
and a value **K** (1 <= K <= N). The task is to choose atleast K
elements(Problems) such that the rating of the coding contest is maximum.  
  
 **Rating of contest:** Rating of a contest is defined as total points of all
problems in the contest multiplied by the minimum upvotes among all problems
in the contest

> Hence, **Rating** = sum of points of contest problems * minimum upvotes
> among contest problems.

 **Examples:**

>  **Input:** Point[] = {2, 10, 3, 1, 5, 8}, Upvote[] = {5, 4, 3, 9, 7, 2}, K
> = 2  
>  **Output:** 60  
>  **Explanation:**  
>  Here we select 2nd and 5th problem to get the maximum rating of the
> contest.  
> So maximum rating is (10 + 5) * min(4, 7) = 60
>
>  **Input:** Point[] = {2, 10, 3, 1, 5, 8}, Upvote[] = {5, 4, 3, 9, 7, 2}, K
> = 3  
>  **Output:** 68  
>  **Explanation:**  
>  Here we select 1st, 2nd and 5th problem to get the maximum rating of the
> contest.  
> So maximum rating is (2 + 10 + 5) * min(5, 4, 7) = 68
>
>  
>
>
>  
>
>
>  **Input:** Point[] = {2, 20, 3, 1, 5, 8}, Upvote[] = {5, 10, 3, 9, 7, 2}, K
> = 4  
>  **Output:** 200  
>  **Explanation:**  
>  Here we select only 2nd problem to get maximum rating of the contest.  
> A further selection of any problems decreases the rating.  
> So maximum rating is 20 * 10 = 200

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach :**

  * Try the value of every upvote from highest to lowest and at the same time maintain an as large as possible points group, keep adding points to total points, if the number of problems in the contest exceeds K, lay off the problem with lowest points. This includes three steps.
    1. Sort problems by their upvotes value in decreasing order.
    2. For index i = 0, 1, …, K-1, we push the points into the min_heap and calculate the rating. We only need to record the maximum rating. We use min_heap to track the problem with minimum points.
    3. For an index i = K, K+1, …, N-1, if the point of the current problem is greater than the top of the min_heap, we pop the existing element and push the current element in the min_heap and update the maximum rating.  
In this way, calculate the maximum rating with respect to the problem with
i-th largest upvotes since we have the problems with the K largest points in
the min_heap.

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the Maximum

// Possible Rating of a Coding Contest

#include <bits/stdc++.h>

using namespace std;

 

// Function to sort all problems

// descending to upvotes

bool Comparator(pair<int, int> p1,

 pair<int, int> p2)

{

 return p1.second > p2.second;

}

 

// Function to return maximum

// rating

int FindMaxRating(int N, int Point[],

 int Upvote[], int K)

{

 // Declaring vector of pairs

 vector<pair<int, int> > vec;

 

 // Each pair represents a problem

 // with its points and upvotes

 for (int i = 0; i < N; i++)

 {

 vec.push_back(make_pair(Point[i],

 Upvote[i]));

 }

 

 // Step (1) - Sort problems by their 

 // upvotes value in decreasing order

 sort(vec.begin(), vec.end(), Comparator);

 

 // Declaring min_heap or priority queue 

 // to track of the problem with 

 // minimum points.

 priority_queue<int, vector<int>,

 greater<int> > pq;

 

 int total_points = 0, max_rating = 0;

 

 // Step (2) - Loop for i = 0 to K - 1 and 

 // do accordingly

 for (int i = 0; i < K; i++)

 {

 total_points = total_points

 + vec[i].first;

 max_rating = max(max_rating, 

 total_points 

 * vec[i].second);

 pq.push(vec[i].first);

 }

 

 // Step (3) - Loop for i = K to N - 1 

 // and do accordingly

 for (int i = K; i < N; i++)

 {

 if (pq.top() < vec[i].first)

 {

 total_points = total_points

 - pq.top() 

 + vec[i].first;

 max_rating = max(max_rating, 

 total_points

 * vec[i].second);

 

 pq.pop();

 

 pq.push(vec[i].first);

 }

 }

 

 return max_rating;

}

 

// Driver code

int main()

{

 int Point[] = { 2, 10, 3, 1, 5, 8 };

 int Upvote[] = { 5, 4, 3, 9, 7, 2 };

 

 int N = sizeof(Point) / sizeof(Point[0]);

 int K = 2;

 

 cout << "Maximum Rating of Coding Contest is: "

 << FindMaxRating(N, Point, Upvote, K);

 

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

# Python3 program to find the Maximum

# Possible Rating of a Coding Contest 

import heapq

 

# Function to sort all problems 

# descending to upvotes

def Comparator(p1):

 

 return p1[1]

 

# Function to return maximum 

# rating 

def FindMaxRating(N, Point, Upvote, K):

 

 # Declaring vector of pairs

 vec = []

 

 # Each pair represents a problem 

 # with its points and upvotes 

 for i in range(N):

 vec.append([Point[i], Upvote[i]])

 

 # Step (1) - Sort problems by their 

 # upvotes value in decreasing order 

 vec.sort(reverse = True, key = Comparator)

 

 # Declaring min_heap or priority queue 

 # to track of the problem with 

 # minimum points. 

 pq = []

 heapq.heapify(pq)

 

 total_points, max_rating = 0, 0

 

 # Step (2) - Loop for i = 0 to K - 1 and 

 # do accordingly 

 for i in range(K):

 total_points = (total_points +

 vec[i][0])

 

 max_rating = max(max_rating,

 total_points *

 vec[i][1])

 

 heapq.heappush(pq, vec[i][0])

 

 # Step (3) - Loop for i = K to N - 1 

 # and do accordingly 

 for i in range(K, N):

 if pq[0] < vec[i][0]:

 total_points = (total_points -

 pq[0] +

 vec[i][0])

 

 max_rating = max(max_rating, 

 total_points *

 vec[i][1])

 

 heapq.heappop(pq)

 heapq.heappush(pq, vec[i][0])

 

 return max_rating

 

# Driver code

Point = [ 2, 10, 3, 1, 5, 8 ]

Upvote = [ 5, 4, 3, 9, 7, 2 ]

 

N = len(Point)

K = 2

 

print("Maximum Rating of Coding Contest is:",

 FindMaxRating(N, Point, Upvote, K))

 

# This code is contributed by stutipathak31jan  
  
---  
  
 __

 __

 **Output:**

    
    
    Maximum Rating of Coding Contest is: 60
    

**Time Complexity:** O(N * logN)  
 **Auxiliary Space:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

