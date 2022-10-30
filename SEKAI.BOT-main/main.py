import discord
import os
from help import *
from unit import *
from music import *
from virture_singer import *
from leo_need import *

client = discord.Client()
prefix = "^"

#Link = https://discord.com/oauth2/authorize?client_id=834636037732171817&permissions=67584&scope=bot


@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("System login!")
    print("==============")
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="^도움말 or ^help로 불러줘!!"))

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    #Chat Logs
    # mention = "<@{}>".format(message.author.name)
    # print(message.channel)
    # print(mention,message.content)

    #Help Commands
    if message.content == f"{prefix}도움말" or message.content == f"{prefix}help":
        await message.channel.send(embed=help)

    if message.content == f"{prefix}세카이검색" or message.content == f"{prefix}세카이검색":
        await message.channel.send(embed=sk_help)

    #PROSEKA UNIT Commands
    #UNIT LIST
    if message.content == f"{prefix}세카이검색 유닛":
        await message.channel.send(embed=un_help)


    #VIRTURE SINGER
    if message.content == f"{prefix}세카이검색 유닛 VIRTURE SINGER" or message.content == f"{prefix}세카이검색 유닛 virture singer" or message.content == f"{prefix}세카이검색 유닛 VIRTURESINGER" or message.content == f"{prefix}세카이검색 유닛 virturesinger" or message.content == f"{prefix}세카이검색 유닛 버츄얼 싱어" or message.content == f"{prefix}세카이검색 유닛 버추얼 싱어" or message.content == f"{prefix}세카이검색 유닛 버츄얼싱어" or message.content == f"{prefix}세카이검색 유닛 버추얼싱어":
        await message.channel.send(embed=virsing)

    #MORE MORE JUMP!
    if message.content == f"{prefix}세카이검색 유닛 MORE MORE JUMP!" or message.content == f"{prefix}세카이검색 유닛 more more jump!" or message.content == f"{prefix}세카이검색 유닛 MOREMOREJUMP!" or message.content == f"{prefix}세카이검색 유닛 moremorejump!" or message.content == f"{prefix}세카이검색 유닛 모어 모어 점프!" or message.content == f"{prefix}세카이검색 유닛 모어모어점프!" or message.content == f"{prefix}세카이검색 유닛 모어 모어 점프" or message.content == f"{prefix}세카이검색 유닛 모어모어점프" or message.content == f"{prefix}세카이검색 유닛 모모점" or message.content == f"{prefix}세카이검색 유닛 모모점!":        
        await message.channel.send(embed=momojum)

    #Leo/need
    if message.content == f"{prefix}세카이검색 유닛 Leo/need" or message.content == f"{prefix}세카이검색 유닛 leo/need" or message.content == f"{prefix}세카이검색 유닛 Leoneed" or message.content == f"{prefix}세카이검색 유닛 leoneed" or message.content == f"{prefix}세카이검색 유닛 Leo need" or message.content == f"{prefix}세카이검색 유닛 leo need" or message.content == f"{prefix}세카이검색 유닛 모어 레오 니드" or message.content == f"{prefix}세카이검색 유닛 레오니드" or message.content == f"{prefix}세카이검색 유닛 레오니":        
        await message.channel.send(embed=leonee)

    #Vivid BAD SQUAD
    if message.content == f"{prefix}세카이검색 유닛 Vivid BAD SQUAD" or message.content == f"{prefix}세카이검색 유닛 vivid bad aquad" or message.content == f"{prefix}세카이검색 유닛 VividBADSQUAD" or message.content == f"{prefix}세카이검색 유닛 vividbadsquad" or message.content == f"{prefix}세카이검색 유닛 비비드 배드 스쿼드" or message.content == f"{prefix}세카이검색 유닛 비비드배드스쿼드" or message.content == f"{prefix}세카이검색 유닛 비비배스":        
        await message.channel.send(embed=vivibas)

    #원더랜즈×쇼타임
    if message.content == f"{prefix}세카이검색 유닛 원더랜즈×쇼타임" or message.content == f"{prefix}세카이검색 유닛 원더랜즈x쇼타임" or message.content == f"{prefix}세카이검색 유닛 원더랜즈X쇼타임" or message.content == f"{prefix}세카이검색 유닛 원더랜즈 쇼타임" or message.content == f"{prefix}세카이검색 유닛 원더랜즈쇼타임" or message.content == f"{prefix}세카이검색 유닛 원더쇼":
        await message.channel.send(embed=wondershow)

    #25시, 나이트코드에서.
    if message.content == f"{prefix}세카이검색 유닛 25시, 나이트코드에서." or message.content == f"{prefix}세카이검색 유닛 25시, 나이트코드에서" or message.content == f"{prefix}세카이검색 유닛 25시,나이트코드에서." or message.content == f"{prefix}세카이검색 유닛 25시,나이트코드에서" or message.content == f"{prefix}세카이검색 유닛 25시 나이트코드에서" or message.content == f"{prefix}세카이검색 유닛 25시나이트코드에서" or message.content == f"{prefix}세카이검색 유닛 니고":
        await message.channel.send(embed=nigo)

    #PROSEKA Charater Commands
    #HATSUNE MIKU
    if message.content == f"{prefix}세카이검색 캐릭터 하츠네 미쿠" or message.content == f"{prefix}세카이검색 캐릭터 하츠네미쿠" or message.content == f"{prefix}세카이검색 캐릭터 Hatsune Miku" or message.content == f"{prefix}세카이검색 캐릭터 hatsune miku" or message.content == f"{prefix}세카이검색 캐릭터 HatsuneMiku" or message.content == f"{prefix}세카이검색 캐릭터 hatsunemiku" or message.content == f"{prefix}세카이검색 캐릭터 미쿠" or message.content == f"{prefix}세카이검색 캐릭터 Miku" or message.content == f"{prefix}세카이검색 캐릭터 miku":
        await message.channel.send(embed=miku)

    #KAGAMINE RIN
    if message.content == f"{prefix}세카이검색 캐릭터 카가미네 린" or message.content == f"{prefix}세카이검색 캐릭터 카가미네린" or message.content == f"{prefix}세카이검색 캐릭터 Kagamine Rin" or message.content == f"{prefix}세카이검색 캐릭터 kagamine rin" or message.content == f"{prefix}세카이검색 캐릭터 KagamineRin" or message.content == f"{prefix}세카이검색 캐릭터 kagaminerin" or message.content == f"{prefix}세카이검색 캐릭터 린" or message.content == f"{prefix}세카이검색 캐릭터 Rin" or message.content == f"{prefix}세카이검색 캐릭터 rin":
        await message.channel.send(embed=rin)

    #KAGAMINE LEN
    if message.content == f"{prefix}세카이검색 캐릭터 카가미네 렌" or message.content == f"{prefix}세카이검색 캐릭터 카가미네렌" or message.content == f"{prefix}세카이검색 캐릭터 Kagamine Len" or message.content == f"{prefix}세카이검색 캐릭터 kagamine len" or message.content == f"{prefix}세카이검색 캐릭터 KagamineLen" or message.content == f"{prefix}세카이검색 캐릭터 kagaminelen" or message.content == f"{prefix}세카이검색 캐릭터 렌" or message.content == f"{prefix}세카이검색 캐릭터 Len" or message.content == f"{prefix}세카이검색 캐릭터 len":
        await message.channel.send(embed=ren)

    #MEGURINE LUKA
    if message.content == f"{prefix}세카이검색 캐릭터 메구리네 루카" or message.content == f"{prefix}세카이검색 캐릭터 메구리네루카" or message.content == f"{prefix}세카이검색 캐릭터 Megurine Luka" or message.content == f"{prefix}세카이검색 캐릭터 megurine luka" or message.content == f"{prefix}세카이검색 캐릭터 MegurineLuka" or message.content == f"{prefix}세카이검색 캐릭터 megurineluka" or message.content == f"{prefix}세카이검색 캐릭터 루카" or message.content == f"{prefix}세카이검색 캐릭터 Luka" or message.content == f"{prefix}세카이검색 캐릭터 luka":
        await message.channel.send(embed=luka)

    #MEIKO
    if message.content == f"{prefix}세카이검색 캐릭터 메이코" or message.content == f"{prefix}세카이검색 캐릭터 MEIKO" or message.content == f"{prefix}세카이검색 캐릭터 meiko" or message.content == f"{prefix}세카이검색 캐릭터 Meiko":
        await message.channel.send(embed=meiko)

    #KAITO
    if message.content == f"{prefix}세카이검색 캐릭터 카이토" or message.content == f"{prefix}세카이검색 캐릭터 KAITO" or message.content == f"{prefix}세카이검색 캐릭터 kaito" or message.content == f"{prefix}세카이검색 캐릭터 Kaito":
        await message.channel.send(embed=kaito)

    #HOSHINO ICHIKA
    if message.content == f"{prefix}세카이검색 캐릭터 호시노 이치카" or message.content == f"{prefix}세카이검색 캐릭터 호시노이치카" or message.content == f"{prefix}세카이검색 캐릭터 Hoshino Ichika" or message.content == f"{prefix}세카이검색 캐릭터 hoshino ichika" or message.content == f"{prefix}세카이검색 캐릭터 HoshinoIchika" or message.content == f"{prefix}세카이검색 캐릭터 hoshinoichika" or message.content == f"{prefix}세카이검색 캐릭터 이치카" or message.content == f"{prefix}세카이검색 캐릭터 Ichika" or message.content == f"{prefix}세카이검색 캐릭터 ichika":
        await message.channel.send(embed=ichika)

    #TENMA SAKI
    if message.content == f"{prefix}세카이검색 캐릭터 텐마 사키" or message.content == f"{prefix}세카이검색 캐릭터 텐마사키" or message.content == f"{prefix}세카이검색 캐릭터 Tenma Saki" or message.content == f"{prefix}세카이검색 캐릭터 tenma saki" or message.content == f"{prefix}세카이검색 캐릭터 TenmaSaki" or message.content == f"{prefix}세카이검색 캐릭터 tenmasaki" or message.content == f"{prefix}세카이검색 캐릭터 사키" or message.content == f"{prefix}세카이검색 캐릭터 Saki" or message.content == f"{prefix}세카이검색 캐릭터 saki":
        await message.channel.send(embed=saki)

    #MOCHIZUKI HONAMI
    if message.content == f"{prefix}세카이검색 캐릭터 모치즈키 호나미" or message.content == f"{prefix}세카이검색 캐릭터 모치즈키호나미" or message.content == f"{prefix}세카이검색 캐릭터 Mochizuki Honami" or message.content == f"{prefix}세카이검색 캐릭터 mochizuki honami" or message.content == f"{prefix}세카이검색 캐릭터 MochizukiHonami" or message.content == f"{prefix}세카이검색 캐릭터 mochizukihonami" or message.content == f"{prefix}세카이검색 캐릭터 호나미" or message.content == f"{prefix}세카이검색 캐릭터 honami" or message.content == f"{prefix}세카이검색 캐릭터 Honami":
        await message.channel.send(embed=honami)

    #HINOMORI SHIHO
    if message.content == f"{prefix}세카이검색 캐릭터 히노모리 시호" or message.content == f"{prefix}세카이검색 캐릭터 히노모리시호" or message.content == f"{prefix}세카이검색 캐릭터 Hinomori Shiho" or message.content == f"{prefix}세카이검색 캐릭터 hinomori shiho"  or message.content == f"{prefix}세카이검색 캐릭터 HinomoriShiho" or message.content == f"{prefix}세카이검색 캐릭터 hinomorishiho" or message.content == f"{prefix}세카이검색 캐릭터 시호" or message.content == f"{prefix}세카이검색 캐릭터 shiho" or message.content == f"{prefix}세카이검색 캐릭터 Shiho":
        await message.channel.send(embed=shiho)


    #PROSEKA Music Commands
    #Music LIST
    if message.content == f"{prefix}세카이검색 음악":
        await message.channel.send(embed=ms_help)

    #Tell your World
    if message.content == f"{prefix}세카이검색 음악 Tell your World" or message.content == f"{prefix}세카이검색 음악 텔유어월드" or message.content == f"{prefix}세카이검색 음악 tell your world" or message.content == f"{prefix}세카이검색 음악 TellYourWorld" or message.content == f"{prefix}세카이검색 음악 tellyourworld" or message.content == f"{prefix}세카이검색 음악 텔 유어 월드":
        await message.channel.send(embed=TYW)

    #Roki
    if message.content == f"{prefix}세카이검색 음악 Roki" or message.content == f"{prefix}세카이검색 음악 로키" or message.content == f"{prefix}세카이검색 음악 roki":
        await message.channel.send(embed=roki)

    #Teo
    if message.content == f"{prefix}세카이검색 음악 테오" or message.content == f"{prefix}세카이검색 음악 teo" or message.content == f"{prefix}세카이검색 음악 Teo":
        await message.channel.send(embed=teo)

    #Hibana
    if message.content == f"{prefix}세카이검색 음악 히바나" or message.content == f"{prefix}세카이검색 음악 Hibana" or message.content == f"{prefix}세카이검색 음악 hibana" or message.content == f"{prefix}세카이검색 음악 Hibana -Reloaded-" or message.content == f"{prefix}세카이검색 음악 hibana -reloaded-" or message.content == f"{prefix}세카이검색 음악 히바나 -Reloaded-" or message.content == f"{prefix}세카이검색 음악 히바나 -reloaded-":
        await message.channel.send(embed=HB)

    #타임머신
    if message.content == f"{prefix}세카이검색 음악 Timemachine" or message.content == f"{prefix}세카이검색 음악 타임머신" or message.content == f"{prefix}세카이검색 음악 timemachine":
        await message.channel.send(embed=TM)

    #해피신디사이저
    if message.content == f"{prefix}세카이검색 음악 해피 신디사이저" or message.content == f"{prefix}세카이검색 음악 해피신디사이저" or message.content == f"{prefix}세카이검색 음악 해피 Happy synthesizer" or message.content == f"{prefix}세카이검색 음악 해피 happy synthesizer" or message.content == f"{prefix}세카이검색 음악 해피 Happysynthesizer" or message.content == f"{prefix}세카이검색 음악 해피 happysynthesizer":
        await message.channel.send(embed=HS)

    #비바해피
    if message.content == f"{prefix}세카이검색 음악 비바해피" or message.content == f"{prefix}세카이검색 음악 vivahappy" or message.content == f"{prefix}세카이검색 음악 해피 VIVAHAPPY" or message.content == f"{prefix}세카이검색 음악 viva happy" or message.content == f"{prefix}세카이검색 음악 해피 VIVA HAPPY":
        await message.channel.send(embed=VH)

    #Nostalogic
    if message.content == f"{prefix}세카이검색 음악 Nostalogic" or message.content == f"{prefix}세카이검색 음악 nostalogic" or message.content == f"{prefix}세카이검색 음악 노스탈로직" or message.content == f"{prefix}세카이검색 음악 노스탤로직":
        await message.channel.send(embed=NL)

    #drop pop candy
    if message.content == f"{prefix}세카이검색 음악 drop pop candy" or message.content == f"{prefix}세카이검색 음악 Drop Pop Candy" or message.content == f"{prefix}세카이검색 음악 드롭 팝 캔디" or message.content == f"{prefix}세카이검색 음악 droppopcandy" or message.content == f"{prefix}세카이검색 음악 DropPopCandy" or message.content == f"{prefix}세카이검색 음악 드롭팝캔디":
        await message.channel.send(embed=DPC)

    #내일의 밤하늘 초계반
    if message.content == f"{prefix}세카이검색 음악 내일의 밤하늘 초계반" or message.content == f"{prefix}세카이검색 음악 내일의밤하늘초계반" or message.content == f"{prefix}세카이검색 음악 내일의밤하늘초계탕" or message.content == f"{prefix}세카이검색 음악 내일의 밤하늘 초계탕":
        await message.channel.send(embed=NBC)

    #하츠네미쿠의 소실
    if message.content == f"{prefix}세카이검색 음악 하츠네미쿠의 소실" or message.content == f"{prefix}세카이검색 음악 하츠네미쿠의소실" or message.content == f"{prefix}세카이검색 음악 소실":
        await message.channel.send(embed=HSS)

    #하츠네미쿠의 격창
    if message.content == f"{prefix}세카이검색 음악 하츠네미쿠의 격창" or message.content == f"{prefix}세카이검색 음악 하츠네미쿠의격창" or message.content == f"{prefix}세카이검색 음악 격창":
        await message.channel.send(embed=HGC)

    #그린라이츠 세레나데
    if message.content == f"{prefix}세카이검색 음악 그린라이츠 세레나데" or message.content == f"{prefix}세카이검색 음악 그린라이츠세레나데" or message.content == f"{prefix}세카이검색 음악 Greenlights Serenade" or message.content == f"{prefix}세카이검색 음악 greenlights serenade" or message.content == f"{prefix}세카이검색 음악 GreenlightsSerenade" or message.content == f"{prefix}세카이검색 음악 greenlightsserenade":
        await message.channel.send(embed=GS)

    #샤를
    if message.content == f"{prefix}세카이검색 음악 샤를":
        await message.channel.send(embed=SR)

    #탈법 록
    if message.content == f"{prefix}세카이검색 음악 탈법 록" or message.content == f"{prefix}세카이검색 음악 탈법록":
        await message.channel.send(embed=TBR)

    #생명에게 미움받고 있어
    if message.content == f"{prefix}세카이검색 음악 생명에게 미움받고 있어" or message.content == f"{prefix}세카이검색 음악 생명에게미움받고있어" or message.content == f"{prefix}세카이검색 음악 생명에게 미움 받고 있어":
        await message.channel.send(embed=SMI)

    #열등상등
    if message.content == f"{prefix}세카이검색 음악 열등상등" or message.content == f"{prefix}세카이검색 음악 BRING IT ON" or message.content == f"{prefix}세카이검색 음악 BRINGITON" or message.content == f"{prefix}세카이검색 음악 bring it on" or message.content == f"{prefix}세카이검색 음악 bringiton":
        await message.channel.send(embed=BIO)

    #Just Be Friends
    if message.content == f"{prefix}세카이검색 음악 Just Be Friends" or message.content == f"{prefix}세카이검색 음악 just be friends" or message.content == f"{prefix}세카이검색 음악 JustBeFriends" or message.content == f"{prefix}세카이검색 음악 justbefriends":
        await message.channel.send(embed=JBF)

    #닥터=펑크 비트
    if message.content == f"{prefix}세카이검색 음악 닥터=펑크 비트" or message.content == f"{prefix}세카이검색 음악 닥터 펑크 비트" or message.content == f"{prefix}세카이검색 음악 닥터펑크비트":
        await message.channel.send(embed=DPB)

    #미라클 페인트
    if message.content == f"{prefix}세카이검색 음악 미라클 페인트" or message.content == f"{prefix}세카이검색 음악 미라클페인트" or message.content == f"{prefix}세카이검색 음악 miracle painting" or message.content == f"{prefix}세카이검색 음악 miraclepainting" or message.content == f"{prefix}세카이검색 음악 Miracle Painting" or message.content == f"{prefix}세카이검색 음악 MiraclePainting":
        await message.channel.send(embed=MP)

    #브리키의 댄스
    if message.content == f"{prefix}세카이검색 음악 브리키의 댄스" or message.content == f"{prefix}세카이검색 음악 브리키의 댄스" or message.content == f"{prefix}세카이검색 음악 브리키노 댄스" or message.content == f"{prefix}세카이검색 음악 브리키노댄스":
        await message.channel.send(embed=BKS)

    #스위트 매직
    if message.content == f"{prefix}세카이검색 음악 스위트 매직" or message.content == f"{prefix}세카이검색 음악 스위트매직" or message.content == f"{prefix}세카이검색 음악 Sweet Magic" or message.content == f"{prefix}세카이검색 음악 sweet magic" or message.content == f"{prefix}세카이검색 음악 SweetMagic" or message.content == f"{prefix}세카이검색 음악 sweetmagic":
        await message.channel.send(embed=SM)

    #넥스트 네스트
    if message.content == f"{prefix}세카이검색 음악 넥스트 네스트" or message.content == f"{prefix}세카이검색 음악 넥스트네스트" or message.content == f"{prefix}세카이검색 음악 Next Nest" or message.content == f"{prefix}세카이검색 음악 next nest" or message.content == f"{prefix}세카이검색 음악 NextNest" or message.content == f"{prefix}세카이검색 음악 nextnest":
        await message.channel.send(embed=NN)

    #Hand in Hand
    if message.content == f"{prefix}세카이검색 음악 Hand in Hand" or message.content == f"{prefix}세카이검색 음악 hand in hand" or message.content == f"{prefix}세카이검색 음악 핸드 인 핸드" or message.content == f"{prefix}세카이검색 음악 핸드인핸드":
        await message.channel.send(embed=HIH)

    #39뮤직!
    if message.content == f"{prefix}세카이검색 음악 39뮤직!" or message.content == f"{prefix}세카이검색 음악 39 뮤직!" or message.content == f"{prefix}세카이검색 음악 39뮤직" or message.content == f"{prefix}세카이검색 음악 39 뮤직" or message.content == f"{prefix}세카이검색 음악 39Music!" or message.content == f"{prefix}세카이검색 음악 39 Music!" or message.content == f"{prefix}세카이검색 음악 39 Music" or message.content == f"{prefix}세카이검색 음악 39Music" or message.content == f"{prefix}세카이검색 음악 39music!" or message.content == f"{prefix}세카이검색 음악 39 music!" or message.content == f"{prefix}세카이검색 음악 39 music" or message.content == f"{prefix}세카이검색 음악 39music":
        await message.channel.send(embed=SKM)

    #멜트
    if message.content == f"{prefix}세카이검색 음악 멜트" or message.content == f"{prefix}세카이검색 음악 Melt" or message.content == f"{prefix}세카이검색 음악 melt":
        await message.channel.send(embed=melt)

    #월드 이즈 마인
    if message.content == f"{prefix}세카이검색 음악 월드 이즈 마인" or message.content == f"{prefix}세카이검색 음악 월드이즈마인" or message.content == f"{prefix}세카이검색 음악 World Is Mine" or message.content == f"{prefix}세카이검색 음악 WorldIsMine" or message.content == f"{prefix}세카이검색 음악 world is mine" or message.content == f"{prefix}세카이검색 음악 worldismine":
        await message.channel.send(embed=WIM)

    #Blessing
    if message.content == f"{prefix}세카이검색 음악 Blessing" or message.content == f"{prefix}세카이검색 음악 blessing" or message.content == f"{prefix}세카이검색 음악 블레싱":
        await message.channel.send(embed=BS)

    #세상은 아직 시작조차 하지 않았어
    if message.content == f"{prefix}세카이검색 음악 세상은 아직 시작조차 하지 않았어" or message.content == f"{prefix}세카이검색 음악 세상은 아직시작조차하지않았어":
        await message.channel.send(embed=SMHS)

    #potato가 되어가
    if message.content == f"{prefix}세카이검색 음악 potato가 되어가" or message.content == f"{prefix}세카이검색 음악 potato가되어가":
        await message.channel.send(embed=PN)

    #Ready Steady
    if message.content == f"{prefix}세카이검색 음악 Ready Steady" or message.content == f"{prefix}세카이검색 음악 ready steady" or message.content == f"{prefix}세카이검색 음악 ReadySteady" or message.content == f"{prefix}세카이검색 음악 readysteady" or message.content == f"{prefix}세카이검색 음악 레디스테디" or message.content == f"{prefix}세카이검색 음악 레디 스테디":
        await message.channel.send(embed=RS)

    #Forward
    if message.content == f"{prefix}세카이검색 음악 Forward" or message.content == f"{prefix}세카이검색 음악 forward" or message.content == f"{prefix}세카이검색 음악 포워드":
        await message.channel.send(embed=FW)

    #아이돌 신예대
    if message.content == f"{prefix}세카이검색 음악 아이돌 신예대" or message.content == f"{prefix}세카이검색 음악 아이돌신예대":
        await message.channel.send(embed=AS)

    #후회한다 쓰고 미래
    if message.content == f"{prefix}세카이검색 음악 후회한다 쓰고 미래" or message.content == f"{prefix}세카이검색 음악 후회한다쓰고미래":
        await message.channel.send(embed=HM)

    #휴대연화
    if message.content == f"{prefix}세카이검색 음악 휴대연화" or message.content == f"{prefix}세카이검색 음악 휴대전화" or message.content == f"{prefix}세카이검색 음악 스마트폰" or message.content == f"{prefix}세카이검색 음악 휴대폰" or message.content == f"{prefix}세카이검색 음악 핸드폰":
        await message.channel.send(embed=phone)

    #잭팟 새드 걸
    if message.content == f"{prefix}세카이검색 음악 잭팟 새드 걸" or message.content == f"{prefix}세카이검색 음악 잭팟새드걸" or message.content == f"{prefix}세카이검색 음악 Jackpot Sad Girl" or message.content == f"{prefix}세카이검색 음악 JackpotSadGirl" or message.content == f"{prefix}세카이검색 음악 jackpot sad girl" or message.content == f"{prefix}세카이검색 음악 jackpotsadgirl":
        await message.channel.send(embed=JSG)

    #needLe
    if message.content == f"{prefix}세카이검색 음악 needLe" or message.content == f"{prefix}세카이검색 음악 needle" or message.content == f"{prefix}세카이검색 음악 니들리" or message.content == f"{prefix}세카이검색 음악 니들레":
        await message.channel.send(embed=NDL)

    #스텔라
    if message.content == f"{prefix}세카이검색 음악 Stella" or message.content == f"{prefix}세카이검색 음악 stella" or message.content == f"{prefix}세카이검색 음악 스텔라":
        await message.channel.send(embed=STL)

    #헬로/하와유
    if message.content == f"{prefix}세카이검색 음악 헬로/하와유" or message.content == f"{prefix}세카이검색 음악 헬로 하와유" or message.content == f"{prefix}세카이검색 음악 헬로하와유" or message.content == f"{prefix}세카이검색 음악 Hello/How Are You" or message.content == f"{prefix}세카이검색 음악 Hello How Are You" or message.content == f"{prefix}세카이검색 음악 HelloHowAreYou" or message.content == f"{prefix}세카이검색 음악 hello/how are you" or message.content == f"{prefix}세카이검색 음악 hello how are you" or message.content == f"{prefix}세카이검색 음악 hellohowareyou":
        await message.channel.send(embed=HHAY)

    #자상무색
    if message.content == f"{prefix}세카이검색 음악 자상무색" or message.content == f"{prefix}세카이검색 음악 자상 무색":
        await message.channel.send(embed=JSMS)

    #댄스 로봇 댄스
    if message.content == f"{prefix}세카이검색 음악 댄스 로봇 댄스" or message.content == f"{prefix}세카이검색 음악 댄스로봇댄스" or message.content == f"{prefix}세카이검색 음악 Dance Robot Dance" or message.content == f"{prefix}세카이검색 음악 DanceRobotDance" or message.content == f"{prefix}세카이검색 음악 dance robot dance" or message.content == f"{prefix}세카이검색 음악 dancerobotdance":
        await message.channel.send(embed=DRD)

    #멜티 랜드 나이트메어
    if message.content == f"{prefix}세카이검색 음악 멜티 랜드 나이트메어" or message.content == f"{prefix}세카이검색 음악 멜티랜드나이트메어" or message.content == f"{prefix}세카이검색 음악 Melty Land Nightmare" or message.content == f"{prefix}세카이검색 음악 MeltyLandNightmare" or message.content == f"{prefix}세카이검색 음악 melty land nightmare" or message.content == f"{prefix}세카이검색 음악 meltylandnightmare":
        await message.channel.send(embed=MLN)

    #누덕누덕 스타카토
    if message.content == f"{prefix}세카이검색 음악 누덕누덕 스타카토" or message.content == f"{prefix}세카이검색 음악 누덕 누덕 스타카토" or message.content == f"{prefix}세카이검색 음악 누덕누덕스타카토":
        await message.channel.send(embed=PS)

    #블레스 유어 브레스
    if message.content == f"{prefix}세카이검색 음악 블레스 유어 브레스" or message.content == f"{prefix}세카이검색 음악 블레스유어브레스" or message.content == f"{prefix}세카이검색 음악 Bless Your Breath" or message.content == f"{prefix}세카이검색 음악 BlessYourBreath" or message.content == f"{prefix}세카이검색 음악 bless your breath" or message.content == f"{prefix}세카이검색 음악 blessyourbreath":
        await message.channel.send(embed=BYB)

    #니아
    if message.content == f"{prefix}세카이검색 음악 니아" or message.content == f"{prefix}세카이검색 음악 Near" or message.content == f"{prefix}세카이검색 음악 near":
        await message.channel.send(embed=near)

    #혼자 놀이 엔비
    if message.content == f"{prefix}세카이검색 음악 혼자 놀이 엔비" or message.content == f"{prefix}세카이검색 음악 혼자놀이엔비":
        await message.channel.send(embed=HSE)

    #갯나리 해저담
    if message.content == f"{prefix}세카이검색 음악 갯나리 해저담" or message.content == f"{prefix}세카이검색 음악 갯나리해저담":
        await message.channel.send(embed=GH)

    #세카이
    if message.content == f"{prefix}세카이검색 음악 세카이" or message.content == f"{prefix}세카이검색 음악 sekai" or message.content == f"{prefix}세카이검색 음악 Sekai" or message.content == f"{prefix}세카이검색 음악 SEKAI":
        await message.channel.send(embed=sekai)

    #와-와-월드
    if message.content == f"{prefix}세카이검색 음악 와-와-월드" or message.content == f"{prefix}세카이검색 음악 와 와 월드" or message.content == f"{prefix}세카이검색 음악 와와월드" or message.content == f"{prefix}세카이검색 음악 Wah Wah World" or message.content == f"{prefix}세카이검색 음악 wah wah world" or message.content == f"{prefix}세카이검색 음악 WahWahWorld" or message.content == f"{prefix}세카이검색 음악 wahwahworld":
        await message.channel.send(embed=WWW)

    #모험의 서가 사라졌습니다!
    if message.content == f"{prefix}세카이검색 음악 모험의 서가 사라졌습니다!" or message.content == f"{prefix}세카이검색 음악 모험의서가사라졌습니다!" or message.content == f"{prefix}세카이검색 음악 모험의 서가 사라졌습니다" or message.content == f"{prefix}세카이검색 음악 모험의서가사라졌습니다":
        await message.channel.send(embed=MSS)

    #야화 디세이브
    if message.content == f"{prefix}세카이검색 음악 야화 디세이브" or message.content == f"{prefix}세카이검색 음악 야화디세이브":
        await message.channel.send(embed=YD)

    #alive
    if message.content == f"{prefix}세카이검색 음악 alive" or message.content == f"{prefix}세카이검색 음악 얼라이브":
        await message.channel.send(embed=alive)

    #Gimme×Gimme
    if message.content == f"{prefix}세카이검색 음악 Gimme×Gimme" or message.content == f"{prefix}세카이검색 음악 gimme×gimme" or message.content == f"{prefix}세카이검색 음악 Gimme Gimme" or message.content == f"{prefix}세카이검색 음악 gimme gimme" or message.content == f"{prefix}세카이검색 음악 GimmeGimme" or message.content == f"{prefix}세카이검색 음악 gimmegimme":
        await message.channel.send(embed=GG)

    #정키 나이트 타운 오케스트라
    if message.content == f"{prefix}세카이검색 음악 정키 나이트 타운 오케스트라" or message.content == f"{prefix}세카이검색 음악 정키나이트타운오케스트라":
        await message.channel.send(embed=JNTO)

    #Leia - Remind
    if message.content == f"{prefix}세카이검색 음악 Leia" or message.content == f"{prefix}세카이검색 음악 leia":
        await message.channel.send(embed=leia)

    #on the rocks
    if message.content == f"{prefix}세카이검색 음악 on the rocks" or message.content == f"{prefix}세카이검색 음악 ontherocks":
        await message.channel.send(embed=OTR)

    #연애재판
    if message.content == f"{prefix}세카이검색 음악 연애재판" or message.content == f"{prefix}세카이검색 음악 연애 재판":
        await message.channel.send(embed=YEJP)

    #츄루리라·츄루리라·땃땃따!
    if message.content == f"{prefix}세카이검색 음악 츄루리라 츄루리라 땃땃따!" or message.content == f"{prefix}세카이검색 음악 츄루리라츄루리라땃땃따!" or message.content == f"{prefix}세카이검색 음악 츄루리라 츄루리라 땃땃따" or message.content == f"{prefix}세카이검색 음악 츄루리라츄루리라땃땃따":
        await message.channel.send(embed=CCD)

    #Color of Drops
    if message.content == f"{prefix}세카이검색 음악 Color of Drops" or message.content == f"{prefix}세카이검색 음악 ColorofDrops" or message.content == f"{prefix}세카이검색 음악 color of drops" or message.content == f"{prefix}세카이검색 음악 colorofdrops":
        await message.channel.send(embed=COD)

    #끝없이 잿빛으로
    if message.content == f"{prefix}세카이검색 음악 끝없이 잿빛으로" or message.content == f"{prefix}세카이검색 음악 끝없이잿빛으로":
        await message.channel.send(embed=GJ)

    #드라마트루기
    if message.content == f"{prefix}세카이검색 음악 드라마트 루기" or message.content == f"{prefix}세카이검색 음악 드라마트루기":
        await message.channel.send(embed=DR)

    #소녀해부
    if message.content == f"{prefix}세카이검색 음악 소녀해부" or message.content == f"{prefix}세카이검색 음악 소녀 해부":
        await message.channel.send(embed=SNHB)

    #푸르게 달려라!
    if message.content == f"{prefix}세카이검색 음악 푸르게 달려라!" or message.content == f"{prefix}세카이검색 음악 푸르게달려라!" or message.content == f"{prefix}세카이검색 음악 푸르게 달려라" or message.content == f"{prefix}세카이검색 음악 푸르게달려라":
        await message.channel.send(embed=FD)

    #너무 아파 아프고 싶어
    if message.content == f"{prefix}세카이검색 음악 너무 아파 아프고 싶어" or message.content == f"{prefix}세카이검색 음악 너무아파아프고싶어":
        await message.channel.send(embed=NAAS)

    #위풍당당
    if message.content == f"{prefix}세카이검색 음악 위풍당당" or message.content == f"{prefix}세카이검색 음악 위풍 당당":
        await message.channel.send(embed=WFDD)

    #from Y to Y
    if message.content == f"{prefix}세카이검색 음악 from Y to Y" or message.content == f"{prefix}세카이검색 음악 fromYtoY" or message.content == f"{prefix}세카이검색 음악 from y to y" or message.content == f"{prefix}세카이검색 음악 fromytoy":
        await message.channel.send(embed=FYTY)

    #날이 개길 기다려
    if message.content == f"{prefix}세카이검색 음악 날이 개길 기다려" or message.content == f"{prefix}세카이검색 음악 날이개길기다려":
        await message.channel.send(embed=NGG)

    #모어! 점프! 모어!
    if message.content == f"{prefix}세카이검색 음악 모어! 점프! 모어!" or message.content == f"{prefix}세카이검색 음악 모어!점프!모어!" or message.content == f"{prefix}세카이검색 음악 모어 점프 모어" or message.content == f"{prefix}세카이검색 음악 모어점프모어" or message.content == f"{prefix}세카이검색 음악 MORE! JUMP! MORE!" or message.content == f"{prefix}세카이검색 음악 MORE JUMP MORE" or message.content == f"{prefix}세카이검색 음악 more! jump! more!" or message.content == f"{prefix}세카이검색 음악 more jump more":
        await message.channel.send(embed=MJM)

    #ECHO
    if message.content == f"{prefix}세카이검색 음악 ECHO" or message.content == f"{prefix}세카이검색 음악 echo":
        await message.channel.send(embed=echo)

    #RAD DOGS
    if message.content == f"{prefix}세카이검색 음악 RAD DOGS" or message.content == f"{prefix}세카이검색 음악 rad dogs" or message.content == f"{prefix}세카이검색 음악 RADDOGS" or message.content == f"{prefix}세카이검색 음악 raddogs":
        await message.channel.send(embed=RD)

    #무지갯빛 스토리즈
    if message.content == f"{prefix}세카이검색 음악 무지개빛 스토리즈" or message.content == f"{prefix}세카이검색 음악 무지개빛스토리즈" or message.content == f"{prefix}세카이검색 음악 무지갯빛 스토리즈" or message.content == f"{prefix}세카이검색 음악 무지갯빛 스토리즈":
        await message.channel.send(embed=MS)

    #원스 어폰 어 드림
    if message.content == f"{prefix}세카이검색 음악 원스 어폰 어 드림" or message.content == f"{prefix}세카이검색 음악 원스어폰어드림" or message.content == f"{prefix}세카이검색 음악 once upon a dream" or message.content == f"{prefix}세카이검색 음악 onceuponadream":
        await message.channel.send(embed=OUAD)

    #마음에 드시는 대로
    if message.content == f"{prefix}세카이검색 음악 마음에 드시는대로" or message.content == f"{prefix}세카이검색 음악 마음에드시는대로" or message.content == f"{prefix}세카이검색 음악 마음에드시는대로":
        await message.channel.send(embed=MDD)

    #밀크크라운・온・소네치카
    if message.content == f"{prefix}세카이검색 음악 밀크 크라운 온 소네치카" or message.content == f"{prefix}세카이검색 음악 밀크크라운온소네치카" or message.content == f"{prefix}세카이검색 음악 Milk Crown on Sonechka" or message.content == f"{prefix}세카이검색 음악 milk crown on sonechka" or message.content == f"{prefix}세카이검색 음악 MilkCrownonSonechka" or message.content == f"{prefix}세카이검색 음악 milkcrownonsonechka":
        await message.channel.send(embed=MCOS)

    #사랑받지 못해도 네가 있어
    if message.content == f"{prefix}세카이검색 음악 사랑받지 못해도 네가 있어" or message.content == f"{prefix}세카이검색 음악 사랑받지 못해도 네가있어" or message.content == f"{prefix}세카이검색 음악 사랑받지못해도네가있어":
        await message.channel.send(embed=SMNI)

    #울려퍼져라
    if message.content == f"{prefix}세카이검색 음악 울려퍼져라" or message.content == f"{prefix}세카이검색 음악 울려 퍼져라" or message.content == f"{prefix}세카이검색 음악 히비카세":
        await message.channel.send(embed=HBKS)

    #천본앵
    if message.content == f"{prefix}세카이검색 음악 천본앵" or message.content == f"{prefix}세카이검색 음악 Senbonzakura" or message.content == f"{prefix}세카이검색 음악 senbonzakura":
        await message.channel.send(embed=SBZKR)

    #천사의 클로버
    if message.content == f"{prefix}세카이검색 음악 천사의 클로버" or message.content == f"{prefix}세카이검색 음악 천사의클로버":
        await message.channel.send(embed=TC)

    #롤링 걸
    if message.content == f"{prefix}세카이검색 음악 롤링 걸" or message.content == f"{prefix}세카이검색 음악 롤링걸" or message.content == f"{prefix}세카이검색 음악 Rollin Girl" or message.content == f"{prefix}세카이검색 음악 rollin girl" or message.content == f"{prefix}세카이검색 음악 RollinGirl" or message.content == f"{prefix}세카이검색 음악 rollingirl":
        await message.channel.send(embed=RG)

    #겉과 속의 러버즈
    if message.content == f"{prefix}세카이검색 음악 겉과 속의 러버즈" or message.content == f"{prefix}세카이검색 음악 겉과속의 러버즈" or message.content == f"{prefix}세카이검색 음악 겉과속의러버즈":
        await message.channel.send(embed=GSL)

    #ODDS&ENDS
    if message.content == f"{prefix}세카이검색 음악 ODDS&ENDS" or message.content == f"{prefix}세카이검색 음악 odds&ends" or message.content == f"{prefix}세카이검색 음악 ODDS ENDS" or message.content == f"{prefix}세카이검색 음악 odds ends" or message.content == f"{prefix}세카이검색 음악 ODDSENDS" or message.content == f"{prefix}세카이검색 음악 oddsends":
        await message.channel.send(embed=OE)

    #*헬로, 플래닛.
    if message.content == f"{prefix}세카이검색 음악 헬로 플래닛" or message.content == f"{prefix}세카이검색 음악 헬로플래닛":
        await message.channel.send(embed=HP)

    #월즈 엔드・댄스홀
    if message.content == f"{prefix}세카이검색 음악 월즈 엔드 댄스홀" or message.content == f"{prefix}세카이검색 음악 월즈엔드댄스홀" or message.content == f"{prefix}세카이검색 음악 World's End Dance Hall" or message.content == f"{prefix}세카이검색 음악 world's end dance hall" or message.content == f"{prefix}세카이검색 음악 World'sEndDanceHall" or message.content == f"{prefix}세카이검색 음악 world'senddancehall":
        await message.channel.send(embed=WEDH)

    #포지티브☆댄스타임
    if message.content == f"{prefix}세카이검색 음악 포지티브 댄스 타임" or message.content == f"{prefix}세카이검색 음악 포지티브 댄스타임" or message.content == f"{prefix}세카이검색 음악 포지티브댄스타임":
        await message.channel.send(embed=PDT)

    #드리밍 츄츄
    if message.content == f"{prefix}세카이검색 음악 드리밍 츄츄" or message.content == f"{prefix}세카이검색 음악 드리밍츄츄":
        await message.channel.send(embed=DCC)

    #미쿠미쿠하게 해줄게♪
    if message.content == f"{prefix}세카이검색 음악 미쿠미쿠하게 해줄게" or message.content == f"{prefix}세카이검색 음악 미쿠미쿠하게해줄게":
        await message.channel.send(embed=MMS)

    #보카 델라 베리타
    if message.content == f"{prefix}세카이검색 음악 보카 델라 베리타" or message.content == f"{prefix}세카이검색 음악 보카델라 베리타" or message.content == f"{prefix}세카이검색 음악 보카델라베리타":
        await message.channel.send(embed=BDV)

    #Brand New Day
    if message.content == f"{prefix}세카이검색 음악 Brand New Day" or message.content == f"{prefix}세카이검색 음악 brand new day" or message.content == f"{prefix}세카이검색 음악 BrandNewDay" or message.content == f"{prefix}세카이검색 음악 brandnewday" or message.content == f"{prefix}세카이검색 음악 브랜드 뉴 데이" or message.content == f"{prefix}세카이검색 음악 브랜드뉴데이":
        await message.channel.send(embed=BND)

    #아이디 스마일
    if message.content == f"{prefix}세카이검색 음악 아이디 스마일" or message.content == f"{prefix}세카이검색 음악 ID SMILE" or message.content == f"{prefix}세카이검색 음악 id smile" or message.content == f"{prefix}세카이검색 음악 아이디스마일" or message.content == f"{prefix}세카이검색 음악 IDSMILE" or message.content == f"{prefix}세카이검색 음악 idsmile":
        await message.channel.send(embed=IS)

    #이치
    if message.content == f"{prefix}세카이검색 음악 「1」" or message.content == f"{prefix}세카이검색 음악 1" or message.content == f"{prefix}세카이검색 음악 이치" or message.content == f"{prefix}세카이검색 음악 원" or message.content == f"{prefix}세카이검색 음악 일":
        await message.channel.send(embed=I)

    #꽃을 노래하다
    if message.content == f"{prefix}세카이검색 음악 꽃을 노래하다" or message.content == f"{prefix}세카이검색 음악 꽃을노래하다":
        await message.channel.send(embed=GN)

    #밤을 달리다
    if message.content == f"{prefix}세카이검색 음악 밤을 달리다" or message.content == f"{prefix}세카이검색 음악 밤을달리다":
        await message.channel.send(embed=BD)

    #유령도쿄
    if message.content == f"{prefix}세카이검색 음악 유령도쿄" or message.content == f"{prefix}세카이검색 음악 유령 도쿄":
        await message.channel.send(embed=GT)

    #시네마
    if message.content == f"{prefix}세카이검색 음악 시네마":
        await message.channel.send(embed=cinema)

    #KING
    if message.content == f"{prefix}세카이검색 음악 KING" or message.content == f"{prefix}세카이검색 음악 king" or message.content == f"{prefix}세카이검색 음악 킹":
        await message.channel.send(embed=king)

    #사랑의 마테리얼
    if message.content == f"{prefix}세카이검색 음악 사랑의 마테리얼" or message.content == f"{prefix}세카이검색 음악 사랑의마테리얼":
        await message.channel.send(embed=AM)

    #가지마
    if message.content == f"{prefix}세카이검색 음악 가지마" or message.content == f"{prefix}세카이검색 음악 이카나이데":
        await message.channel.send(embed=IND)

    #로미오와 신데렐라
    if message.content == f"{prefix}세카이검색 음악 로미오와 신데렐라" or message.content == f"{prefix}세카이검색 음악 로미오와신데렐라":
        await message.channel.send(embed=RC)

    #거품 미래
    if message.content == f"{prefix}세카이검색 음악 거품미래" or message.content == f"{prefix}세카이검색 음악 거품 미래":
        await message.channel.send(embed=GM)

    #터무니없는 원더즈
    if message.content == f"{prefix}세카이검색 음악 터무니없는 원더즈" or message.content == f"{prefix}세카이검색 음악 터무니없는원더즈" or message.content == f"{prefix}세카이검색 음악 톤데모원더즈" or message.content == f"{prefix}세카이검색 음악 톤데모 원더즈":
        await message.channel.send(embed=TW)

    #연주하여 밝히는 하늘
    if message.content == f"{prefix}세카이검색 음악 연주하여 밝히는 하늘" or message.content == f"{prefix}세카이검색 음악 연주하여밝히는하늘":
        await message.channel.send(embed=YBH)

    #트래픽 잼
    if message.content == f"{prefix}세카이검색 음악 트래픽 잼" or message.content == f"{prefix}세카이검색 음악 트래픽잼" or message.content == f"{prefix}세카이검색 음악 Traffic Jam" or message.content == f"{prefix}세카이검색 음악 traffic jam" or message.content == f"{prefix}세카이검색 음악 trafficjam" or message.content == f"{prefix}세카이검색 음악 TrafficJam":
        await message.channel.send(embed=TJ)

    #프롬 도쿄
    if message.content == f"{prefix}세카이검색 음악 프롬 도쿄" or message.content == f"{prefix}세카이검색 음악 프롬도쿄" or message.content == f"{prefix}세카이검색 음악 프럼 도쿄" or message.content == f"{prefix}세카이검색 음악 프럼도쿄" or message.content == f"{prefix}세카이검색 음악 From Tokyo" or message.content == f"{prefix}세카이검색 음악 from tokyo" or message.content == f"{prefix}세카이검색 음악 FromTokyo" or message.content == f"{prefix}세카이검색 음악 fromtokyo":
        await message.channel.send(embed=FT)

    #Beat Eater
    if message.content == f"{prefix}세카이검색 음악 Beat Eater" or message.content == f"{prefix}세카이검색 음악 beat eater" or message.content == f"{prefix}세카이검색 음악 BeatEater" or message.content == f"{prefix}세카이검색 음악 beateater" or message.content == f"{prefix}세카이검색 음악 비트 이터" or message.content == f"{prefix}세카이검색 음악 비트이터" or message.content == f"{prefix}세카이검색 음악 비트 이더" or message.content == f"{prefix}세카이검색 음악 비트이더":
        await message.channel.send(embed=BE)

    #육조 년과 하룻밤 이야기
    if message.content == f"{prefix}세카이검색 음악 육조 년과 하룻밤 이야기" or message.content == f"{prefix}세카이검색 음악 육조년과 하룻밤 이야기" or message.content == f"{prefix}세카이검색 음악 육조년과하룻밤이야기":
        await message.channel.send(embed=YNHI)

    #지구 최후의 고백을
    if message.content == f"{prefix}세카이검색 음악 지구 최후의 고백을" or message.content == f"{prefix}세카이검색 음악 지구최후의고백을":
        await message.channel.send(embed=JCJ)

    #비터 초코 데코레이션
    if message.content == f"{prefix}세카이검색 음악 비터 초코 데코레이션" or message.content == f"{prefix}세카이검색 음악 비터초코 데코레이션" or message.content == f"{prefix}세카이검색 음악 비터초코데코레이션":
        await message.channel.send(embed=BCD)

    #그랬지!!
    if message.content == f"{prefix}세카이검색 음악 그랬지!!"or message.content == f"{prefix}세카이검색 음악 그랬지!" or message.content == f"{prefix}세카이검색 음악 그랬지" or message.content == f"{prefix}세카이검색 음악 그랫지!!" or message.content == f"{prefix}세카이검색 음악 그랫지!" or message.content == f"{prefix}세카이검색 음악 그랫지":
        await message.channel.send(embed=SDT)

    #아지랑이 데이즈
    if message.content == f"{prefix}세카이검색 음악 카게로우 데이즈" or message.content == f"{prefix}세카이검색 음악 카게로우데이즈" or message.content == f"{prefix}세카이검색 음악 아지랑이 데이즈" or message.content == f"{prefix}세카이검색 음악 아지랑이데이즈":
        await message.channel.send(embed=KRD)

    #아이스 드롭
    if message.content == f"{prefix}세카이검색 음악 아이스 드롭" or message.content == f"{prefix}세카이검색 음악 아이스드롭" or message.content == f"{prefix}세카이검색 음악 Ice Drop" or message.content == f"{prefix}세카이검색 음악 IceDrop" or message.content == f"{prefix}세카이검색 음악 ice drop" or message.content == f"{prefix}세카이검색 음악 icedrop":
        await message.channel.send(embed=ID)

    #Glory Steady Go!
    if message.content == f"{prefix}세카이검색 음악 Glory Steady Go!" or message.content == f"{prefix}세카이검색 음악 GlorySteadyGo!" or message.content == f"{prefix}세카이검색 음악 glory steady go!" or message.content == f"{prefix}세카이검색 음악 glorysteadygo!" or message.content == f"{prefix}세카이검색 음악 Glory Steady Go" or message.content == f"{prefix}세카이검색 음악 GlorySteadyGo" or message.content == f"{prefix}세카이검색 음악 glory steady go" or message.content == f"{prefix}세카이검색 음악 glorysteadygo" or message.content == f"{prefix}세카이검색 음악 글로리 스테디 고!" or message.content == f"{prefix}세카이검색 음악 글로리스테디고!" or message.content == f"{prefix}세카이검색 음악 글로리 스테디 고" or message.content == f"{prefix}세카이검색 음악 글로리스테디고":
        await message.channel.send(embed=GSG)

    #칠드런 레코드
    if message.content == f"{prefix}세카이검색 음악 칠드런 레코드" or  message.content == f"{prefix}세카이검색 음악 칠드런레코드":
        await message.channel.send(embed=CR)

    #magic number
    if message.content == f"{prefix}세카이검색 음악 magic number" or message.content == f"{prefix}세카이검색 음악 Magic Number" or message.content == f"{prefix}세카이검색 음악 MAGIC NUMBER" or message.content == f"{prefix}세카이검색 음악 매직 넘버" or message.content == f"{prefix}세카이검색 음악 매직넘버":
        await message.channel.send(embed=MN)

    #유성의 펄스
    if message.content == f"{prefix}세카이검색 음악 유성의 펄스" or message.content == f"{prefix}세카이검색 음악 유성의펄스":
        await message.channel.send(embed=YP)


client.run(os.environ['token'])
