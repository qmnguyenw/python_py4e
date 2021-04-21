Python program to create Bankaccount class with deposit, withdraw function



Prerequisite: Object Oriented Programming in Python

Let’s write a simple Python program using OOP concept to perform some simple
bank operations like deposit and withdrawal of money.

First of all, define class Bankacccount. This step is followed by defining a
function using __init__. It is run as soon as an object of a class is
instantiated. This __init__ method is useful to do any initialization you
want to do with object, then we have the default argument self.

 __

 __  
 __

 __

 __  
 __  
 __

# BankAccount class

class Bankaccount:

 def __init__(self):  
  
---  
  
 __

 __

This step is followed by declaring that balance is 0 usingself argument then
we simply print a statement welcoming to Machine. In function deposit and
withdraw , _amount_ is taken as input(in float) and is then added/subtracted
to the balance. Thus resultant balance is printed in next line.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to deposite amount

def deposit(self):

 amount = float(input("Enter amount to be deposited: "))

 self.balance += amount

 print("\n Amount Deposited:", amount)  
  
---  
  
 __

 __

Use an if condition to check whether there is a sufficient  
amount of money available in the account to process a fund withdrawal.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Function to withdraw the amount

def withdraw(self):

 amount = float(input("Enter amount to be withdrawn: "))

 if self.balance >= amount:

 self.balance -= amount

 print("\n You Withdrew:", amount)

 else:

 print("\n Insufficient balance ")  
  
---  
  
 __

 __

Next, we use adisplay function to display the remianing balnce in the
account. Then we create a object and call it to get the program executed.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to display the amount

def display(self):

 print("\n Net Available Balance =", self.balance)  
  
---  
  
 __

 __

Below is the implementation:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create Bankaccount class

# with both a deposit() and a withdraw() function

class Bank_Account:

 def __init__(self):

 self.balance=0

 print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

 

 def deposit(self):

 amount=float(input("Enter amount to be Deposited: "))

 self.balance += amount

 print("\n Amount Deposited:",amount)

 

 def withdraw(self):

 amount = float(input("Enter amount to be Withdrawn: "))

 if self.balance>=amount:

 self.balance-=amount

 print("\n You Withdrew:", amount)

 else:

 print("\n Insufficient balance ")

 

 def display(self):

 print("\n Net Available Balance=",self.balance)

 

# Driver code

 

# creating an object of class

s = Bank_Account()

 

# Calling functions with that class object

s.deposit()

s.withdraw()

s.display()  
  
---  
  
 __

 __

 **Output:**

    
    
    Hello !!! Welcome to Deposit&Withdrawal Machine
    Enter amount to be deposited: 
     Amount Deposited: 1000.0
    Enter amount to be withdrawn: 
     You Withdrew: 500.0
    
     Net Available Balance = 500.0

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

