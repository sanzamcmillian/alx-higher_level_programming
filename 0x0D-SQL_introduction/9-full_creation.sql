-- Creates and fills the table second_table with attributes id, name and score in my MySQL server with mutliple rows.
CREATE table IF NOT EXISTS second_table('id' INT, 'name' VARCHAR, 'score' INT);
INSERT INTO second_table('id', 'name', 'score') 
VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);