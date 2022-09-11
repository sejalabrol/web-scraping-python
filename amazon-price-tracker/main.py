from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
import os
from dotenv import load_dotenv

# Fetching environment variables
load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
MY_EMAIL_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

"""
# Example url and favourable price
url = "https://www.amazon.in/Solobolo-Madhubani-Painting-Coasters-Supplies/dp/B09H72TYGJ/?_encoding=UTF8&pd_rd_w=p7Qex&content-id=amzn1.sym.e932aeaf-89ea-47b8-9c31-e92696d33d85&pf_rd_p=e932aeaf-89ea-47b8-9c31-e92696d33d85&pf_rd_r=V4F1P0KTSZ9SMQFSG368&pd_rd_wg=MyJMA&pd_rd_r=77878242-184e-420c-bf39-ac58de049e7c&ref_=pd_gw_ci_mcx_mr_hp_d"
favourable_price = 700
"""

url = input("Enter link of Amazon India product to track: ")
favourable_price = int(input("Enter favourable price: "))

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    },
)
contents = response.text

soup = BeautifulSoup(contents, "lxml")
price = soup.find(class_="a-price-whole").getText()[:-1]  # to remove decimal from price
product_title = soup.find(id="productTitle").getText().strip()  # to remove extra space

if price <= favourable_price:
    message_to_send = (
        f"The price of '{product_title}' is Rs {price}. Click the link to buy it\n{url}"
    )
else:
    message_to_send = f"The price of '{product_title}' is not yet under Rs {favourable_price}, it is for Rs {price}. Click the link to buy it anyway.\n{url}"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=recv_email, msg=message_to_send)
