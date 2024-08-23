# webpage text file save and run web page 

import requests
import os
import webbrowser as wb

url = "https://github.com/Saddam6260"

response = requests.get(url)

with open("github.html", "w", encoding=response.encoding) as fp:
    fp.write(response.text)

file_path = os.path.realpath("github.html")
print(file_path)

wb.open("file://" + file_path)


 