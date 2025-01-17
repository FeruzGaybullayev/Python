import requests
from bs4 import BeautifulSoup
import json

# Saytga so'rov yuborish va asosiy sahifani yuklash
url = "https://www.demoblaze.com/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

laptops = []

def scrape_laptops(page_soup):
    items = page_soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
    for item in items:
        name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        description = item.find("p", class_="card-text").text.strip()
        laptops.append({"name": name, "price": price, "description": description})

# Dastlabki sahifani qirib olish
scrape_laptops(soup)

# Keyingi sahifalarga o'tish va ma'lumotlarni qirib olish
while True:
    next_btn = soup.find("button", id="next2")
    if next_btn:
        onclick_value = next_btn.get("onclick")
        if onclick_value:
            next_page_url = "https://www.demoblaze.com/" + onclick_value.split("'")[1]
            response = requests.get(next_page_url)
            soup = BeautifulSoup(response.text, "html.parser")
            scrape_laptops(soup)
        else:
            break
    else:
        break

# JSON formatida saqlash
with open("laptops.json", "w") as file:
    json.dump(laptops, file, indent=4)

print("Noutbuk ma'lumotlari JSON formatida saqlandi.")
