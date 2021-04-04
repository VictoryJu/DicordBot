# -*- coding:utf-8 -*-
import discord
import asyncio
from discord.ext import commands
import datetime
#from config import config
import os
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

weather.mask


#token = config.token 
badWord = ["씨발","좆냥이","쒸벌련","cex","ㅅㅂ","ㅆㅂ","씨벌","시발","시벌","좆냥","나비탕","좆냥이쉑"]

def checkBad(badword):
  for i in badWord:
    if badword == i:
      return True


def dday():
  startdday1 = datetime.date.today()
  startdday = startdday1.strftime('%Y-%m-%d')
  startyy=int(startdday.split('-')[0])
  startmm=int(startdday.split('-')[1])
  startdd=int(startdday.split('-')[2])
  sd = datetime.date(startyy, startmm, startdd) #시작기준일 설정
  enddday = ("2021-06-19")
  endyy = int(enddday.split('-')[0])
  endmm = int(enddday.split('-')[1])
  enddd = int(enddday.split('-')[2])
  ed = datetime.date(endyy, endmm, enddd) #끝 기준일 설정
  result=(sd - ed).days #차를 구하고 일수로 바꿈
  return result

def today():
  startdday1 = datetime.date.today()
  startdday = startdday1.strftime('%m월%d일')
  return startdday

#client = discord.Client()
client = commands.Bot(command_prefix='>',status=discord.Status.online, activity=discord.Game("반갑다옹 :D"))

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')
  await client.change_presence()

@client.event
async def on_message(message):
  message_content = message.content
  # bad = message_content.find("씨발")
  # if bad >= 0:
  if checkBad(message_content) == True:
    await message.channel.send("언어폭력 멈춰라옹!!!")
    await message.delete()
  await client.process_commands(message)
  
  if message.author.bot:
    return None
  
  if message.content.startswith("!안녕" or "hello"):
    await message.channel.send("반갑다옹")

  if message.content.startswith("!cat"):
    await message.channel.send("애옹")
  
  if message.content.startswith("!종강"):
    thisday=dday()
    if thisday > 0:
      text = "종강까지 디데이 결과 " + str(thisday) + "일 지났다옹"
      await message.channel.send(text)
    if thisday == 0:
      text = "종강까지 디데이 결과 D-DAY 다옹 "
      await message.channel.send(text)
    else:
      text = "종강까지 디데이 결과 D" + str(thisday) + "일 남았다옹"
      await message.channel.send(text)
    
  if message.content.startswith("!sex"):
    await message.author.send("닥쳐라옹 하찮은 닝겐")
  
  if message.content.startswith("!날짜"):
    text = "오늘 날짜는" + str(today()) +"이다옹"
    await message.channel.send(text)
  
  if message.content.startswith("!날씨"):
    html = requests.get('https://search.naver.com/search.naver?query=날씨')
    soup = BeautifulSoup(html.text, 'html.parser')
    data1 = soup.find('div', {'class':'weather_box'})
    pprint(soup)
    find_address = data1.find('span', {'class':'btn_select'}).text
    Area = '현재 위치는 '+find_address+
    find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
    Temp = '현재 온도는 '+find_currenttemp+'도다옹'
    data2 = data1.findAll('dd')
    find_dust = data2[0].find('span', {'class':'num'}).text
    mask = find_dust[0:2]
    text = Area + '이고' + Temp
    if mask<=30:
      await message.channel.send(text)
      await message.channel.send("미세먼지 없이 쾌적하다옹")
    else:
      await message.channel.send(text)
      await message.channel.send("마스크 꼭 껴라옹")
  
  if message.content.startswith("!도움" or "help"):
    embed = discord.Embed(title="떼껄룩 사용법", description="명령어는 아래서 봐라옹 추가기능 필요하면 말해라옹", color=0x62c1cc)
    embed.add_field(name="!도움",value="설명서가 나온다옹",inline=False)
    embed.add_field(name="!안녕",value="인사 해준다옹",inline=False)
    embed.add_field(name="!cat",value="애옹",inline=False)
    embed.add_field(name="!종강",value="용붕쿤 종강날짜다옹",inline=True)
    embed.add_field(name="!날짜",value="오늘 날짜도 알려준다옹",inline=False)
    embed.add_field(name="!sex",value="궁금하면 해보라옹",inline=False)
    await message.channel.send("반갑다옹 설명서좀 읽으라옹", embed=embed)
    

client.run(os.environ['token'])