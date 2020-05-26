import discord
from discord.ext import commands

class Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def 말하기(self, ctx):
        await ctx.trigger_typing()
        reply = ctx.message.content.split(" ")
        if len(reply) > 1:
            for i in range(2, len(reply)):
                reply[1] = reply[1] + " " + reply[i]
        await ctx.message.delete()
        await ctx.send(reply[1])

def setup(client):
    client.add_cog(Say(client))
