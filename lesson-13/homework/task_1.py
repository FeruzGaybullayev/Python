import sqlite3

# Task 1
# Connect to the database
conn_roster = sqlite3.connect('roster.db')
cursor_roster = conn_roster.cursor()

# Step 1 & 2: Create the Roster table
cursor_roster.execute('''CREATE TABLE IF NOT EXISTS Roster (
                          Name TEXT, 
                          Species TEXT, 
                          Age INTEGER)''')

# Step 3: Insert Data
cursor_roster.executemany('''INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)''',
                          [('Benjamin Sisko', 'Human', 40),
                           ('Jadzia Dax', 'Trill', 300),
                           ('Kira Nerys', 'Bajoran', 29)])

# Step 4: Update Data
cursor_roster.execute('''UPDATE Roster
                         SET Name = 'Ezri Dax'
                         WHERE Name = 'Jadzia Dax' ''')

# Step 5: Query Data
cursor_roster.execute('''SELECT Name, Age
                         FROM Roster
                         WHERE Species = 'Bajoran' ''')
print(cursor_roster.fetchall())

# Step 6: Delete Data
cursor_roster.execute('''DELETE FROM Roster
                         WHERE Age > 100 ''')

# Bonus Task: Add a new column and update data
cursor_roster.execute('''ALTER TABLE Roster
                         ADD COLUMN Rank TEXT''')

# Update Rank values
cursor_roster.execute('''UPDATE Roster
                         SET Rank = 'Captain'
                         WHERE Name = 'Benjamin Sisko' ''')
cursor_roster.execute('''UPDATE Roster
                         SET Rank = 'Lieutenant'
                         WHERE Name = 'Ezri Dax' ''')
cursor_roster.execute('''UPDATE Roster
                         SET Rank = 'Major'
                         WHERE Name = 'Kira Nerys' ''')

# Advanced Query: Retrieve all characters sorted by Age in descending order
cursor_roster.execute('''SELECT * FROM Roster
                         ORDER BY Age DESC ''')
print(cursor_roster.fetchall())

# Save (commit) the changes and close the connection
conn_roster.commit()
conn_roster.close()
