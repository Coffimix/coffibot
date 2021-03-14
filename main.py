import discord
from discord.ext import commands
from discord import Embed
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import youtube_dl
import os
import requests
import random
import shutil
from os import system
import traceback
import asyncio
import sys

bad_words = ['хуй', 'ты еблан?', 'ты даун?', 'ты конч?', 'ты уёбок', 'ты чмо', 'ты конч', 'ты даун', 'ты еблан',
             'уебись нахуй', 'сдохни от спида', 'ебаная шлюха', 'ебать ты тупой',
             'ебать ты днище', 'тупой блять', 'нытик ебаный', 'мать жива?', 'педрила', 'животное ебливое',
             'гандон сука', 'хуйца сосни', 'хуйца сосни школьница', 'днище ебаное', 'соси хуй',
             'соси письку', 'соси дно тупорылое', 'глотни хуйца', 'ебланище', 'ебланище тупое', 'хуй соси',
             'хуй соси еблан', 'ппиздец ты даун', 'тупой еблан', 'сын шлюхи', 'гандон ебаный',
             'пиздец', 'нахуй', 'ебать', 'уебись', 'еблан', 'ебаное', 'гандон', 'гондон', 'ебаный', 'Хуесос', 'Залупа',
             'Залупа', 'захуярить', 'нихуя', 'Нехуй', 'Ни хуя себе', 'Охуевать', 'Охуенно',
             'Похую', 'Соси хуй', 'Хуёво', 'Пизда', 'Хуй его знает', 'Хуеплёт', 'Хуета', 'иди нахуй', 'даун тупой',
             'даун', 'хуй забей', 'пиздец тупой', 'пиздец ты тупой', 'пиздец тупоой',
             'пиздец ты тупоой', 'пиздец я тупой', 'нахуй иди', 'нахуй иди даун', 'нахуй вали', 'нахуй проваливай',
             'нахуй сука', 'нахуй блять', 'ебать я тупой', 'ебать я тупоой', 'хуй знает',
             'хуйня', 'это все хуйня', 'иди нахуй чмо', 'сосни хуйца', 'сосни хуйцы школьница']

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')  # Удаляем изначальную команду "help"


# @


# ошибки

# command error
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, укажи аргумент')
    else:
        print(error)

# нет такой команды

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'{ctx.author.name}, Такой команды не существует!')


# clear error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.name}, пожалуйста, укажи количество сообщений для удаления.')


# @client.event
# async def on_ready():
# играет
# await client.change_presence(activity=discord.Game(name="on {len(client.guilds')} servers | $help")
# стримит
# await client.change_presence(activity=discord.Streaming(name="My Stream", url=My_twich_url))
# слушает
# await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="моргена"))
# смотрит
# await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="за сервером COFFIMIXA"))
# print("Ready")

# async def ch_pr():
# await client.wait_until_ready()

# statuses = ["a game", f"on {len(client.guilds)} servers | $help0", "discord.py"]

# while not client.is_closed():

# status = random.choice(statuses)
# await client.change_presence(activity=discord.Game(name=status))

# await asyncio.sleep(10)


# client.loop.create_task(ch_pr())
# client.run()


# random
@bot.event
async def on_ready():
    print('bot is ready')
    while True:
        await bot.change_presence(status=discord.Status.idle, activity=discord.Game('в $help'))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.idle,
                                     activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name=f" за сервером COFFIMIXA"))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.idle,
                                     activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name=f"видосы  COFFIMIXA"))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.idle,
                                     activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name=f"$help помощь"))
        await asyncio.sleep(10)


initial_extensions = ['Cogs.music']
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Неудалось загрузить {extension}', file=sys.stderr)
            traceback.print_exc()


@bot.command(pass_context=True)
async def random_10(ctx):
    await ctx.send(random.randint(1, 11))


@bot.command(pass_context=True)
async def random_20(ctx):
    await ctx.send(random.randint(1, 21))


@bot.command(pass_context=True)
async def random_30(ctx):
    await ctx.send(random.randint(1, 31))


@bot.command(pass_context=True)
async def random_40(ctx):
    await ctx.send(random.randint(1, 41))


@bot.command(pass_context=True)
async def random_50(ctx):
    await ctx.send(random.randint(1, 51))


@bot.command(pass_context=True)
async def random_60(ctx):
    await ctx.send(random.randint(1, 61))


@bot.command(pass_context=True)
async def random_70(ctx):
    await ctx.send(random.randint(1, 71))


@bot.command(pass_context=True)
async def random_80(ctx):
    await ctx.send(random.randint(1, 81))


@bot.command(pass_context=True)
async def random_90(ctx):
    await ctx.send(random.randint(1, 91))


@bot.command(pass_context=True)
async def random_100(ctx):
    await ctx.send(random.randint(1, 101))


# roli
@bot.event
async def on_member_join(member):
    print('new user')
    channel = bot.get_channel(735961769046048809)
    role = discord.utils.get(member.guild.roles, id=735957419699732601)
    role1 = discord.utils.get(member.guild.roles, id=736135702416326698)
    await member.add_roles(role)
    await member.add_roles(role1)
    await channel.send(
        embed=discord.Embed(description=f'Пользователь ``{member.name}``, Залетел к нам!', color=0x0c0c0c, ))


# BOT_MESSEGE!!!!!!!!!!!!!!!!!!!!

