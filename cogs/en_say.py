import discord
from discord.ext import commands

class en_Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def say(self, ctx):
        await ctx.trigger_typing()
        reply = ctx.message.content.split(" ")
        if len(reply) > 1:
            for i in range(2, len(reply)):
                reply[1] = reply[1] + " " + reply[i]
        await ctx.message.delete()
        await ctx.send(reply[1])

def setup(client):
    client.add_cog(en_Say(client))
