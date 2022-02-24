from email import message
import keep_alive
from bs4 import BeautifulSoup
import discord
import asyncio
import time
import random
import datetime
import pytz
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord.player import FFmpegPCMAudio
import googletrans
from googletrans import Translator
from googletrans.constants import LANGCODES, LANGUAGES
from googletrans.models import Detected
import sys
from exitstatus import ExitStatus
from discord.channel import VoiceChannel
import time
import html
import urllib.request
from urllib.request import Request, urlopen

chaton = True #setup
adminlist = ['']
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0
t8 = 0
t9 = 0
t10 = 0
t11 = 0
t12 = 0
t13 = 0
t14 = 0
pracinfo = 0
t15 = 0
t16 = 0
user = 0
url = ""
yes = ['yes', 'Yes', 'Y', 'y', '네', 'YES']
no = ['no', 'N', '아니요', '아니오', 'NO', 'n']
history = []
practiced = ['안녕', '디보']
playing = True
blacklist = ['즘', '틱', '늄', '슘', '퓸', '늬', '뺌', '섯', '숍', '튼', '름', '늠', '쁨']
translator = Translator()
sgame = False
pw1 = 0
list_c = ['씨', '시', 'C', 'c', 'ㅆ', 'ㅅ']
list_bal = ['발', 'ㅂ']
path = "cromedriver.exe"
fuck = True
numud = 0
list_fuck = ['ㅗ', '십알', 'ㅈㄹ', 'ㅅㅂ', 'ㅅ1ㅂ', '시1발', 'ㅄ', '지랄', '씨발', '또라이', '적출', '니미', '매도', '병신', '좆', '버러지', '니엄마', '시11발', '주식', '느금마', '새끼', '주식', '애미', '매입', '시발']
song_tkdtn = "https://www.youtube.com/watch?v=wbHweCdCRQE"
prefix = "!" #접두사
ranud = 0
runtime = 0
nums = []
cb = False
wt = False
pw = 0
c = 1
detfuck = False
adminsay = 0
admincheck = 0
admin = ['DIBO | 디보', 'ko_Kr_gg ( | 코르 1세 | )', '유보 (YOU-BO)']
position = "원활"
firstime = time.time()
secondtime = time.time()
wtm = False
admin_1 = 0
blackuserlist = [1]
admin_2 = 0
bankey = True
admin_3 = 0
admin_4 = 0
bothap = 0
hook = 0
money = 10000
baseurl = "https://kr.op.gg/summoner/userName="

client = discord.Client()

with open("token.txt", "r") as file:
    token = file.read()
    print(token)

bot = commands.Bot(command_prefix='!')

voiceChannel: VoiceChannel

