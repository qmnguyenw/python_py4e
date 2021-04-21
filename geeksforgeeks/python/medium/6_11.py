What is H – Index?



 **What is H – index ?** ‘H’ stands for Hirsch index as it was proposed by the
J.E. Hirsch in 2005. The h-index is defined as the author-level metric that
attempts to measure both the productivity and the citation impact of the
publication of the scientist or the scholar.

There are two parameters to be considered –

  1.  **Quantity** – Numbers of papers
  2.  **Quality** – Number of citations

Basically, H-index is the largest number such that a number of publications
have at least the same number of citations. As a useful index to characterize
the scientific output of a researcher.

 **Calculating the H-index –**

For example, consider a Researcher has published total 10 papers.

  

  
 **Research Paper**|  **No. of Citations**|  1|  50|  2|  40|  3|  33|  4|
23|  5|  12|  6|  11|  7|  8|  8|  5|  9|  1|  10|  0  
---|---  
  
> H-index is always <= total numbers of papers published

For convenience let us arrange the number of citations in decreasing order.

H-index can not be 10, because there must be at least 10 research papers which
have 10 or more than 10 citations. Similarly,

H-index can not be 9,  
H-index can not be 8,  
H-index is 7 as there are 7 research papers having 7 or more than 7 citations.

 **Example :**

    
    
    **Input :** Citations = [7, 6, 5, 4, 3]
    **Output :** 4
    **Explanation :** There are 5 papers in total. 
                  Since the researcher has 4 papers with at least 4 citations each 
                  and the remaining one paper has less than 4 citations. 
                  So H-index is 4.
    

**Approach for finding the H – index :**

  1. Sort the citation array in ascending order or descending order.
  2. Iterate from the lowest paper to the highest paper.
  3. The remaining papers (result) is the count of papers that satisfy the condition for H-index.

 __

 __  
 __

 __

 __  
 __  
 __

# calculating H-Index

def H_index(citations):

 

 # sorting in ascending order

 citations.sort()

 

 # iterating over the list

 for i, cited in enumerate(citations):

 

 # finding current result

 result = len(citations) - i

 

 # if result is less than or equal

 # to cited then return result

 if result <= cited:

 return result

 

 return 0

 

# creating the citations

citation = [50, 40, 33, 23, 12, 11, 8, 5,
1, 0]

 

# calling the function

print(H_index(citation))  
  
---  
  
 __

 __

 **Output**

    
    
    7

 **Time Complexity :** O(nlogn + n)  
 **Space Complexity :** O(1)

 **Limitations of H – Index :**

  1. Different fields of researchers can have different citation behavior.
  2. We can not compare two researchers having different field and huge gap of research experience. Experienced researcher will have high H-index as compare to less experienced researcher.
  3. H-index value depends on the database you are using it may vary for the different platform.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

