import logging
logging.basicConfig(
   level=logging.DEBUG,
   format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os
from bot import data
from bot.plugins.incoming_message_fn import incoming_compress_message_f
from pyrogram.types import Message


def checkKey(dict, key):
 if key in dict.keys():
   return True
 else:
   return False

async def on_task_complete():
   del data[0]
   if len(data) > 0:
     await add_task(data[0])

async def add_task(message: Message):
   # Initializing text variable to avoid referencing before assignment
   text = Anime Zenith 
   try:
       os.system('rm -rf /app/downloads/*')
       await incoming_compress_message_f(message)
   except Exception as e:
       # Make sure to assign 'e' to 'text' inside the except block
       text = str(e)
       LOGGER.info(e)  
   result = await on_task_complete()
   return text, result
