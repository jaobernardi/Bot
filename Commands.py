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
def handler(message, client):
	if message.content == "oi":
		return client.send_message(message.channel, "Teste module top")