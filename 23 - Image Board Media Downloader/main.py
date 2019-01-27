import requests, sys, urllib.request, os, time
from bs4 import BeautifulSoup

url = str(sys.argv[1]).replace('http://', '').replace('https://', '')

start_time = time.time()
interval = 10
for x in range(20):
    time.sleep(start_time + x * interval - time.time())

    data = requests.get(f'https://{url}')

    soup = BeautifulSoup(data.text, 'html.parser')

    imgs = []
    for i in soup.find_all('a', {'class': 'fileThumb'}, href=True):
        imgs.append(i['href'].replace('//', ''))

    names = []
    for i in soup.find_all('div', {'class': 'fileText'}):
        for x in i.find_all('a'):
            names.append(x.text)

    if not os.path.exists(f'downloads/{url.split("/")[1]} - {url.split("/")[3]}'):
        os.makedirs(f'downloads/{url.split("/")[1]} - {url.split("/")[3]}')

    for i in range(0, len(imgs)):
        if(os.path.isfile(f'downloads/{url.split("/")[1]} - {url.split("/")[3]}/{names[i]}') == False):
            print(names[i], end=' - ')
            urllib.request.urlretrieve(f'https://{imgs[i]}', f'downloads/{url.split("/")[1]} - {url.split("/")[3]}/{names[i]}')
            print("Done")
