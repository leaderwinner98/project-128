import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table', {'class': 'wikitable'})
    all_data = []
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['td', 'th'])  

            cols = [col.text.strip() for col in cols]
            all_data.append(cols)


    df = pd.DataFrame(all_data)

    # Step 8: Save into CSV
    df.to_csv('brown_dwarfs_list.csv', index=False)

    print("Data saved to 'brown_dwarfs_list.csv'")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
