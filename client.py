import discord
import asyncio
from discord.ext import commands
import datetime
import config

token = config.token
# def dday():
#   today = datetime.date.today() #현재날짜
#   targetday = datetime.date(2021,6,26) #d-day셀 날짜
#   values = targetday - today
#   values.strftime('%d')
#   return values

def dday():
  startdday1 = datetime.date.today()
  startdday = startdday1.strftime('%Y-%m-%d')
  startyy=int(startdday.split('-')[0])
  startmm=int(startdday.split('-')[1])
  startdd=int(startdday.split('-')[2])
  sd = datetime.date(startyy, startmm, startdd) #시작기준일 설정
  enddday = ("2021-06-28")
  endyy = int(enddday.split('-')[0])
  endmm = int(enddday.split('-')[1])
  enddd = int(enddday.split('-')[2])
  ed = datetime.date(endyy, endmm, enddd) #끝 기준일 설정
  result=(sd - ed).days #차를 구하고 일수로 바꿈

  return result

    

app = commands.Bot(command_prefix='!')

@app.event
async def on_ready():
    print('Logged in as')
    print(app.user.name)
    print(app.user.id)
    print('------')
    await app.change_presence(status=discord.Status.online, activity=None)


@app.command()
async def 안녕(ctx):
    await ctx.send('떼-껄룩')

@app.command()
async def cats(ctx):
    await ctx.send('애옹')

@app.command()
async def 종강(ctx):
    thisday=dday()
    if thisday > 0:
      text = "종강까지 디데이 결과 " + str(thisday) + "일 지났다옹"
      await  ctx.send(text)
    if thisday == 0:
      text = "종강까지 디데이 결과 D-DAY 다옹 "
      await ctx.send(text)
    else:
      text = "종강까지 디데이 결과 D" + str(thisday) + "일 남았다옹"
      await ctx.send(text)

@app.command()
async def sex(ctx):
  await ctx.send('헨타이 닥치라옹')

@app.command()
async def help(ctx):
  embed = discord.Embed(title="메인 제목", description="설명", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다 embed.set_footer(text="하단 설명") # 하단에 들어가는 조그마한 설명을 잡아줍니다
  await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다. 
  await message.channel.send("설명서좀 읽으라옹", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.

    # if message.content.startswith('!test'):
    #     await message.channel.send(message.channel, 'test!!!!')

    # elif message.content.startswith('!say'):
    #     await message.channel.send(message.channel, 'leave message')
    #     msg = await app.wait_for_message(timeout=15.0, author=message.author)

    #     if msg is None:
    #         await message.channel.send(message.channel, '15초내로 입력해주세요. 다시시도: !say')
    #         return
    #     else:
    #         await message.channel.send(message.channel, msg.content)

app.run(token)