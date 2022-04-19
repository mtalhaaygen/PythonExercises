import requests
import json

url = "https://api.themoviedb.org/3/{0}?api_key=fffdac669e0889fd6f1554619ec5a5d2&{1}page=1"

while True:
    menu = input("""
    En popüler filmler-->1
    Vizyondaki filmler-->2
    Film ara   -->3
    Exit    -->4
    """)

    if menu == "4":
        break
    else:
        if menu == "1":
            result = requests.get(url.format("movie/popular","language=tr-TR&"))
            result = json.loads(result.text)
            for i in range(20):
                print(i+1,result["results"][i]["title"])
        elif menu == "2":
            result = requests.get(url.format("movie/now_playing","language=tr-TR&"))
            result = json.loads(result.text)
            for i in range(20):
                print(i+1,result["results"][i]["title"])
        elif menu == "3":
            a = input("Bir kelimeye göre ara : ")
            a = f"query={a}&"
            result = requests.get(url.format("search/company", a))
            result = json.loads(result.text)
            for i in result['results']:
                print(i["name"])

