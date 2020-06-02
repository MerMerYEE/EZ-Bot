import discord
from discord.ext import commands
import time
import os
import re

if os.path.isfile("./lib/lister.txt"):
    print("카운터파일 존재")
else:
    f = open("./lib/lister.txt", 'w')
    f.write("0")
    f.close()
    print("mk lister")

class ko_lister(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_message(self, ctx):
        f = open("./lib/lister.txt", 'r')
        ln = int(f.read())
        f.close()
        ln = ln + 1
        f = open("./lib/lister.txt", 'w')
        f.write(str(ln))
        f.close()

    # Commands
    @commands.command()
    async def 봇(self, ctx):
        await ctx.trigger_typing()
        f = open("./lib/lister.txt", 'r')
        n = f.read()
        f.close()
        embed = discord.Embed(title="지금까지의 함수 호출량", description= str(n) + "번입니다.", color=0x8680df)
        embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ko_lister(client))
