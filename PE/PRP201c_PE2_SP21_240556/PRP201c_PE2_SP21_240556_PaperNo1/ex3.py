import sqlite3

conn = sqlite3.connect('dbSubList.sqlite')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS SubList')
cursor.execute('CREATE TABLE SubList(SCode TEXT, credit INTEGER, SDes TEXT)')

with open('./SubjectList.txt', 'r') as f:
    f.readline()
    for line in f:
        scode = line.split()[0]
        credit = line.split()[1]
        try:
            credit = int(credit)
            if credit > 3:
                sdes = 'too many'
            else:
                sdes = None
        except:
            continue
        cursor.execute('''INSERT INTO SubList(SCode, credit, SDes) VALUES (?, ?, ?)''',(scode, credit, sdes))

conn.commit()

table = cursor.execute('''SELECT * FROM SubList''')
rows = cursor.fetchall()

print('Inserted row:')
for row in rows:
    print(row)

cursor.execute('''SELECT count(*) FROM SubList''')
num = cursor.fetchall()
print('Number of processed recored: {}'.format(num[0][0]))

cursor.execute('''SELECT * FROM SubList
                    Order by credit DESC LIMIT 3''')
rows = cursor.fetchall()
print('Print top 3 row of table :{}'.format(rows))
# for row in rows:
#     print(row)

print("SCode\tcredit\tSDes")
for row in rows:
    print(row[0], row[1], row[2], sep = '\t')
conn.close()

    
    

