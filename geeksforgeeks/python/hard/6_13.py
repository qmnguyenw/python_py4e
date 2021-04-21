Differential Privacy and Deep Learning



Differential privacy is a new topic in the field of deep learning. It is about
ensuring that when our neural networks are learning from sensitive data,
they’re only learning what they’re supposed to learn from the data.

 **Robust definition of privacy proposed by Cynthia Dwork (from her book
Algorithmic Foundations) –**

> “Differential Privacy” describes a promise, made by a data holder, or
> curator, to a data subject, and the promise is like this: “You will not be
> affected, adversely or otherwise, by allowing your data to be used in any
> study or analysis, no matter what other studies, data sets, or information
> sources, are available.”

The general goal of differential privacy is to ensure that different kind of
statistical analysis doesn’t compromise privacy and privacy is preserved if,
after the analysis, the analyzer doesn’t know anything about the features in
data-set, that means Information which has been made public elsewhere isn’t
harmful to an individual.  
To define privacy in the context of a simple database, we’re performing some
query against the database and if we remove a person from the database and the
query doesn’t change then that person’s privacy would be fully protected.

 **Let’s Understand with An Example**  
Given a database, which contains some numbers ‘1’ and ‘0’ which is some
sensitive data like if an individual has some kind of disease or not (maybe
patients don’t want to reveal this data).

  

  

    
    
      db = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0]

and now, you have your databases with one of each entry removed , which are
called parallel dbs. so there are ‘n’ number of parallel dbs if the length of
original db is ‘n’ , in our case it’s 10.  
Now, we consider one of parallel DBS, let’s take first one in which the first
individual is removed and what do we get?

    
    
     pdbs[0] = [0, 1, 1, 0, 1, 0, 1, 0, 0]

So you see that now this database has length ‘n-1’. So to calculate
sensitivity we need a query function so , we assume the simplest ‘sum’. So we
now focus on two results:

    
    
     sum(db) = 5
     sum(pdbs[0]) = 4

and the difference between above two is ‘1’ and we know that we need to find
the maximum of all these differences , since this db only contains ‘1’ and ‘0’
all those differences will either be ‘1’ (when similar like above , when 1 is
removed) or ‘0’ (when 0 is removed).  
Therefore, we get our sensitivity for this example as ‘1’ and this is really
high value and therefore differencing attacks can be easily done using this
‘sum’ query.  
The sensitivity should below so that it gives a quantitative idea of what
level of differencing attacks can reveal info/leak privacy.

 **Implementing the code for Differential Privacy in Python**

 __

 __  
 __

 __

 __  
 __  
 __

import torch

 

# the number of entries in our database

num_entries = 5000

 

db = torch.rand(num_entries) > 0.5

 

# generating parallel databases

def get_parallel_db(db, remove_index):

 

 return torch.cat((db[0:remove_index], 

 db[remove_index+1:]))

get_parallel_db(db, 52352)

 

def get_parallel_dbs(db):

 

 parallel_dbs = list()

 

 for i in range(len(db)):

 pdb = get_parallel_db(db, i)

 parallel_dbs.append(pdb)

 

 return parallel_dbs

 

pdbs = get_parallel_dbs(db)

 

# Creating linear and parallel databases

 

def create_db_and_parallels(num_entries):

 

 db = torch.rand(num_entries) > 0.5

 pdbs = get_parallel_dbs(db)

 

 return db, pdbs

 

db, pdbs = create_db_and_parallels(2000)

 

# Creating sensitivity function

 

def sensitivity(query, n_entries=1000):

 

 db, pdbs = create_db_and_parallels(n_entries)

 

 full_db_result = query(db)

 

 max_distance = 0

 for pdb in pdbs:

 pdb_result = query(pdb)

 

 db_distance = torch.abs(pdb_result - full_db_result)

 

 if(db_distance > max_distance):

 max_distance = db_distance

 

 return max_distance

 

# query our database and evaluate whether or not the result of the 

# query is leaking "private" information

 

def query(db):

 return db.float().mean()

sensitivity(query)  
  
---  
  
 __

 __

    
    
    Input : A randomly generated database(with the help of torch library)
    
    
    Output : tensor(0.0005)

 **Explanation**  
First of all, we create a random database with the help of torch library then
we defined two functions get_parallel_db and get_parallel_dbs for linear and
parallel databases. Now we defined sensitivity function then we measured the
difference between each parallel DB’s query result and the query result for
the entire database and then calculated the max value (which was 1). This
value is called **“sensitivity”**.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

