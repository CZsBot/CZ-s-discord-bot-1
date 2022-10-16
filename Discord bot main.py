#token ='stfu7YBojWfnWBY'

import discord
from discord import File
import pickle
import random
import csv
import requests
from datetime import date, datetime
import re

Dict_user_id = {"#92JCYPYGL" : ["#92JCYPYGL", "cool ghost", 738253033703473293], 
                "#9PUY8P28J" : ["#9PUY8P28J", "A.B.H.A.Y", 713067746761375846],
                "#9UQR0998R" : ["#9UQR0998R", "Loner Guy", 758664468925513739],
                "#8G089R9CL" : ["#8G089R9CL", "Sheel", 738253033703473293],
                "#89VJVYU9V" : ["#89VJVYU9V", "NP", 0],
                "#YRPRYJRG9" : ["#YRPRYJRG9", "Blackcat", 0], 
                "#LLGRQUJJ2" : ["#LLGRQUJJ2", "Brian", 909913793189003344],
                "#990LP89LQ" : ["#990LP89LQ", "Pavnaj@114", 0],
                "#8JRCYPU0Y" : ["#8JRCYPU0Y", "cool zombie",764850061561561088],
                "#YV0JUUJ0P" : ["#YV0JUUJ0P", "nlp", 0],
                "#80CLYUU8C" : ["#80CLYUU8C", "ŔITVIK", 483606784305659924],
                "#LV8GJJGLJ" : ["#LV8GJJGLJ", "Gero", 872916750994378843],
                "#90PJYG909" : ["#90PJYG909", "STROM BRAKER",864550626557558814],
                "#RV0LUPG0"  : ["#RV0LUPG0", "VIBHAV",0],
                "#9RQVPGVGG" : ["#9RQVPGVGG", "troops doner",864550626557558814],
                "#9Y0QYPQ0Y" : ["#9Y0QYPQ0Y", "Ûfføŕđ Ďū ŤĞ", 713067746761375846],
                "#9VQYYR0CJ" : ["#9VQYYR0CJ", "Kashi",1029669537945239562],
                "#LVR0C2Y8C" : ["#LVR0C2Y8C", "RAHUL 1",0],
                "#99YUQYCL2" : ["#99YUQYCL2", "Sahil0511",740505920886407228],
                "#LPYURPY8P" : ["#LPYURPY8P", "STROM_SHADOW_7",864550626557558814],
                "#YGL0J22QQ" : ["#YGL0J22QQ", "Cool Zombie 992",764850061561561088],
                "#LU2PCR2G9" : ["#LU2PCR2G9", "Avtar",864550626557558814],
                "#LYGY8YVRP" : ["#LYGY8YVRP", "Heman",1005826110258421921],
                "#UYPLYPJR"  : ["#UYPLYPJR", "Master Abhishek",740505920886407228],
                "#PVLV2CLYC" : ["#PVLV2CLYC", "Calibur_OP",901860387853566003],
                "#L9P2UL88J" : ["#L9P2UL88J", "Tommy",0],
                "#9RQ8UUGC2" : ["#9RQ8UUGC2", "Deadpool",0],
                "#9PYC9PLUV" : ["#9PYC9PLUV", "SWAPNIL",0],
                "#9GJCJRLQR" : ["#9GJCJRLQR", "Ghost Rider",738253033703473293],
                "#2QCQCPYPC" : ["#2QCQCPYPC", "yo yo honey",601810849752940576],
                "#PQU0Y288G" : ["#PQU0Y288G", "Optimus prime",738253033703473293],
                "#PC09QV09V" : ["#PC09QV09V", "cool virus",738253033703473293],
                "#2Q2UCRJ98" : ["#2Q2UCRJ98", "Zotumn",0],
                "#LJC8YCC92" : ["#LJC8YCC92", "Lilly",0],
                "#QQVQ89R0Q" : ["#QQVQ89R0Q", "larry",996406447212609558],
                "#2PYUY908Q" : ["#2PYUY908Q", "Yornewt",982668513351184507],
                "#Q22GPLPVL" : ["#Q22GPLPVL", "Cool corona",764850061561561088],
                "#Q8RC82YCP" : ["#Q8RC82YCP", "Beans",569313016169103370],
                "#P92C08U2L" : ["#P92C08U2L", "Cool Zombie 99",764850061561561088],
                "#YP29G82VY" : ["#YP29G82VY", "Supriy",0],
                "#PGCGG898Y" : ["#PGCGG898Y", "GAMARICKI",0],
                "#2J89ULQRU" : ["#2J89ULQRU", "HELLCODER",0],
                "#28QG9JUUR" : ["#28QG9JUUR", "KHACHEDU ROXX",601810849752940576],
                "#9VUQPVCJC" : ["#9VUQPVCJC", "HYDRA",0],
                "#PV2P89LPP" : ["#PV2P89LPP", "COOL ZOMBIE 4",764850061561561088],
                "#QUYRJ9U98" : ["#QUYRJ9U98", "Gero 2.O",872916750994378843],
                "#8GG9VG9VY" : ["#8GG9VG9VY", "•§•ᎡΣᎥᎠ•§•",0],
                "#P8GP9PULC" : ["#P8GP9PULC", "cool tantrik",738253033703473293],
                "#QUR9QQUCU" : ["#QUR9QQUCU", "CZ is bugged!",764850061561561088],
                "#9J89U02QV" : ["#9J89U02QV", "cool delusion",738253033703473293],
                "#PRUC9PQGR" : ["#PRUC9PQGR", "abhay",758664468925513739],
                "#YRPRYJRG9" : ["#YRPRYJRG9", "Blackcat",0],
                "#8GG9VG9VY" : ["#8GG9VG9VY", "•§•ᎡΣᎥᎠ•§•",0],
                "#YV0JUUJ0P" : ["#YV0JUUJ0P", "nlp",0]}

