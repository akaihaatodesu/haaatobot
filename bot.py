import discord
from discord.ext import commands



intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+' , intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>心心 code-92 上線了")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(805371305855025184)
    await channel.send(f"{member.mention} 加入了! (踩")
    
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(834079223802232853)
    await channel.send(f'{member.mention} 離開了! (踢')




@bot.command()
async def ping(ctx):
    await ctx.send(f'心心code-92延遲為{round(bot.latency*1000)}ms')



@bot.command()
async def stomp(ctx):
    pic = discord.File('D:\\code file\\haaatobot\\tenor.gif')
    await ctx.send(file = pic)


@bot.command()









bot.run('ODU0MjMyMDc1MDIwMjcxNjI1.YMg7nQ.ZELatX7tt4oxtzkr9lTqeF1My6E')
