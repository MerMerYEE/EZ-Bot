import discord
from discord.ext import commands
import time

class ko_Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('EZ is Online.')

    # Commands
    @commands.command()
    async def 핑(self, ctx):
        await ctx.trigger_typing()
        embed = discord.Embed(title="핑", description= f"{str(round(self.client.latency*1000))}ms", color=0x8680df)
        embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ko_Ping(client))
