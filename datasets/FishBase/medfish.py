# medfish.py

"""
FishBase scrapper that exports a list of all fish in the Mediterranean, 
as listed in the FishBase database.
"""

import csv
import requests
from bs4 import BeautifulSoup as BS

def scrap_medfish(target_url: str) -> tuple[tuple[str]]:
    page = requests.get(target_url)
    soup = BS(page.content, "html.parser")
    medfish_dataset = []
    # Spot header
    header_entries = soup.find_all("th")
    hdr = []
    for h in header_entries:
        hdr.append(h.text)
    medfish_dataset.append(tuple(hdr))
    # Add data lines
    table_body = soup.find("tbody")
    table_rows = table_body.find_all("tr")
    rows = map(parse_table_row, table_rows)
    medfish_dataset += rows
    # Return dataset as tuple of tuples
    return tuple(medfish_dataset)
    
def parse_table_row(row) -> tuple[str]:
    cells = row.find_all("td")
    species = cells[0].find("a").text.lower()
    prow = [species] + [x.text.lower() for x in cells[1:]]
    return tuple(prow)

def save_as_csv(dataset: tuple[tuple[str]], path='medfish.csv') -> None:
    with open(path, 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(dataset)

if __name__ == "__main__":
    URL = "https://www.fishbase.se/TrophicEco/FishEcoList.php?ve_code=13"
    medfish = scrap_medfish(URL)
    save_as_csv(medfish)
