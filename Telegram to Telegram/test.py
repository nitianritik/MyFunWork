import tkinter as tk
from telethon import TelegramClient
import secrets,time,re

# API ID and hash key
api_id = secrets.telegram_api_id
api_hash = secrets.app_api_hash

# Create the client
client = 0
while 1:
    try:
        print("Trying to connect to Telegram Client...")
        client = TelegramClient('Ritik_telegram_session', api_id, api_hash)
        print("Successfully connected !!!")
        break
    except Exception as e:
        print(f"Exception: {e}")

# Funtion to check links in the message
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
def contains_link(message):
    return pattern.search(message.lower()) is not None

# Set to search the keyword required in the meassage
keyword_set = {"loot", "big", "boat", "earphone", "protein powder","whey protein", "giveaway" , "give away"}

async def main():
    try:
        # Connect to Telegram
        await client.start()

        # Get all dialogs (chats and channels)
        async for dialog in client.iter_dialogs():
            # Filter out dialogs with unread messages
            if dialog.unread_count > 0:
                messages = await client.get_messages(dialog.input_entity, limit=dialog.unread_count)
                # Print the messages from the unread dialogs
                for message in messages:   
                    # Check if message contains links
                    contains_link = contains_link(message.message)

                    # Create the frame and the label for the message
                    frame = tk.Frame(root, bg='white', bd=2, relief=tk.GROOVE)
                    label = tk.Label(frame, text=message.message, bg='white', font=('Helvetica', 12))

                    # Add the frame and the label to the window
                    frame.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)
                    label.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)

                    # Update the chat
                    await client.send_read_acknowledge(dialog.input_entity, message)

    except Exception as e:
        pass

root = tk.Tk()
root.title('Telegram Messages')
root.geometry('800x600')

while True:
    import asyncio


    time.sleep(5)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

root.mainloop()
