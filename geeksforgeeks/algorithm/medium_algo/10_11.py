How to evenly put N objects into N places with adjacent moves



Suppose you have N objects distributed unevenly in N containers. You can move
one object from a container to an adjacent container, it is considered to be
one move. What is the strategy that minimizes the number of moves to keep the
time complexity O(N)?  
Examples:

> Example 1. Suppose you have 5 containers that are filled as:  
> 1, 2, 1, 1, 0  
> You will need three moves to pass one object from the second container to
> the last one ->, move from 2nd to the third first, then to the fourth and
> finally to the fifth:  
> 1, 1, 2, 1, 0  
> 1, 1, 1, 2, 0  
> 1, 1, 1, 1, 1
>
> Example 2. Now a bit more complicated one.  
> Suppose you have 5 containers and all objects are in the last container:  
> 0, 0, 0, 0, 5  
> Obviously, you will move from right to the left:  
> 0, 0, 0, 1, 4  
> 0, 0, 1, 0, 4  
> 0, 1, 0, 0, 4  
> 1, 0, 0, 0, 4  
> 1, 0, 0, 1, 3  
> 1, 0, 1, 0, 3  
> 1, 1, 0, 0, 3  
> 1, 1, 0, 1, 2  
> 1, 1, 1, 0, 2  
> 1, 1, 1, 1, 1  
> It takes 10 moves
>
> Example 3. All objects are in the middle:  
> 0, 0, 5, 0, 0  
> That is what seems right:  
> 0, 1, 4, 0, 0  
> 1, 0, 4, 0, 0  
> 1, 1, 3, 0, 0  
> 1, 1, 2, 1, 0  
> 1, 1, 2, 0, 1  
> 1, 1, 1, 1, 1  
> It takes 6 moves

The problem weakly reminds a so-called pigeonhole or Dirichlet principle –
that n item are put into m containers, with n>m, then at least one container
must contain more than one item. Hence it appears in the title.

  

  

 **Approach** sounds rather trivial: move along the row of containers from the
beginning to the end, if you meet an empty container, fill it, and if you meet
a container with several objects (more than one), try to decrease the amount
to just one.

More precisely, one must keep a queue of containers with too many objects and
another queue of empty places and use them to pass objects. Obviously, since
we try to pass objects as soon as there is a possibility, one of the queues
will become empty on every step after we make all possible movements.  
Still more detailed:  
Every time we meet an empty place, we check if there is something in the queue
of containers with multiple objects, if yes, take one object and fill the
empty place. If no, add this empty place to the queue.  
Every time we meet an overcrowded container, check if the queue of empty
spaces has something, if yes, try to put objects from the current container as
many as possible into these empty containers and remove them from their queue.
If no empty ready, push the overcrowded container into the queue for full
containers.

The queue for overcrowded containers keeps pairs of numbers: location and
amount of superfluous objects. The queue for empty containers keeps just
numbers for locations since they are empty.

If the input is supplied as an array of coordinates of objects A, first
reorganize it like an array of amounts per location.

This problem can be in more then one dimensions like in the Codility challenge
Selenium 2016, which inspired this article. But since dimensions are
independent, the results min every dimension just summarized to get the final
answer.  
The full implementation for the problem in Codility includes that the final
answer is taken Modulo 10^9+7.

Examples:

    
    
    Input : 
    Coordinates of objects are
    X = [1, 2, 2, 3, 4] and array Y = [1, 1, 4, 5, 4] 
    Output :
    5
    Input :
    X = [1, 1, 1, 1] and array Y = [1, 2, 3, 4] 
    Output :
    6
    Input :
     X = [1, 1, 2] and array Y = [1, 2, 1]
    Output :
    4
    

Note: there is another way to do it, possibly will be covered in another
article, inspired by a more hard problem in Codility Future Mobility
Challenge. It includes the following steps:

  * Subtract from every location 1, now we strife for all 0 instead of all 1
  * Cut the array into fragments such as in every fragment the movement of objects are all in one direction, starting and trailing zeroes can be dropped for evey fragment. Sample: 1, 0, -1, 0, -2, 2 is cut into 1, 0, -1 and -2, 2. The cut points are discovered by zeroes of prefix sum
  * For every fragment calculate the second integral. That is the prefix of prefix from left to right. The most right value is the amount of moves. Sample sequence: 1, 0, -1. The prefix is 1, 1, 0. The second prefix is 1, 2, 2. The answer for this fragment is 2 (two moves from 0 to 2)
  * The result is the sum of results for all fragments