'''Dict_loot_data =   {738253033703473293 : ["#92JCYPYGL", 'cool ghost', 738253033703473293],
                    713067746761375846 : ["#9PUY8P28J", 'A.B.H.A.Y', 713067746761375846],
                    758664468925513739 : ["#9UQR0998R", 'Loner Guy', 758664468925513739],
                    738253033703473293 : ["#8G089R9CL", 'Sheel', 738253033703473293],    
                    909913793189003344 : ["#LLGRQUJJ2", 'Brian', 909913793189003344],    
                    764850061561561088 : ["#8JRCYPU0Y", 'cool zombie', 764850061561561088],
                    483606784305659924 : ["#80CLYUU8C", 'ŔITVIK', 483606784305659924],
                    872916750994378843 : ["#LV8GJJGLJ", 'Gero', 872916750994378843],
                    864550626557558814 : ["#90PJYG909", 'STROM BRAKER', 864550626557558814],
                    864550626557558814 : ["#9RQVPGVGG", 'troops doner', 864550626557558814],
                    713067746761375846 : ["#9Y0QYPQ0Y", 'Ûfføŕđ Ďū ŤĞ', 713067746761375846],
                    1029669537945239562 : ["#9VQYYR0CJ", 'Kashi', 1029669537945239562],
                    740505920886407228 : ["#99YUQYCL2", 'Sahil0511', 740505920886407228],
                    864550626557558814 : ["#LPYURPY8P", 'STROM_SHADOW_7', 864550626557558814],
                    764850061561561088 : ["#YGL0J22QQ", 'Cool Zombie 992', 764850061561561088],
                    864550626557558814 : ["#LU2PCR2G9", 'Avtar', 864550626557558814],
                    1005826110258421921 : ["#LYGY8YVRP", 'Heman', 1005826110258421921],
                    740505920886407228 : ["#UYPLYPJR", 'Master Abhishek', 740505920886407228],
                    901860387853566003 : ["#PVLV2CLYC", 'Calibur_OP', 901860387853566003],
                    738253033703473293 : ["#9GJCJRLQR", 'Ghost Rider', 738253033703473293],
                    601810849752940576 : ["#2QCQCPYPC", 'yo yo honey', 601810849752940576],
                    738253033703473293 : ["#PQU0Y288G", 'Optimus prime', 738253033703473293],
                    738253033703473293 : ["#PC09QV09V", 'cool virus', 738253033703473293],
                    996406447212609558 : ["#QQVQ89R0Q", 'larry', 996406447212609558],
                    982668513351184507 : ["#2PYUY908Q", 'Yornewt', 982668513351184507],
                    764850061561561088 : ["#Q22GPLPVL", 'Cool corona', 764850061561561088],
                    569313016169103370 : ["#Q8RC82YCP", 'Beans', 569313016169103370],
                    764850061561561088 : ["#P92C08U2L", 'Cool Zombie 99', 764850061561561088],
                    601810849752940576 : ["#28QG9JUUR", 'KHACHEDU ROXX', 601810849752940576],
                    764850061561561088 : ["#PV2P89LPP", 'COOL ZOMBIE 4', 764850061561561088],
                    872916750994378843 : ["#QUYRJ9U98", 'Gero 2.O', 872916750994378843],
                    738253033703473293 : ["#P8GP9PULC", 'cool tantrik', 738253033703473293],
                    764850061561561088 : ["#QUR9QQUCU", 'CZ is bugged!', 764850061561561088],
                    738253033703473293 : ["#9J89U02QV", 'cool delusion', 738253033703473293],
                    758664468925513739 : ["#PRUC9PQGR", 'abhay', 758664468925513739]}

'''

