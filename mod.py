import sqlite3
import time
import random
import urllib
from urllib import request
from urllib.parse import quote
import re, os, sys  

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

start = r"C:\Users\Админ\Desktop\Работы\lolkof's bot"

def lines_counter(fp):
    f_lines = open(fp, 'r', encoding = 'utf-8').readlines()
    mass = []
    for i in f_lines:
        line = i.strip()
        if line != '':
            mass.append(line)
        return len(mass)

def s_folder(f_path):
    lines = 0
    os.chdir(f_path)
    for a_f, b_f, c_f in os.walk(start):
        for x in c_f:
            if x.endswith('.py') and not x.startswith('_'):
                temp = lines_counter(os.path.join(a_f, x))
                lines += temp
        return lines

def log(logtext):
    f = open('log.txt', 'a')
    f.write(f"\n[log]{logtext} Время: {time.ctime(time.time())}")
    f.close()
    print(f"[log]{logtext} Время: {time.ctime(time.time())}")


def db_exec(table, search_info, search, where_search):
    for i in cursor.execute(f"SELECT {search} FROM {table} WHERE {search_info}={where_search}"):
        exet = i[0]
        if exet==None:
            return None
        else:
            return exet


def member_info(member_id, guild_id):
    info = []
    for i in cursor.execute(f"SELECT balance FROM member WHERE member={member_id} AND guildid={guild_id}"):
        balance = i[0]
    for i in cursor.execute(f"SELECT name FROM member WHERE member={member_id} AND guildid={guild_id}"):
        name = i[0]
    info.append(balance)
    info.append(name)
    return info


def member_update(member_id, guild_id, money):
    cursor.execute(f'UPDATE member SET balance = {money} WHERE member={member_id} and guildid={guild_id}')
    conn.commit()

def pars(url,who):
    mas = []
    doc = urllib.request.urlopen(sq).read().decode('cp1251', errors='ignore')
    match = re.findall("who", doc)
    if not (match is None):
        for ii in match:
            if (len(ii) < 25):
                mas.append(ii)
    mas = dict(zip(mas, mas)).values()
    a = []
    for y in mas: a.append('https://www.youtube.com/watch?v=' + y)
    print(a)