import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

# Saytga so'rov yuborish
url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Ish o'rinlari ro'yxatini topish
jobs = soup.find_all("div", class_="card-content")

# SQLite bazasini o'rnatish
conn = sqlite3.connect("jobs.db")
c = conn.cursor()

# Jadvalni yaratish (agar hali mavjud bo'lmasa)
c.execute('''CREATE TABLE IF NOT EXISTS jobs
             (title TEXT, company TEXT, location TEXT, description TEXT, link TEXT, PRIMARY KEY (title, company, location))''')

# Ma'lumotlarni kiritish
for job in jobs:
    title = job.find("h2", class_="title").text.strip() if job.find("h2", class_="title") else "No Title"
    company = job.find("h3", class_="company").text.strip() if job.find("h3", class_="company") else "No Company"
    location = job.find("p", class_="location").text.strip() if job.find("p", class_="location") else "No Location"
    description = job.find("div", class_="description").text.strip() if job.find("div", class_="description") else "No Description"
    link = job.find_all("a")[-1]["href"] if job.find_all("a") else "No Link"

    c.execute('''INSERT OR IGNORE INTO jobs (title, company, location, description, link) 
                 VALUES (?, ?, ?, ?, ?)''', 
              (title, company, location, description, link))

conn.commit()
conn.close()