The final implementation of the first way:

 __

 __  
 __

 __

 __  
 __  
 __

#include<queue>

#include <vector>

using namespace std;

#define MODULO 1000000007

 

/* Utility function for one dimension

unsigned long long solution(vector<int>& A)

Parameters: vector<int>& A - an array of numbers 

of objects per container 

Return value: How many moves to make all containers

 have one object */

unsigned long long solution(vector<int>& A)

{

 // the final result cannot be less than

 // zero, so we initiate it as 0 

 unsigned long long res = 0; 

 

 // just to keep the amount of objects for future usage

 const unsigned int len = (unsigned int)A.size(); 

 

 // The queue of objects that are ready for move,

 // as explained in the introduction. The queue is 

 // of pairs, where the first value is the index 

 // in the row of containers, the second is the 

 // number of objects there currently.

 queue<pair<unsigned int, unsigned int> > depot;

 

 // The queue of vacant containers that are ready

 // to be filled, as explained in the introduction, 

 // just the index on the row, since they are 

 // empty - no amount, zero is meant.

 queue<unsigned int> depotOfEmpties; 

 

 // how many objects have coordinate i 

 vector<unsigned int> places(len, 0); 

 

 // initiates the data into a more convenient way, 

 // not coordinates of objects but how many objects

 // are per place

 for (unsigned int i = 0; i < len; i++) { 

 places.at(A.at(i) - 1)++;

 }

 

 // main loop, movement along containers as

 // explained in the introduction

 for (unsigned int i = 0; i < len; i++) { 

 

 // if we meet the empty container at place i 

 if (0 == places.at(i)) { 

 

 // we check that not objects awaiting 

 // to movement, the queue of objects 

 // is possible empty 

 if (depot.empty()) { 

 

 // if true, no object to move, we

 // insert the empty container into 

 // a queue of empties 

 depotOfEmpties.push(i);

 }

 

 // there are some object to move, take 

 // the first from the queue 

 else {

 

 // and find how distant it is 

 unsigned int distance = (i - depot.front().first); 

 

 // we move one object and making

 // "distance" moves by it

 res += distance; 

 

 // since the result is expected MODULO

 res = res % MODULO; 

 

 // now one object left the queue

 // for movement, so we discount it 

 depot.front().second--; 

 

 // if some elements in the objects

 // queue may loose all objects, 

 while (!depot.empty() && depot.front().second < 1) {

 depot.pop(); // remove all them from the queue

 }

 }

 }

 

 // places.at(i) > 0, so we found the current 

 // container not empty

 else { 

 

 // if it has only one object, nothing must 

 // be done 

 if (1 == places.at(i)) { 

 

 // so the object remains in its place, 

 // go further 

 continue; 

 }

 

 // there are more than one there, need 

 // to remove some

 else {

 

 // how many to remove? To leave one

 unsigned int pieces = places.at(i) - 1; 

 

 // how many empty places are awaiting to fill

 // currently? Are they enough to remove "pieces"?

 unsigned int lenEmptySequence = depotOfEmpties.size(); 

 

 // Yes, we have places for all objects 

 // to remove from te current 

 if (pieces <= lenEmptySequence) { 

 

 // move all objects except one

 for (unsigned int j = 0; j < pieces; j++) { 

 

 // add to the answer and aply MODULOto

 // prevent overflow

 res = (res + i - depotOfEmpties.front()) % MODULO; 

 

 // remove former empty from the queue of empties

 depotOfEmpties.pop(); 

 }

 }

 

 // empty vacancies are not enough or absent at all

 else { 

 for (unsigned int j = 0; j < lenEmptySequence; j++) {

 

 // fill what we can

 res = (res + i - depotOfEmpties.front()) % MODULO; 

 

 // and remove filled from the vacancies queue 

 depotOfEmpties.pop(); 

 }

 

 // since we still have too many objects in

 // this container, push it into the queue for

 // overcrowded containers

 depot.push(pair<unsigned int, unsigned int>(i,

 pieces - lenEmptySequence)); 

 }

 }

 }

 } 

 

 // the main loop end

 return res; // return the result

}

 

/* Main function for two dimensions as in 

 Codility problem

int solution(vector<int>& A, vector<int>& B)

Parameters:

 vector<int>& A - coordinates x of the objects

 vector<int>& B - coordinates y of the objects

Return value:

 No. of moves to make all verticals and horizontals

 have one object

*/

int solution(vector<int>& A, vector<int>& B)