Dict_loot_data =   {738253033703473293 : ["#92JCYPYGL", 'cool ghost', 738253033703473293],
                    713067746761375846 : ["#9PUY8P28J", 'A.B.H.A.Y', 713067746761375846],
                    758664468925513739 : ["#9UQR0998R", 'Loner Guy', 758664468925513739],
                    909913793189003344 : ["#LLGRQUJJ2", 'Brian', 909913793189003344],    
                    764850061561561088 : ["#8JRCYPU0Y", 'cool zombie', 764850061561561088],
                    483606784305659924 : ["#80CLYUU8C", 'ŔITVIK', 483606784305659924],
                    872916750994378843 : ["#LV8GJJGLJ", 'Gero', 872916750994378843],
                    1029669537945239562 : ["#9VQYYR0CJ", 'Kashi', 1029669537945239562],
                    864550626557558814 : ["#LU2PCR2G9", 'Avtar', 864550626557558814],
                    1005826110258421921 : ["#LYGY8YVRP", 'Heman', 1005826110258421921],
                    740505920886407228 : ["#UYPLYPJR", 'Master Abhishek', 740505920886407228],
                    901860387853566003 : ["#PVLV2CLYC", 'Calibur_OP', 901860387853566003],
                    601810849752940576 : ["#2QCQCPYPC", 'yo yo honey', 601810849752940576],
                    996406447212609558 : ["#QQVQ89R0Q", 'larry', 996406447212609558],
                    982668513351184507 : ["#2PYUY908Q", 'Yornewt', 982668513351184507],
                    569313016169103370 : ["#Q8RC82YCP", 'Beans', 569313016169103370],
                    }




f2 = open("Rax Tower Raids Info.csv", "w", newline='')
f_csv = csv.writer(f2)
now = date.today()
d2 = now.strftime("%d th %B , %Y")
f_csv.writerow([str(d2)])
f_csv.writerow([])
f_csv.writerow(["Player Tag", "Name", "Total Attacks", "Attack Limit", "Bonus Attack", "Capital Gold Looted"])
f_csv.writerow([])
f2.close()


head = {
  "Accept":
  '*/*',
  "authorization":
  "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjhiOGY1YTA2LTZjOWQtNDA2NC04YThjLTMyMTYyZDQxNzllNiIsImlhdCI6MTY2NTQyOTc2NCwic3ViIjoiZGV2ZWxvcGVyLzc1YzlhMTE5LTJmNTEtODhhYi0wZWE1LTA5ZTIwMDMxM2M0MiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjQ5LjM2LjE3OS42NyIsIjQ1Ljc5LjIxOC43OSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.f0AfQ6bwh_bosfs3gzNfNhXQEWxA2S0wzTCq98l17bgcDs6tU3azzHJHVvq61DNDfoBx4YNGmQJe9tAzJ3Rmeg"
}

