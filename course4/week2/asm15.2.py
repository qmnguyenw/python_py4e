import sqlite3

# Create and connect to database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Initialise database
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Open file and execute
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    # Get domain name
    if not line.startswith('From: '): continue
    email = line.split()[1]
    domain = email.split('@')[1]

    # Get the current count value from the database
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()

    # if the domain is not yet in db, add it
    if row is None:
        cur.execute('INSERT INTO Counts(org, count) VALUES (?, 1)', (domain,))
    # or update count value of it
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

# commit changes to the db
conn.commit()

# get back data from db 
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(row[0], row[1])
    # print(str(row[0]), row[1])

cur.close()

