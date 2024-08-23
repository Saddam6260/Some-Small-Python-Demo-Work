# image download
import requests

url = "https://images.unsplash.com/photo-1719568174150-cfb595eb588b?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

response = requests.get(url)

with open("img.png", "wb") as fp:
    fp.write(response.content)

    