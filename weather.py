import bs4
from bs4 import BeautifulSoup
from pprint import pprint
import requests

def weather():
  html = requests.get('https://search.naver.com/search.naver?query=날씨')
  soup = BeautifulSoup(html.text, 'html.parser')
  data1 = soup.find('div', {'class':'weather_box'})
  pprint(soup)
  find_address = data1.find('span', {'class':'btn_select'}).text
  Area = '현재 위치는 '+find_address+'이다옹'
  find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
  Temp = '현재 온도는 '+find_currenttemp+'도다옹'
  data2 = data1.findAll('dd')
  find_dust = data2[0].find('span', {'class':'num'}).text
  mask = find_dust[0:2]



# if int(mask) <= 30:
#     print("현재 미세먼지 적정")
# elif int(mask) <= 80:
#     print("현재 미세먼지 보통")
# elif int(mask) <= 150:
#     print("현재 미세먼지 나쁨")
# else:
#     print("현재 미세먼지 최악")