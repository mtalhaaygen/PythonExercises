import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

htmldoc = requests.get(url).text
corba = BeautifulSoup(htmldoc, "html.parser")
#/html/body/div[3]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody
#//*[@id="main"]/div/span/div/div/div[3]/table/tbody
for i in range(20):
    title = corba.find("tbody", {"class":"lister-list"}).find_all("td", {"class": "titleColumn"})[i]
    print(f"{i+1}. {title.a.text}".ljust(52), f"Yıl = {title.span.text.strip('()')}")
#
# url = "https://www.trendyol.com/laptop-x-c103108"
# htmldoc = requests.get(url).text
# htmldoc = BeautifulSoup(htmldoc , "html.parser")
# corba = htmldoc.body.find_all("div",{"class":"prdct-desc-cntnr-wrppr"})
# for i in corba:
#     baslik = i.find("span",{"class":"prdct-desc-cntnr-name hasRatings"})
#     fiyat = i.find("div",{"class":"prc-box-dscntd"}).text
#     print(baslik, fiyat)