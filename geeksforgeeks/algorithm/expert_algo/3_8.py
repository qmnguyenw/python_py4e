Generating OTP (One time Password) in PHP



Now these days, OTP (one time password) is mandatory in almost each and every
service. A developer can generate OTP in many ways but the challenge is not to
be predictive as any one can predict the OTP and can exploit the service.

Some of popular format of OTPs are:

  * 4 or 6 digit Numeric OTP.
  * 4 or 6 alphabetic (lowercase / uppercase) OTP.
  * 4 or 6 digit alphanumeric OTP.

Examples for n-digit numeric OTP:

    
    
    Input : n = 4
    Output : 8723
    
    Input : n = 8
    Output : 23914072
    

**Note:** The output of program will be different in every execution.

One of the best way to generate OTP is to use random function. But using
random function directly can be dangerous. So here is an method which uses
random function and some algorithm for generating the n-digit numeric OTP.

  

  

 **Program:**

 __

 __  
 __

 __

 __  
 __  
 __

<?php

 

// Function to generate OTP

function generateNumericOTP($n) {

 

 // Take a generator string which consist of

 // all numeric digits

 $generator = "1357902468";

 

 // Iterate for n-times and pick a single character

 // from generator and append it to $result

 

 // Login for generating a random character from generator

 // ---generate a random number

 // ---take modulus of same with length of generator (say i)

 // ---append the character at place (i) from generator to result

 

 $result = "";

 

 for ($i = 1; $i <= $n; $i++) {

 $result .= substr($generator,
(rand()%(strlen($generator))), 1);

 }

 

 // Return result

 return $result;

}

 

// Main program

$n = 6;

print_r(generateNumericOTP($n));

 

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    561862
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

