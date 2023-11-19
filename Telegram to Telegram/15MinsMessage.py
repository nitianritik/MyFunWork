# from telethon import TelegramClient
# import secret,time,re,helpers
# import asyncio
# from telethon.tl.types import PeerUser, PeerChannel, PeerChat
# from tqdm import tqdm
# from telegram import Bot


# bot_token = secret.TeleBot_Token2
# # chat_id = '@offers_and_loot_deals_zone'  
# chat_id = '@theunknownlooterz'
# bot = Bot(token=bot_token)

# async def send_broadcast(message):
#     await bot.send_message(chat_id=chat_id, text=message)



# # API ID and hash key
# api_id = secret.telegram_api_id
# api_hash = secret.app_api_hash
# session_file = 'Ritik_telegram_session'


# # Create the client
# while 1:
#  try:
#     print("Trying to connect to Telegram Client...")
#     client = TelegramClient(session_file, api_id, api_hash)
#     print("✅ Successfully connected !!!")
#     break
#  except Exception as e:
#     print("🟡 Telegram Client connect Exception ->")
#     print(f"Exception: {e}")

# this_message = '''#buyer 

# Amazon prime subscription needed 👈
# for 1 month

# 👉 Price DM kar dena '''


# async def main():
#     global NOMS
#     await client.start()
#     print("we are in main")
#     while 1:
#         try :
#             await send_broadcast(str(this_message))
#             print("Message Sent")
#         except Exception as e:
#             print(f"🟡  Could not send message because: {e}")
#         time.sleep(900)

# if __name__ == '__main__':
#     asyncio.run(main())












from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import time,secret

# Replace with your own values
API_ID = secret.telegram_api_id
API_HASH = secret.app_api_hash
SESSION_STRING = 'Ritik_telegram_session'
GROUP_USERNAME = 'theunknownlooterz'

# Create a TelegramClient instance
client = TelegramClient(SESSION_STRING, API_ID, API_HASH)

async def send_message():
    await client.start()
    this_message = '''#buyer 

    Amazon prime subscription needed 👈
    for 1 month

    👉 Price DM kar dena '''
    await client.send_message(GROUP_USERNAME, this_message)
    await client.disconnect()

# Main loop
while True:
    try:
        # Send a message
        client.loop.run_until_complete(send_message())
        
        # Wait for 15 minutes
        time.sleep(15 * 60)
    
    except Exception as e:
        # Handle any error that occurs
        print("An error occurred:", e)
