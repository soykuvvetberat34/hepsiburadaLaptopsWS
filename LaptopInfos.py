import requests
from bs4 import BeautifulSoup

url="https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
}


html=requests.get(url,headers=headers).content
soup=BeautifulSoup(html,"lxml")
result=soup.find("ul",{"class":"productListContent-frGrtf5XrVXRwJ05HUfU productListContent-rEYj2_8SETJUeqNhyzSm"}).find_all("li")

for item in result:
    print(item.text.strip())
