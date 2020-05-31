import discord
from discord.ext import commands

class en_Avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def avatar(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                pfp = str(user.avatar_url)
                embed = discord.Embed(title="**" +user.name + "**'s Avatar", description="[Link]" + "(" + pfp + ")",
                                      color=0x8680df)
                embed.set_image(url=pfp)
                embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
                await ctx.trigger_typing()
                await ctx.send(embed=embed)
        else:
            pfp = ctx.author.avatar_url
            embed = discord.Embed(title="**" + ctx.author.name + "**'s Avatar", description="[Link]" + "(" + str(pfp) + ")",
                                color=0x8680df)
            embed.set_image(url=pfp)
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
            await ctx.trigger_typing()
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(en_Avatar(client))
