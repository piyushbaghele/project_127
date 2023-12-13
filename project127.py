import pandas as pd , time
from bs4 import BeautifulSoup
from selenium import webdriver

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"

browser = webdriver.Edge()
browser.get(START_URL)

scraped_data = []
time.sleep(7)
def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")

    bright_star_table = soup.find("table", attrs={"class", "sortable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')

        temp_list = []

        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)

        scraped_data.append(temp_list)

scrape()

# Print scraped_data to inspect the structure
for row in scraped_data:
    print(row)

# Update indices based on the structure of the table
stars_data = []

for i in range(0, len(scraped_data)):
    Star_names = scraped_data[i][1]  # Update index
    Distance = scraped_data[i][3]    # Update index

    required_data = [Star_names, Distance]
    stars_data.append(required_data)

headers = ['Star_name', 'Distance']
star_df_1 = pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv("scraped_data_1.csv", index=True, index_label='id')
