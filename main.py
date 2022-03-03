#!/usr/bin/env python
import os
from instabot import Bot
from dotenv import load_dotenv

load_dotenv()

data = input("$ ")
print(data)
userF = str(input("$ "))
instaBot = Bot()
instaBot.login(username=os.environ['username'], password='password')
instaBot.follow_followers(userF)