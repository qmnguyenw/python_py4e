Python Program for Coin Change



Given a value N, if we want to make change for N cents, and we have infinite
supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we
make the change? The order of coins doesn\’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions:
{1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2,
5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5}
and {5,5}. So the output should be 5.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Dynamic Programming Python implementation of Coin

# Change problem

def count(S, m, n):

 # We need n+1 rows as the table is constructed 

 # in bottom up manner using the base case 0 value

 # case (n = 0)

 table = [[0 for x in range(m)] for x in
range(n+1)]

 

 # Fill the entries for 0 value case (n = 0)

 for i in range(m):

 table[0][i] = 1

 

 # Fill rest of the table entries in bottom up manner

 for i in range(1, n+1):

 for j in range(m):

 

 # Count of solutions including S[j]

 x = table[i - S[j]][j] if i-S[j] >= 0 else 0

 

 # Count of solutions excluding S[j]

 y = table[i][j-1] if j >= 1 else 0

 

 # total count

 table[i][j] = x + y

 

 return table[n][m-1]

 

# Driver program to test above function

arr = [1, 2, 3]

m = len(arr)

n = 4

print(count(arr, m, n))

 

# This code is contributed by Bhavya Jain  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Dynamic Programming Python implementation of Coin

# Change problem

def count(S, m, n):

 

 # table[i] will be storing the number of solutions for

 # value i. We need n+1 rows as the table is constructed

 # in bottom up manner using the base case (n = 0)

 # Initialize all table values as 0

 table = [0 for k in range(n+1)]

 

 # Base case (If given value is 0)

 table[0] = 1

 

 # Pick all coins one by one and update the table[] values

 # after the index greater than or equal to the value of the

 # picked coin

 for i in range(0,m):

 for j in range(S[i],n+1):

 table[j] += table[j-S[i]]

 

 return table[n]

 

# Driver program to test above function

arr = [1, 2, 3]

m = len(arr)

n = 4

x = count(arr, m, n)

print (x)

 

# This code is contributed by Afzal Ansari  
  
---  
  
 __

 __

Please refer complete article onDynamic Programming | Set 7 (Coin Change) for
more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

