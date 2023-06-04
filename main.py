from bs4 import BeautifulSoup
import requests
import time

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=books&_sacat=0"

for i in range(1, 6):
    page = {"_pgn": i}

    try:
        r = requests.get(url, params=page)
        if r.ok:
            soup = BeautifulSoup(r.content, 'html.parser')
            items = soup.find_all("li", class_="s-item")

            for item in items:
                name_element = item.find("div", class_="s-item__title")
                if name_element:
                    name = name_element.get_text()
                    print(name)

            time.sleep(15)

    except requests.exceptions.RequestException as ex:
        print('Error:', ex)
