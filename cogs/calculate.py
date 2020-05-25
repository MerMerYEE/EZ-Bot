import discord
from discord.ext import commands
import wolframalpha

class Calculate(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def 계산(self, ctx):
        reply = ctx.message.content.split(" ")
        if len(reply) > 1:
            for i in range(2, len(reply)):
                reply[1] = reply[1] + " " + reply[i]
        app_id = "VPR9G7-54PV53JYTK"
        client = wolframalpha.Client(app_id)
        res = client.query(reply[1])
        answer = next(res.results).text
        embed = discord.Embed(title="Result", description=answer, color=0xffffff)
        embed.set_footer(text="Powered by Salt Cube#7951", icon_url="https://raw.githubusercontent.com/SaltCube7/CXT/master/n_images/saltcube.jpg")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Calculate(client))
