import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os 






# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")

# driver = webdriver.Chrome(options=options)
# url3 = 'https://www.op.gg/summoner/userName=' + Name
# # action = ActionChains(driver)
# driver.get(url3)


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
url = "https://www.op.gg/ranking/ladder/"
url2 = "https://kr.leagueoflegends.com/ko-kr/news/game-updates/"
# Name = ''
# url3 = "https://www.op.gg/summoner/userName=" + Name

#승률(몇승/몇패), 최근 게임 플레이 언제했는지, 챔피언 모스트3, 티어(점수), 총 게임 수

res = requests.get(url, headers=headers)
res2 = requests.get(url2, headers=headers)


res.raise_for_status()
res2.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
soup2 = BeautifulSoup(res2.text, "lxml")

rankings = soup.select("a.ranking-highest__name")
rankings2 = soup2.select("a.style__Wrapper-i44rc3-0.style__ResponsiveWrapper-i44rc3-13.gkCnQM.isVisible")
# rankings = soup.find_all("td", attrs={"class":"title"})
# title = ranking[1].get_text()
# link = ranking[1].a["href"]


title = []
link = []
for ranking in rankings:
    #텍스트만 불러오기
    # title.append(ranking.get_text())
    
    # href불러오기
    link.append(ranking.attrs["href"])


link1 = []
viewLink = []
for ranking2 in rankings2:
    title.append(ranking2.find("h2", attrs={"class":"style__Title-i44rc3-8 jprNto"}).get_text())
    
    viewLink.append("https://kr.leagueoflegends.com" + ranking2.attrs["href"])


#업데이트소식 원본 주소
# print("https://kr.leagueoflegends.com" + link1[0])
print(title, link)


print(os.path.isfile("C:/Users/wjeeh/Desktop/웹 크롤링 프로젝트/selenium/index.html")) 
file = open('C:/Users/wjeeh/Desktop/웹 크롤링 프로젝트/selenium/index.html','w',encoding='UTF-8')
start = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>페이지 소개</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
  </head>
  <body>
"""
#이 파일 돌리면 파일이 하나 생서되는거임  그게 html임
#추가하고있따이가 내용하나씩//////////////
empty = """
<div class="list-group">
  <a href="
""" + viewLink[0] + """
  " class="list-group-item list-group-item-action active" aria-current="true">
""" + title[0] + """
  </a>
  <a href="
""" + viewLink[1] + """
  " class="list-group-item list-group-item-action">
""" + title[1] + """
  </a>
  <a href="
""" + viewLink[2] + """
" class="list-group-item list-group-item-action">
""" + title[2] + """
A third link item</a>
  <a href="
""" + viewLink[3] + """
" class="list-group-item list-group-item-action">
""" + title[3] + """
A fourth link item</a>
  <a href="
""" + viewLink[4] + """
" class="list-group-item list-group-item-action disabled" tabindex="-1" aria-disabled="true">
""" + title[4] + """
A disabled link item</a>
</div>
"""
end = """
    </body>
</html>
"""
# #여기에 문자형 변수 하나 지정하고 그 변수에다가 다 넣으면 될듯
# # 아니면 변수 3개 지정하고 body안에 들어갈것만 따로 저 크롤링 한 내용 넣어서 연결시키고 write에 다 넣고 저장 
file.write(start + empty + end) 
file.close()





def parseOPGG(Name):
    Container = {}
    # Container
    SummonerName = ""
    Ranking = ""

    Tier = []
    LP = []
    Wins = []
    Losses = []
    Ratio = []

    url3 = 'https://www.op.gg/summoner/userName=' + Name
    req = requests.get(url3, headers=headers)
    html = req.text
    soup3 = BeautifulSoup(html, 'lxml')

    for i in soup3.select('span.Name'):
        SummonerName = i.text
        
    Container['SummonerName'] = SummonerName
    

    for j in soup3.select('div.TierRank'):
        Tier.append(j.text.strip())
    Container['Tier'] = Tier

    for i in soup3.select('span.LeaguePoints'):
        LP.append(i.text.strip())
    Container['LP'] = LP

    for i in soup3.select('span.wins'):
        if len(Wins) >= len(Tier):
            break
        Wins.append(i.text)
    Container['Wins'] = Wins
    
    for i in soup3.select('span.losses'):
        if len(Losses) >= len(Tier):
            break
        Losses.append(i.text)
    Container['Losses'] = Losses
    
    for i in soup3.select('span.winratio'):
        Ratio.append(i.text)
    Container['Ratio'] = Ratio
    
    return Container

def printSummonerInfo(Container):
    rankCase = ['솔로', '자유']
    for i in range(len(Container['Tier'])):
        if Container['SummonerName'] != '':
            print("==================================")
            if len(Container['Tier']):
                print(Container['SummonerName'] + "님의 " + rankCase[i] + "랭크 정보입니다.")
                print("==================================")
                print("티어: " + Container['Tier'][i])
                print("LP: " + Container['LP'][i])
                print("승/패: " + Container['Wins'][i] + "/" + Container['Losses'][i])
                print("승률: " + Container['Ratio'][i])
            else:
                print(Container['SummonerName'] + "님은 Unranked입니다.")
                print("==================================")

# name = input("검색할 닉네임을 입력하세요 : ")
# printSummonerInfo(parseOPGG(name))
# #import를 하는 경우 실행을 방지하기 위해서 이런식으로 작성하는듯
# if __name__ == "__main__":

#     printSummonerInfo(parseOPGG("DRX deft"))        

