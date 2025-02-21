import re
import json
import requests
import pandas as pd
from selenium import webdriver
# import os

# assert os.path.isfile(file_path)

# url = "https://www.nba.com/players"
url = "https://www.nba.com/stats/players/traditional?PerMode=Totals&sort=PTS&dir=-1"
file_path = r"C:\Users\dusti\Documents\PythonPractice\PythonWebScaper\testResults2"

data = re.search(r'({"props":.*})', requests.get(url).text).group(0)
data = json.loads(data)

# uncomment to print all data:
# print(json.dumps(data, indent=4))

with open(file_path, 'w') as file:
    json.dump(data,file, indent=4)

df = pd.DataFrame(data["props"]["pageProps"]["players"])
# print(df.head().to_markdown())