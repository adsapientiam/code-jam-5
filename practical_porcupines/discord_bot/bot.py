import discord
from discord.ext import commands
from practical_porcupines.utils import ConfigApi, ConfigBot

config_api = ConfigApi()
config_bot = ConfigBot()

bot_client = commands.Bot(command_prefix=config_bot.PREFIX)
API_ENDPOINT = f"{config_api.API_DOMAIN}:{config_api.API_PORT}"


@client.event
async def on_ready():
    """
    Runs when client boots
    """

    print(f"{client.user.name} is online with the id of '{client.user.id}'!")