def get_clan():
  L = []
  Lx = []
  resp = requests.get(
      "https://cocproxy.royaleapi.dev/v1/clans/%23RJJ0LP0Y/members", headers=head)
  u_j = resp.json()
  for i in u_j["items"]:
     #print("\""+ i["tag"] + "\" : [\"" + i["tag"] +"\", \""+ i["name"] + "\",]")
     L.append(i["tag"])
     Lx.append(i["name"])
  return L, Lx

def get_cap_log(var1 = 0):
  L2 = []
  List_players= []
  Dict_info = {}
  resp = requests.get(
      "https://cocproxy.royaleapi.dev/v1/clans/%23RJJ0LP0Y/capitalraidseasons", headers=head)
  u_j = resp.json()

  l_cap = u_j["items"]
  
  #for i in u_j["items"][0]:
  #  print(i)
  #print(l_cap[0]["startTime"])

  if len(l_cap) - var1 < 20 or var1 == 0:
    List_players = u_j["items"][0]["members"]
    for i in List_players:
        for j in i:
            L2.append(i[j])
        Dict_info[str(i["tag"])] = L2
        L2 = []
    variable = len(l_cap)
  #elif var1 == 0:
  #  List_players = u_j["items"][-1]["members"]
  else:
    #List_players = u_j["items"][-1*(var1 + 1)]["members"]
    with open("file_record.dat", "rb") as f1:
        try:
            while True:
                dict123 = pickle.load(f1)
                for i in dict123:
                    print(i)
                if dict123["date"] ==  len(l_cap) - var1:
                    Dict_info = dict123
                    variable = len(dict123)
        except EOFError:
            pass

  

  #for i in Dict_info:
  #  print(Dict_info[i])
  return Dict_info, variable



def get_player(tag = "#92JCYPYGL"):
  link1 = "https://cocproxy.royaleapi.dev/v1/players/%23" + tag[1:]
  resp = requests.get(
      link1, headers=head)
  u_j = resp.json()
  List_user = [tag, u_j["achievements"][5]["value"], u_j["achievements"][6]["value"], u_j["achievements"][16]["value"]]  
  return List_user



def send_csv(int1 = 0):

    f2 = open("C:\\Users\\WCD\\Desktop\\Final\\Discord bot testing\\Rax Tower Raids Info.csv", "w", newline='')
    f_csv = csv.writer(f2)
    now = date.today()
    d2 = now.strftime("%d th %B , %Y")
    f_csv.writerow([str(d2)])
    f_csv.writerow([])
    f_csv.writerow(["Player Tag", "Name", "Total Attacks", "Attack Limit", "Bonus Attack", "Capital Gold Looted"])
    f_csv.writerow([])
    f2.close()

    with open("C:\\Users\\WCD\\Desktop\\Final\\Discord bot testing\\Rax Tower Raids Info.csv", "a", newline = '') as f1:
        dict_final, int_w = get_cap_log(int1)
        L, Lx = get_clan()        
        f_csv = csv.writer(f1)
        for i in range(len(L)):
            try:
                L_input = dict_final[L[i]]
                try:
                    f_csv.writerow(L_input)
                except UnicodeEncodeError:
                    str1 = dict_final[L[i]][1]
                    str1 = str1.encode('utf-8')
                    List_uni = [L[i], str1] + dict_final[L[i]][2:]
                    f_csv.writerow(List_uni)
            
            except KeyError:

                try:
                    f_csv.writerow([L[i], Lx[i], 0, 0, 0, 0])
                except UnicodeEncodeError:
                    str1 = Lx[i]
                    str1 = str1.encode('utf-8')
                    List_uni = [L[i], str1] + [0,0,0,0]
                    f_csv.writerow(List_uni)
            f1.flush()
        f_csv.writerow([])
        f_csv.writerow(["Total Members:", str(len(L))])
        f_csv.writerow([])
    f1.close()



