Python | Count set bits in a range



Given a non-negative number **n** and two values **l** and **r**. The problem
is to count the number of set bits in the range **l** to **r** in the binary
representation of **n** , i.e, to count set bits from the rightmost **lth**
bit to the rightmost **rth** bit.

 **Constraint:** 1 <= l <= r <= number of bits in the binary representation of
**n**.

Examples:

    
    
    Input : n = 42, l = 2, r = 5
    Output : 2
    **(42) 10** = (1 **0101** 0)2
    There are '2' set bits in the range **2** to **5**.
    
    Input : n = 79, l = 1, r = 4
    Output : 4
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Count set bits in a
range link. We can solve this problem quickly in Python. Approach is very
simple,

  

  

  1. Convert decimal into binary using bin(num) function.
  2. Now remove first two characters of output binary string because bin function appends ‘0b’ as prefix in output string by default.
  3. Slice string starting from index **(l-1)** to index **r** and reverse it, then count set bits in between.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to count set bits in a range

 

def countSetBits(n,l,r):

 

 # convert n into it's binary

 binary = bin(n)

 

 # remove first two characters

 binary = binary[2:]

 

 # reverse string

 binary = binary[-1::-1]

 

 # count all set bit '1' starting from index l-1

 # to r, where r is exclusive

 print (len([binary[i] for i in range(l-1,r) if
binary[i]=='1']))

 

# Driver program

if __name__ == "__main__":

 n=42

 l=2

 r=5

 countSetBits(n,l,r)  
  
---  
  
 __

 __

Output:

    
    
    2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