@bot.command()
async def send(ctx, member: discord.Member):
    await member.send(f'{member.name}, привет от {ctx.author.name} ')


# BOT_MESSEGE!!!!!!!!!!!!!!!!!!!!
@bot.command()
async def maniac(ctx):
    membs = ctx.guild.members
    for i in membs:
        print(f'Отправляю {i.name}')
        await i.send('Го играть в маньяка (проигнорьте это сообщение это тест)')


# clear message
@bot.command(pass_context=True, aliases=['cl', 'CL'])
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=10000):
    await ctx.channel.purge(limit=amount)
    await ctx.send(embed=discord.Embed(description=f':white_check_mark: Удалено {amount} сообщений', color=0x0c0c0c, ))


# Kick
@bot.command(pass_context=True, aliases=['KICK'])
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.kick(reason=reason)

    emb = discord.Embed(title='Информация о кике',
                        description=f'{member.name.title()}, был кикнут в связи c нарушением правил',
                        color=0x979c9f)

    emb.set_author(name=member, icon_url=member.avatar_url)
    emb.set_footer(text=f'Был кикнут администратором {ctx.message.author.name}', icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)


# ban
@bot.command(pass_context=True, aliases=['BAN'])
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    emb = discord.Embed(title='Ban', color=discord.Color.red())
    await ctx.channel.purge(limit=1)

    await member.ban(reason=reason)

    emb.set_author(name=member, icon_url=member.avatar_url)
    emb.add_field(name='забанен ', value='игрок : {}'.format(member.mention))
    emb.set_footer(text='Был забанен Администратором {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)


# unban
@bot.command(pass_context=True, aliases=['UNBAN'])
async def unban(ctx, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for banned_entry in banned_users:
        user = banned_entry.user
    if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f"{user} разбанен")
        return


# отправить сообщения
@bot.command()
async def maniak(ctx, member: discord.Member):
    await member.send(
        f'{member.name}, привет не хочешь ли ты поиграть в маньяка? пиши на сервере COFFIMIXA или мне в лс {ctx.author.name}')


# filter
@bot.event
async def on_message(msg, ):
    author = msg.author
    mes = msg.content.lower()
    for line in bad_words:
        if mes.find(line) != -1:
            if msg.author.bot or mes.find('play') != -1:
                pass
            else:
                await msg.delete()
                await msg.channel.send(f"Плохо выражаешься: {author.mention}")
    await bot.process_commands(msg)


# commandhelp
@bot.command()
async def help(ctx):
    emb = discord.Embed(
        title='КОМАНДЫ :clipboard:',
        color=0x7aa13d
    )

    emb.add_field(name='**ДЛЯ МУЗЫКИ**', value='''
        :robot:$join ; $j ; $joi :robot:   добавить бота в голосовой канал 
        :headphones:$play; $p; $pl ссылка :headphones: - воспроизвести музыку 
        :robot:$leave ; $le :robot:-     убрать бота из голосового канала 
        :pause_button:$pause ; $p ; $pau :pause_button: - поставить бота на паузу 
        :record_button:$resume ; $r ; $res :record_button: - снять с паузы бота 
        :stop_button:$stop ; $s ; $st :stop_button: - остановить музыку 
        :musical_note:$q ссылка :musical_note: - поставить музыку в очередь 
        :track_next: $next ; $n ; $nex:track_next:  - следующая музыка в очереди 
        ''')

    emb.add_field(name='**КОМАНДЫ ДЛЯ ИГРОКОВ**', value='''
        :woman_detective:$maniak @user:woman_detective: - позвать играть в маньяка 
        :1234:$random_10:1234: - рандомное число (20,30,40,50,60,70,80,90,100)
        :robot:$maps:robot:  - в следующих обновлениях 
        ''')
    emb.add_field(name='**КОМАНДЫ ДЛЯ АДМИНОВ**', value='''
        :face_with_symbols_over_mouth:$ban ; $BAN @user:face_with_symbols_over_mouth: - БАН 
        :rage:$kick ; $KICK @user:rage: - КИК 
        :innocent:$unban ; $UNBAN user#2134:innocent: - разбанить 
        :wastebasket:$clear ; $cl ; $CL  число :wastebasket:- очистить чат 
        ''')

    await ctx.send(embed=emb)


@bot.command()
async def ip_info(ctx, arg):
    response = requests.get(f'http://ipinfo.io/{arg}/json')

    user_ip = response.json()['ip']
    user_city = response.json()['city']
    user_region = response.json()['region']
    user_country = response.json()['country']
    user_location = response.json()['loc']
    user_org = response.json()['org']
    user_timezone = response.json()['timezone']

    global all_info
    all_info = f'\n<INFO>\nIP : {user_ip}\nCity : {user_city}\nRegion : {user_region}\nCountry : {user_country}\nLocation : {user_location}\nOrganization : {user_org}\nTime zone : {user_timezone}'

    await ctx.author.send(all_info)


@bot.command(pass_context=True)
# .hello
async def hello(ctx):
    author = ctx.message.author

    await ctx.send(f'Привет {author.mention} я бот COFFIMIXA! Что хотел спросить? напиши !help')


# voice chat

# 1



bot.run('NzU5MzQyOTU0MjMzMjAwNjQw.X28HPA.IAMZf6dKepQqDYGPKwdbvgyny40')
