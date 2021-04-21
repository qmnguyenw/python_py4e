What are Hash Functions and How to choose a good Hash Function?



 **Prerequisite:** Hashing | Set 1 (Introduction)

**_What is a Hash Function?_**

A function that converts a given big phone number to a small practical integer
value. The mapped integer value is used as an index in the hash table. In
simple terms, a hash function maps a big number or string to a small integer
that can be used as the index in the hash table.

**_What is meant by Good Hash Function?_**

A good hash function should have the following properties:

  

  

  1. Efficiently computable.
  2. Should uniformly distribute the keys (Each table position equally likely for each key)

 **For example:** For phone numbers, a bad hash function is to take the first
three digits. A better function is considered the last three digits. Please
note that this may not be the best hash function. There may be better ways.

In practice, we can often employ _**heuristic techniques**_ to create a hash
function that performs well. Qualitative information about the distribution of
the keys may be useful in this design process. In general, a hash function
should depend on every single bit of the key, so that two keys that differ in
only one bit or one group of bits (regardless of whether the group is at the
beginning, end, or middle of the key or present throughout the key) hash into
different values. Thus, a hash function that simply extracts a portion of a
key is not suitable. Similarly, if two keys are simply digited or character
permutations of each other _(such as 139 and 319)_ , they should also hash
into different values.

The two heuristic methods are _**hashing by division**_ and _**hashing by
multiplication**_ which are as follows:

  1. **The mod method:**
    * In this method for creating hash functions, we map a key into one of the slots of table by taking the remainder of key divided by table_size. That is, the hash function is   

    
    
    h(key) = key **mod** table_size 
    
    i.e. key % table_size

  * Since it requires only a single division operation, hashing by division is quite fast.
  * When using the division method, we usually avoid certain values of table_size like table_size should not be a power of a number suppose **r** , since if _**table_size = r^p**_ , then h(key) is just the p lowest-order bits of key. Unless we know that all low-order p-bit patterns are equally likely, we are better off designing the hash function to depend on all the bits of the key.
  * It has been found that the best results with the division method are achieved when the table size is prime. However, even if table_size is prime, an additional restriction is called for. If **r** is the number of possible character codes on an computer, and if **table_size** is a prime such that r % table_size equal 1, then hash function **h(key) = key % table_size** is simply the _sum of the binary representation of the characters_ in the key mod table_size.
  * Suppose **r** = 256 and **table_size** = 17, in which r % table_size i.e. 256 % 17 = 1.
  * So for **key = 37599** , its hash is   

    
    
    37599 % 17 = 12

  * But for **key = 573** , its hash function is also

    
    
    573 % 17 = 12

  * Hence it can be seen that by this hash function, many keys can have the same hash. This is called Collision.
  * A prime not too close to an exact power of 2 is often good choice for table_size.

  1.  **The multiplication method:**
    * In multiplication method, we multiply the key **k** by a constant real number **c** in the range **0 < c < 1** and extract the _fractional part of **k * c**_.
    * Then we multiply this value by table_size **m** and take the floor of the result. It can be represented as

    
    
     **h(k) = floor (m * (k * c mod 1))**
    **or**
    **h(k) = floor (m * frac (k * c))**

  * where the function **floor(x)**, available in standard library _math.h_ , yields the integer part of the real number x, and **frac(x)** yields the fractional part. **[frac(x) = x – floor(x)]**   

  * An advantage of the multiplication method is that the value of _m is not critical_ , we typically choose it to be a power of 2 ( **m = 2 p** for some integer **p** ), since we can then easily implement the function on most computers
  * Suppose that the word size of the machine is **w** bits and that key fits into a single word.
  * We restrict **c** to be a fraction of the form **s / (2 w)**, where s is an integer in the range **0 < s < 2w**.   

  * Referring to figure, we first multiply key by the w-bit integer **s = c * 2 w**. The result is a 2w-bit value

    
    
     **r1 * 2 w + r0**
    
    where **r1** = high-order word of the product
          **r0** = lower order word of the product

  * Although this method works with any value of the constant **c** , it works better with some values than the others.

    
    
     **c ~ (sqrt (5) – 1) / 2 = 0.618033988 . . .**

  * is likely to work reasonably well.
  * Suppose **k** = 123456, **p** = 14,
  *  **m** = 2^14 = 16384, and **w** = 32.
  * Adapting **Knuth’s suggestion** , **c** to be fraction of the form **s / 2^32**.
  * Then **key * s** = 327706022297664 = (76300 * 2^32) + 17612864,
  * So **r1** = 76300 and **r0** = 176122864.
  * The 14 most significant bits of r0 yield the value **h(key) = 67.**

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

