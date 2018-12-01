import discord
import asyncio
import sys
import json
import time
import random
import requests
import dhooks
from pathlib import Path
import string
import Commands
client = discord.Client()
regular_commands = {}
hook = dhooks.Webhook('https://discordapp.com/api/webhooks/516092910081409058/dQ1YJOs3qwD57lM6CH9nhChJyhVO39Oc1YchGpUQE3f1qvpHIu8EXptI-_qlXUVxBjkG')
def KeyGen(size=1979, chars=string.ascii_uppercase + string.digits):
	global Key
	Key = ''.join(random.choice(chars) for _ in range(size)) 
class commands(object):
	def register(command, exemplearguments, arguments):
		regular_commands[f'{command}'] = {'arguments': f'{arguments}', 'exemple_arguments': f'{exemplearguments}'}
	def info(command):
		return regular_commands[f'{command}']['exemple_arguments'], regular_commands[f'{command}']['arguments']
	def remove(command):
		regular_commands.pop(command)
class server(object):
	def getInfo(id):
		server_path = Path(f"Servers/{id}.json")
		if server_path.exists():
			info = json.load(open(f'Servers/{id}.json'))
			if not info['commands']:
				info['commands'] = "0"
				f.write(json.dumps(info))
			return info
		else:
			with open(f'Servers/{id}.json', 'w') as f:
				x = json.load(open(f'ServerBase.json'))
				x['id'] = id
				f.write(json.dumps(x))
				return x
commands.register('comousar', 'comando', 'say')
commands.register('say', 'messagem', 'sou lindo')
commands.register('avatar','<@516116193044725780>', '@usuario')
commands.register('perfil', '<@516116193044725780>', '@usuario')
commands.register('img', 'bacalhau', 'imagem')
commands.register('yt', 'Goats', 'vídeo')
commands.register('invite', '', '')
commands.register('weather', 'Belo Horizonte', 'cidade')
commands.register('clear', '100', 'nº de linhas')
commands.register('mute', '<@516116193044725780>', '@usuario')
commands.register('ban', '<@516116193044725780>', '@usuario')
commands.register('tempmute', '<@516116193044725780> 10 min', '@usuario tempo tipo')
commands.register('play', 'Dark Knight', 'musica')
commands.register('queue', ' ', '' )
commands.register('stop', '', '')
commands.register('pause', '', '')
commands.register('skip', '', '')
commands.register('config', 'prefix !', 'nome valor')
commands.register('command', 'oi "oi"', 'comando resposta')
commands.register('wegotthem', 'SD756DS...', 'chave')
commands.register('keygen', '', '')
def ComoUsar(command):
	if command in regular_commands:
		args, exempleagrs = commands.info(command)
	embed=discord.Embed(title=f"Como usar", description=f"Aqui está a sintaxe do comando **{command}**\n**Uso Correto**: `{command} {args}`\n**Exemplo de uso**: `{command} {exempleagrs}`")
	return embed
@client.event

async def on_message(message):
	server_info = server.getInfo(f"{message.server.id}")
	prefix = server_info['prefix']
	do = Commands.handler(message, client)
	await do
@client.event
async def on_ready():
	await client.change_status(game=discord.Game(name='Jogos! ;)'))
	KeyGen()
	print(f"[+] Logged as {client.user.name}")
	await client.send_message(client.get_channel('518178372493246482'), "Key generated:")
	await client.send_message(client.get_channel('518178372493246482'), f"{Key}")
client.run(f"NTE2MTE2MTkzMDQ0NzI1Nzgw.Dtu-yg.8y-5tV-e4qqmE9Uhub5sWio4w7g")