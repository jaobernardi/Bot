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
def ComoUsar(command):
	if command in regular_commands:
		args, exempleagrs = commands.info(command)
	embed=discord.Embed(title=f"Como usar", description=f"Aqui está a sintaxe do comando **{command}**\n**Uso Correto**: `{command} {args}`\n**Exemplo de uso**: `{command} {exempleagrs}`")
	return embed
def handler(message, client):
	if message.content == "oi":
		return await client.send_message(message.channel, "Teste module top")
	
	
	
	
	
	
	
	
	
	
	