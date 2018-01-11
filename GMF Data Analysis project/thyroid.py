from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(open("thyroid.html"), "html.parser")

name = soup.title.get_text() + ".csv"

f = csv.writer(open(name, "w"))
f.writerow(["Year","Incidences Seer 9", "Incidences Seer 13", "Deaths"])


tableRows = soup.find_all('tr')
for row in tableRows:
    tableDatas = row.find_all("td")

    try:
        years = str(tableDatas[0].get_text())
        incds9 = str(tableDatas[1].get_text())
        incds13 = str(tableDatas[2].get_text())
        deaths = str(tableDatas[3].get_text())
    except:
        print("bad row string")
        continue

    f.writerow([years, incds9, incds13, deaths])
