import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CheckFailure
import os
import sys
import re
import numpy as np
import json
import traceback

class ko_Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    @has_permissions(administrator = True)
    async def 뮤트(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                await ctx.trigger_typing()
                embed = discord.Embed(title="**테스트중**", description= "당신은 어드민입니다.", color=0x8680df)
                embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
                embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
                await ctx.send(embed=embed)
        else:
            await ctx.trigger_typing()
            embed = discord.Embed(title="**에러!**", description= "음소거할 대상을 멘션해주세요", color=0x8680df)
            embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
            await ctx.send(embed=embed)

        await ctx.trigger_typing()
        embed = discord.Embed(title="**테스트중**", description= "당신은 어드민입니다.", color=0x8680df)
        embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
        embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ko_Moderation(client))
