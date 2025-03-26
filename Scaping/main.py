from bs4 import BeautifulSoup
import requests
import re


# URL of the webpage to scrape
url = "https://petkeen.com/most-expensive-dog-breeds/"

# Send a GET request to fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


data=soup.find_all('h3')[1:10]
dct={}
print("Name - Price")
for i in data:
    text=i.get_text(strip=True)
    prices = re.findall(r'\$\d{1,6}', text)
    print(prices)


    
