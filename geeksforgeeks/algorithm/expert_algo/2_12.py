Adaptive Huffman Coding And Decoding



 **Prerequisite:** Huffman Coding, Huffman Decoding  
Adaptive Huffman Coding is also known as Dynamic Huffman Coding. The
implementation is done using Vitter Algorithm.

 _ **Encoding**_

Adaptive Huffman coding for a string containing alphabets:  
Let m be the total number of alphabets. So m = 26.  
For Vitter Algorithm, find a parameters e & r such that

    
    
    m = 2e + r and 0 ≤ r ≤ 2e
    Therefore, for m = 26 we get e = 4 & r = 10
    

There are two type of code NYT Code & Fixed Code.

    
    
    NYT code = Traversing tree from the root node to that particular NYT node.
    

For Fixed Code, it can be calculated from the following two conditions:

  

  

  1. If 0 ≤ k ≤ 2r Then the letter Sk is encoded as the binary representation of (k-1) in (e+1) bits. (where k is position of alphabet in sorted order)
  2. Else the letter Sk is encoded as the binary representation of (k-r-1) in e bits.

 **Tree Updation**  
Tree Updation in Vitter Algorithm follows Implicit Numbering. In Implicit
numbering,

  * Nodes are numbered in increasing order i.e., by level and from left to right
  * The Nodes that have the same weight and the type together form a block
  * Blocks are related to each other as by increasing order of their weights
  * Internal Node is represented by Oval shape. Weight of internal nodes = Sum of child node weights
  * External Node is represented by a square shape. Weight of external nodes = Initially 1 and if repeated then increased the weight by 1

 **Steps for Tree Updation:**

  1. Initialize the tree with the NYT Node
  2. For a symbol is recognized for the first time, the initial NYT node is further divided into an NYT Node and new Node initialize to that symbol and weight = 1.
  3. Assign the sum of the weight of child nodes to the parent node
  4. If a repeated symbol is encountered than weights are updated to that symbol.

 **Note:** During Updation in Tree if the weight of the left subtree is
greater than the right subtree, then nodes must be swapped.

 **Example**

    
    
    **code** = "aardvark"
    The final Code we get is:
    00000 1 010001 0000011 0001011 0 10  110001010
      a   a   r      d        v    a  r     k
    

![](https://media.geeksforgeeks.org/wp-content/uploads/20200205075816/Binary-
tree2.jpg)

**Explanation:**  
For string code = “aardvark”, e = 5, r = 10  
As shown in the above image Tree is initialize with NYT Node with weight 0.

  1. For symbol ‘a’, k = 1.
    
    
    NYT Code = "" (initially tree is empty)
    

For Fixed Code: As k < 2r i.e, 1 < 2*10, satisfy condtion (1)  
So Fixed Code is Binary Representation of (k-1) = 0 as 5-bit representation

    
        Fixed Code = "00000"
    
        Huffman Code for symbol for 'a' is "00000"

  2. For symbol ‘a’ which already exists in the tree. Traversing Tree up to symbol ‘a’, we get code = “1”
    
        Huffman Code for symbol for 'a' is "1"

  3. For symbol ‘r’, k = 18.
    
        NYT Code = "0" (traversing up to NYT Node)

For Fixed Code: As k > 2r i.e, 18 > 2*10, satisfy condtion (2)  
So Fixed Code is Binary Representation of (k-1 = 17) as 5-bit representation

  

  

    
        Fixed Code = "10001"
    
        Huffman Code for symbol for 'r' is "010001"

  4. For symbol ‘d’, k = 4.
    
        NYT Code = "000" (traversing up to NYT Node)

For Fixed Code: As k < 2r i.e, 4 < 2*10, satisfy condtion (1)  
So Fixed Code is Binary Representation of (k-1 = 3) as 5-bit representation

    
        Fixed Code = "00011"
    
        Huffman Code = "00000011"

  5. For symbol ‘v’, k = 22.
    
        NYT Code = "000" (traversing up to NYT Node)

