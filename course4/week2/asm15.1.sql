-- SQLite
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
);

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Briaddon', 17);
INSERT INTO Ages (name, age) VALUES ('Alishba', 23);
INSERT INTO Ages (name, age) VALUES ('TJ', 18);
INSERT INTO Ages (name, age) VALUES ('Oona', 13);
INSERT INTO Ages (name, age) VALUES ('Emilia', 36);

SELECT * FROM Ages

SELECT hex(name || age) AS X FROM Ages ORDER BY X;