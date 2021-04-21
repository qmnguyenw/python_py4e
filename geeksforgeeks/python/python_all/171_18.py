Python program to calculate age in year



Given birth date in y/m/d format, write a Python program to find the present
age in years.

 **Examples:**

    
    
    **Input :** 1997/2/3
    **Output :** 21 years (for present year i.e 2018)
    
    **Input :** 2010/12/25
    **Output :** 8 years (for present year i.e 2018)
    

**Approach # 1:**  
The naive approach to find the current age in years is to find the difference
between the current year and birth year. Refer the Naive appraoch from here.

 **Approach #2:** Using datetime module  
Python provides datetime module to deal with all datetime related issues in
python. Using datetime we can find the age by subtracting birth year from
current year. Along with this, we need to focus on the birth month and
birthday. For this, we check if current month and date are less than birth
month and date. If yes subtract 1 from age, otherwise 0.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to calculate age in years

 

from datetime import date

 

def calculateAge(birthDate):

 today = date.today()

 age = today.year - birthDate.year -

 ((today.month, today.day) <

 (birthDate.month, birthDate.day))

 

 return age

 

# Driver code 

print(calculateAge(date(1997, 2, 3)), "years")  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    21 years
    

