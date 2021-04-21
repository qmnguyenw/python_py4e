Python program to calculate gross pay



Gross pay is the amount of money an employee earns in a specific time period
before any deductions. There are lots of different ways to calculate gross pay
depending on how an employee is paid. This article describes the two most
common ways -hourly and salary.

### Hourly paid employee

If an employee is paid hourly, he is paid a fixed amount for every hour of
work. So, if he gets paid Rs.100 an hour, and he works eight hours his gross
pay is Rs.800. An hourly employee’s gross pay must be calculated on a ****
weekly basis because of a Rule called overtime, the federal government’s Fair
Labor Standards Act states that for overtime an employee must receive overtime
pay for hours worked over 40 in a work week at a rate not less than 1.5 times
regular rates of pay.

**Example:**

> Let’s assume A works as an hourly paid employee, and he is paid 100/hour.  
>
>
> If he worked for 50 hours in a week then he will get the overtime pay for
> the extra hours he worked i.e. he will be paid 1.5 times of Rs.100 for 10
> hours (50-40).  
>
>
>  
>
>
>  
>
>
> if worked_hours > 40 then:  
> total gross pay = (hourly_wage *40) + (1.5 * hourly_wage *
> (worked_hours-40)).
>
> if worked_hours < 40 then:  
> total gross pay = hourly_wage *worked_hours.  
> ramu’s worked_hours=50 i.e. greater than 40 hours.  
> total gross pay = 100*40 + (1.5)*100*10 => Rs.5,500.  
>

**Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def weeklyPaid(hours_worked, wage):

 if hours_worked > 40:

 return 40 * wage + (hours_worked - 40) * wage *
1.5

 else:

 return hours_worked * wage

 

 

hours_worked = 50

wage = 100

 

pay = weeklyPaid(hours_worked, wage)

 

print(f"Total gross pay: Rs.{pay:.2f} ")  
  
---  
  
 __

 __

 **Output:**

    
    
    Total gross pay: Rs.5500.00 
    

### Salaried employee

Salary is usually quoted annually but commonly, employees are paid monthly. To
calculate gross pay of a salaried employee, we need to divide the annual
salary by number of pay periods in a year (i.e. how many installments they are
getting paid in a year).

 **Example:**

> Let’s assume B works as a salaried employee, and he is paid 12 lakhs per
> annum.  
> If B was paid monthly then the gross payment will be 12 lakhs / 12.  
>
>
> gross pay= 12/12 => 1 lakh.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def getGrossPay(annual_salary, no_of_pay_peroids):

 return float(annual_salary/no_of_pay_peroids)

 

# driver code

 

 

# annual_salary in lakhs

annual_salary = 12

no_of_pay_peroids = 12

pay = getGrossPay(annual_salary, no_of_pay_peroids)

 

print(f"Total gross pay: Rs.{pay:.2f} lakhs ")  
  
---  
  
 __

 __

 **Output:**

    
    
    Total gross pay: Rs.1.00 lakhs 
    

**Time complexity :** O (1)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

