from telethon import TelegramClient
import secret,time,re,helpers
import asyncio
from telethon.tl.types import PeerUser, PeerChannel, PeerChat
import json,os
from tqdm import tqdm
import pygame
from telegram import Bot


bot_token = secret.TeleBot_Token2
chat_id = '@offers_and_loot_deals_zone'  
bot = Bot(token=bot_token)

async def send_broadcast(message):
    await bot.send_message(chat_id=chat_id, text=message)



imp_words = {"loot",'boat','big loot','umbrella','shirt','fast' , "big", "boat", "earphone", "protein powder","whey protein", "giveaway" , "give away", "acnofight", "acno", "fight facewash","Garnier Men"}
unread_count = 0

async def mark_all_messages_as_read():
    global unread_count
    async for dialog in client.iter_dialogs():
        if dialog.unread_count > 0:
            unread_count = unread_count+dialog.unread_count
            await client.send_read_acknowledge(dialog.input_entity, max_id=0)
    print(f"All {unread_count} messages marked as read.")


def to_json_string(message_list):
        message_dict = {
            "senderName": message_list[0],
            "messageText": message_list[1],
            "important": message_list[2],
            "views": message_list[3],
            "timee": message_list[4]
        }

        json_string = json.dumps(message_dict)
        # print(json_string)
        return json_string

client = 0
MAX_SIZE = 100
fifo_list = []
unique_set = set()
temp_list = []
Duplicate_count = 0
NOMS = 0 # Nymber of message sent to websocket count

def add_to_fifo_set(list_item):
    # print("🔵 Start of add_to_fifo_set")

    global Duplicate_count,temp_list
    tuple_item = tuple(list_item)
    message = helpers.strip_links(tuple_item[1])
    message = message.lower().strip()

    if message in unique_set:
        Duplicate_count = Duplicate_count+1
        return False
    else:
        print(f"▶► Duplicate Message Found:- [{message}]")

    temp_list = list_item
    print(f"Duplicate count ————————> {Duplicate_count}")
    print(f"Unique Set size ————————> {len(unique_set)}")
    print(f"Fifo Set size ————————> {len(fifo_list)}")

    fifo_list.append(message)
    unique_set.add(message)

    if len(fifo_list) > MAX_SIZE:
        oldest_list = fifo_list.pop(0)
        unique_set.remove(oldest_list)

    return True


# API ID and hash key
api_id = secret.telegram_api_id
api_hash = secret.app_api_hash
session_file = 'Ritik_telegram_session'


# Create the client
while 1:
 try:
    print("Trying to connect to Telegram Client...")
    client = TelegramClient(session_file, api_id, api_hash)
    print("✅ Successfully connected !!!")
    break
 except Exception as e:
    print("🟡 Telegram Client connect Exception ->")
    print(f"Exception: {e}")


# Function to process the message
id_and_links_dict = {}

def process(message_object, Sender):
    message = message_object.message
    important = any(word.lower() in message.lower() for word in imp_words)
    timee = str(message_object.date.hour) + ":" + str(message_object.date.minute)
    sending_list = [Sender, message.strip(), important, message_object.views, timee]
    flag = add_to_fifo_set(sending_list)
    return flag 


import shutil

def print_horizontal_line(character):
    terminal_width = shutil.get_terminal_size().columns
    line = character * terminal_width
    print(line)


async def main():
    global NOMS
    await client.start()
    await mark_all_messages_as_read()

    while 1:
        try:
            async for dialog in client.iter_dialogs():
                if dialog.unread_count > 0:
                    print(f"{dialog.unread_count} UNREAD from ————————> {dialog.name.upper()} ")
                    messages = await client.get_messages(dialog.input_entity, limit=dialog.unread_count)
                    for message in messages:
                        try:
                            try:
                                entity = await client.get_entity(PeerChannel(channel_id=int(message.peer_id.channel_id)))
                                Sender = entity.title
                            except:
                                entity = await client.get_entity(PeerUser(user_id=int(message.peer_id.user_id)))
                                Sender = entity.first_name + " " + entity.last_name

                            if message.post and message.message != "" and process(message, Sender):

                                print_horizontal_line("↔")   
                                print(message.message)

                                try :
                                  await send_broadcast(str(message.message))
                                except Exception as e:
                                    print(f"🟡  Could not send message because: {e}")

                                NOMS += 1
                                print(f"NOMS   ————————> {NOMS}")
                                # asyncio.sleep(2)

                            if message.post:
                                # pass
                                await client.send_read_acknowledge(dialog.input_entity, message)

                        except Exception as e:
                            print(f"\n🟡 Exception in inner loop: {e}")
                            if "going away" in str(e):
                                try:
                                    if not client.is_connected():
                                      await client.start()
                                except Exception as e:
                                    print("🟡 Was 'Going Away' then Client Start Exception ->")
                                    print(f"Exception: {e}")
                            print_horizontal_line("↔") 
                            print(client.is_connected())  

            if dialog.unread_count == 0:
                pass

        except Exception as e:
            print(f"\n🟡 Exception in outer loop: {e}")
        print(f"* Duplicate Count:      {Duplicate_count}")
        print(f"* Unread Count was:     {unread_count}")
        print(f"* fifo_list size:       {len(fifo_list)}")
        print(f"* unique_set size:      {len(unique_set)}")
        print(f"* temp_list size:       {len(temp_list)}")
        print_horizontal_line("=")

        if client.is_connected:
            total_iterations = 10
            print(f"🔵 Client is connected, reading new messages again after {total_iterations} seconds...")
            for _ in tqdm(range(total_iterations)):
                time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif not client.is_connected: 
            print("❌ Client is not connected !!!") 


if __name__ == '__main__':
    asyncio.run(main())
