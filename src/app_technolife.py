import requests
import sqlite3
from bs4 import BeautifulSoup

url = 'https://www.technolife.com/category/mobile/mobile-phone'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

DB_NAME = "MobileProduct.db"
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

query = '''CREATE TABLE IF NOT EXISTS MobileData
(id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
price TEXT,
ram TEXT,
rom TEXT,
score TEXT
)
'''
cursor.execute(query)
conn.commit()
print("TABLE CREATED")

cards = soup.select(".relative.w-full.rounded-\\[10px\\]")
print("cards found:", len(cards))

for card in cards:
    title_tag = card.find("h2")
    if title_tag is None:
        continue
    title = title_tag.text.strip()

    price_tag = card.select_one("p.text-\\[22px\\].font-semiBold.leading-5")
    if price_tag is None:
        continue
    price = price_tag.text.strip()

    img_tag = card.select_one('a[href^="/product-"] img')
    image = img_tag.get("src") if img_tag else None
    img_url = "https://www.technolife.com" + image if image else None

    link_tag = card.select_one('a[href^="/product-"]')
    link = "https://www.technolife.com" + link_tag.get("href") if link_tag else None

    print(title, price, img_url, link)

    cursor.execute(
        "INSERT INTO MobileData (title, price, image, link) VALUES (?, ?, ?, ?)",
        (title, price, img_url, link)
    )

conn.commit()
conn.close()
print("WEB DATA Scraped")