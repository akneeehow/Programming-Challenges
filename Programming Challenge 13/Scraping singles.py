from os import sep
from bs4 import BeautifulSoup
import datetime

URL = ('https://www.officialcharts.com/charts/singles-chart/')
page = requests.get(URL) 

songs = []
artists = []
separate = []
seperate = [] 

soup = BeautifulSoup(page.content, 'html.parser')
codedtitle = soup.findAll("div", {"class": "title"}, limit=10)

for x in codedtitle:
    for i in x:
        separate.append(i)
songnumber = 1
for count in range(10):
    cv = str(separate[songnumber])
    big = cv.index(">") + 1
    small = [i for i, n in enumerate(cv) if n == '<'][1]
    songs.append((cv[big:small]))
    songnumber += 3

artist = soup.findAll("div", {"class": "artist"}, limit=10)
for x in artist: 
    for c in x:  
        seperate.append(c) 
artistnumber = 1 
for count in range(10): 
    av = str(seperate[artistnumber]) 
    abig = av.index(">") + 1 
    asmall = [i for i, n in enumerate(av) if n == '<'][1] 
    artists.append((av[abig:asmall])) 
    artistnumber += 3 

date = datetime.date.today()

print("Top 10 Official Singles")
print("-"*10)
print(f"As of {date}:")
print()
for x in range(10):
    print(f"{x + 1}. {songs[x]} - {artists[x]}") 


countdown = soup.find("section", {"class": "sidebar-countdown"})
print(countdown)
