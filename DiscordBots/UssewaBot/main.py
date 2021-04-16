import discord
import imageFunc as im

client = discord.Client()

@client.event
async def on_ready():
    print('うっせえわボットです ' + str(client.user.name))

@client.event
async def on_message(message):
     if message.author.bot:
          return
     if message.content.startswith("aho "):
          im.syori(message.content[4:])
          await message.channel.send("さあ､どうぞ 大好きだ!")
          await message.channel.send(file=discord.File("saved/savedImage.png"))

client.run('ボットID')