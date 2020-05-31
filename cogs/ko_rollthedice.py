import discord
from discord.ext import commands
import time
import random

class ko_Dice(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def 주사위(self, ctx):
        await ctx.trigger_typing()

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        if randomNum == 1:
            embed = discord.Embed(title= "**주사위**", description = ':game_die:'+ ':one:', color=0x8680df)
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
            await ctx.send(embed=embed)
        if randomNum == 2:
            embed = discord.Embed(title= "**주사위**", description = ':game_die:'+ ':two:', color=0x8680df)
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
            await ctx.send(embed=embed)
        if randomNum ==3:
            embed = discord.Embed(title= "**주사위**", description = ':game_die:'+ ':three:', color=0x8680df)
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
            await ctx.send(embed=embed)
        if randomNum ==4:
            embed = discord.Embed(title= "**주사위**", description = ':game_die:'+ ':four:', color=0x8680df)
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
            await ctx.send(embed=embed)
        if randomNum ==5:
            embed = discord.Embed(title= "**주사위**", description = ':game_die:'+ ':five:', color=0x8680df)
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
            await ctx.send(embed=embed)
        if randomNum ==6:
            embed = discord.Embed(title= "**주사위**", description = ':game_die:'+ ':six:', color=0x8680df)
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ko_Dice(client))
