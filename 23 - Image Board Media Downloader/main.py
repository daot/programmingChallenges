import requests, sys, urllib.request, os, time, datetime
from bs4 import BeautifulSoup

while(True):
    count = 1
    while (count < len(sys.argv)):
        url = str(sys.argv[count]).replace('http://', '').replace('https://', '')

        data = requests.get(f'https://{url}')

        soup = BeautifulSoup(data.text, 'html.parser')
		
        sys.stdout.write(f'{datetime.datetime.now()} Checking: {soup.find("span", {"class": "subject"}).text} - {url}\n')
        sys.stdout.flush()

        imgs = []
        for i in soup.find_all('a', {'class': 'fileThumb'}, href=True):
            imgs.append(i['href'].replace('//', ''))

        names = []
        for i in soup.find_all('div', {'class': 'fileText'}):
            for x in i.find_all('a'):
                names.append(x.text.replace("(...)", ""))

        if not os.path.exists(f'downloads/{soup.find("span", {"class": "subject"}).text} - {url.split("/")[1]} - {url.split("/")[3]}'):
            os.makedirs(f'downloads/{soup.find("span", {"class": "subject"}).text} - {url.split("/")[1]} - {url.split("/")[3]}')

        for i in range(0, len(imgs)):
            if(os.path.isfile(f'downloads/{soup.find("span", {"class": "subject"}).text} - {url.split("/")[1]} - {url.split("/")[3]}/{names[i]}') == False):
                sys.stdout.write(f'{datetime.datetime.now()} Downloading: {names[i]}\n')
                sys.stdout.flush()
                urllib.request.urlretrieve(f'https://{imgs[i]}', f'downloads/{soup.find("span", {"class": "subject"}).text} - {url.split("/")[1]} - {url.split("/")[3]}/{names[i]}')
        count += 1

    time.sleep(10)
