import discord
from discord.ext import commands
import time

class en_Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def help(self, ctx):
        await ctx.trigger_typing()
        embed = discord.Embed(title="도움말", description= "**EZ봇 1.1 \nPrefix: ``.``**", color=0xffffff)
        embed.add_field(name='**도움**', value='**이 메시지를 보여줍니다.**', inline = False)
        embed.add_field(name='**Utility**', value='**`아바타`, `아바타 (멘션)`, `말하기`, `핑`, `계산 (식)`, `주사위`, `한영`, `영한`, `한일`, `일한`, `한중`, `중한`**', inline = False)
        embed.add_field(name='**서버 이벤트**', value='**`포인트`, `포인트 (멘션)`, `포인트추가 (멘션)`**', inline = False)
        embed.add_field(name='**레벨**', value='**`레벨`, `레벨 (멘션)`**', inline = False)
        embed.add_field(name='**음악**', value='**`connect`, `play`, `pause`, `resume`, `skip`, `volume(vol)`, `stop`, `now_playing`**', inline = False)
        embed.add_field(name='**지원 서버**', value='**[클릭!](https://discord.gg/HerTmj5)**', inline = False)
        embed.add_field(name="**봇 초대하기**", value = "**[바로가기](https://discord.com/oauth2/authorize?client_id=713182729063235694&scope=bot&permissions=8)**", inline = False)
        embed.set_footer(text="Offered by NACL - Shio", icon_url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/Shio7.png")
        embed.set_thumbnail(url="https://raw.githubusercontent.com/Shio7/EZ-Bot/master/images/ez_bot.png")
        embed.add_field(name='**Desc**', value='**이지 봇은 [오픈소스](https://github.com/Shio7/EZ-Bot)프로젝트입니다.**', inline = False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(en_Help(client))
