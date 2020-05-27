import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CheckFailure
import os
import sys
import re
import numpy as np
import json


if os.path.isdir("./lib"):
    print("Lib Exist")
else:
    os.mkdir("./lib")
    print("Make Lib Folder")

if os.path.isdir("./lib/servers"):
    print("Servers Folder Exist")
else:
    os.mkdir("./lib/servers")
    print("Make Servers Folder")


class Pointer(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if os.path.isdir("./lib/servers/" + str(ctx.guild.id)):
            print("Guild Exist")
        else:
            os.mkdir("./lib/servers/" + str(ctx.guild.id))
            print("Mk Guild Folder")

        if os.path.isfile("./lib/servers/" + str(ctx.guild.id) + "/" + str(ctx.author.id) + ".txt"):
            print("Guild-User Exist")
        else:
            f = open("./lib/servers/" + str(ctx.guild.id) + "/" + str(ctx.author.id) + ".txt", 'w')
            f.write("0")
            f.close()

    #Commands
    @commands.command()
    async def 포인트(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                if os.path.isfile("./lib/servers/" + str(ctx.guild.id) + "/" + str(user.id) + ".txt"):
                    f = open("./lib/servers/" + str(ctx.guild.id) + "/" + str(user.id) + ".txt", 'r')
                    pp = str(f.read())
                    f.close()
                    embed = discord.Embed(title="**" + user.name + "**님의 포인트", description= "**" + pp + " pp**",color=0xffffff)
                    pfp = str(user.avatar_url)
                    embed.set_thumbnail(url=pfp)
                    embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio.png")
                    await ctx.trigger_typing()
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="**에러!**", description= "데이터가 존재하지 않아요!", color=0xffffff)
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
                    embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio.png")
                    await ctx.trigger_typing()
                    await ctx.send(embed=embed)

        else:
            if os.path.isfile("./lib/servers/" + str(ctx.guild.id) + "/" + str(ctx.author.id) + ".txt"):
                f = open("./lib/servers/" + str(ctx.guild.id) + "/" + str(ctx.author.id) + ".txt", 'r')
                pp = str(f.read())
                f.close()
                embed = discord.Embed(title="**" + ctx.author.name + "**님의 포인트", description= "**" + pp + " pp**",color=0xffffff)
                pfp = ctx.author.avatar_url
                embed.set_thumbnail(url=pfp)
                embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio.png")
                await ctx.trigger_typing()
                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(title="**에러!**", description= "데이터가 존재하지 않아요!", color=0xffffff)
                embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
                embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio.png")
                await ctx.trigger_typing()
                await ctx.send(embed=embed)

    @포인트.error
    async def 포인트_error(error, ctx):
        if isinstance(error, CheckFailure):
            embed = discord.Embed(title="**에러!**", description= "당신은 이 명령어를 실행할 권한이 없어요!", color=0xffffff)
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio.png")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Pointer(client))
