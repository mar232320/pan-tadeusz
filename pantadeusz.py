import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('zalogowano jako {0.user}'.format(client))
    
@client.command()
async def pomoc(ctx):
    await ctx.send(f'Lista komend //kiedys bedzie w embedzie \n-ping pokazuje ping \n-inwokacja cytuje inwokacje z pana tadeusza \n-purge usuwa 5 wiadomosci //w przyszlosci bedzie mozna wybrac dokladna liczbe')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    
@client.command()    
async def inwokacja(ctx):
    await ctx.send(f'Litwo! Ojczyzno moja! ty jesteś jak zdrowie \nIle cię trzeba cenić, ten tylko się dowie \nKto cię stracił. Dziś piękność twą w całej ozdobie \nWidzę i opisuję, bo tęsknię po tobie. \nPanno święta, co Jasnej bronisz Częstochowy \nI w Ostrej świecisz Bramie! Ty, co gród zamkowy \nNowogródzki ochraniasz z jego wiernym ludem!  \nJak mnie dziecko do zdrowia powróciłaś cudem, \n(Gdy od płaczącej matki pod Twoję opiekę \nOfiarowany, martwą podniosłem powiekę \nI zaraz mogłem pieszo do Twych świątyń progu \nIść za wrócone życie podziękować Bogu), \nTak nas powrócisz cudem na Ojczyzny łono. \nTymczasem przenoś moję duszę utęsknioną \nDo tych pagórków leśnych, do tych łąk zielonych, \nSzeroko nad błękitnym Niemnem rozciągnionych; \nDo tych pól malowanych zbożem rozmaitem, \nWyzłacanych pszenicą, posrebrzanych żytem; \nGdzie bursztynowy świerzop, gryka jak śnieg biała, \nGdzie panieńskim rumieńcem dzięcielina pała, \nA wszystko przepasane jakby wstęgą, miedzą \nZieloną, na niej z rzadka ciche grusze siedzą')
    
@client.command()
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    
client.run('NzQyNDE2ODE2ODA2Mjk3Njcw.XzFzig.DlT92vs3BAoTOWtnyVbeaEp93O0')