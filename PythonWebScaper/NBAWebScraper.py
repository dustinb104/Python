import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pandas as pd
import time
import numpy as np


file_path = r"C:\Users\dusti\Documents\PythonPractice\PythonWebScaper\testResults2"
# html_text = requests.get('https://www.nba.com/stats/players/traditional?PerMode=Totals&sort=PTS&dir=-1').text
# print(pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers))
api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2012-13&SeasonType=Regular%20Season&StatCategory=PTS'
r = requests.get(url=api_url).json()
table_headers = r['resultSet']['headers']

# print(table_headers)

df_cols = ['Year','Season_type'] + table_headers


season_types = ['Regular%20Season','Playoffs']
years = ['2012-13','2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21','2021-22','2022-23','2023-24']
df = pd.DataFrame(columns=df_cols)
begin_loop = time.time()

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9',
    'connection': 'keep-alive',
    'host': 'stats.nba.com',
    'origin': 'https://www.nba.com',
    'referer': 'https://www.nba.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

for y in years:
    for s in season_types:
        api_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season='+y+'&SeasonType='+s+'&StatCategory=PTS'
        r = requests.get(url=api_url, headers=headers).json()
        temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
        temp_df2 = pd.DataFrame({'Year': [y for i in range(len(temp_df1))],
                                'Season_type': [s for i in range(len(temp_df1))]})
        temp_df3 = pd.concat([temp_df2,temp_df1], axis=1)
        df = pd.concat([df, temp_df3], axis=0)
        print(f'Finished scraping data for the {y} {s}.')
        lag = np.random.uniform(low=5,high=30)
        print(f'...waiting {round(lag,1)} seconds')
        time.sleep(lag)

print(f'Process Complete! Total run time: {round((time.time()-begin_loop)/60,2)}')
df.to_excel('nba_player_data.xlsx', index=False)







# # print(temp_df3)
# # with open(file_path, 'w',encoding='utf-8') as file:
# #     json.dump(r['resultSet']['headers'],file,ensure_ascii=False, indent=4)

# # print(json_print_string)

# # soup = BeautifulSoup(html_text, 'lxml')
# # # players = soup.find_all('table', class_='Crom_table_p1iZz')

# # [print(item.prettify() ) for item in soup.find('div', class_='Crom_base__f0niE')]

# # print(players)