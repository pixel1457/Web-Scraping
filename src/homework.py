import requests
import sqlite3
from bs4 import BeautifulSoup

url = 'https://www.technolife.com/product-165916/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%D9%8A%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%85%D8%AF%D9%84-galaxy-s25-fe-%D8%B8%D8%B1%D9%81%DB%8C%D8%AA-256-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%B1%D9%85-8-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA---%D9%88%DB%8C%D8%AA%D9%86%D8%A7%D9%85'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

DB_NAME = "MobileProduct2.db"
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

query = '''CREATE TABLE IF NOT EXISTS MobileData
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
brand TEXT,
price TEXT,
ram TEXT,
rom TEXT,
color TEXT,
score TEXT
)
'''

cursor.execute(query)
conn.commit()
print("TABLE CREATED")

cards = soup.select(r".relative.flex.w-\[55\%\]")
print("cards found:", len(cards))

for card in cards:
    title_tag = card.find("h2")
    if title_tag is None:
        continue
    title = title_tag.text.strip()

    price_tag = card.select_one(".text-\\[19px\\]")
    if price_tag is None:
        continue
    price = price_tag.text.strip()

    ram_tag = card.select_one(".ml-1.line-clamp-5.text-\\[12px\\]")
    if ram_tag is None:
        continue
    ram = ram_tag.text.strip()

    rom_tag = card.select_one(".ml-1.line-clamp-5.text-\\[12px\\]")
    if rom_tag is None:
        continue
    rom = rom_tag.text.strip()

    color_tag = card.select_one(".div.border-primary-shade-10 p")
    if color_tag is None:
        continue
    color = color_tag.text.strip()

    score_tag = card.select_one("strong.text-5xl.text-primary-tint-1")
    if score_tag is None:   
        continue
    score = score_tag.text.strip()

    print(title, price, ram, rom, color, score)
    cursor.execute(
        "INSERT INTO MobileData (title, brand, price, ram, rom, color, score) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (title, "", price, ram, rom, color, score),
    )

    conn.commit()
conn.close()
print("WEB DATA Scraped")