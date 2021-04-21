Python | Binning method for data smoothing



 **Prerequisite:** ML | Binning or Discretization

Binning method is used to smoothing data or to handle noisy data. In this
method, the data is first sorted and then the sorted values are distributed
into a number of buckets or bins. As binning methods consult the neighborhood
of values, they perform local smoothing.

 **There are three approaches to perform smoothing –**

>  **Smoothing by bin means :** In smoothing by bin means, each value in a bin
> is replaced by the mean value of the bin.  
>  **Smoothing by bin median :** In this method each bin value is replaced by
> its bin median value.  
>  **Smoothing by bin boundary :** In smoothing by bin boundaries, the minimum
> and maximum values in a given bin are identified as the bin boundaries. Each
> bin value is then replaced by the closest boundary value.

 **Approach:**

  

  

  1. Sort the array of given data set.
  2. Divides the range into N intervals, each containing the approximately same number of samples(Equal-depth partitioning).
  3. Store mean/ median/ boundaries in each row.

 **Examples:**

    
    
    Sorted data for price (in dollars): 4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34
    
    **Smoothing by bin means:**
          - Bin 1: 9, 9, 9, 9
          - Bin 2: 23, 23, 23, 23
          - Bin 3: 29, 29, 29, 29
    
    **Smoothing by bin boundaries:**
          - Bin 1: 4, 4, 4, 15
          - Bin 2: 21, 21, 25, 25
          - Bin 3: 26, 26, 26, 34
    
    **Smoothing by bin median:**
          - Bin 1: 9 9, 9, 9
          - Bin 2: 24, 24, 24, 24
          - Bin 3: 29, 29, 29, 29
    

Below is the Python implementation for above algorithm –

