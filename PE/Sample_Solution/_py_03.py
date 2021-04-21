import sqlite3

# Create database file
fu_db = sqlite3.connect("dbFPT.sqlite")
cursor = fu_db.cursor()

# Initialize the database
init_script = """
DROP TABLE IF EXISTS InFos;

CREATE TABLE InFos
(
    ProCode INTEGER PRIMARY KEY,
    Deleted TEXT
);
"""
cursor.executescript(init_script)

# Read datafile, and add to the database
data_raw = open('datafile.txt')
num_line = 0
for line in data_raw:
    # Skip the first line (the title line)
    num_line += 1
    if num_line == 1:
        continue
    data_piece = line.rstrip().split()
    # Add to the database
    pro_code = int(data_piece[0].strip())
    deleted = data_piece[3]
    cursor.execute("""INSERT INTO InFos(ProCode, Deleted)
    VALUES (?, ?)""", (pro_code, deleted))
    fu_db.commit()

# Show data
cursor.execute("SELECT COUNT(*) FROM InFos")
num_of_records = cursor.fetchone()[0]
print("Number of processed records:", num_of_records)
show_data = "SELECT * FROM InFos ORDER BY ProCode DESC LIMIT 3"
cursor.execute(show_data)
data = cursor.fetchall()
print("ProCode\tDeleted")
for row in data:
    print(row[0], row[1], sep = '\t')
fu_db.close()