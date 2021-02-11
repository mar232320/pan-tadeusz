import discord
from discord.ext import commands
import requests
from requests import *

description = "bot cytujacy pana tadeusza"

bot = commands.Bot(command_prefix = "-", description=description)

@bot.event
async def on_voice_state_update(member, before, after):
    logchannel = bot.get_channel(793162324478394368)  #id kanalu do logow
    if before.channel == None and after.channel != None:
        await logchannel.send(str(member) + " dolaczyl do kanalu glosowego " + str(after.channel) + " na serwerze " + str(member.guild.name))
    if before.channel != None and after.channel == None:
        await logchannel.send(str(member) + " wyszedl z kanalu glosowego " + str(before.channel) + " na serwerze " + str(member.guild.name))
    if before.channel != None and after.channel != None:
        if before.channel != after.channel:
            await logchannel.send(str(member) + " przeniosl sie z kanalu " + str(before.channel) + " na " + str(afer.channel) + " na serwerze " + str(member.guild.name))

@bot.command(description="wysyla customowy tekst")
async def custom(ctx, *, content):
    await ctx.send(content)       
       
@bot.command(brief="cytuje inwokacje z pana tadeusza", description="cytuje inwokacje z pana tadeusza")    
async def inwokacja(ctx):
    await ctx.send("Litwo! Ojczyzno moja! ty jesteś jak zdrowie \nIle cię trzeba cenić, ten tylko się dowie \nKto cię stracił. Dziś piękność twą w całej ozdobie \nWidzę i opisuję, bo tęsknię po tobie. \nPanno święta, co Jasnej bronisz Częstochowy \nI w Ostrej świecisz Bramie! Ty, co gród zamkowy \nNowogródzki ochraniasz z jego wiernym ludem!  \nJak mnie dziecko do zdrowia powróciłaś cudem, \n(Gdy od płaczącej matki pod Twoję opiekę \nOfiarowany, martwą podniosłem powiekę \nI zaraz mogłem pieszo do Twych świątyń progu \nIść za wrócone życie podziękować Bogu), \nTak nas powrócisz cudem na Ojczyzny łono. \nTymczasem przenoś moję duszę utęsknioną \nDo tych pagórków leśnych, do tych łąk zielonych, \nSzeroko nad błękitnym Niemnem rozciągnionych; \nDo tych pól malowanych zbożem rozmaitem, \nWyzłacanych pszenicą, posrebrzanych żytem; \nGdzie bursztynowy świerzop, gryka jak śnieg biała, \nGdzie panieńskim rumieńcem dzięcielina pała, \nA wszystko przepasane jakby wstęgą, miedzą \nZieloną, na niej z rzadka ciche grusze siedzą")
    
@bot.command()
async def ksiega13(ctx):
    with open("ksiega13.txt") as file:
        lines = file.readlines()
        for line in lines:
            await ctx.send(line)
    
@bot.command()
async def pantadeusz(ctx, ksiega):
    if ksiega == None:
        with open("ksiega1.txt") as file:
            lines = file.readlines()
            for line in lines:
                await ctx.send(line)
        with open("ksiega2.txt") as file:
            lines = file.readlines()
            for line in lines:
                await ctx.send(line)        
    if ksiega == "ksiega1":    
        with open("ksiega1.txt") as file:
            lines = file.readlines()
            for line in lines:
                await ctx.send(line)
    if ksiega == "ksiega2":    
        with open("ksiega2.txt") as file:
            lines = file.readlines()
            for line in lines:
                await ctx.send(line)            
 
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
 
@bot.command()
async def purge(ctx, amount):
    await ctx.channel.purge(limit=int(amount))   
       
@bot.command()
async def ruletka(ctx):
    hisrandomint = random.randint(int(1),int(6))
    targetrandomint = random.randint(int(1),int(6))
    if int(hisrandomint) == int(targetrandomint):
        await ctx.guild.ban(ctx.message.author, reason="przegral w rosyjska ruletke")
        await ctx.channel.send(str(ctx.message.author) + " przegral w ruletke...          :)")
    else:
      await ctx.channel.send(str(ctx.message.author) + " tym razem miales szczescie :)")
     
@bot.command()
async def shoot(ctx, member : discord.Member):
    hisrandomint = random.randint(int(1),int(6));
    targetrandomint = random.randint(int(1),int(6));
    if int(hisrandomint) == int(targetrandomint):
        await ctx.guild.ban(member, reason="zastrzelony")
        await ctx.channel.send(str(ctx.message.author) + " zastrzelil " + str(member) + "...          :)")
    else:
        await ctx.guild.ban(ctx.message.author, reason="glupota")
        await ctx.channel.send(str(ctx.message.author) +  " zastrzelil sam siebie :)")
       
@bot.command()
async def wirus(ctx):
    getdata = requests.get("https://api.apify.com/v2/key-value-stores/3Po6TV7wTht4vIEid/records/LATEST?disableRedirect=true")
    wirus = getdata.json()
    await ctx.send("**statystyki nowego wirusa**" + "\n\n" + "zarazonych " + str(wirus["infected"]) + "\n" + "dead " + str(wirus["deceased"]) + "\n\n" + "__po wojewodztwach__" + "\n\n" + "*" + str(wirus["infectedByRegion"][0]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][0]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][0]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][1]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][1]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][1]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][2]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][2]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][2]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][3]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][3]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][3]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][4]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][4]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][4]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][5]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][5]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][5]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][6]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][6]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][6]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][7]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][7]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][7]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][8]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][8]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][8]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][9]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][9]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][9]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][10]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][10]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][10]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][11]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][11]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][11]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][12]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][12]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][12]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][13]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][13]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][13]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][14]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][14]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][14]["deceasedCount"]) + "\n\n" + "*" + str(wirus["infectedByRegion"][15]["region"]) + "*" + "\n" + "zarazonych " + str(wirus["infectedByRegion"][15]["infectedCount"]) + "\n" + "dead " + str(wirus["infectedByRegion"][15]["deceasedCount"]))
    
bot.run(token)
