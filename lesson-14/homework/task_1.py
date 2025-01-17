from bs4 import BeautifulSoup
import re

# HTML faylini ochish
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Jadvalni topish
table = soup.find("table")
rows = table.find_all("tr")

# Ob-havo ma'lumotlarini chiqarish
forecast = []
for row in rows[1:]:
    cols = row.find_all("td")
    day = cols[0].text
    temp = re.sub(r'[^\d]', '', cols[1].text)  # Haroratdagi raqamdan boshqa belgilarni olib tashlash
    condition = cols[2].text
    forecast.append({"day": day, "temp": int(temp), "condition": condition})
    print(f"{day}: {temp}°C, {condition}")

# Ma'lum kunlarning ma'lumotlarini topish
max_temp_day = max(forecast, key=lambda x: x["temp"])
sunny_days = [day["day"] for day in forecast if day["condition"] == "Sunny"]

print(f"\nEng yuqori harorat {max_temp_day['day']} kuni: {max_temp_day['temp']}°C")
print("Quyoshli kunlar: " + ", ".join(sunny_days))

# O'rtacha haroratni hisoblash
avg_temp = sum(day["temp"] for day in forecast) / len(forecast)
print(f"O'rtacha harorat: {avg_temp:.2f}°C")
