from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
from email.mime.text import MIMEText

출처: https://yeolco.tistory.com/93 [열코의 프로그래밍 일기]

hdrs = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}
url = "https://www.amazon.com/EVGA-GeForce-12G-P5-3657-KR-Dual-Fan-Backplate/dp/B08WM28PVH/ref=sr_1_1?keywords=rtx+3060&qid=1645779490&sprefix=rtx%2Caps%2C386&sr=8-1"
webpage = requests.get(url, headers=hdrs)

soup = BeautifulSoup(webpage.content, "lxml")

price = soup.select(".a-price.a-text-price.a-size-medium.apexPriceToPay")
value = price[0].contents[0].getText()
value = float(value[1:])

if value <= 600:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('yjh15340@gmail.com', '')
