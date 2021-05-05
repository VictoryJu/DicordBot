# -*- coding:utf-8 -*-
import discord
import asyncio
from discord.ext import commands
import datetime
#from config import config
import os
import bs4
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, Request
import urllib
import html5lib

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
  enddday = ("2021-06-14")
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
  
  if message.content.startswith("!박승균"):
    await message.channel.send("야근중이다옹")
  
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
  
  if message.content.startswith("!날짜"):
    text = "오늘 날짜는" + str(today()) +"이다옹"
    await message.channel.send(text)
  
  if message.content.startswith("!날씨"):
    location = '서울'
    enc_location = urllib.parse.quote(location + '+날씨')
    url = 'https://search.naver.com/search.naver?ie=utf&query='+enc_location
    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html5lib')
    text = ('현재 ' + location + '날씨는 ' + soup.find('p', class_='info_temperature').find('span',class_='todaytemp').text + '도 다옹')
    await message.channel.send(text)
  
  if message.content.startswith("!경기 날씨"):
    location = '경기도'
    enc_location = urllib.parse.quote(location + '+날씨')
    url = 'https://search.naver.com/search.naver?ie=utf&query='+enc_location
    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html,'html5lib')
    text = ('현재 ' + location + '날씨는 ' + soup.find('p', class_='info_temperature').find('span',class_='todaytemp').text + '도 다옹')
    await message.channel.send(text)
  
  if message.content.startswith("!도움" or "help"):
    embed = discord.Embed(title="떼껄룩 사용법", description="명령어는 아래서 봐라옹 추가기능 필요하면 말해라옹", color=0x62c1cc)
    embed.add_field(name="!도움",value="설명서가 나온다옹",inline=False)
    embed.add_field(name="!안녕",value="인사 해준다옹",inline=False)
    embed.add_field(name="!cat",value="애옹",inline=False)
    embed.add_field(name="!종강",value="용붕쿤 종강날짜다옹",inline=True)
    embed.add_field(name="!날짜",value="오늘 날짜도 알려준다옹",inline=True)
    embed.add_field(name="!날씨",value="오늘 서울 날씨를 알려준다옹",inline=False)
    embed.add_field(name="!경기 날씨",value="오늘 경기도 날씨를 알려준다옹",inline=False)
    await message.channel.send("반갑다옹 설명서좀 읽으라옹", embed=embed)
    

client.run(os.environ['token'])