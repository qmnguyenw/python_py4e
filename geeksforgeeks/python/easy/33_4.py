A basic Python Programming Challenge



Heya guys! I am back with another article my previous article on secure
coding. This time we are not going to go into any theoretical stuff. Some
months ago, I wrote a program in Python for my students so that they can
practice basic BODMAS questions. The purpose was that the program should
generate random set of questions (number of questions to be entered by the
user) and then check whether the entered answer is correct or not. Now,
obviously it was quite easy for me to code, But, the thing was I had to ensure
that 5/2 = 2.5 is as much correct as 2.500. So, I just couldn’t go and match
two strings. I had to come up with a different solution. Just to have fun and
see if any of my students or volunteers could come up with a vulnerability in
the program, I specifically wrote a weak program. Now, I have modified the
program to make it easier for you all to identify the mistakes and the
vulnerabilities in it.

Now, here is what I want you to do:

  1.  **Don’t look at the code. Just compile it, run it and see if you can figure out the vulnerabilities in the code.**
  2.  **If you can’t figure out the vulnerabilities in step 1 or even if you did, go and take a look at the program code and try to figure out what are the things you missed!**

Once you are done, please comment what you think are the vulnerabilities in
the code and how will you correct them!

Here we go!!

Given Input:

  

  

    
    
    3
    6
    -1
    

**Program for the small basic python Challenge**

 __

 __  
 __

 __

 __  
 __  
 __

## Note: This program has been modified a bit for

## GeeksForGeeks article

import random,operator

print ('===========================================')

 

def randomCalc(i,j):

 ops = {'+':operator.add,

 '-':operator.sub,

 '*':operator.mul,

 '/':operator.truediv }

 num = [1,2,3,4]

 num1,num2 = num[i],num[j]

 op = (list(ops.keys()))[i]

 answer = round(ops.get(op)(num1,num2),3)

 print('What is {} {} {}?\n'.format(num1, op, num2))

 return answer

 

def askQuestion(i):

 answer = randomCalc(i,i+1)

 guess = float(input())

 return guess == answer,answer

 

def quiz(numOfQues):

 print('\nWelcome. This is a '+str(numOfQues)+' question math
quiz.')

 print('Your answer should be correct to three decimal places.\n')

 score = 0

 for i in range(numOfQues):

 correct,ans = askQuestion(i)

 if correct:

 score += 1

 print('Correct!\n')

 else:

 print('Incorrect! The correct answer is ' +
str(ans)+'\n')

 return ('Your score was {}/'+str(numOfQues)).format(score)

 

# Driver Code

print (quiz(3))  
  
---  
  
 __

 __

### Output:

    
    
    ===========================================
    
    Welcome. This is a 3 question math quiz
     Your answer should be correct to three decimal places.
    
    What is 1 + 2?
    
    Correct!
    
    What is 2 * 3?
    
    Correct!
    
    What is 3 - 4?
    
    Correct!
    
    Your score was 3/3
    

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above!!

 **About the author:**

 **Vishwesh Shrimali** is an Undergraduate Mechanical Engineering student at
BITS Pilani. He fulfils![vish](http://d1gjlxt8vb0knt.cloudfront.net//wp-
content/uploads/vish-100x100.png) about all the requirements not taught in his
branch- white hat hacker, network security operator, and an ex – Competitive
Programmer. As a firm believer in power of Python, his majority work has been
in the same language. Whenever he get some time apart from programming,
attending classes, watching CSI Cyber, he go for a long walk and play guitar
in silence. His motto of life is – “Enjoy your life, ‘cause it’s worth
enjoying!”

 **If you also wish to showcase your blog here, please seeGBlog for guest blog
writing on GeeksforGeeks.**

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save