def ded_fn(int1 = 0):
    List_ded = []
    dict_final, int_w = get_cap_log(int1)
    L, Lx = get_clan() 
    for i in range(len(L)):
        if L[i] not in dict_final:
            try:
                List_ded.append([Lx[i], 0])
            except UnicodeEncodeError:
                str1 = dict_final[L[i]][1]
                str1 = str1.encode('utf-8')
                List_ded.append([str1, 0])
        elif dict_final[L[i]][2] < 5:
            try:
                List_ded.append([Lx[i], dict_final[L[i]][2]])
            except UnicodeEncodeError:
                str1 = dict_final[L[i]][1]
                str1 = str1.encode('utf-8')
                List_ded.append([str1, dict_final(L[i])[2]])
    List_ded = Sort(List_ded)
    return List_ded

'''def cz_sort(List_g):
    Lt = []
    Lt.append(List_g[0])
    Len = len(List_g)
    for i in range(1, Len):
        for j in range(len(Lt)):
            if List_g[i][1] <= Lt[j][1]:
                Lt.insert(j, List_g[i])'''


List_aboose = ['fuck', 'stfu', 'bsdk', 'kys', 'kill you', 'bitch', 'did i ask']

def Sort(sub_li):
    l = len(sub_li)
    for i in range(l):
        for j in range(l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li


def List_noob():
    L_n = []
    D_n, int_w = get_cap_log()
    for i in D_n:
        if D_n[i][2] < 6:
            try:
                if Dict_user_id[i][2] != 0:
                    L_n.append(["<@" + str(Dict_user_id[i][2])+ ">", D_n[i][2], Dict_user_id[i][1]])
                else:
                    L_n.append(["<@" + str(Dict_user_id[i][1])+ ">", D_n[i][2], Dict_user_id[i][1]])

            except KeyError:
                L_n.append(["<@" + str(D_n[i][1])+ ">", D_n[i][2], D_n[i][1]])
    return L_n



TOKEN = 'MTAyOTUwODgyNDU5MzM1MDc1Nw.GpG5Yv.OYczVf5INmzi3ynRBdBgKQxa3J47YBojWfnWBY'




client = discord.Client(intents=discord.Intents.all())
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    username =str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    ID1 = str(message.author.id)
    Cap_sup = ['764850061561561088','738253033703473293','872916750994378843','713067746761375846']
    List_emotes = ['<:pepe_pray:986293546627788911>', '🔥', '😈','😂', '🤓','☠️', '<:denk_troll:985819182094491649>',"💀", "<:woah:1002943901612650579>", "🗿", ":clown:", "<:forget_it:986294620805791774>", "<:goofy_ahh:985823480341749770>", "<:hehehehaw:986323343823212615>", "<:ok:986291991799271444>", "<:wot:976469711103619152>", "🫡","🤝","👍", "🤡", "<:trolled_asf:986294543991336980>","<:troll:985818585307938826>", "<:no_bully:986290639547289600>"]

    print(f'{username}: ({user_message}) ({channel})')
    if message.author == client.user:
       return
    if message.channel.name == "cz-bot":
        if user_message.lower == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See ya\' {username}!')
            return
        elif user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == '!random':
            resp = f'this is it'
            await message.channel.send(resp)
            return

