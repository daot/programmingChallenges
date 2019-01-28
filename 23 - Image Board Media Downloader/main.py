import requests, sys, urllib.request, os, time, datetime
from bs4 import BeautifulSoup

while(True):
    count = 1
    while (count < len(sys.argv)):
        url = str(sys.argv[count]).replace('http://', '').replace('https://', '')
        print(datetime.datetime.now(),'Checking:', url)

        data = requests.get(f'https://{url}')

        soup = BeautifulSoup(data.text, 'html.parser')

        imgs = []
        for i in soup.find_all('a', {'class': 'fileThumb'}, href=True):
            imgs.append(i['href'].replace('//', ''))

        names = []
        for i in soup.find_all('div', {'class': 'fileText'}):
            for x in i.find_all('a'):
                names.append(x.text.replace("(...)", ""))

        if not os.path.exists(f'downloads/{url.split("/")[1]} - {url.split("/")[3]}'):
            os.makedirs(f'downloads/{url.split("/")[1]} - {url.split("/")[3]}')

        for i in range(0, len(imgs)):
            if(os.path.isfile(f'downloads/{url.split("/")[1]} - {url.split("/")[3]}/{names[i]}') == False):
                print(datetime.datetime.now(), 'Downloading:', names[i], end=' - ')
                urllib.request.urlretrieve(f'https://{imgs[i]}', f'downloads/{url.split("/")[1]} - {url.split("/")[3]}/{names[i]}')
                print('Done')
        count += 1

    time.sleep(10)
