from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# # print(soup)
# latest_news = soup.find("div", attrs={"class":"medium-widget blog-widget"})
# # print("len latest news", len(latest_news))
# # print(latest_news)

# # titles = latest_news.find_all("a")
# # times = latest_news.find_all("time")
# #print(title)

# # for item in titles:
# #     print(item.get_text())
# #     print(item.get("href"))
# #     print("-"*30)

# # for item in times:
# #     print(item.get_text())
# #     print("-"*30)

# Upcoming_Events = soup.find("div", attrs={"class":"medium-widget event-widget last"})
# # print("len Upcoming Events", len(Upcoming_Events))
# # print(Upcoming_Events)

# titles = Upcoming_Events.find_all("a")
# times = Upcoming_Events.find_all("time")
# # print(titles)

# for item in titles:
#     print(item.get_text())
#     print(item.get("href"))
#     print("-"*30)

# for item in times:
#     print(item.get_text())
#     print("-"*30)


titles = soup.select("div.medium.widget.event.widget.last ul.menu li a")
# print(titles)

for item in titles:
    print(item.get_text())
