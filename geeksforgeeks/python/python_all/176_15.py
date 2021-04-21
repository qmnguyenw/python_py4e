Python code to convert SOP to POS



Write a program in python to convert standard SOP(sum of products) form to
standard POS(product of sums) form.

 **Assumptions:** The input SOP expression is standard. The variables in SOP
expression are continuous i.e. if expression contains variable A then it will
have variables B, C respectively and each Product term contains the alphabets
in sorted order i.e. ABC (not like BAC).

 **Examples:**

    
    
    Input : ABC'+A'BC+ABC+AB'C 
    Output : (A+B+C).(A+B+C').(A+B'+C).(A'+B+C)
    
    Input : A'B+AB'
    Output : (A+B).(A'+B')
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  1. First of all convert each product term to its equivalent binary form(for ex: if ABC’ then take 1 for uncomplement variable(A, B) and take 0 for complement variable(C) so binary conversion is 110) and then finally equivalent to its decimal form(for ex: 110 = 6) and store in a list.
  2. Now for POS form take all those terms which are not present in the list formed in step 1st and then convert each term to binary and hence change to SOP form.For ex: suppose 5 was not in the list then  
5 ==> 101 (binary)  
Now, replace 1 by complement variables(A, C)  
replace 0 by uncomplement variables(B)  
and between the variables use ‘+’  
101 ==> A’+B+C’  
After each individual sum term use ‘.’  
For more clarity use brackets between each individual term.  
ex: (A’+B+C’).(A+B+C’)

 **Python Code**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to convert standard SOP form

# to standard POS form 

 

# function to calculate no. of variables 

# used in SOP expression 

def count_no_alphabets(SOP): 

 i = 0

 no_var = 0

 

 # As expression is standard so total no. 

 # of alphabets will be equal 

 # to alphabets before first '+' character 

 while (SOP[i]!='+'): 

 

 # checking if character is alphabet 

 if (SOP[i].isalpha()): 

 no_var+= 1

 i+= 1

 return no_var 

 

# function to calculate the min terms in integers 

def Cal_Min_terms(Min_terms, SOP): 

 a ="" 

 i = 0

 while (i<len(SOP)): 

 if (SOP[i]=='+'): 

 

 # converting binary to decimal 

 b = int(a, 2) 

 

 # insertion of each min term(integer) into the list 

 Min_terms.append(b) 

 

 # empty the string 

 a ="" 

 i+= 1

 else: 

 

 # checking whether variable is complemented or not 

 if(i + 1 != len(SOP) and SOP[i + 1]=="'"): 

 

 # concatenating the string with '0' 

 a+='0' 

 

 # incrementing by 2 because 1 for alphabet and 

 # another for "'"

 i+= 2

 else: 

 

 # concatenating the string with '1' 

 a+='1'

 i+= 1

 

 # insertion of last min term(integer) into the list 

 Min_terms.append(int(a, 2)) 

 

# function to calculate the max terms in binary then 

# calculate POS form of SOP 

def Cal_Max_terms(Min_terms, no_var, start_alphabet): 

 

 # declaration of the list 

 Max_terms =[] 

 

 # calculation of total no. of terms that can be 

 # formed by no_var variables 

 max = 2**no_var 

 for i in range(0, max): 

 

 # checking whether the term is not 

 # present in the min terms 

 if (Min_terms.count(i)== 0): 

 

 # converting integer to binary and then 

 # taking the value from 2nd index as 1st 

 # two index contains '0b' 

 b = bin(i)[2:] 

 

 # loop used for inserting 0's before the 

 # binary value so that its length will be 

 # equal to no. of variables present in 

 # each product term 

 while(len(b)!= no_var): 

 b ='0'+b 

 

 # appending the max terms(integer) in the list 

 Max_terms.append(b) 

 

 POS ="" 

 

 # loop till there are max terms 

 for i in Max_terms: 

 

 # before every sum term append POS by '(' 

 POS = POS+"("

 

 # acquire the starting variable came from 

 # main function in every sum term 

 value = start_alphabet 

 

 # loop till there are 0's or 1's in each max term 

 for j in i: 

 

 # checking for complement variable to be used 

 if (j =='1'): 

 

 # concatenating value, ' and + in string POS 

 POS = POS + value+"'+"

 

 # checking for uncomplement variable to be used 

 else: 

 

 # concatenating value and + in string POS 

 POS = POS + value+"+"

 

 # increment the alphabet by 1 

 value = chr(ord(value)+1) 

 

 # for discarding the extra '+' in the last 

 POS = POS[:-1] 

 

 # appending the POS string by ')." after 

 # every sum term 

 POS = POS+")."

 

 # for discarding the extra '.' in the last 

 POS = POS[:-1] 

 return POS 

 

# main function 

def main(): 

 # input1 

 SOP_expr ="ABC'+A'BC + ABC + AB'C"

 Min_terms =[] 

 no_var = count_no_alphabets(SOP_expr) 

 Cal_Min_terms(Min_terms, SOP_expr) 

 POS_expr = Cal_Max_terms(Min_terms, no_var, SOP_expr[0]) 

 print ("Standard POS form of", SOP_expr, " ==> ", POS_expr) 

 

 # input2 

 SOP_expr ="A'B + AB'"

 Min_terms =[] 

 no_var = count_no_alphabets(SOP_expr) 

 Cal_Min_terms(Min_terms, SOP_expr) 

 POS_expr = Cal_Max_terms(Min_terms, no_var, SOP_expr[0]) 

 print ("Standard POS form of", SOP_expr, " ==> ", POS_expr) 

 

 # input3 

 SOP_expr ="xyz'+x'y'z'+xy'z"

 Min_terms =[] 

 no_var = count_no_alphabets(SOP_expr) 

 Cal_Min_terms(Min_terms, SOP_expr) 

 POS_expr = Cal_Max_terms(Min_terms, no_var, SOP_expr[0]) 

 print ("Standard POS form of", SOP_expr, " ==> ", POS_expr )

 

# driver code 

if __name__=="__main__": 

 main()   
  
---  
  
__

__

**Output:**

    
    
    Standard POS form of ABC'+A'BC + ABC + AB'C  ==>  (A+B+C).(A+B+C').(A+B'+C).(A+B'+C').(A'+B+C).(A'+B+C')
    Standard POS form of A'B + AB'  ==>  (A+B).(A+B').(A'+B)
    Standard POS form of xyz'+x'y'z'+xy'z  ==>  (x+y+z').(x+y'+z).(x+y'+z').(x'+y+z).(x'+y'+z')
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

