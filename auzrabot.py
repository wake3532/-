import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('봇 작동이 시작됌')

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith(f'n/비코문상계산'):
        split = message.content.split(" ")
        won = split[1]
        sslghm = "%.2f" % (24.34 * float(won) / 100.0)
        gap = float(won)+float(sslghm)
        await message.channel.send(f"<:bitcoin:786832277610561537> 비트코인가격 : **{gap} 원** \n\n<:project:786832262721044540>  계산한 가격  : **{won} 원**")

    if message.content.startswith(f'n/이더문상계산'):
        split = message.content.split(" ")
        won = split[1]
        sslghm = "%.2f" % (24.34 * float(won) / 100.0)
        gap = float(won)+float(sslghm)
        await message.channel.send(f" 이더 가격 : **{gap} 원** \n\n 계산한 가격  : **{won} 원**")
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
