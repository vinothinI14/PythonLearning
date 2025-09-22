import requests
from bs4 import BeautifulSoup

subLi=[]
mainLi = []
data = requests.get("https://www.jiosaavn.com/featured/mersal-hits/x7NaWNE3kRw_")
soup = BeautifulSoup(data.content,"html.parser")
# print(soup.prettify())

songList=soup.find('ol',{'class':'o-list-bare u-margin-bottom-none@sm'})
print(songList.prettify())
lists = songList.find_all('li')
for list in lists:
    data = list.find('figure')
    if data:
        image = data.find('figcaption')

        mainLi.append(image.a.text)
        url = image.a['href']
        song = requests.get("https://www.jiosaavn.com"+url)
        sngSoup=BeautifulSoup(song.content,"html.parser")
        songData = sngSoup.find('figure')

        if songData:
            subLi.append(songData.a['title'])
print("Main song list",mainLi)
print("Sub song list",subLi)
assert mainLi == subLi