import sqlite3

name = "mbox-short.txt"
handle = open(name.strip(), 'r')

email_counts = dict()
org_counts = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    email = line.strip().split()[1]
    email_counts[email] = email_counts.get(email, 0) + 1
    org = email.strip().split('@')[1]
    org_counts[org] = org_counts.get(org, 0) + 1

# print(org_counts)

conn = sqlite3.connect('q3.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

for k, v in org_counts.items():
    # print(k)
    # print(v)
    cursor.execute('''INSERT INTO Counts(org, count) VALUES (?,?)''', (k, v))

conn.commit()

table = cursor.execute('''SELECT * FROM Counts''')
rows = cursor.fetchall()

print('Output:')
for row in rows:
    print(row)
