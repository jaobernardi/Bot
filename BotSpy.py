import discord
import asyncio
import sys
import json
import time
import random
import requests
import dhooks
from pathlib import Path
client = discord.Client()

hook = dhooks.Webhook('https://discordapp.com/api/webhooks/516092910081409058/dQ1YJOs3qwD57lM6CH9nhChJyhVO39Oc1YchGpUQE3f1qvpHIu8EXptI-_qlXUVxBjkG')
def ServerInfo(id):
	server_path = Path(f"Servers/{id}.json")
	if server_path.exists():
		info = json.load(open(f'Servers/{id}.json'))
		return info
	else:
		with open(f'Servers/{id}.json', 'w') as f:
			x = json.load(open(f'ServerBase.json'))
			x['id'] = id
			f.write(json.dumps(x))
			return x
			
@client.event
async def on_message(message):
	server_info = ServerInfo(f"{message.server.id}")
	prefix = server_info['prefix']
	command = message.content.lower().startswith
	if command(prefix):
		args = message.content.split(" ")
		if command(prefix + "help"):
			await client.send_message(message.channel, "Version: ALPHA 1 SNPSHT:BG01")
@client.event
async def on_ready():
	await client.change_status(game=discord.Game(name='Jogos! ;)'))
	print(f"[+] Logged as {client.user.name}")
client.run(f"NTE2MTE2MTkzMDQ0NzI1Nzgw.Dtu-yg.8y-5tV-e4qqmE9Uhub5sWio4w7g")