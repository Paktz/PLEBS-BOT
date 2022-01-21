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


############# chat bot

@bot.event
async def on_message(message):
    if message.content == '555' :
        await message.channel.send('So funny huh.')

@bot.event
async def on_message(message):
    if message.content == 'What are you doing' :
        await message.channel.send('Nothing.')
        
@bot.event
async def on_message(message):
    if message.content == '' :
        await message.channel.send('Nothing')
  


bot.run(token)