import os
try:
    import discord
except ImportError:
    os.system('python -m pip install discord')

try:
    import schedule
except ImportError:
    os.system('python -m pip install schedule')
    
try:
    import plyer
except ImportError:
    os.system('python -m pip install plyer')
    
try:
    import colorama
except ImportError:
    os.system('python -m pip install colorama')


import discordBot.py