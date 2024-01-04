import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'./{file_name}')
            await ctx.send(f'File telah disimpan di=./{file_name}')
            Hasil = get_class('keras_model.h5','labels.txt', file_name)
            await ctx.send(Hasil)
            if Hasil[0] == 'Rusa\n' and Hasil[1] >= 0.6:
                await ctx.send('Ini adalah Rusa')
                await ctx.send('Rusa jantan biasanya memiliki tanduk yang besar dan panjang')
            elif Hasil[0] == 'Kijang\n' and Hasil[1] >= 0.6:
                await ctx.send('Ini adalah Kijang')
                await ctx.send('Meskipun mirip dengan rusa betina, namun Kijang memiliki tanduk yang lebih panjang dari pada Rusa betina namun lebih pendek dari Rusa jantan')
            else:
                await ctx.send('Gambar tidak valid')

    else:
        await ctx.send(f'Tidak ada file yang dikirim')

bot.run("MTEwMzk4MjAwOTI3NTE0MjIxNQ.G04bvI.kt6oirRJ7J2QCnZwrG7Jev2vhoD9lv9feidz9M")
