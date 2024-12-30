import sqlite3

# Ma'lumotlar bazasiga ulanish
con = sqlite3.connect('chinook.db')
cur = con.cursor()

# Jadvalni yaratish (agar u mavjud bo'lmasa)
cur.execute('''
CREATE TABLE IF NOT EXISTS albums (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    artist_id INTEGER NOT NULL
);
''')

# Jadvaldan ma'lumotlarni olish
cur.execute("SELECT * FROM albums")
albums = cur.fetchall()

# Natijani ko'rsatish
print(albums)

# O'zgarishlarni saqlash va ulanishni tugatish
con.commit()
con.close()

