import asyncio
import json
import os

from discord.ext.commands import Bot

from chiguibot.database import Database
from chiguibot.hotslogs_api import HotsLogsAPI

from chiguibot.cogs.general.cog import GeneralCommands
from chiguibot.cogs.users import UserCommands

bot = Bot(command_prefix="!", description="I am ChiguiBot! I help showing your stats, and do other bot-y things.")

@bot.event
async def on_ready():
    print("ChiguiBot: logged in as %s" % (bot.user.name))

token = os.environ["DISCORD_TOKEN"]
channel = os.environ.get("DISCORD_CHANNEL")
uri = os.environ["MONGO_URI"]

db = Database(uri)
asyncio.get_event_loop().run_until_complete(db.test_connection())

api = HotsLogsAPI()

bot.add_cog(GeneralCommands(bot))
bot.add_cog(PickupCommands(bot, api, db, channel))
bot.add_cog(UserCommands(bot, api, db))

bot.run(token)
