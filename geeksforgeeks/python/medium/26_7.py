Functors and their use in Python



Let’s understand Functors First:  
Functors are objects the that can be treated as though they are a function.

 **When to use functors?**

  * Functors are used when you want to hide/abstract the real implementation. Let’s say you want to call the different functions depending on the input but you don’t want the user code to make explicit calls to those different functions. This is the ideal situation where functors can help.
  * In this scenario, we can go for a functor which internally calls the most suitable function depending on the input
  * Now if later, none of functions to be called increases, then it would be just a simple change in the backend code without disturbing any of the user code. Thus functors help in creating maintainable, decoupled and extendable codes.

Let’s understand it by a simple design problem example. The problem is to
design class/method which will call different sorting method based on the
input type. If the input is of type int then Mergesort function should be
called and if the input is of type float then Heapsort otherwise just call
quicksort function

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate program

# without functors 

class GodClass(object): 

 

 def DoSomething(self,x): 

 

 x_first=x[0] 

 

 if type(x_first) is int : 

 return self.__MergeSort(x) 

 if type(x_first) is float : 

 return self.__HeapSort(x) 

 else : 

 return self.__QuickSort(x) 

 

 def __MergeSort(self,a): 

 #" Dummy MergeSort " 

 print ("Data is Merge sorted")

 return a 

 

 def __HeapSort(self,b): 

 # " Dummy HeapSort " 

 print( "Data is Heap sorted")

 return b

 

 def __QuickSort(self,c): 

 # "Dummy QuickSort" 

 print ("Data is Quick sorted")

 return c 

# Here the user code need to know about the conditions for calling different
strategy 

# and making it tightly coupled code. 

 

godObject=GodClass() 

print (godObject.DoSomething([1,2,3]))   
  
---  
  
__

__

Output:

    
    
    Data is Merge sorted
    [1, 2, 3]
    

**There are some evident design gaps in this code**  
1\. Inner Implementation should be hidden from the user code i.e abstraction
should be maintained  
2\. Every class should handle single responsibility/functionality.  
2\. The code is tightly coupled.

  

  

Let’s solve the same problem using functors in python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate program

# using functors 

 

class Functor(object): 

 def __init__(self, n=10): 

 self.n = n 

 

 # This construct allows objects to be called as functions in python 

 def __call__(self, x) : 

 x_first = x[0] 

 if type(x_first) is int: 

 return self. __MergeSort(x) 

 if type(x_first) is float: 

 return self. __HeapSort(x) 

 else : 

 return self.__QuickSort(x) 

 

 def __MergeSort(self,a): 

 #" Dummy MergeSort " 

 print ("Data is Merge sorted")

 return a 

 def __HeapSort(self,b): 

 # " Dummy HeapSort " 

 print ("Data is Heap sorted")

 return b 

 def __QuickSort(self,c): 

 # "Dummy QuickSort" 

 print ("Data is Quick sorted")

 return c 

 

# Now let's code the class which will call the above functions. 

# Without the functor this class should know which specific function to be
called 

# based on the type of input 

 

### USER CODE 

class Caller(object): 

 def __init__(self): 

 self.sort=Functor() 

 

 def Dosomething(self,x): 

# Here it simply calls the function and doesn't need to care about 

# which sorting is used. It only knows that sorted output will be the 

# result of this call 

 return self.sort(x) 

 

Call=Caller() 

 

# Here passing different input 

print(Call.Dosomething([5,4,6])) # Mergesort 

 

print(Call.Dosomething([2.23,3.45,5.65])) # heapsort 

print(Call.Dosomething(['a','s','b','q'])) # quick sort 

# creating word vocab   
  
---  
  
__

__

Output:

    
    
    
    Data is Merge sorted
    [5, 4, 6]
    Data is Heap sorted
    [2.23, 3.45, 5.65]
    Data is Quick sorted
    ['a', 's', 'b', 'q']
    
    

The above design makes it easy to change the underneath strategy or
implementation without disturbing any user code. Usercode can reliably use the
above functor without knowing what is going underneath the hood,  
making the code decoupled, easily extendable and maintainable.

Now, along with the functions in the python, you have also understood the
strategy pattern in Python which calls for the separation between the Class
calling the specific function and Class where strategies are listed or chosen.

References:  
https://www.daniweb.com/programming/software-
development/threads/485098/functors-in-python

This article is contributed by **Ankit Singh**. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