{

 unsigned long long res = solution(B);

 res += solution(A);

 res = res % MODULO;

 return (int)res;

}

 

// test utility for the driver below

#include <iostream>

void test(vector<int>& A, vector<int>& B, int expected, 

 bool printAll = false, bool doNotPrint = true)

{

 int res = solution(A, B);

 if ((expected != res && !doNotPrint) || printAll) {

 for (size_t i = 0; i < A.size(); i++) {

 cout << A.at(i) << " ";

 }

 cout << endl;

 for (size_t i = 0; i < B.size(); i++) {

 cout << B.at(i) << " ";

 }

 cout << endl;

 if (expected != res)

 cout << "Error! Expected: " << expected << " ";

 else

 cout << "Expected: " << expected << " ";

 }

 cout << " Result: " << res << endl;

}

 

// Driver (main)

int main()

{

 int A4[] = { 1, 2, 2, 3, 4 };

 int B4[] = { 1, 1, 4, 5, 4 };

 vector<int> VA(A4, A4 + 5);

 vector<int> VB(B4, B4 + 5);

 test(VA, VB, 5);

 

 int A0[] = { 1, 1, 1, 1 };

 int B0[] = { 1, 2, 3, 4 };

 VA = vector<int>(A0, A0 + 4);

 VB = vector<int>(B0, B0 + 4);

 test(VA, VB, 6);

 

 int A2[] = { 1, 1, 2 };

 int B2[] = { 1, 2, 1 };

 VA = vector<int>(A2, A2 + 3);

 VB = vector<int>(B2, B2 + 3);

 test(VA, VB, 4);

 

 // square case

 int A3[] = { 1, 2, 3, 1, 2, 3, 1, 2, 3 };

 int B3[] = { 1, 1, 1, 2, 2, 2, 3, 3, 3 };

 VA = vector<int>(A3, A3 + 9);

 VB = vector<int>(B3, B3 + 9);

 test(VA, VB, 54);

 // also

 int A5[] = { 7, 8, 9, 7, 8, 9, 7, 8, 9 };

 int B5[] = { 7, 7, 7, 8, 8, 8, 9, 9, 9 };

 VA = vector<int>(A5, A5 + 9);

 VB = vector<int>(B5, B5 + 9);

 test(VA, VB, 54);

 

 int A6[] = { 1, 1, 2, 3 };

 int B6[] = { 1, 2, 3, 4 };

 VA = vector<int>(A6, A6 + 4);

 VB = vector<int>(B6, B6 + 4);

 test(VA, VB, 3);

 test(VB, VA, 3);

 

 int A7[] = { 1, 1, 3, 5, 5 };

 int B7[] = { 1, 5, 3, 1, 5 };

 VA = vector<int>(A7, A7 + 5);

 VB = vector<int>(B7, B7 + 5);

 test(VA, VB, 4);

 test(VB, VA, 4);

 

 // smaller square case

 int A8[] = { 1, 2, 1, 2 };

 int B8[] = { 1, 1, 2, 2 };

 VA = vector<int>(A8, A8 + 4);

 VB = vector<int>(B8, B8 + 4);

 test(VA, VB, 8);

 

 int A9[] = { 3, 4, 3, 4 };

 int B9[] = { 3, 3, 4, 4 };

 VA = vector<int>(A9, A9 + 4);

 VB = vector<int>(B9, B9 + 4);

 test(VA, VB, 8);

 

 int A10[] = { 1, 2, 3, 4, 1, 2, 3, 4, 1,

 2, 3, 4, 1, 2, 3, 4 };

 int B10[] = { 1, 1, 1, 1, 2, 2, 2, 2, 3, 

 3, 3, 3, 4, 4, 4, 4 };

 VA = vector<int>(A10, A10 + 16);

 VB = vector<int>(B10, B10 + 16);

 test(VA, VB, 192);

 

 int A11[] = { 13, 14, 15, 16, 13, 14, 15,

 16, 13, 14, 15, 16, 13, 14, 15, 16 };

 int B11[] = { 13, 13, 13, 13, 14, 14, 14, 

 14, 15, 15, 15, 15, 16, 16, 16, 16 };

 VA = vector<int>(A11, A11 + 16);

 VB = vector<int>(B11, B11 + 16);

 test(VA, VB, 192);

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    Result: 5
     Result: 6
     Result: 4
     Result: 54
     Result: 54
     Result: 3
     Result: 3
     Result: 4
     Result: 4
     Result: 8
     Result: 8
     Result: 192
     Result: 192
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

