import os
from instabot import Bot
from dotenv import load_dotenv

load_dotenv()

instaBot = Bot()
instaBot.login(username=os.environ['username'], password='password')
instaBot.unfollow_everyone()