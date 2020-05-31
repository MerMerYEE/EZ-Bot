import discord
from discord.ext import commands
import wolframalpha

class ko_Calculate(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def 계산(self, ctx):
        await ctx.trigger_typing()
        reply = ctx.message.content.split(" ")
        if len(reply) > 1:
            for i in range(2, len(reply)):
                reply[1] = reply[1] + " " + reply[i]
        app_id = ""
        client = wolframalpha.Client(app_id)
        res = client.query(reply[1])
        answer = next(res.results).text
        embed = discord.Embed(title="Result", description=answer, color=0xffffff)
        embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ko_Calculate(client))