For Fixed Code: As k > 2r i.e, 22 > 2*10, satisfy condtion (2)  
So Fixed Code is Binary Representation of (k-r-1 = 11) as 4-bit representation

    
        Fixed Code = "1011"
    
        Huffman Code = "0001011"

  6. Swap the node of left subtree and right as the tree is violating property
  7. For symbol ‘a’ which already exists in the tree. Traversing Tree up to symbol ‘a’, we get code = “0”
    
        Huffman Code for symbol for 'a' is "0"

  8. For symbol ‘r’ which already exists in the tree. Traversing Tree up to symbol ‘a’, we get code = “10”
    
        Huffman Code for symbol for 'r' is "10"

  9. For symbol ‘k’, k = 11.
    
        NYT Code = "1100" (traversing up to NYT Node)

For Fixed Code: As k < 2r i.e, 11 < 2*10, satisfy condtion (1)  
So Fixed Code is Binary Representation of (k-1 = 10) as 5-bit representation

    
        Fixed Code = "01010"
    
        Huffman Code for symbol for 'r' is "110001010"

 _ **Decoding**_

 **Steps for Decoding:**

  1. Read Binary string
  2. If encountered leaf node is NYT
    * Read next e bits
      1. If e bit value < r, Then to get required symbol convert (e+1) bits to decimal value of (e+1) bits + 1
      2. If e bit value > r, Then to get required symbol convert e bits to decimal value of e bits + r + 1

 **Example:**

    
    
    **code** = "00000101000100000110001011010110001010"
    We get final decoded code as
     00000  1   0    10001  00   00011  000  1011  0  10  1100  01010
       a    a  NYT     r    NYT    d    NYT   v    a   r   NYT    k
    

**Explanation:**

  * Begin decoding by reading first e bits. So the first 4 bits are 0000, converting into decimal = 0.  
Now the value 0 < r , i.e, 0 < 10 satisfy condition (1).  
Now according to the condition (1), convert first e+1 = 5 bit into decimal and
add 1 to it.

    
        00000 = 0
    0 + 1 = 1, which is value for alphabet a.
    

Update the tree and add a node for the symbol ‘a’ in the tree

  * Read the next bit in the given code and traverse the tree. We reach the external leaf node ‘a’. So the next decoded symbol is ‘a’.
  * Read the next set of bits given code and traverse the tree. We have 0 as NYT Node. After reaching the NYT Node, read e bits which are 1000. Convert 1000 to decimal is 8. As 8 < r satisfy condition (1).  
Now Convert e+1 bits in decimal and add 1 to it.

    
    
    10001 = 17
    17 + 1 = 18, which is value for alphabet r.
    

Update the tree and add a node for the symbol ‘r’ in the tree.

  * Reading the next set of bits and traversing the Tree we reach NYT node at 00. Read e bits which are 0001. Convert 0001 to decimal is 1. As 1 < r satisfy condition (1).  
Now Convert e+1 bits in decimal and add 1 to it.

    
    
    00011 = 3
    3 + 1 = 4, which is value for alphabet d.
    

Update the tree and add a node for the symbol ‘d’ in the tree.

  * Reading the next set of bits and traversing the Tree we reach NYT node at 000. Read e bits which are 1011. Convert 1011 to decimal is 11. As 11 > r satisfy condition (2).  
Now Convert k+r+1 bits in decimal and decode the symbol.

    
    
    10110 = 22, which is value for alphabet v.
    

Update the tree and add a node for the symbol ‘v’ in the tree.

  * Reading the next set of bits and traversing the Tree we get symbol ‘a’ at 0. Update the tree and add a node for the symbol ‘a’ in the tree.
  * Reading the next set of bits and traversing the Tree we get symbol ‘r’ at 10. Update the tree and add a node for the symbol ‘a’ in the tree.
  * Reading the next set of bits and traversing the Tree we reach NYT node at 1100. Read e bits which are 0101. Convert 0101 to decimal is 9. As 9 < r satisfy condition (1).  
Now Convert e+1 bits in decimal and and add 1 to it.

    
    
    01000 = 8, 
    8 + 1 = 9. which is value for alphabet k.
    

Update the tree and add a node for the symbol ‘v’ in the tree.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

