import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('CXT is Online.')

    # Commands
    @commands.command()
    async def 핑(self, ctx):
        await ctx.send('Pong!')
        await ctx.send(f"({str(round(self.client.latency*1000))}ms)")

def setup(client):
    client.add_cog(Ping(client))
