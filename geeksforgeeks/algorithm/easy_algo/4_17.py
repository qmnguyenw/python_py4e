Comparison among Bubble Sort, Selection Sort and Insertion Sort



 **Bubble sort** repeatedly compares and swaps(if needed) adjacent elements in
every pass. In **i-th pass** of Bubble Sort (ascending order), **last (i-1)
elements are already sorted** , and i-th largest element is placed at (N-i)-th
position, i.e. i-th last position.

**Algorithm:**

    
    
    **BubbleSort (Arr, N)** // Arr is an array of size N.
    {
        For ( I:= 1 to (N-1) ) // N elements => (N-1) pass
        {
        // Swap adjacent elements of Arr[1:(N-I)]such that
        // largest among { Arr[1], Arr[2], ..., Arr[N-I] } reaches to Arr[N-I]
            For ( J:= 1 to  (N-I) ) // Execute the pass
            {
                If ( Arr [J] > Arr[J+1] ) 
                    Swap( Arr[j], Arr[J+1] );
            }
        }
    }

 ** _Optimization of Algorithm_ :** Check if there happened any swapping
operation in the inner loop (pass execution loop) or not. If there is no
swapping in any pass, it means the array is now fully sorted, hence no need to
continue, stop the sorting operation. So we can optimize the number of passes
when the array gets sorted before the completion of all passes. And it can
also detect if the given / input array is sorted or not, in the first pass.

    
    
    **BubbleSort (Arr, N)** // Arr is an array of size N.
    {
        For ( I:= 1 to (N-1) ) // N elements => (N-1) pass
        {
        // Swap adjacent elements of Arr[1:(N-I)]such that
        // largest among { Arr[1], Arr[2], ..., Arr[N-I] } reaches to Arr[N-I]
            noSwap = true; // Check occurrence of swapping in inner loop
            For ( J:= 1 to  (N-I) ) // Execute the pass
            {
                If ( Arr [J] > Arr[J+1] )
                { 
                    Swap( Arr[j], Arr[J+1] );
                    noSwap = false;
                }
            }
            If (noSwap) // exit the loop
                break;
        }
    }

 ** _Time Complexity_** :

  * **Best Case** Sorted array as input. Or almost all elements are in proper place. [ **O(N)** ]. **O(1)** swaps.
  *  **Worst Case** : Reversely sorted / Very few elements are in proper place. [ **O(N 2)** ] . **O(N 2)** swaps.
  *  **Average Case** : [ **O(N 2)** ] . **O(N 2)** swaps.

 ** _Space Complexity_** : A temporary variable is used in swapping [
auxiliary, **O(1)** ]. Hence it is In-Place sort.

  

  

**_Advantage_** :

  1. It is the simplest sorting approach.
  2. Best case complexity is of **O(N)** [for optimized approach] while the array is sorted.
  3. Using **optimized approach** , it **can detect already sorted array in first pass** with time complexity of **O(1)**.
  4. Stable sort: does not change the relative order of elements with equal keys.
  5. In-Place sort.

 ** _Disadvantage_** :

  1. Bubble sort is comparatively slower algorithm.

### 2\. Selection Sort

Selection sort selects i-th smallest element and places at i-th position. This
algorithm divides the array into two parts: sorted (left) and unsorted (right)
subarray. It selects the smallest element from unsorted subarray and places in
the first position of that subarray (ascending order). It repeatedly selects
the next smallest element.

