from telethon import TelegramClient
#from telethon.sync import TelegramClient, events, mark_read

import secrets
import time
# Your API ID and hash key
api_id = secrets.telegram_api_id
api_hash = secrets.app_api_hash

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # Create the client

   try:
    # client = TelegramClient('session_name', api_id, api_hash)

    # # Connect to Telegram
    await client.start()

    # Get all dialogs (chats and channels)
    async for dialog in client.iter_dialogs():
        # Filter out dialogs with unread messages
        if dialog.unread_count > 0:
            messages = await client.get_messages(dialog.input_entity, limit=dialog.unread_count)
            # Print the messages from the unread dialogs
            for message in messages:   
                print(message.message.strip())
                if message.message != "":
                  print("\n----------------------------------------------\n")
                #print(f"MESSAGE: \n {message.message}\n  TYPE: \n {type(message.message)} ")
                await client.send_read_acknowledge(dialog.input_entity, message)
                #await client.mark_read(dialog.input_entity, message)

   except Exception as e:
      pass
      #print(f"Exception: {e}")
                

if __name__ == '__main__':
    import asyncio

    while 1:
        time.sleep(5)
        #print("----> Request Reading...")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        #print("----> Reading done !")
        # print("______________________________________")
      
        
