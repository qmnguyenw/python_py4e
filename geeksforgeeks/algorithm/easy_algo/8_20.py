BankBazaar Interview Experience | Set 2



I had an interview with BankBazaar.com. Their process is online coding test
followed by a telephonic and f2f interviews.

 **Written test**  
The person who wrote this problem is going through the bad phase of his life.
But, fortunately he won some cash in his last programming event.  
Now to make his girlfriend feel special, he wants to buy her some chocolates.
As mentioned, he is not having good time so he want to spend as less as
possible.  
Keeping that in mind, he decided to play a game with her. The rule of game is
as follows:  
1) There are N chocolates represented by type 1..N  
2) He will arrange them in a row in some random order  
3) Now she (his girlfriend ofcourse) has to pick an index say i, then she will
get all the chocolates at index j such that j>i and type of chocolate at j is
strictly less than type of chocolate at index i.

He believes that his girlfriend is not that clever and will surely not choose
the most optimal index, but he wants to know that if by any chance she picked
the optimal index then how many chocolates will he have to buy.

Input:  
First line contain N. then next line contain N space separated integers.

output :  
A single integer which is the answer.

  

  

Constraints :  
1 = N = 105

1<=A[i]<=10^5 Sample Input (Plaintext Link) 10 7 6 10 5 2 8 1 9 3 4 Sample
Output (Plaintext Link) 7 Explanation If she chooses i=3, then all the
elements in right of i have type less than 10, hence ans is 7. In none of the
other case she can get more chocolates 2) Forgot the 2nd question. **Round-1
Telephonic**  
Given a binary tree find the pairs which violate the BST property.  
In BST EVERY element in left subtree must be less than every element in the
right subtree

    
    
    eg:                              50
                                30         60
    			20      25  10     40 

In above tree the pairs violating BST property are (20, 10), (30, 25), (30,
10) , (25, 10), (50, 10) and (60, 40).  
Expected time complexity for the problem is O(nlogn) time ?  
solution: Make in-order traversal. Store the in-order traversal in an array.
Find the pairs which voilate the property

I have not cleared this round so no f2f interview questions.

If you like GeeksforGeeks and would like to contribute, you can also write an
article and mail your article to contribute@geeksforgeeks.org. See your
article appearing on the GeeksforGeeks main page and help other Geeks.

All Practice Problems for BankBazaar !

Attention reader! Don???t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.** In case you are prepared, test your skills using **TCS** ,
**Wipro** , **Amazon** and **Microsoft** Test Serieses.

My Personal Notes _arrow_drop_up_

Save