if chaton == True:

    @client.event #start
    async def on_ready():
    
        print('Logged in! start DIBO - bot v1 \n welcome!')
        game = discord.Streaming(name="봇", url='https://www.twitch.tv/gguni1118')
        await client.change_presence(status=discord.Status.online, activity=game)
    
    @client.event #command
    async def on_message(message):
        global admincheck
        global firstime
        global secondtime
        global runtime
        global t1
        global t2
        global t3
        global t4
        global t5
        global t6
        global t7
        global pracinfo
        global t8
        global t9
        global t10
        global t11
        global t12
        global t13
        global t14
        global t15
        global t16
        global pw1
        global c
        global bankey
        global cb
        global voiceChannel
        global pw
        global prefix
        global ranud
        global user
        global blackuserlist
        global hook
        global sgame
        global url
        global chaton
        global wt
        global detfuck
        global bothap
        global money
        if message.content == prefix + "봇":
            firstime = time.time()
            await message.channel.send("RUNTIME 측정중...")
            secondtime = time.time()
            runtime1 = secondtime - firstime
            runtime = round(runtime1, 2)
            if runtime < 0.4:
                position = "매우 원활"
            if 0.41 < runtime < 0.5:
                position = "매우 원활"
            if 0.51 < runtime < 0.6:
                position = "원활"
            if 0.61 < runtime < 0.65:
                position = "원활"
            if 0.66 < runtime < 0.69:
                position = "양호"
            if 0.7 < runtime:
                position = "혼잡"
            embed = discord.Embed(title="[ 봇 ]", description="DI-BOT", color=0x00ff00)
            embed.add_field(name="[ 봇 ]", value=f"현재 봇의 상태는 {position} 합니다!", inline=False)
            embed.add_field(name="[ RUNTIME ]", value=f"{runtime} ms", inline=False)
            embed.add_field(name="[ ✏️ 소개 ]", value=f"봇 이름 - 디보(DIBO) | DI-BO", inline=False)
            embed.add_field(name="[ 채팅 로그 ]", value="채팅 로그는 서버 파일에 1주일동안 기록된 후 지워집니다 ( 채팅 로그는 개인의 목적으로 열람하지 않습니다 )", inline=False)
            embed.add_field(name="[ 제작자 유튜브 ]", value="[제작자 유튜브 링크](<https://www.youtube.com/channel/UCLxuaPUJvnFHvuChjQquJUA>)", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
        
        if message.content.startswith (prefix + "user "):
            user = message.content.replace(prefix + "user ", "")
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            pfp = user.avatar_url
            id = user.id
            embed = discord.Embed(title=f"{user.display_name} 님의 유저 정보", description="INFORMATION", color=0x00ff00)
            embed.add_field(name="유저 태그", value=f"{user}", inline=False)
            embed.add_field(name="유저 이름", value=f"{user.name}", inline=False)
            embed.add_field(name="유저 가입일", value=f"{date.year}년 {date.month}월 {date.day}일", inline=False)
            embed.add_field(name="유저 아이디", value=f"{user.id}", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            embed.set_thumbnail(url=pfp)
            await message.channel.send(embed=embed)
        
        if message.content.startswith (prefix + "경고 "):
            if message.author.guild_permissions.administrator:
                name = message.content.replace(prefix + "경고 ", "")
                blackuserlist.append(name)
                await message.channel.send("해당 유저에게 채팅 금지 명령어를 실행하였습니다 해제를 원하시면 \"!해제 <유저 이름>\" 을 사용하여 주세요")
            else:
                await message.channel.send("PERMISSIONS ERROR - 권한 부족")


        if message.content != "fffooowpwppepoirweoriwpeoi":
            id = message.author.name
            if id in blackuserlist:
                await message.delete()

        if message.content.startswith (prefix + "해제 "):
            if message.author.guild_permissions.administrator:
                name = message.content.replace(prefix + "해제 ", "")
                blackuserlist.remove(name)
            else:
                await message.channel.send("PERMISSIONS ERROR - 권한 부족")
        
        if message.content == prefix + "개발자":
            embed = discord.Embed(title="[ 개발자 ]", description="Bot_Developer#4371", color=0x00ff00)
            embed.add_field(name="[ 개발 현황 ]", value="현재 날씨 정보 기능 제작 중", inline=False)
            embed.add_field(name="[ 채팅 로그 사용 목적 ]", value=f"사용자 분들의 안전을 위하여 채팅 로그 기록, 개인적인 목적으로 열람하지 않습니다", inline=False)
            embed.add_field(name="[ 채팅 로그 ]", value="채팅 로그는 서버 파일에 1주일동안 기록된 후 지워집니다", inline=False)
            embed.add_field(name="[ 제작자 유튜브 ]", value="[제작자 유튜브 링크](<https://www.youtube.com/channel/UCLxuaPUJvnFHvuChjQquJUA>)", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
        
        if message.content.startswith (prefix + "임베드 "):
            embed = discord.Embed(title="[ 임베드 ]", description="EMBED", color=0x00ff00)
            t1 = message.content.replace(prefix + "임베드 ", "").split('/')[0]
            t2 = message.content.replace(prefix + "임베드 ", "").split('/')[1]
            embed.add_field(name=f"{t1}", inline=False)
            embed.set_thumbnail(url=t2)
            await message.channel.send(embed=embed)

        if message.content.startswith (prefix + "날씨 "):
            setplace1 = message.content.replace(prefix + "날씨 ", "")
            setplace = setplace1.replace(" ", "+")
            setweather = (str(setplace) + "+날씨").encode('utf8')
            a = b'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + setweather
            firstime = time.time()
            await message.channel.send("날씨 정보를 수집하는중...")
            a = urllib.request.urlopen(a.decode('ASCII')).read()
            webpage = urllib.request.urlopen(a)
            soup = BeautifulSoup(webpage, 'html.parser')
            cph = "https://ifh.cc/g/LHu1Cb.jpg"
            titles = soup.find_all("span")
            secondtime = time.time()
            for title in titles:
                dayconfirm = (title.next_sibling.strip())
            runtime1 = secondtime - firstime
            runtime = round(runtime1, 2)
            embed = discord.Embed(title="[ 날씨 ]", description="WEATHER", color=0x00ff00)
            embed.add_field(name=f"오늘 {setplace} 날씨", value=str(dayconfirm.get_text()) + "°C", inline=False)
            embed.add_field(name="[ RUNTIME ]", value=f"{runtime} ms", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            embed.set_thumbnail(url=cph)
            await message.channel.send(embed=embed)
        
        if message.content != "oiasjdoiajsodijasodijas":
            message_c = message.content
            for i in list_fuck:
                if i in message_c:
                    if bankey == True:
                        id = message.author.id
                        if id != 931744333990858773:

                            await message.delete()
                            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                            await message.channel.send(embed=embed)
                        else:
                            print("BOT CAN'T DELETE HIS MESSAGE !")
                    else:
                        print("BANKEY IS FALSE NOW !")
        
        if message.content != "dpaisjdpasdpaisjdiaosjdpasdpasj":

            message_f = message.content
            for i in list_c:
                if i in message_f:
                    for b in list_bal:
                        if b in message_f:
                            if bankey == True:
                                name = message.author.name
                                if name in admin:
                                    print("BOT CAN'T DELETE HIS MESSAGE !")
                                else:
                                    await message.delete()
                                    embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                                    await message.channel.send(embed=embed)
                            else:
                                print(f"[ BOT ] BANKEY IS FALSE NOW ! ( {message_f} )")
        
        if message.content != "spdifsdofisdpo":
            user = message.author
            guild = message.guild.name
            log = str("[ SERVER : " + guild + " ] [ Name : " + str(user.name) + "( " + str(user.id) + " ) ] : " + message.content)
            print("[ SERVER : " + guild + " ] [ Name : " + str(user.name) + "( " + str(user.id) + " ) ] : " + message.content)
            with open("chatlog.txt", 'a', encoding='utf-8') as chattinglog:
                chattinglog.write(f"{log}\n")

        if message.content.startswith (prefix + "ev "):
            name = message.author.name
            if name in admin:
                try:
                    command = message.content.replace(prefix + "ev ", "")
                    com = eval(command)
                    await message.channel.send("명령어 수행을 완료 하였습니다!\n실행 결과 : " + str(com))
                except (ValueError, RuntimeError, TypeError, NameError, SyntaxError) as error:
                    await message.channel.send(f"에러가 발생했습니다! \n{error}")
        
        if message.content.startswith(prefix + "롤 "):
            message_content = message.content.replace(prefix + "롤 ", "")
            plusurl = message_content.replace(" ", "")
            url = baseurl + plusurl
            webpage = urllib.request.urlopen(url)
            soup = BeautifulSoup(webpage, "html.parser")

            img = soup.find("div", attrs={"class":"SummonerRatingMedium"}).find("img").get('src')

            tiername = soup.find("div", attrs={"class":"TierRank"}).get_text()
            tieraka = soup.find("div", attrs={"class":"LeagueName"}).get_text().strip()

            userlp = soup.find("span", attrs={"class":"LeaguePoints"}).get_text().strip()

            win = soup.find("span", attrs={"class":"wins"}).get_text().replace("W", "승")
            lose = soup.find("span", attrs={"class":"losses"}).get_text().replace("L", "패")
            odds = soup.find("span", attrs={"class":"winratio"}).get_text()

            mostchamp = soup.find_all("div", attrs={"class":"ChampionBox Ranked"}, limit=3)
            mostchamp_list = []
            for most in mostchamp:
                mostchamp_list.append(most.find('div').get('title'))

            embed = discord.Embed(title=message_content + " 님의 플레이어 정보", description="", color=0x62c1cc)
            embed.set_thumbnail(url="http:" + img)

            embed.add_field(name="티어 정보", value="`" + userlp + " | " + tiername + " | " + tieraka + "`", inline=False)
            embed.add_field(name="모스트 챔피언", value="`" + mostchamp_list[0] + ", " + mostchamp_list[1] + ", " + mostchamp_list[2] + "`", inline=False)
            embed.add_field(name="승, 패, 승률", value="`" + win + " " + lose + " | " + odds + "`", inline=False)

            embed.set_footer(text="솔로랭크 기준 티어입니다. | 랭크 정보가 없을 시 출력되지 않습니다.")
            await message.channel.send(embed=embed)

        if message.content.startswith (prefix + "코로나"):
            firstime = time.time()
            await message.channel.send("코로나 정보를 수집 하는 중...")
            webpage = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98')
            soup = BeautifulSoup(webpage, 'html.parser')
            cph = "https://ifh.cc/g/LHu1Cb.jpg"
            dayconfirm = soup.find('p',"info_num")
            secondtime = time.time()
            runtime1 = secondtime - firstime
            runtime = round(runtime1, 2)
            embed = discord.Embed(title="[⚔ 코로나 현황 ⚔]", description="COVID-19", color=0x00ff00)
            embed.add_field(name="일일 확진", value="`" + str(dayconfirm.get_text()) + "명" + "`", inline=False)
            embed.add_field(name="[ RUNTIME ]", value=f"`{runtime} ms`", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            embed.set_thumbnail(url=cph)
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "날씨"):
            setplace = message.content[4:]
            weatherurl = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=" + setplace +"+날씨"
            soup = BeautifulSoup(weatherurl, 'html.parser')
            placeweather = soup.find('span', "blind")
            embed = discord.Embed(title="[ WEATHER ]", description="INFO", color=0x00ff00)
            embed.add_field(name="현재 " + setplace + " 날씨", value=str(placeweather.get_text()) + "°C", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
        
        if message.content.startswith (prefix + "날씨"):
            weatherurl = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=시흥+날씨"
            soup = BeautifulSoup(weatherurl, 'html.parser')
            placeweather = soup.find('strong')
            embed = discord.Embed(title="[ WEATHER ]", description="INFO", color=0x00ff00)
            embed.add_field(name="현재 " + setplace + " 날씨", value=str(placeweather.get_text()) + "°C", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "코인"):
            webpage = urllib.request.urlopen('https://www.google.com/search?q=%EB%8F%84%EC%A7%80%EC%BD%94%EC%9D%B8&ei=gB_xYZGoNtLf2roPvuCiuA4&ved=0ahUKEwiR6NH3l8_1AhXSr1YBHT6wCOcQ4dUDCA4&uact=5&oq=%EB%8F%84%EC%A7%80%EC%BD%94%EC%9D%B8&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHkoECEEYAEoECEYYAFAAWM8EYL8FaAFwAngBgAGDAYgB9QKSAQMwLjOYAQCgAQHAAQE&sclient=gws-wiz')
            soup = BeautifulSoup(webpage, 'html.parser')
            dogecoin = soup.find('span', "pclqee")
            dogecoinup = soup.find('span', "D3VPPe")
            embed = discord.Embed(title="[ DOGECOIN ]", description="DOGE", color=0x00ff00)
            embed.add_field(name="현재 도지코인 가격", value=str(dogecoin.get_text()) + "KRW", inline=False)
            embed.add_field(name="DGC", value=str(dogecoinup.get_text()), inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "로또"):
            lotto1 = random.randint(1,45)
            lotto2 = random.randint(1,45)
            lotto3 = random.randint(1,45)
            lotto4 = random.randint(1,45)
            lotto5 = random.randint(1,45)
            lotto6 = random.randint(1,45)
            if lotto1 == lotto2:
                lotto2 = random.randint(1,45)
            if lotto1 == lotto3:
                lotto3 = random.randint(1,45)
            if lotto1 == lotto4:
                lotto4 = random.randint(1,45)
            if lotto1 == lotto5:
                lotto5 = random.randint(1,45)
            if lotto1 == lotto6:
                lotto6 = random.randint(1,45)
            if lotto2 == lotto3:
                lotto3 = random.randint(1,45)
            if lotto2 == lotto4:
                lotto4 = random.randint(1,45)
            if lotto2 == lotto5:
                lotto5 = random.randint(1,45)
            if lotto2 == lotto6:
                lotto6 = random.randint(1,45)
            if lotto3 == lotto4:
                lotto4 = random.randint(1,45)
            if lotto3 == lotto5:
                lotto5 = random.randint(1,45)
            if lotto3 == lotto6:
                lotto6 = random.randint(1,45)
            if lotto4 == lotto5:
                lotto5 = random.randint(1,45)
            if lotto4 == lotto6:
                lotto6 = random.randint(1,45)
            if lotto5 == lotto6:
                lotto6 = random.randint(1,45)
            embed = discord.Embed(title="[ LOTTO ]", description="LOTTO", color=0x00ff00)
            embed.add_field(name="첫번째", value="`" + str(lotto1) + "`", inline=True)
            embed.add_field(name="두번째", value="`" + str(lotto2) + "`", inline=False)
            embed.add_field(name="세번째", value="`" + str(lotto3) + "`", inline=True)
            embed.add_field(name="네번째", value="`" + str(lotto4) + "`", inline=False)
            embed.add_field(name="다섯번째", value="`" + str(lotto5) + "`", inline=True)
            embed.add_field(name="여섯번째", value="`" + str(lotto6) + "`", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
        
        
        
        if message.content == prefix + "욕감지":
            if bankey == False:
                bankey = True
                await message.channel.send("[ ! ] 욕 감지가 활성화 되었습니다")
            elif bankey == True:
                bankey = False
                await message.channel.send("[ ! ] 욕 감지가 비활성화 되었습니다")
            
        if message.content.startswith (prefix + "롣도"):
            webpage = urllib.request.urlopen('https://dhlottery.co.kr/gameResult.do?method=byWin')
            soup = BeautifulSoup(webpage, 'html.parser')
            befor = soup.find_all('span', "ball_645 lrg ball1")
            for befor in soup.find_all('span', "ball_645 lrg ball1"):
                before = befor.get_text()
            for befor1 in soup.find_all('span', "ball_645 lrg ball2"):
                before1 = befor1.get_text()
            before2 = soup.find('span', "ball_645 lrg ball3")
            round1 = soup.find("strong")
            embed = discord.Embed(title="[" + str(round1) + " 회차" + "]", description="LOTTO", color=0x00ff00)
            embed.add_field(name="로또", value=str(before) + str(before1) + str(before2.get_text()), inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "s"):
            embed = discord.Embed(title="[ GAME ]", description="GAME-01", color=0x00ff00)
            embed.add_field(name="START", value="게임을 시작합니다\n!g n/n으로 진행하세요", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            time.sleep(1)
            await message.channel.send("🔠1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣\n🇦🟨🟨🟨🟨🟨🟨🟨\n🇧🟨🟨🟨🟨🟨🟨🟨\n🇨🟨🟨🟨🟨🟨🟨🟨\n🇩🟨🟨🟨🟨🟨🟨🟨\n🇪🟨🟨🟨🟨🟨🟨🟨\n🇫🟨🟨🟨🟨🟨🟨🟨")
            sgame = True
            
        if message.content.startswith (prefix + "g"):
            if sgame == True:
                play1 = message.content[3:3]
                play2 = message.content[5:5]
                if play1 == "a":
                    if play2 == 1:
                        await message.channel.send("🔠1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣\n🇦🟥🟨🟨🟨🟨🟨🟨\n🇧🟨🟨🟨🟨🟨🟨🟨\n🇨🟨🟨🟨🟨🟨🟨🟨\n🇩🟨🟨🟨🟨🟨🟨🟨\n🇪🟨🟨🟨🟨🟨🟨🟨\n🇫🟨🟨🟨🟨🟨🟨🟨")
            
        if message.content == prefix + "업초":
            s = 0
            m = 0
            h = 0
                
        if message.content.startswith == prefix + "중지":
            wt = False
            
        if message.content.startswith == prefix + "밴키":
            if detfuck != False:
                detfuck = False
                await message.channel.send("[!] 욕 감지를 종료합니다")
            elif detfuck == False:
                detfuck = True
                await message.channel.send("[!] 욕 감지를 시작합니다")
            
        if message.content == prefix + "챗온":
            if chaton == True:
                chatone = False
                                    
        if message.content == prefix + "도배":
            await message.channel.send("시룬뎁 :(")
            
        if message.content.startswith (prefix + "아이디"):
            id = message.author.id
            embed = discord.Embed(title="[!] 아이디", description="<@"+str(id)+"> 당신의 아이디가 맞는지 멘션으로 확인하세요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(id)
            await message.channel.send(embed=embed)
        
        if message.content.startswith (prefix + "멘션 "):
            id = message.content.replace(prefix + "멘션 ", "")
            await message.channel.send("<@"+str(id)+"> 님을 멘션했습니다")
            
        if message.content.startswith ("Dev"):
            id = message.author.id
            if id == 931741804544532510:
                await message.channel.send("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B4%80%EB%A6%AC%EC%9E%90")

                        
        if message.content == prefix + "노래 명사수":
            await message.channel.send(song_tkdtn)
            
        if message.content == "d":
            print("d")
            
        if message.content.startswith (prefix + "청소"):
            i = (message.author.guild_permissions.administrator)

            if i is True:
                amount = message.content[4:]
                await message.channel.purge(limit=2)
                await message.channel.purge(limit=int(amount))

                embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
        
            if i is False:
                await message.channel.purge(limit=1)
                await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))
                
        if message.content == "-업다운":
            ranud = random.randint(1, 10)
            embed = discord.Embed(title="업다운", description="-업다운 n으로 게임을 진행하세요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            await message.channel.send (embed=embed)
            if message.content.startswith ("-업다운 "):
                updown = message.content[6:]
                await message.channel.send(limit=1)
                await message.channel.send(limit=int(updown))
                if updown < ranud:
                    await message.channel.send("up")
                elif updown > ranud:
                    await message.channel.send("up")
                elif updown == ranud:
                    embed = discord.Embed(title="업다운", description="정답입니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    await message.channel.send(embed=embed)
        
        if message.content == prefix + "뽑기":
            a = random.randint(0, 100)
            a += 1
            if a == 1:
                b = "당첨"
                embed = discord.Embed(title="뽑기 도박", description="당첨입니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            else:
                b = "꽝"
                embed = discord.Embed(title="뽑기 도박", description="꽝.. 다시 시도해봐요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
                
        if message.content.startswith (prefix + "인증 "):
            if message.author.guild_permissions.administrator:
                await message.delete()
                user = message.mentions[0]

                embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
                embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
                embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
                embed.set_footer(text="Bot Made by. Bot_Developer#4371")
                await message.author.send (embed=embed)
                role = discord.utils.get(message.guild.roles, name = '[멤버]')
                await user.add_roles(role)

            else:
                await message.delete()
                await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))
            
        if message.content == prefix + "off":
            await message.channel.send("OFF")
            chaton = False
            
        if message.content == prefix + "명령어":
            await message.channel.send("🛠️ 현재 명령어 종류입니다!\n\n" + f"{prefix}명령어\n" + "명령어 목록을 가져옵니다\n\n" + f"{prefix}봇\n" + "봇 작동 여부를 확인합니다\n\n" + f"{prefix}뽑기\n" + "1%확률의 뽑기를 합니다\n\n" + f"{prefix}검색\n" + f"구글, 유튜브, 네이버 에서 검색한 결과를 알려줍니다 (ex. {prefix}검색 디스코드)\n\n" + f"{prefix}정보\n" + "자신의 가입일, 아이디, 유저 태그, 유저 가입일, 유저 이름 을 알려줍니다\n\n" + f"{prefix}코로나\n" + "코로나 정보를 수집하여 알려줍니다\n\n" + f"{prefix}디코\n" + f"디스코드에서 서버를 검색해 줍니다 (ex. {prefix}디코 마인크래프트)\n\n" + f"{prefix}따라해\n" + f"봇이 따라합니다 (ex. {prefix}따라해 안녕!)\n\n" + f"{prefix}임베드\n" + f"임베드를 보내준다 (ex. {prefix}임베드 안녕!)\n\n" + f"{prefix}ev\n" + f"명령어를 실행합니다 (ex. {prefix}ev 1 + 1)\n\n" + f"{prefix}로또\n" + "로또 추천번호를 랜덤으로 생성하여 알려줍니다\n\n" + f"{prefix}청소\n" + f"메시지를 삭제합니다 (ex. {prefix}청소 5)\n\n" + f"{prefix}시작\n" + "업다운 게임을 시작합니다\n\n" + f"{prefix}업다운\n" + f"업다운 게임을 합니다 (ex. {prefix}업다운 500)\n\n" + f"{prefix}뽑기\n" + "당첨확률이 1%인 뽑기를 진행합니다\n\n" + "ㄷㅂㄱ\n" + "돈을 벌어줍니다 - 도박은 협동게임입니다\n\n" + "ㄷㅂ\n" + "도박을 합니다 (ex. ㄷㅂ 1000 <- 배팅금)\n\n" + "올인\n" + "도박에 올인합니다\n\n" + f"{prefix}어드민리스트\n" + "현재 어드민인 사람을 확인한다\n\n" + f"{prefix}번역\n" + f"번역을 해줍니다 | 한국어 -> 영어 (ex. {prefix}번역 안녕!)\n\n" + f"{prefix}trans\n" + f"번역을 해줍니다 | 영어 -> 한국어 (ex. {prefix}trans hi!)\n\n" + f"{prefix}dm\n" + "봇이 dm(개인 메시지) 을 보냅니다\n\n" + "__이외의 기능들은 이스터 에그들이니 직접 찾아 보길 바랍니다__")
        
        if message.content.startswith (prefix + "접두사 "):
            id = message.author.id
            if id in admin:

                prefix = message.content.replace(prefix + "접두사 ", "")
                await message.channel.send(f"CHANGED BOT'S PREFIX TO {prefix} !")
                print(f"{prefix} IS PREFIX NOW !")
            else:
                await message.channel.send("[ PERMISSIONS ERROR ] YOU DON'T HAVE ANY PERMISSIONS !")
            
        if message.content.startswith (prefix + "유튜브 "):
            pfp = "https://ifh.cc/g/CKqNtq.png"
            youtube = message.content.replace(prefix + "유튜브 ", "")
            song = youtube.replace(" ", "+")
            #"[여기](<https://www.google.com/search?q=" + googlereplace + ">)" + "를 클릭해 검색 결과로 이동하세요"
            #"https://www.youtube.com/results?search_query=" + song
            embed = discord.Embed(title="[ 유튜브 ]", description="[여기](<https://www.youtube.com/results?search_query=" + song + ">)" + "를 클릭해 검색 결과로 이동하세요",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_thumbnail(url=pfp)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "네이버"):
            naver = message.content[5:]
            pfp = "https://ifh.cc/g/KKz4d9.png"
            navereplace = naver.replace(" ","+")
            embed = discord.Embed(title="[ 네이버 ]", description="[여기](<https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=" + navereplace + ">)" + "를 클릭해 검색 결과로 이동하세요",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            #"[여기](<https://www.google.com/search?q=" + googlereplace + ">)" + "를 클릭해 검색 결과로 이동하세요"
            embed.set_thumbnail(url=pfp)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content == "ㄷㅂㄱ":
            gambling = random.randint(1, 2000)
            money = int(money) + int(gambling)
            embed = discord.Embed(title="[ 돈 벌기 ]", description="카지노",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            time.sleep(3)
            
        if message.content == "올인":
            gambling = random.randint(1, 5)
            if gambling == 1:
                money = int(money) * 100
                embed = discord.Embed(title="[ 도박 ]", description="성공",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
                embed.add_field(name="[ 배 ]", value = "100배", inline = True)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            else:
                money = 0
                embed = discord.Embed(title="[ 도박 ]", description="실패",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            if money == 0:
                embed = discord.Embed(title="[ 도박 ]", description="돈 부족",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            
        if message.content.startswith ("ㄷㅂ "):
            setmoney = message.content[3:]
            if int(setmoney) > int(money):
                await message.channel.send("[ ErRor - 1293 ] 돈 부족")
            if int(setmoney) < int(money):
                
                money = int(money) - int(setmoney)
                gambling = random.randint(1,20)
                if gambling < 10:
                    money = int(money) + int(setmoney) * int(gambling)
                    embed = discord.Embed(title="[ 도박 ]", description="성공",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
                    embed.add_field(name="[ 배 ]", value = str(gambling) + "배", inline = True)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(title="[ 도박 ]", description="실패",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                    
            
        if message.content.startswith (prefix + "구글"):
            google = message.content[4:]
            pfp = "https://ifh.cc/g/cX4RyA.png"
            googlereplace = google.replace(" ","+")
            embed = discord.Embed(title="[ 구글 ]", description="[여기](<https://www.google.com/search?q=" + googlereplace + ">)" + "를 클릭해 검색 결과로 이동하세요",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_thumbnail(url=pfp)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
        
        if message.content == prefix + "방송":
            game = discord.Streaming(name="봇", url='https://www.twitch.tv/gguni1118')
            await client.change_presence(status=discord.Status.online, activity=game)
            
        if message.content == prefix + "어드민리스트":
            await message.channel.send(admin)
        
        if message.content.endswith (" 하는중"):
            play1 = message.content.replace(" 하는중", "")
            play = play1.replace("!", "")
            game = discord.Game(play)
            await client.change_presence(status=discord.Status.online, activity=game)
        
        if message.content == prefix + "인증":
            await message.channel.send("은 시러ㅋ")
            
        if message.content == prefix + "권한":
            id = message.author.id
            user = message.author
            fp = random.randint(1, 9)
            sp = random.randint(1, 9)
            tp = random.randint(1, 9)
            pw = str(fp) + str(sp) + str(tp)
            print("VERIFICATION CODE: " + str(pw))
        
        user = message.author
        if message.content == pw:
            if pw != 0:
                admin.append(user.name)
                await message.channel.send(f'{user.name} 님이 새로운 관리자가 되셨습니다!')
                print(f"NEW ADMIN VERIFICATION: {user.name} ( {user.id} )")
                with open("adminlist.txt", 'a', encoding='utf-8') as adminlog:
                    adminlog.write(f"{user.name}\n")

            
        if message.content == prefix + "종료":
            pw1 = random.randint(1, 1000)
            print(f'EXIT VERIFICATION CODE: {pw1}')
            firstime = time.time()
        
        secondtime = time.time()
        runtime = secondtime - firstime
        if runtime == 10:
            print("10초동안 종료 코드를 입력하지 않아 자동으로 종료 코드가 초기화 되었습니다")
            pw1 = 0
            runtime = 0
        
        if message.content == pw1:
            if pw1 != 0:
                embed = discord.Embed(title="[ 봇 ]", description="종료합니다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
                print(message.author.mention + "process excited by")
                sys.exit(ExitStatus.success)
            
            
        if message.content.startswith (prefix + "tts"):
            tts = message.content.replace(prefix + "tts ", "")
            tts1 = "{}".format(tts)
            url1 = "http://tts-translate.kakao.com/newtone?message=" + tts1
            with urlopen(url) as res:
                res_data = res.read()

                with open('tts.mp3', 'wb') as f:
                    f.write(res_data)
            
        if message.content == prefix + "욕":
            await message.channel.send("귀여운 DISCORD_BOT_001은 욕을 몰라서 못해요 ><")
        

        
        if message.content.startswith ("?"):
            hook += 1
            embed = discord.Embed(title="[ 갈고리 수집 ]", description=str("갈고리수집 : ") + str(hook),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content == "고?속":
            hook += 500
            embed = discord.Embed(title="[ 갈고리 수집 ]", description=str("갈고리수집 : `") + str(hook) + "`",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "멘도"):
            user = message.content[4:]
            wtm = True
            while wtm:
                i = 0
                await message.channel.send("[", i, "]",  "<@"+str(user)+">")
                i = i + 1
                
        if message.content == prefix + "중지":
            wtm = False
            
        if message.content.startswith ("<@!"):
            id = message.author.id
            newid = message.content.replace("<@!", "")
            newid1 = newid.replace(">", "")
            embed = discord.Embed(title="[ 멘션 ]", description="<@"+str(id)+"> 님이 " + "<@"+str(newid1)+"> 님을 호출하였습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "따라해"):
            reply = message.content[5:]
            if reply.startswith("ㅗ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("십알"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("ㅈㄹ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("ㅅㅂ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("ㅅ1ㅂ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("ㅂㅅ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("ㅄ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("지랄"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("씨발"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("또라이"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("적출"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("니미"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("매도"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("병신"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("좆"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("버러지"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("느금마"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("니애미"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("니엄마"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("시11발"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("주식"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("개"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("새끼"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("주식"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("애미"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("매입"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("시발"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="[ 따라하기 ]", description=reply,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
                
        if message.content.startswith (prefix + "임베드"):
            emti = message.content[5:]
            embed = discord.Embed(title="[ 임베드 ]", description=emti,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "디코 "):
            searchroom = message.content.replace(prefix + "디코 ", "")
            embed = discord.Embed(title="[ 디스코드 ]", description="[여기](<https://discord.com/guild-discovery?query=" + searchroom + "&offset=0&limit=12&preferredLocale=ko&categoryId=-1&tag=" + ">)" + "를 클릭해 검색 결과로 이동하세요",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "IP"):
            await message.channel.send("https://iplogger.org/2LHYf7")


        if message.content.startswith (prefix + "검색 "):
            google = message.content.replace(prefix + "검색 ", "")
            naver = message.content.replace(prefix + "검색 ", "")
            youtube = message.content.replace(prefix + "검색 ", "")
            googlereplace = google.replace(" ","+")
            navereplace = naver.replace(" ","+")
            youtubereplace = youtube.replace(" ","+")
            pfp = "https://ifh.cc/g/Ans1xV.png"
            embed = discord.Embed(title="[ 검색 ]", description=f"{google}의 검색 결과입니다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="[ 구글 검색 결과 ]    ", value="[여기](<https://www.google.com/search?q=" + googlereplace + ">)" + "를 클릭해 검색 결과로 이동하세요", inline=False)
            embed.add_field(name="[ 네이버 검색 결과 ]", value="[여기](<https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=" + navereplace + ">)" + "를 클릭해 검색 결과로 이동하세요", inline=False)
            embed.add_field(name="[ 유튜브 검색 결과 ]", value="[여기](<https://www.youtube.com/results?search_query=" + youtubereplace + ">)" + "를 클릭해 검색 결과로 이동하세요", inline=False)
            embed.set_thumbnail(url=pfp)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)



























                
                
        if message.content == prefix:
            wt = False
            wtf = []
            
        if message.content.startswith (prefix + "번역"):
            langs = message.content[4:]
            langs = translator.translate(langs, src='ko', dest='en')
            embed = discord.Embed(title="[ Translator ]", description="[ Translator ] " + langs.text,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "trans"):
            langs = message.content[4:]
            langs = translator.translate(langs, src='en', dest='ko')
            embed = discord.Embed(title="[ Translator ]", description="[ Translator ]" + langs.text,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content == prefix + "시작":
            ranud = random.randint(1, 1000)
            embed = discord.Embed(title="업다운", description="[ GAME ] 업다운 게임이 시작되었어요\n1~1000까지의 숫자 중 골라주세요",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content == prefix + "포기":
            ranud = 0
            udis = 0
            embed = discord.Embed(title="업다운", description="게임을 포기하셨습니다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            time.sleep(1)  

        if message.content == prefix + "정보":
            user = message.author
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            pfp = user.avatar_url
            id = message.author.id
            embed = discord.Embed(title=f"{user.display_name} 님의 유저 정보", description="INFORMATION", color=0x00ff00)
            embed.add_field(name="유저 태그", value=f"{user}", inline=False)
            embed.add_field(name="유저 이름", value=f"{user.name}", inline=False)
            embed.add_field(name="유저 가입일", value=f"{date.year}년 {date.month}월 {date.day}일", inline=False)
            embed.add_field(name="유저 아이디", value=f"{user.id}", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            embed.set_thumbnail(url=pfp)
            await message.channel.send(embed=embed)
        
        if message.content.startswith (prefix + "프사"):
            user = message.author
            pfp = user.avatar_url
            print(pfp)
            await message.channel.send(pfp)
            embed = discord.Embed(title=f"{user}님의 프로필 사진", description="INFORMATION", color=0x00ff00)
            embed.set_thumbnail(url=pfp)
            time.sleep(1)
            await message.channel.send(embed=embed)

        if message.content.startswith ("몰?루"):
            pfp = "https://ifh.cc/g/fe7w3r.jpg"
            embed = discord.Embed(title="몰루티콘", description="몰?루", color=0x00ff00)
            embed.set_thumbnail(url=pfp)
            await message.delete()
            await message.channel.send(embed=embed)
            
        if message.content == prefix + "업타임":
            embed = discord.Embed(title="봇의 업타임 정보", description="INFORMATION", color=0x00ff00)
            embed.add_field(name="시간", value=h, inline=False)
            embed.add_field(name="분", value=m, inline=False)
            embed.add_field(name="초", value=s, inline=False)
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "Ek "):
            Ek = message.content[4:]
            await message.channel.send(Ek)

        if message.content.startswith (prefix + "dm "):
            dmm = message.content[4:]
            dm = await message.author.create_dm()
            await dm.send("Bot이 보낸 메시지 : " + dmm)

        if message.content.startswith (prefix + "갠챗 "):
            dmm = message.content[4:]
            dm = await dmm.create_dm()
            sendm = input(dmm + " 님께 보낼 메시지를 입력해 주세요 - ")
            await dm.send("Bot이 보낸 메시지 : " + sendm)
            
        if message.content.startswith (prefix + "업다운 "):
            if ranud == 0:
                embed = discord.Embed(title="업다운", description="게임을 먼저 시작해주세요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif ranud != 0:
                udis = int(message.content[5:])
                if udis < ranud:
                    embed = discord.Embed(title="업다운", description="[ UP ] 정답이 아니에요",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                    udis = 0
                elif udis > ranud:
                    embed = discord.Embed(title="업다운", description="[ DOWN ] 정답이 아니에요",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                    udis = 0
                elif udis == ranud:
                    embed = discord.Embed(title="업다운", description="[ CORRECT ] " + message.author.mention + " 정답이에요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                    udis = 0
                    ranud = 0
                else:
                    embed = discord.Embed(title="업다운", description="[ ERROR ] ErRor_CoDE_1329",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                    
        if message.content.startswith (prefix + '홀짝 '):
            evod = message.content[4:5]
            paymo = int(message.content[6:])
            money = money - paymo
            even = random.randint(1, 2)
            if even == 1:
                evodmo = "홀"
            if even == 2:
                evodmo = "짝"
            if evod == evodmo:
                money += paymo * 2
                embed = discord.Embed(title="홀짝도박", description="[ 성공 ] 홀짝도박에 성공하였습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="남은 돈", value=f"{money}", inline=False)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif evod != evodmo:
                embed = discord.Embed(title="홀짝도박", description="[ 실패 ] 홀짝도박에 실패하였습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="남은 돈", value=f"{money}", inline=False)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
        
        if message.content.startswith (prefix + "학습 "):
            if t1 == 0:
                t1 = message.content.replace(prefix + "학습 ", "").split('/')[0]
                t2 = message.content.replace(prefix + "학습 ", "").split('/')[1]
                pracinfo += 1
                await message.channel.send(f"학습이 완료되었습니다 ( {pracinfo} / 8 )")



            elif t3 == 0:
                t3 = message.content.replace(prefix + "학습 ", "").split('/')[0]
                t4 = message.content.replace(prefix + "학습 ", "").split('/')[1]
                pracinfo += 1
                if t3 != t1:
                    
                    await message.channel.send(f"학습이 완료되었습니다 ( {pracinfo} / 8 )")
                elif t3 == t1:
                    pracinfo -= 1
                    t3 = 0
                    t4 = 0
                    await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")



            elif t5 == 0:
                t5 = message.content.replace(prefix + "학습 ", "").split('/')[0]
                t6 = message.content.replace(prefix + "학습 ", "").split('/')[1]
                pracinfo += 1
                if t5 != t3:
                    if t5 != t1:
                        await message.channel.send(f"학습이 완료되었습니다 ( {pracinfo} / 8 )")
                    elif t5 == t1:
                        pracinfo -= 1
                        t5 = 0
                        t6 = 0
                        await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                elif t5 == t3:
                    pracinfo -= 1
                    t5 = 0
                    t6 = 0
                    await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")



            elif t7 == 0:
                t7 = message.content.replace(prefix + "학습 ", "").split('/')[0]
                t8 = message.content.replace(prefix + "학습 ", "").split('/')[1]
                pracinfo += 1
                if t7 != t5:
                    if t7 != t3:
                        if t7 != t1:
                            await message.channel.send(f"학습이 완료되었습니다 ( {pracinfo} / 8 )")
                        elif t7 == t1:
                            pracinfo -= 1
                            t7 = 0
                            t8 = 0
                            await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                    elif t7 == t3:
                        pracinfo -= 1
                        t7 = 0
                        t8 = 0
                        await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                elif t7 == t5:
                    pracinfo -= 1
                    t7 = 0
                    t8 = 0
                    await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")



            elif t9 == 0:
                t9 = message.content.replace(prefix + "학습 ", "").split('/')[0]
                t10 = message.content.replace(prefix + "학습 ", "").split('/')[1]
                pracinfo += 1
                if t9 != t7:
                    if t9 != t5:
                        if t9 != t3:
                            if t9 != t1:
                                await message.channel.send(f"학습이 완료되었습니다 ( {pracinfo} / 8 )")
                            elif t9 == t1:
                                pracinfo -= 1
                                t9 = 0
                                t10 = 0
                                await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                        elif t9 == t3:
                            pracinfo -= 1
                            t9 = 0
                            t10 = 0
                            await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                    elif t9 == t5:
                        pracinfo -= 1
                        t9 = 0
                        t10 = 0
                        await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                elif t9 == t7:
                    pracinfo -= 1
                    t9 = 0
                    t10 = 0
                    await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")



            elif t11 == 0:
                t11 = message.content.replace(prefix + "학습 ", "").split('/')[0]
                t12 = message.content.replace(prefix + "학습 ", "").split('/')[1]
                pracinfo += 1
                if t11 != t9:
                    if t11 != t7:
                        if t11 != t5:
                            if t11 != t3:
                                if t11 != t1:
                                    await message.channel.send(f"학습이 완료되었습니다 ( {pracinfo} / 8 )")
                                elif t11 == t1:
                                    pracinfo -= 1
                                    t11 = 0
                                    t12 = 0
                                    await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                            elif t11 == t3:
                                pracinfo -= 1
                                t11 = 0
                                t12 = 0
                                await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                        elif t11 == t5:
                            pracinfo -= 1
                            t11 = 0
                            t12 = 0
                            await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                    elif t11 == t7:
                        pracinfo -= 1
                        t11 = 0
                        t12 = 0
                        await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                elif t11 == t9:
                    pracinfo -= 1
                    t11 = 0
                    t12 = 0
                    await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")



            elif t13 == 0:
                t13 = message.content.replace(prefix + "학습 ", "").split('/')[0]
                t14 = message.content.replace(prefix + "학습 ", "").split('/')[1]
                pracinfo += 1
                if t13 != t11:
                    if t13 != t9:
                        if t13 != t7:
                            if t13 != t5:
                                if t13 != t3:
                                    if t13 != t1:
                                        await message.channel.send(f"학습이 완료되었습니다 ( {pracinfo} / 8 )")
                                    elif t13 == t1:
                                        pracinfo -= 1
                                        t13 = 0
                                        t14 = 0
                                        await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                                elif t13 == t3:
                                    pracinfo -= 1
                                    t13 = 0
                                    t14 = 0
                                    await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                            elif t13 == t5:
                                pracinfo -= 1
                                t13 = 0
                                t14 = 0
                                await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                        elif t13 == t7:
                            pracinfo -= 1
                            t13 = 0
                            t14 = 0
                            await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                    elif t13 == t9:
                        pracinfo -= 1
                        t13 = 0
                        t14 = 0
                        await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                elif t13 == t11:
                    pracinfo -= 1
                    t13 = 0
                    t14 = 0
                    await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")



            elif t15 == 0:
                t15 = message.content.replace(prefix + "학습 ", "").split('/')[0]
                t16 = message.content.replace(prefix + "학습 ", "").split('/')[1]
                pracinfo += 1
                if t15 != t13:
                    if t15 != t11:
                        if t15 != t9:
                            if t15 != t7:
                                if t15 != t5:
                                    if t15 != t3:
                                        if t15 != t1:
                                            await message.channel.send(f"학습이 완료되었습니다 ( {pracinfo} / 8 )")
                                        elif t15 == t1:
                                            pracinfo -= 1
                                            t15 = 0
                                            t16 = 0
                                            await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                                    elif t15 == t3:
                                        pracinfo -= 1
                                        t15 = 0
                                        t16 = 0
                                        await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                                elif t15 == t5:
                                    pracinfo -= 1
                                    t15 = 0
                                    t16 = 0
                                    await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                            elif t15 == t7:
                                pracinfo -= 1
                                t15 = 0
                                t16 = 0
                                await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                        elif t15 == t9:
                            pracinfo -= 1
                            t15 = 0
                            t16 = 0
                            await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                    elif t15 == t11:
                        pracinfo -= 1
                        t15 = 0
                        t16 = 0
                        await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")
                elif t15 == t13:
                    pracinfo -= 1
                    t15 = 0
                    t16 = 0
                    await message.channel.send("학습 불가 ( 같은 학습이 존재합니다 )")



            else:
                await message.channel.send(f"현재 수집 가능한 공간이 없습니다 ( {pracinfo} / 8 )")

        if message.content == prefix + "학습초기화":
            await message.channel.send("학습 목록을 초기화 합니다\n잠시 기다려 주세요...")
            t1 = 0
            t2 = 0
            pracinfo -= 1
            time.sleep(1)
            await message.channel.send(f"학습 목록중 1개를 초기화 하였습니다 ( {pracinfo} / 8 )")
            t3 = 0
            t4 = 0
            pracinfo -= 1
            time.sleep(1)
            await message.channel.send(f"학습 목록중 2개를 초기화 하였습니다 ( {pracinfo} / 8 )")
            t5 = 0
            t6 = 0
            pracinfo -= 1
            time.sleep(1)
            await message.channel.send(f"학습 목록중 3개를 초기화 하였습니다 ( {pracinfo} / 8 )")
            t7 = 0
            t8 = 0
            pracinfo -= 1
            time.sleep(1)
            await message.channel.send(f"학습 목록중 4개를 초기화 하였습니다 ( {pracinfo} / 8 )")
            t9 = 0
            t10 = 0
            pracinfo -= 1
            time.sleep(1)
            await message.channel.send(f"학습 목록중 5개를 초기화 하였습니다 ( {pracinfo} / 8 )")
            t11 = 0
            t12 = 0
            pracinfo -= 1
            time.sleep(1)
            await message.channel.send(f"학습 목록중 6개를 초기화 하였습니다 ( {pracinfo} / 8 )")
            t13 = 0
            t14 = 0
            pracinfo -= 1
            time.sleep(1)
            await message.channel.send(f"학습 목록중 7개를 초기화 하였습니다 ( {pracinfo} / 8 )")
            t15 = 0
            t16 = 0
            pracinfo -= 1
            time.sleep(1)
            await message.channel.send(f"학습 목록중 8개를 초기화 하였습니다 ( {pracinfo} / 8 )")
            pracinfo = 0


        if message.content == t1:
            id = message.author.id
            if id != 931744333990858773:
                await message.channel.send(t2)

        if message.content == t3:
            id = message.author.id
            if id != 931744333990858773:
                await message.channel.send(t4)

        if message.content == t5:
            id = message.author.id
            if id != 931744333990858773:
                await message.channel.send(t6)

        if message.content == t7:
            id = message.author.id
            if id != 931744333990858773:
                await message.channel.send(t8)

        if message.content == t9:
            id = message.author.id
            if id != 931744333990858773:
                await message.channel.send(t10)

        if message.content == t11:
            id = message.author.id
            if id != 931744333990858773:
                await message.channel.send(t12)

        if message.content == t13:
            id = message.author.id
            if id != 931744333990858773:
                await message.channel.send(t14)

        if message.content == t15:
            id = message.author.id
            if id != 931744333990858773:
                await message.channel.send(t16)
            
        if message.content.startswith (prefix + "off"):
            if chaton == True:
                chaton = False
                await message.channel.send("ON")
            else:
                chaton = True
                await message.channel.send("OFF")
                    
        if cb != False:
            if message.content != prefix + "시비중지":
                await message.channel.send("ㅋ")
                await message.channel.send("아무고토모타쥬?")
                
        if message.content == prefix + "시비털기":
            cb = True
            
        if message.content == prefix + "시비중지":
            cb = False
                 
elif chaton == False:
    @client.event #command
    async def on_message(message):
        await message.channel.send("현재는 봇 작동중이 아니에요!")
    
        if message.content == "-on": #hiden command
            await message.channel.send("ON")
            chaton = True
            
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
            
client.run(token)