import asyncio
import json
import discord

from chiguibot.database import Database
from chiguibot.hotslogs_api import HotsLogsAPI

from chiguibot.cogs.general.cog import GeneralCommands
from chiguibot.cogs.users import UserCommands

client = discord.Client()

@client.event
async def on_ready():
    print("ChiguiBot: logged in as %s" % (client.user.name))

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
db = Database(uri)
asyncio.get_event_loop().run_until_complete(db.test_connection())

api = HotsLogsAPI()

client.add_cog(GeneralCommands(bot))
client.add_cog(PickupCommands(bot, api, db, channel))
client.add_cog(UserCommands(bot, api, db))

client.run('Mzg4NDM1MTE2ODQzNzI4OTA4.DQtDxw.L7r-HWHMzca_ZHpWwWyQus_K4Qg')
