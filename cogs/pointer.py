import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CheckFailure
import os
import sys
import openpyxl
from openpyxl import Workbook
import re
import numpy as np

class Pointer(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def 포인트(self, ctx):

        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                pfp = str(user.avatar_url)
                embed = discord.Embed(title=user.name + "님의 포인트", description="[Link]" + "(" + pfp + ")", color=0xffffff)
                embed.set_image(url=pfp)
                embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio.png")
                await ctx.trigger_typing()
                await ctx.send(embed=embed)
        else:
            pfp = ctx.author.avatar_url
            embed = discord.Embed(title="**" + ctx.author.name + "**님의 포인트", description="[Link]" + "(" + str(pfp) + ")", color=0xffffff)
            embed.set_image(url=pfp)
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio.png")
            await ctx.trigger_typing()
            await ctx.send(embed=embed)

    @포인트.error
    async def mod_ban_error(error, ctx):
        if isinstance(error, CheckFailure):
            embed = discord.Embed(title="이런!", description= "당신은 이 명령어를 실행할 권한이 없어요!", color=0xffffff)
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio.png")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Pointer(client))
