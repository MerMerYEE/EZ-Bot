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
                role = discord.utils.get(ctx.guild.roles, name="Muted")
                if not role:
                    try:
                        muted = await ctx.guild.create_role(name="Muted")
                        for channel in ctx.guild.channels:
                            await channel.set_permissions(muted, send_messages=False, read_message_history=False, read_messages=False)
                    except discord.Forbidden:
                        await ctx.trigger_typing()
                        embed = discord.Embed(title="**에러!**", description= "음소거 역할을 만들 권한이 없어요!", color=0x8680df)
                        embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
                        embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
                        await ctx.send(embed=embed)

                    await user.add_roles(muted)
                    await ctx.trigger_typing()
                    embed = discord.Embed(title="**Moderation**", description= f"{user.mention}가 음소거 처리되었어요.", color=0x8680df)
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
                    embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
                    await ctx.send(embed=embed)
                else:
                    await user.add_roles(role)
                    await ctx.trigger_typing()
                    embed = discord.Embed(title="**Moderation**", description= f"{user.mention}가 음소거 처리되었어요.", color=0x8680df)
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
                    embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
        else:
            await ctx.trigger_typing()
            embed = discord.Embed(title="**에러!**", description= "음소거할 대상을 멘션해주세요", color=0x8680df)
            embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ko_Moderation(client))
