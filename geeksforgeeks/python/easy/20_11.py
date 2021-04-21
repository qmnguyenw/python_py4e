TCS National Qualifier 2 Coding Question.



You are given a string and your task is to print the frequency of each
character character.

###### Direction to Solve Problem  

1\. Take string from STDIN.

    
    
    aaaabbBcddee
    

2\. Get all different characters in give string using set().

    
    
    set ={a, b, B, c, d, e}  # unordered set
    

3\. Iterate for different characters ( len(set )) because we only need to
print a character one time and it count in input sting

  

  

    
    
    range 0 to 5 i.e total 6 element
    

4\. In every iteration take first character print it and its count.

    
    
    now for 0
    input_string[0]  is 'a' and its count is 4
    

5 . Remove all occurrence of fist character, this will make next character as
1st character.

    
    
    remove 'a' by replacing all 'a' in string by ""
    new input string will be
    bbBcddee
    

6\. Repeat the same process, go to step 4.  
7\. Either print value to STDOUT on each iteration (python3) or print in one
go(python2), your output will be same as

    
    
    a4b2B1c1d2e2

Examples:

    
    
    Input : aaaabbBcddee
    Output :a4b2B1c1d2e2
    
    Input :aazzZ
    Output :a2z2Z1
    

__

__  
__

__

__  
__  
__

# Python2 code here

input_string = raw_input()

temp_string =""

for _ in range(len(set(input_string))):

 temp_string += input_string[0] +
str(input_string.count(input_string[0])) 

 input_string = input_string.replace(input_string[0], "")

print temp_string  
  
---  
  
 __

 __

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code here

input_string = input()

for _ in range(len(set(input_string))):


print(input_string[0]+str(input_string.count(input_string[0])),
end ="")

 input_string = input_string.replace(input_string[0], "")  
  
---  
  
 __

 __

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.** In case you are prepared, test your skills using **TCS** ,
**Wipro** , **Amazon** and **Microsoft** Test Serieses.

My Personal Notes _arrow_drop_up_

Save

