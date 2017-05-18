import urllib
import urllib.request
from bs4 import BeautifulSoup
from string import ascii_lowercase
import os

def make_soup(url):
    thrpage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thrpage, "html.parser")
    return  soupdata

soup =make_soup("http://iiitvadodara.ac.in/gallery.html")
num=1
i=1
for img in soup.findAll('img'):

    temp="http://iiitvadodara.ac.in/"+img.get('src')
    print(temp)

    filepath= "images/"
    dir=os.path.dirname(filepath)
    if not os.path.exists(dir):
        os.makedirs(dir)
    nametemp = img.get('alt')
    print(img.get('alt'))
    if len(nametemp) == 0:
        filename = str(i)
        i = i+1
    else:
        filename = nametemp

    imgfile = open("images/"+filename + ".jpeg", "wb")
    imgfile.write(urllib.request.urlopen(temp).read())
    imgfile.close()


