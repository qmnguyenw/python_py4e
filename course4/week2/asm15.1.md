# Our First Database

Create a SQLITE database or use an existing database and create a table in the database called "Ages":

```sql
CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)
```

Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

```sql
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Briaddon', 17);
INSERT INTO Ages (name, age) VALUES ('Alishba', 23);
INSERT INTO Ages (name, age) VALUES ('TJ', 18);
INSERT INTO Ages (name, age) VALUES ('Oona', 13);
INSERT INTO Ages (name, age) VALUES ('Emilia', 36);
```

Once the inserts are done, run the following SQL command:

```sql
SELECT hex(name || age) AS X FROM Ages ORDER BY X
```

Find the first row in the resulting record set and enter the long string that looks like **53656C696E613333**.

Note: This assignment must be done using SQLite - in particular, the `SELECT` query above will not work in any other database. So you cannot use MySQL or Oracle for this assignment.
