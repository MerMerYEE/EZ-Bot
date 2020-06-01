import discord
from discord.ext import commands
import time

class en_Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.trigger_typing()
        embed = discord.Embed(title="Ping", description= f"{str(round(self.client.latency*1000))}ms", color=0x8680df)
        embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(en_Ping(client))