#        elif user_message.lower() == '!ded':
#            List_dedbot = ded_fn()
#            embedVar = discord.Embed(title="Available commands", color=0x00FFFF)
#            for i in range(len(List_dedbot)):
#                embedVar.add_field(name=str(List_dedbot[i][0]), value=str(List_dedbot[i][1]) + " attacks done in raids", inline=False)
#            await message.channel.send(embed=embedVar)
#            return

        elif user_message.lower()[:4] == '!ded':
            List_csv = user_message.lower().split()
            if len(List_csv) == 1:
                List_dedbot = ded_fn()
                if len(List_dedbot) <= 25:
                    embedVar = discord.Embed(title="Following players didn't complete their attacks", color=0x00FFFF)
                    for i in range(len(List_dedbot)):
                        embedVar.add_field(name=str(List_dedbot[i][0]), value=str(List_dedbot[i][1]) + " attacks done in raids", inline=False)
                    await message.channel.send(embed=embedVar)
                    return
                else:
                    embedVar = discord.Embed(title="Following players didn't complete their attacks", color=0x00FFFF)
                    for i in range(25):
                        embedVar.add_field(name=str(List_dedbot[i][0]), value=str(List_dedbot[i][1]) + " attacks done in raids", inline=False)
                    await message.channel.send(embed=embedVar) 
                    embedVar = discord.Embed(title="  ", color=0x00FFFF)                                   
                    for i in range(25, len(List_dedbot)):
                        embedVar.add_field(name=str(List_dedbot[i][0]), value=str(List_dedbot[i][1]) + " attacks done in raids", inline=False)
                    await message.channel.send(embed=embedVar)
                    return

            elif len(List_csv) == 2:
                int1 = int(List_csv[1])
                if int1 <0:
                    await message.channel.send("Enter positive values!")
                    return
                else:
                    List_dedbot = ded_fn(int1)
                    embedVar = discord.Embed(title="Available commands", color=0x00FFFF)
                    for i in range(len(List_dedbot)):
                        embedVar.add_field(name=str(List_dedbot[i][0]), value=str(List_dedbot[i][1]) + " attacks done in raids", inline=False)
                    await message.channel.send(embed=embedVar)
                    return
        
        elif user_message.lower() == '!cz_help':
            embedVar = discord.Embed(title="Available commands", color=0x00ff00) #embedVar = discord.Embed(title="Available commands", description="Desc", color=0x00ff00)
            embedVar.add_field(name="!cz_help", value="Lists all commands", inline=False)
            embedVar.add_field(name="!ded", value="Lists all the members who didn't use all attacks in raids", inline=False)
            embedVar.add_field(name="!ded <How many weeks before (positive int)>", value="Lists all the members who didn't use all attacks in raids of specified weekend", inline=False)
            embedVar.add_field(name="!clan_csv", value="Provides a csv file for raids", inline=False)
            embedVar.add_field(name="!clan_csv <How many weeks before (positive int)>", value="Provides a csv file for the raids of specified week", inline=False)
            embedVar.add_field(name="!cz_tag", value="Tags players who havn't completed their raid attacks. \nNote: Only CZ, CG, Gero, and Abhay can use this!", inline=False)

            
            await message.channel.send(embed=embedVar)
            return
        
        elif user_message.lower()[:9] == '!clan_csv':
            List_csv = user_message.lower().split()
            if len(List_csv) == 1:
                send_csv()
                await message.channel.send(file=File('C:\\Users\\WCD\\Desktop\\Final\\Discord bot testing\\Rax Tower Raids Info.csv'))
                return
            elif len(List_csv) == 2:
                
                int1 = int(List_csv[1])
                if int1 <0:
                    await message.channel.send("Enter positive values!")
                    return
                else:
                    send_csv(int1)
                    await message.channel.send(file=File('C:\\Users\\WCD\\Desktop\\Final\\Discord bot testing\\Rax Tower Raids Info.csv'))
                    return
            
            #await message.channel.send(file=File('C:\\Users\\WCD\\Desktop\\Final\\Discord bot testing\\Rax Tower Raids Info.csv'))
            #return

        elif user_message.lower() == '!cz_tag':
            if str(ID1) in Cap_sup:
                L_n = List_noob()
                string1 = 'Following players haven\'t used all their attacks in raids yet \n \n'
                for i in L_n:
                    string1 += "➡️" + str(i[0]) + " has " + str(6 - i[1]) + " attacks left on " + i[2] + "! \n"
                await message.channel.send(string1)
                return
            else:
                await message.channel.send("Sorry <@" + str(ID1) + ">! You cannot use this command. Please contact <@764850061561561088> to know more" )
                return




        elif user_message.lower() == 'cz, it\'s time to update!' and ID1 in [str(159985870458322944), str(764850061561561088)]:
            with open("file_record.dat", "ab") as f1:
                try:
                    dict_record, var123 = get_cap_log()
                    dict_record["date"] = var123
                    pickle.dump(dict_record, f1)
                    f1.close()
                except EOFError:
                    pass

        elif user_message.lower()[:9] == '!cz_start':
            l1 = user_message.lower().split()
            now = datetime.now()
            now = str(now)
            List_date_time = re.split("-| |:", now)
            time_format = str(List_date_time[2]) + "/" + str(List_date_time[1]) + "/" +str(List_date_time[0]) + ", at " + str(List_date_time[3]) + ":" + str(List_date_time[4]) + ":" + str(List_date_time[5][:2])
            if len(l1) == 1:  
                try:
                    tag1 = Dict_loot_data[int(ID1)][0]
                    L1 = get_player(tag1)
                    print(tag1, L1)
                    if 2000000000 in L1:
                        await message.channel.send("<@" + str(ID1) + ">, sorry...but you have already capped out on one or more of your achievements, so I can't track you")
                        return
                    else:
                        with open("Loot Record.dat", "ab") as f1:
                            pickle.dump(L1, f1)
                        await message.channel.send("Your resources are being recorded from " + time_format + ", <@" + str(ID1) + ">!")
                        return
                except KeyError:
                    await message.channel.send("<@" + str(ID1) + ">, provide your tag as well!")
                    return

                
            elif len(l1) == 2:
                L1 = get_player(l1[1])
                print(l1[1], L1)
                if 2000000000 in L1:
                    await message.channel.send("<@" + str(ID1) + ">, sorry...but the account is already capped out on one or more of your achievements, so I can't track you")
                    return
                else:
                    with open("Loot Record.dat", "ab") as f1:
                        pickle.dump(L1, f1)
                    await message.channel.send("Your resources are being recorded from " + time_format + ", <@" + str(ID1) + ">!")
                    return

        elif user_message.lower()[:7] == '!cz_end':
            l1 = user_message.lower().split()
            if len(l1) == 1:  
                try:
                    tag1 = Dict_loot_data[int(ID1)][0]
                except KeyError:
                    await message.channel.send("<@" + str(ID1) + ">, provide your tag as well!")
                    return
                L1 = get_player(tag1)
                print("List api", L1)

                with open("Loot Record.dat", "rb+") as f1:
                    try:
                        while True:
                            print(1)
                            posi = f1.tell()
                            Lx1 = pickle.load(f1)
                            print(Lx1)
                            if Lx1[0] == tag1:
                                f1.seek(posi)
                                pickle.dump('', f1)
                                await message.channel.send(str(L1) + "   "+ str(Lx1))
                                return
                    except EOFError:        
                        await message.channel.send("<@" + str(ID1) + ">, you\'re not being recorded!")
                        return

                    
            elif len(l1) == 2:
                L1 = get_player(l1[1])
                print("List api", L1)
                with open("Loot Record.dat", "ab+") as f1:
                    try:
                        f1.seek(0)
                        while True:
                            posi = f1.tell()
                            print("loop:", posi)
                            Lx1 = pickle.load(f1)
                            print(str(posi), Lx1)
                            if str(Lx1[0]).lower() == l1[1].lower():
                                f1.seek(0)
                                print("if statement", posi)
                                pickle.dump([1,1,1,1], f1)
                                embedVar = discord.Embed(title="Amount looted since recording started", color=0x00ff00) #embedVar = discord.Embed(title="Available commands", description="Desc", color=0x00ff00)
                                embedVar.add_field(name="Gold", value=str(L1[1]-Lx1[1]), inline=False)
                                embedVar.add_field(name="ELixir", value=str(L1[2]-Lx1[2]), inline=False)
                                embedVar.add_field(name="Dark Elixir", value=str(L1[3]-Lx1[3]), inline=False)
            
                                await message.channel.send(embed=embedVar)
                                return
                    except EOFError:        
                        await message.channel.send("<@" + str(ID1) + ">, you\'re not being recorded!")
                        return


    if True:
        
        for i in List_aboose:
            if i in user_message.lower():
                x1 = random.randint(0, len(List_emotes) - 1)
                await message.channel.send("Stfu <@" + str(ID1) + "> " + str(List_emotes[x1]))
                return
            else:
                pass
        for i in List_emotes:
            if i in user_message.lower():
                x1 = random.randint(0, len(List_emotes) - 1)
                x2 = random.randint(0,1)
                if x2//2 == x2/2:
                    await message.channel.send(str(List_emotes[x1]))
                    return
                else:
                    pass
client.run(TOKEN)




'''elif user_message.lower() == '!clan_csv':
            send_csv()
            await message.channel.send(file=File('C:\\Users\\WCD\\Desktop\\Final\\Discord bot testing\\Rax Tower Raids Info.csv'))
            return'''
