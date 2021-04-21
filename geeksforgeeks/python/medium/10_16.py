__getitem__ and __setitem__ in Python



Dunder methods are double underscored methods that are used to emulate the
behavior of built-in types. They are predefined methods that simplify many
operations that can be performed on a class instance, like __init__(),
__str__(), __call__() etc. These methods are very helpful because they are
used in binary operations, assignment operations, unary and binary comparison
operations.

 **Note:** For more information, refer to Dunder or magic methods in Python

## __getitem__ and __setitem__

There are getter and setter methods as a part of these magical methods. They
are implemented by __getitem__() and __setitem__() methods. But, these
methods are used only in indexed attributes like arrays, dictionaries, lists
e.t.c. Instead of directly accessing and manipulating class attributes, it
provides such methods, so these attributes can be modified only by its own
instances and thus implements abstraction.

Instead of making class attributes as public, these methods make them private,
provide validation that only correct values are set to the attributes and the
only correct caller has access to these attributes.

Let’s take the example of a bank record of a person. It contains balance,
transaction history, and other confidential records as part of it. Now, this
bank record needs to be handled as a built-in data type to facilitate many
operations. There are several methods which need access for balance and
transaction history. If they directly modify the balance, they might end up
inserting null values, or negative values that are very vulnerable. So, the
__getitem__() and __setitem__() helps in presenting the details securely.

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

class bank_record:

 

 def __init__(self, name):

 

 self.record = {

 "name": name,

 "balance": 100,

 "transaction":[100]

 }

 

 def __getitem__(self, key):

 

 return self.record[key]

 

 def __setitem__(self, key, newvalue):

 

 if key =="balance" and newvalue != None and
newvalue>= 100:

 self.record[key] += newvalue

 

 elif key =="transaction" and newvalue != None:

 self.record[key].append(newvalue)

 

 def getBalance(self):

 return self.__getitem__("balance")

 

 def updateBalance(self, new_balance):

 

 self.__setitem__("balance", new_balance)

 self.__setitem__("transaction", new_balance) 

 

 def getTransactions(self):

 return self.__getitem__("transaction")

 

 def numTransactions(self):

 return len(self.record["transaction"])

 

sam = bank_record("Sam")

print("The balance is : "+str(sam.getBalance()))

 

sam.updateBalance(200)

print("The new balance is : "+str(sam.getBalance()))

print("The no. of transactions are: "+str(sam.numTransactions()))

 

sam.updateBalance(300)

print("The new balance is : "+str(sam.getBalance()))

print("The no. of transactions are: "+str(sam.numTransactions()))

print("The transaction history is: "+ str(sam.getTransactions()))  
  
---  
  
 __

 __

 **Output**

    
    
    The balance is : 100
    The new balance is : 300
    The no. of transactions are: 2
    The new balance is : 600
    The no. of transactions are: 3
    The transaction history is: [100, 200, 300]

Here you can see, how easy to implement numTransactions(),
getTransactions(), getBalance(), setBalance(), just by implementing
__getitem__() and __setitem__() methods. Also, it takes care of validation
of balance and transaction history.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

