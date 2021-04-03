import requests
from config import config
riotUrl = "https://kr.api.riotgames.com"

API_KEY = config.token
HEADER = {
  "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
  "X-Riot-Token": config.rtoken,
  "Accept-Language": "ko-KR,ko;q=0.9,en-US;9=0.8,en;q=0.7"
}


def get_SummonerId(summonerName):
  url = f"{riotUrl}/lol/summoner/v4/summoners/by-name/{summonerName}"
  req = requests.get(url=url, headers=HEADER)
  print(req.status_code)
  if req.status_code == 200:
    print(req.json())
  else:
    print(req.status_code)

get_SummonerId("Hide on bush")

def get_RankInfo(summonerID):
  url = f"{riotUrl}/lol/league/v4/entries/by-summoner/{summonerID}"
  req = requests.get(url=url, headers=HEADER)
  if req.status_code == 200:
    leagues = req.json()
    if len(leagues) == 0:
      return None
    for league in leagues:
      if league["queueType"] == "RANKED_SOLO_5x5":
        return league
    return None
  else:
    print(req.status_code)

print(get_RankInfo("BUiq-vfugVTftZKE8BW20T-v2dKpOr0mLuovbZVwaE3xWw"))