**_Algorithm_ :**

    
    
    **SelectionSort (Arr, N)** // Arr is an array of size N.
    {
        For ( I:= 1 to (N-1) ) // N elements => (N-1) pass
        {
        // I=N is ignored, Arr[N] is already at proper place.
        // Arr[1:(I-1)] is sorted subarray, Arr[I:N] is undorted subarray
        // smallest among { Arr[I], Arr[I+1], Arr[I+2], ..., Arr[N] } is at place min_index
            
            min_index = I;
            For ( J:= I+1 to N ) // Search Unsorted Subarray (Right lalf)
            {
                If ( Arr [J] < Arr[min_index] ) 
                    min_index = J; // Current minimum
            }
            // Swap I-th smallest element with current I-th place element
            If (min_Index != I)
                  Swap ( Arr[I], Arr[min_index] ); 
            
        }
    }

 ** _Time Complexity_** :

  * **Best Case** [ **O(N 2)** ]. And **O(1)** swaps.
  *  **Worst Case** : Reversely sorted, and when the inner loop makes a maximum comparison. [ **O(N 2)** ] . Also, **O(N)** swaps.
  *  **Average Case** : [ **O(N 2)** ] . Also **O(N)** swaps.

 ** _Space Complexity_** : [ auxiliary, **O(1)** ]. In-Place sort.

**_Advantage_** :

  1. It can also be used on list structures that make add and remove efficient, such as a linked list. Just remove the smallest element of unsorted part and end at the end of sorted part.
  2. The number of swaps reduced. **O(N)** swaps in all cases.
  3. In-Place sort.

 ** _Disadvantage_** :

  

  

  1. Time complexity in all cases is **O(N 2)**, no best case scenario.

### 3\. Insertion Sort

Insertion Sort is a simple comparison based sorting algorithm. It inserts
every array element into its proper position. In i-th iteration, previous
(i-1) elements (i.e. subarray Arr[1:(i-1)]) are already sorted, and the i-th
element (Arr[i]) is inserted into its proper place in the previously sorted
subarray.  
Find more details in this GFG Link.

**_Algorithm_ :**

    
    
    **InsertionSort (Arr, N)** // Arr is an array of size N.
    {
        For ( I:= 2 to N ) // N elements => (N-1) pass
        {
        // Pass 1 is trivially sorted, hence not considered
        // Subarray { Arr[1], Arr[2], ..., Arr[I-I] } is already sorted
            
            insert_at = I; // Find suitable position insert_at, for Arr[I]
            // Move subarray Arr [ insert_at: I-1 ] to one position right
    
            item = Arr[I]; J=I-1;
            While ( J ? 1 && item < Arr[J] ) 
            {
                    Arr[J+1] = Arr[J]; // Move to right   
                    // insert_at = J;
                    J--;
                }
                insert_at = J+1; // Insert at proper position
                Arr[insert_at] = item; // Arr[J+1] = item;
            }
        }
    }

 ** _Time Complexity_** :

  * **Best Case** Sorted array as input, [ **O(N)** ]. And **O(1)** swaps.
  *  **Worst Case** : Reversely sorted, and when inner loop makes maximum comparison, [ **O(N 2)** ] . And **O(N 2)** swaps.
  *  **Average Case** : [ **O(N 2)** ] . And **O(N 2)** swaps.

 ** _Space Complexity_** : [ auxiliary, **O(1)** ]. In-Place sort.

**_Advantage_** :

  1. It can be easily computed.
  2. Best case complexity is of **O(N)** while the array is already sorted.
  3. Number of swaps reduced than bubble sort.
  4. For smaller values of N, insertion sort performs efficiently like other quadratic sorting algorithms.
  5. Stable sort.
  6. Adaptive: total number of steps is reduced for partially sorted array.
  7. In-Place sort.

 ** _Disadvantage_** :

  1. It is generally used when the value of N is small. For **larger values of N** , it is **inefficient**.   

**Time and Space Complexity:** Sorting Algorithm| Time Complexity| Space
Complexity|  | Best Case| Average Case| Worst Case| Worst Case| Bubble Sort|
**O(N)**|  **O(N 2)**|  **O(N 2)**|  **O(1)**|  Selection Sort|  **O(N 2)**|
**O(N 2)**|  **O(N 2)**|  **O(1)**|  Insertion Sort|  **O(N)**|  **O(N 2)**|
**O(N 2)**|  **O(1)**  
---|---|---|---|---  
  
Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

