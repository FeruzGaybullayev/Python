import sqlite3

# Task 2
# Connect to the library database
conn_library = sqlite3.connect('library.db')
cursor_library = conn_library.cursor()

# Step 1 & 2: Create the Books table
cursor_library.execute('''CREATE TABLE IF NOT EXISTS Books (
                           Title TEXT, 
                           Author TEXT, 
                           Year_Published INTEGER, 
                           Genre TEXT)''')

# Step 3: Insert Data
cursor_library.executemany('''INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)''',
                           [('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
                            ('1984', 'George Orwell', 1949, 'Dystopian'),
                            ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')])

# Step 4: Update Data
cursor_library.execute('''UPDATE Books
                          SET Year_Published = 1950
                          WHERE Title = '1984' ''')

# Step 5: Query Data
cursor_library.execute('''SELECT Title, Author
                          FROM Books
                          WHERE Genre = 'Dystopian' ''')
print(cursor_library.fetchall())

# Step 6: Delete Data
cursor_library.execute('''DELETE FROM Books
                          WHERE Year_Published < 1950 ''')

# Bonus Task: Add a new column and update data
cursor_library.execute('''ALTER TABLE Books
                          ADD COLUMN Rating REAL''')

# Update Rating values
cursor_library.execute('''UPDATE Books
                          SET Rating = 4.8
                          WHERE Title = 'To Kill a Mockingbird' ''')
cursor_library.execute('''UPDATE Books
                          SET Rating = 4.7
                          WHERE Title = '1984' ''')
cursor_library.execute('''UPDATE Books
                          SET Rating = 4.5
                          WHERE Title = 'The Great Gatsby' ''')

# Advanced Query: Retrieve all books sorted by Year_Published in ascending order
cursor_library.execute('''SELECT * FROM Books
                          ORDER BY Year_Published ASC ''')
print(cursor_library.fetchall())

# Save (commit) the changes and close the connection
conn_library.commit()
conn_library.close()
