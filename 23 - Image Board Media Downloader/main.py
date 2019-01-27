import requests, sys, urllib.request, os
from bs4 import BeautifulSoup

url = str(sys.argv[1]).replace('http://', '').replace('https://', '')

data = requests.get(f'https://{url}')

soup = BeautifulSoup(data.text, 'html.parser')

imgs = []
for i in soup.find_all('a', {'class': 'fileThumb'}, href=True):
    imgs.append(i['href'].replace('//', ''))

if not os.path.exists(f'downloads/{url.split("/")[1]} - {url.split("/")[3]}'):
    os.makedirs(f'downloads/{url.split("/")[1]} - {url.split("/")[3]}')

for i in imgs:
    print(i.split("/")[2], end=' - ')
    urllib.request.urlretrieve(f'https://{i}', f'downloads/{url.split("/")[1]} - {url.split("/")[3]}/{i.split("/")[2]}')
    print("Done")
