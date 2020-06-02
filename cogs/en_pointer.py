import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CheckFailure
import os
import sys
import re
import numpy as np
import json
import traceback


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
    async def point(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                if os.path.isfile("./lib/servers/" + str(ctx.guild.id) + "/" + str(user.id) + ".txt"):
                    f = open("./lib/servers/" + str(ctx.guild.id) + "/" + str(user.id) + ".txt", 'r')
                    pp = str(f.read())
                    f.close()
                    embed = discord.Embed(title="**" + user.name + "**'s Point", description= "**" + pp + " pp**",color=0x8680df)
                    pfp = str(user.avatar_url)
                    embed.set_thumbnail(url=pfp)
                    embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
                    await ctx.trigger_typing()
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="**Error!**", description= "The data does not exist!", color=0x8680df)
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
                    embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
                    await ctx.trigger_typing()
                    await ctx.send(embed=embed)

        else:
            if os.path.isfile("./lib/servers/" + str(ctx.guild.id) + "/" + str(ctx.author.id) + ".txt"):
                f = open("./lib/servers/" + str(ctx.guild.id) + "/" + str(ctx.author.id) + ".txt", 'r')
                pp = str(f.read())
                f.close()
                embed = discord.Embed(title="**" + ctx.author.name + "**'s Point", description= "**" + pp + " pp**",color=0x8680df)
                pfp = ctx.author.avatar_url
                embed.set_thumbnail(url=pfp)
                embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
                await ctx.trigger_typing()
                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(title="**Error!**", description= "The data does not exist!", color=0x8680df)
                embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
                embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
                await ctx.trigger_typing()
                await ctx.send(embed=embed)

    @commands.command()
    @has_permissions(administrator = True)
    async def addpoint(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                if os.path.isfile("./lib/servers/" + str(ctx.guild.id) + "/" + str(user.id) + ".txt"):
                    f = open("./lib/servers/" + str(ctx.guild.id) + "/" + str(user.id) + ".txt", 'r')
                    pp = int(f.read())
                    f.close()
                    reply = ctx.message.content.split(" ")
                    pp = pp + int(reply[2])
                    f = open("./lib/servers/" + str(ctx.guild.id) + "/" + str(user.id) + ".txt", 'w')
                    f.write(str(pp))
                    f.close()
                    embed = discord.Embed(title="**" + user.name + "**'s Point", description= "**" + str(pp) + " pp**",color=0x8680df)
                    pfp = str(user.avatar_url)
                    embed.set_thumbnail(url=pfp)
                    embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
                    await ctx.trigger_typing()
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="**Error!**", description= "The data does not exist!", color=0x8680df)
                    embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
                    embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
                    await ctx.trigger_typing()
                    await ctx.send(embed=embed)

        else:
            await ctx.trigger_typing()
            embed = discord.Embed(title="**Error!**", description= "Please mention the user to give Point", color=0x8680df)
            embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
            embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
            await ctx.send(embed=embed)

    async def on_command_error(error, ctx):
        if isinstance(error, commands.MissingPermissions):
                embed = discord.Embed(title="**Error!**", description= "You do not have permission to execute this command!", color=0x8680df)
                embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/shio_error.png")
                embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio8.png")
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Pointer(client))
