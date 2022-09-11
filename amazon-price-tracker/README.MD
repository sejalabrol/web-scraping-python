# Amazon Price Tracker
A Python Script to track the price of a product on [Amazon India](https://www.amazon.in/) using Beautiful Soup and receive an email alert whenever the price is favourable. 

## Tools
- [smtplib — SMTP protocol client](https://docs.python.org/3/library/smtplib.html)
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)

## Screenshot
![image](https://user-images.githubusercontent.com/87208681/189534243-beb5de43-3da6-4b37-9abb-476d577d62ae.png)

## Environment Variables
To run this project, you will need to add the following environment variables to your .env file
`MY_EMAIL` `MY_EMAIL_PASSWORD` `RECEIVER_EMAIL`

Refer to the [env template](https://github.com/sejalabrol/web-scraping-python/blob/main/amazon-price-tracker/.env.template)

## Run Locally
Clone the project
```bash
  git clone https://github.com/sejalabrol/web-scraping-python/
```
Go to the project directory
```bash
  cd web-scraping-python/amazon-price-tracker
```
Create a .env file and enter environment variables
```bash
  cp .env.template .env
```
[Create a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) (optional but recommended) 
```bash
  python -m venv venv
  source venv/Scripts/activate
```
Install dependencies
```bash
  pip install -r requirements.txt
```
Run the project
```bash
  python main.py
```
