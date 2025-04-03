from bs4 import BeautifulSoup
import requests

url = "https://indianexpress.com/"
try:
    response = requests.get(url)
except Exception:
    print("Something Went Wrong:")

else:
    soup = BeautifulSoup(response.text, "html.parser")
    all_h3=soup.find_all('h3')
    news_list=[]
    for i in all_h3:
        news_list.append(i.get_text(strip=True)+"\n")
    
    try:
        with open('./data_files/news_list.txt',mode='w',newline='') as file:
            file.writelines(news_list)
    except Exception:
        print("End Of FileError:")
    
    finally:
        print("Write File Success Fully:")

finally:
    print("Program Complete Successfully:")