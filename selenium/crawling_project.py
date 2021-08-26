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
rankName = []
for ranking in rankings:
    #텍스트만 불러오기
    # title.append(ranking.get_text())
    rankName.append(ranking.get_text())
    # href불러오기
    link.append("https://www.op.gg/summoner/userName=" + ranking.get_text())


link1 = []
viewLink = []
for ranking2 in rankings2:
    title.append(ranking2.find("h2", attrs={"class":"style__Title-i44rc3-8 jprNto"}).get_text())
    
    # viewLink.append("https://kr.leagueoflegends.com" + ranking2.attrs["href"])
    viewLink.append(ranking2.attrs["href"])


print(title)

#업데이트소식 원본 주소
# print("https://kr.leagueoflegends.com" + link1[0])


print(os.path.isfile("C:/Users/wjeeh/Desktop/웹 크롤링 프로젝트/selenium/index.html")) 
file = open('C:/Users/wjeeh/Desktop/web_crawling_project/selenium/index.html','w',encoding='UTF-8')
start = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>페이지 소개</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <link rel="stylesheet" href="default.css">   
    <!-- <script src='./gg.js'></script> -->
  </head>
  <body>
"""
#이 파일 돌리면 파일이 하나 생서되는거임  그게 html임
#추가하고있따이가 내용하나씩//////////////
linkFront = """
  </a>
  <a href="
"""
linkBack = '" class="list-group-item list-group-item-action">'
empty = """
<div class="container mt-5">
      <h1>gntech.gg</h1>
      <div class="row mt-3">
        <div class="list-group col-4">
          <a href="
""" + viewLink[0] + linkBack + title[0] + linkFront + viewLink[1] + linkBack + title[1] + linkFront + viewLink[2] + linkBack + title[2] + linkFront + viewLink[3] + linkBack + title[3] + linkFront + viewLink[4] + linkBack + title[4] + """
          </a>
</div>
<div class="list-group col-4">
          <a href="
""" + link[0] + linkBack + rankName[0] + linkFront + link[1] + linkBack + rankName[1] + linkFront + link[2] + linkBack + rankName[2] + linkFront + link[3] + linkBack + rankName[3] + linkFront + link[4] + linkBack + rankName[4] + """
          </a>
        </div>
        <div class="topnav col-4" >
          <form class='search' action="https://www.op.gg/summoner/">
            <input  class="keyword" type="text" placeholder="소환사명을 입력해주세요" name="userName" value="">
            <!-- 일단 네임으로 값을 넘기고? 그걸 자바크립트 함수로 받고 함수에서 반환값을 주고? 그거를 주소에다가 더하면? 근데 클릭하면 주소로 이동해야하니까 바로바로 함수를 반환할수있는 걸 넣어야겠네 -->
            <button class="img-button" value ="" type="submit">검색</button>
          </form>
        </div>
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



#여기부터

# def parseOPGG(Name):
#     Container = {}
#     # Container
#     SummonerName = ""
#     Ranking = ""

#     Tier = []
#     LP = []
#     Wins = []
#     Losses = []
#     Ratio = []

#     url3 = 'https://www.op.gg/summoner/userName=' + Name
#     req = requests.get(url3, headers=headers)
#     html = req.text
#     soup3 = BeautifulSoup(html, 'lxml')

#     for i in soup3.select('span.Name'):
#         SummonerName = i.text
        
#     Container['SummonerName'] = SummonerName
    

#     for j in soup3.select('div.TierRank'):
#         Tier.append(j.text.strip())
#     Container['Tier'] = Tier

#     for i in soup3.select('span.LeaguePoints'):
#         LP.append(i.text.strip())
#     Container['LP'] = LP

#     for i in soup3.select('span.wins'):
#         if len(Wins) >= len(Tier):
#             break
#         Wins.append(i.text)
#     Container['Wins'] = Wins
    
#     for i in soup3.select('span.losses'):
#         if len(Losses) >= len(Tier):
#             break
#         Losses.append(i.text)
#     Container['Losses'] = Losses
    
#     for i in soup3.select('span.winratio'):
#         Ratio.append(i.text)
#     Container['Ratio'] = Ratio
    
#     return Container

# def printSummonerInfo(Container):
#     rankCase = ['솔로', '자유']
#     for i in range(len(Container['Tier'])):
#         if Container['SummonerName'] != '':
#             print("==================================")
#             if len(Container['Tier']):
#                 print(Container['SummonerName'] + "님의 " + rankCase[i] + "랭크 정보입니다.")
#                 print("==================================")
#                 print("티어: " + Container['Tier'][i])
#                 print("LP: " + Container['LP'][i])
#                 print("승/패: " + Container['Wins'][i] + "/" + Container['Losses'][i])
#                 print("승률: " + Container['Ratio'][i])
#             else:
#                 print(Container['SummonerName'] + "님은 Unranked입니다.")
#                 print("==================================")
# 여기까지


# name = input("검색할 닉네임을 입력하세요 : ")
# printSummonerInfo(parseOPGG(name))
# #import를 하는 경우 실행을 방지하기 위해서 이런식으로 작성하는듯
# if __name__ == "__main__":

#     printSummonerInfo(parseOPGG("DRX deft"))        

