from email import message
import discord
from discord.utils import get
from discord.ext import commands
from song import songAPI 
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')


bot = commands.Bot(command_prefix='?',help_command=None)

#นำเข้า class songAPI จาก ไฟล์ song import class songAPI from "song"
songsInstance = songAPI()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command() 
async def help(ctx):
    em = discord.Embed(title='Commands', description='These are our commands choose wisely :)',color=0xF90716)
    em.add_field(name='?p  or ?play',value='play the song',inline=False)
    em.add_field(name='?sk or ?skip',value='skipidiBOP curruntly music',inline=False)
    em.add_field(name='?li or ?list',value='show Q list',inline=False)
    em.add_field(name='?pa or ?pause',value='poos the music',inline=False)
    em.add_field(name='?re or ?resume',value='rezoom the music',inline=False)
    em.add_field(name='?c or ?clear',value='Delete all Qed music',inline=False)
    em.add_field(name='?le or ?leave',value='Kick my ass out of the room',inline=False)
    em.add_field(name='?PLL',value='PLL Algorithms',inline=False)
    await ctx.channel.send(embed=em)


@bot.command() 
async def PLL(ctx):
    em = discord.Embed(title='Permutation of Last Layer', description='Permutation of Last Layer(PLL) the last step of CFOP Method',color=0xF90716)
    em.add_field(name="Aa",value=" x L2 D2 L' U' L D2 L' U L' ",inline=False)
    em.add_field(name="Ab",value=" x' L2 D2 L U L' D2 L U' L ",inline=True)
    em.add_field(name="F",value=" R' U' F' R U R' U' R' F R2 U' R' U' R U R' U R ",inline=False)
    em.add_field(name="Ga",value=" R2 U R' U R' U' R U' R2 U' D R' U R D' ",inline=False)
    em.add_field(name="Gb",value=" R' U' R U D' R2 U R' U R U' R U' R2 D ",inline=True)
    em.add_field(name="Gc",value=" R2 U' R U' R U R' U R2 U D' R U' R' D ",inline=False)
    em.add_field(name="Gd",value=" R U R' U' D R2 U' R U' R' U R' U R2 D' ",inline=True)
    em.add_field(name="Ja",value=" x R2 F R F' R U2 r' U r U2 ",inline=False)
    em.add_field(name="Jb",value=" R U R' F' R U R' U' R' F R2 U' R' ",inline=True)
    em.add_field(name="Ra",value=" R U' R' U' R U R D R' U' R D' R' U2 R' ",inline=False)
    em.add_field(name="Rb",value=" R2 F R U R U' R' F' R U2 R' U2 R ",inline=False)
    em.add_field(name="T",value=" R U R' U' R' F R2 U' R' U' R U R' F' ",inline=False)
    em.add_field(name="E",value=" x' L' U L D' L' U' L D L' U' L D' L' U L D ",inline=False)
    em.add_field(name="Na",value=" R U R' U R U R' F' R U R' U' R' F R2 U' R' U2 R U' R' ",inline=False)
    em.add_field(name="Nb",value=" R' U R U' R' F' U' F R U R' F R' F' R U' R",inline=True)
    em.add_field(name="V",value=" R' U R' U' y R' F' R2 U' R' U R' F R F ",inline=False)
    em.add_field(name="Y",value=" F R U' R' U' R U R' F' R U R' U' R' F R F' ",inline=False)
    em.add_field(name="H",value=" M2 U M2 U2 M2 U M2 ",inline=False)
    em.add_field(name="Ua",value=" M2 U M U2 M' U M2 ",inline=False)
    em.add_field(name="Ub",value=" M2 U' M U2 M' U' M2 ",inline=False)
    em.add_field(name="Z",value=" M' U M2 U M2 U M' U2 M2 ",inline=False)
    await ctx.channel.send(embed=em)
#play
@bot.command() 
async def play(ctx,* ,search: str):
    await songsInstance.play(ctx, search)

@bot.command() 
async def p(ctx,* ,search: str):
    await songsInstance.play(ctx, search)
#skip
@bot.command()
async def skip(ctx):
    await songsInstance.skip(ctx)

@bot.command()
async def sk(ctx):
    await songsInstance.skip(ctx)
#show list
@bot.command()
async def list(ctx):
    await songsInstance.queueList(ctx)

@bot.command()
async def ls(ctx):
    await songsInstance.queueList(ctx)
#pause
@bot.command()
async def pa(ctx):
    await songsInstance.pause(ctx)
#resume
@bot.command()
async def resume(ctx):
    await songsInstance.resume(ctx)

@bot.command()
async def re(ctx):
    await songsInstance.resume(ctx)
#kick
@bot.command()
async def leave(ctx):
    await songsInstance.leave(ctx)

@bot.command()
async def le(ctx):
    await songsInstance.leave(ctx)
#clear
@bot.command()
async def clear(ctx):
    await songsInstance.clear(ctx)

@bot.command()
async def c(ctx):
    await songsInstance.clear(ctx)

bot.run(token)