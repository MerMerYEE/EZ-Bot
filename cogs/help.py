import discord
from discord.ext import commands
import time

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def 도움(self, ctx):
        embed = discord.Embed(title="도움말", description= "쓸 예정", color=0xffffff)
        embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))
