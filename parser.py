from urllib.request import *
from bs4 import BeautifulSoup

url = 'https://wallhaven.cc/search?q=fire&page='


def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html


def main():
    opener = build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    install_opener(opener)
    for i in range(1,2):
        html = get_html(url + str(i))
        soup = BeautifulSoup(html, 'html.parser')
        list = soup.find_all(class_='preview')
        for a in list:
            sec_html = get_html(a['href'])
            sec_soup = BeautifulSoup(sec_html, 'html.parser')
            image = sec_soup.find(id='wallpaper')['src']
            print(image)
            urlretrieve(image, image[41:])


main()
