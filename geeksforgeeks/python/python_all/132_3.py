Running Python script on GPU.



  
GPU’s have more cores than CPU and hence when it comes to parallel computing
of data, GPUs performs exceptionally better than CPU even though GPU has lower
clock speed and it lacks several core managements features as compared to the
CPU.  
Thus, running a python script on GPU can prove out to be comparatively faster
than CPU, however it must be noted that for processing a data set with GPU,
the data will first be transferred to the GPU’s memory which may require
additional time so if data set is small then cpu may perform better than gpu.  
 **Getting started:**  
Only NVIDIA GPU’s are supported for now and the ones which are listed in this
page. If your graphics card has CUDA cores, them u can proceed further with
setting up things.  
 **Installation:**  
First make sure that Nvidia drivers are upto date also you can install
cudatoolkit explicitly from here.then install Anaconda add anaconda to
environment while installing.  
After completion of all the installations run the following commands in the
command prompt.

    
    
    conda install numba & conda install cudatoolkit
    

**NOTE:** If Anaconda is not added to the environment then navigate to
anaconda installation and locate the Scripts directory and open command prompt
there.

###  **CODE :**

We will use the _numba.jit_ decorator for the function we want to compute over
the GPU. The decorator has several parameters but we will work with only the
_target_ parameter. Target tells the jit to compile codes for which
source(“CPU” or “Cuda”). “Cuda” corresponds to GPU. However, if CPU is passed
as an argument then the jit tries to optimize the code run faster on CPU and
improves the speed too.

 __

 __  
 __

 __

 __  
 __  
 __

from numba import jit, cuda

import numpy as np

# to measure exec time

from timeit import default_timer as timer 

 

# normal function to run on cpu

def func(a): 

 for i in range(10000000):

 a[i]+= 1

 

# function optimized to run on gpu 

@jit(target ="cuda") 

def func2(a):

 for i in range(10000000):

 a[i]+= 1

if __name__=="__main__":

 n = 10000000

 a = np.ones(n, dtype = np.float64)

 b = np.ones(n, dtype = np.float32)

 

 start = timer()

 func(a)

 print("without GPU:", timer()-start) 

 

 start = timer()

 func2(a)

 print("with GPU:", timer()-start)  
  
---  
  
 __

 __

 **Output:** _based on CPU = i3 6006u, GPU = 920M._

    
    
    without GPU: 8.985259440999926
    with GPU: 1.4247172560001218

However, it must be noted that the array is first copied from ram to the GPU
for processing and if the function returns anything then the returned values
will be copied from GPU to CPU back. Therefore for small data sets the speed
of CPU is comparatively faster but the speed can be further improved even for
small data sets by passing target as “CPU”. Special care should be taken when
the function which is written under the jit attempts to call any other
function then that function should also be optimized with jit else the jit may
produce even more slower codes.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

  
  

  

My Personal Notes _arrow_drop_up_

Save

