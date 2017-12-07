import asyncio
import json
import discord


from chiguibot.hotslogs_api import HotsLogsAPI

from chiguibot.cogs.general.cog import GeneralCommands
from chiguibot.cogs.users import UserCommands

client = discord.Client()

@client.event
async def on_ready():
    print("ChiguiBot: logged in as %s" % (client.user.name))


    

api = HotsLogsAPI()


client.run('Mzg4NDM1MTE2ODQzNzI4OTA4.DQtDxw.L7r-HWHMzca_ZHpWwWyQus_K4Qg')
