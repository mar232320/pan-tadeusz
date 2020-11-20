import discord
from discord.ext import commands
import requests
from requests import *

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('zalogowano jako {0.user}'.format(client))
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
 
@client.command()
async def pantadeusz(ctx):
    with open("ksiega1.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            await ctx.send(line.strip())
         
@client.command()
async def covid(ctx):
    r = requests.get('https://api.apify.com/v2/key-value-stores/3Po6TV7wTht4vIEid/records/LATEST?disableRedirect=true')
    covid_data = r.json()
    await ctx.send('**statystyki koronawirusa**' + '\n\n' + 'zarazonych ' + str(covid_data['infected']) + '\n' + 'zmarlo ' + str(covid_data['deceased']) + '\n\n' + '__po wojewodztwach__' + '\n\n' + '*' + str(covid_data['infectedByRegion'][0]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][0]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][0]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][1]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][1]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][1]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][2]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][2]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][2]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][3]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][3]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][3]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][4]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][4]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][4]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][5]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][5]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][5]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][6]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][6]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][6]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][7]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][7]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][7]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][8]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][8]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][8]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][9]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][9]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][9]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][10]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][10]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][10]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][11]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][11]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][11]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][12]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][12]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][12]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][13]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][13]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][13]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][14]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][14]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][14]['deceasedCount']) + '\n\n' + '*' + str(covid_data['infectedByRegion'][15]['region']) + '*' + '\n' + 'zarazonych ' + str(covid_data['infectedByRegion'][15]['infectedCount']) + '\n' + 'zmarlo ' + str(covid_data['infectedByRegion'][15]['deceasedCount']))
       
@client.command()    
async def inwokacja(ctx):
    await ctx.send('Litwo! Ojczyzno moja! ty jesteś jak zdrowie \nIle cię trzeba cenić, ten tylko się dowie \nKto cię stracił. Dziś piękność twą w całej ozdobie \nWidzę i opisuję, bo tęsknię po tobie. \nPanno święta, co Jasnej bronisz Częstochowy \nI w Ostrej świecisz Bramie! Ty, co gród zamkowy \nNowogródzki ochraniasz z jego wiernym ludem!  \nJak mnie dziecko do zdrowia powróciłaś cudem, \n(Gdy od płaczącej matki pod Twoję opiekę \nOfiarowany, martwą podniosłem powiekę \nI zaraz mogłem pieszo do Twych świątyń progu \nIść za wrócone życie podziękować Bogu), \nTak nas powrócisz cudem na Ojczyzny łono. \nTymczasem przenoś moję duszę utęsknioną \nDo tych pagórków leśnych, do tych łąk zielonych, \nSzeroko nad błękitnym Niemnem rozciągnionych; \nDo tych pól malowanych zbożem rozmaitem, \nWyzłacanych pszenicą, posrebrzanych żytem; \nGdzie bursztynowy świerzop, gryka jak śnieg biała, \nGdzie panieńskim rumieńcem dzięcielina pała, \nA wszystko przepasane jakby wstęgą, miedzą \nZieloną, na niej z rzadka ciche grusze siedzą')
   
@client.command()
async def purge(ctx, amount):
    await ctx.channel.purge(limit=int(amount))    
      
client.run(token)
