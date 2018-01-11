from bs4 import BeautifulSoup
import requests
import csv

page = requests.get("https://www.ers.usda.gov/webdocs/charts/58020/biotechcrops_d.html?v=42565")
geSoup = BeautifulSoup(page.content, "html.parser")
thyroidSoup = BeautifulSoup(open("thyroid.html"), "html.parser")

f = csv.writer(open("overlap.csv", "w"))
f.writerow(["Year", "HT Soybeans", "HT Cotton", "Bt Cotton", "Bt Corn", "Ht Corn", "Incidences Seer 9", "Incidences Seer 13", "Deaths"])

tTR = thyroidSoup.find_all('tr')
for row in tTR:
    tTD = row.find_all("td")

    try:
        years = str(tTD[0].get_text())
        incds9 = str(tTD[1].get_text())
        incds13 = str(tTD[2].get_text())
        deaths = str(tTD[3].get_text())


        hTSoybeans = "-"
        hTCotton = "-"
        bTCotton = "-"
        bTCorn = "-"
        hTCorn = "-"

        geTR = geSoup.find_all("tr")
        for geRow in geTR:
            geTD = geRow.find_all("td")

            # try:
            if (years == str(geTD[0].get_text())):
                hTSoybeans = str(geTD[1].get_text())
                hTCotton = str(geTD[2].get_text())
                bTCotton = str(geTD[3].get_text())
                bTCorn = str(geTD[4].get_text())
                hTCorn = str(geTD[5].get_text())

    except:
        print("bad row string")
        continue

    f.writerow([years, hTSoybeans, hTCotton, bTCotton, bTCorn, hTCorn, incds9, incds13, deaths])
