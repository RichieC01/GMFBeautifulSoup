from bs4 import BeautifulSoup
import requests
import csv

page = requests.get("https://www.ers.usda.gov/webdocs/charts/58020/biotechcrops_d.html?v=42565")
soup = BeautifulSoup(page.content, "html.parser")

name = soup.h1.get_text() + ".csv"

f = csv.writer(open(name, "w"))
f.writerow(["Year", "HT Soybeans", "HT Cotton", "Bt Cotton", "Bt Corn", "Ht Corn"])

tableRows = soup.find_all("tr")
for row in tableRows:
    tableDatas = row.find_all("td")

    try:
        years = str(tableDatas[0].get_text())
        hTSoybeans = str(tableDatas[1].get_text())
        hTCotton = str(tableDatas[2].get_text())
        bTCotton = str(tableDatas[3].get_text())
        bTCorn = str(tableDatas[4].get_text())
        hTCorn = str(tableDatas[5].get_text())
    except:
        print("bad row string")

    f.writerow([years, hTSoybeans, hTCotton, bTCotton, bTCorn, hTCorn])
