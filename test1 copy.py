import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='>', intents=intents)

channel_pysever_bot_testing_ID = 1083403814389940214


async def start_message():
    channel = client.get_channel(channel_pysever_bot_testing_ID)
    await channel.send('おいらはパチモンだ!botを起動したぞ!')

def kanna_divines_who_is_rotten_this_week():
    The_Zodiac_Sign_tuple = {'おひつじ座':"大金の入った財布を失くしてしまうかもだぞ",
                            'おうし座':"回線が落ちる",
                            'ふたご座':"迷子になるぞ",
                            'かに座':"事件に巻き込まれるぞ",
                            'しし座':"ま じ や ば い",
                            'おとめ座':"MAJI YABAI",
                            'てんびん座':"てんびん座は絶滅します",
                            'さそり座':"煽りメッセが届く",
                            'いて座':"トイレから出られなくなるかも～",
                            'やぎ座':"人生に疲れるぞ",
                            'みずがめ座':"知り合いが呪い殺してくるぞ",
                            'うお座':"大きな失敗をして死にたくなるぞ"} #内容と星座をランダムにする
    sign, fortune = random.choice(list(The_Zodiac_Sign_tuple.items()))
    mess = sign+":"+fortune
    return mess


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game(name="原神"))
    await start_message() #起動確認済み、可動可

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if message.content.startswith("Patimon!Help!"):
        await message.channel.send("bye")

    if message.content.startswith('えへっ'):
        await message.channel.send('えへってなんだよ！')

    if message.content.startswith("トール?"):
        await message.channel.send("ハイハイ～！トールです！")

    if message.content.startswith("マジやばくね"):
        await message.channel.send("https://images-ext-1.discordapp.net/external/WPlUDNWyPIRvu_RV2SfHJf9CQBKKciHl-62Kl1-eoM4/https/media.tenor.com/ULCY5B996-oAAAPo/kanna-kobayashi.mp4")

    if message.content.startswith("今週の腐ったやつだ～れだ?"):
        await message.channel.send("これまだ開発中。腐った奴お前。でも一応、占う")
        mess = kanna_divines_who_is_rotten_this_week()
        await message.channel.send(mess)

    if message.content.startswith("ok"):
        await message.channel.send("ok")

    if message.content.startswith("最近，忙吗？"):
        await message.channel.send("很忙")


client.run('')
#人に見せるよう