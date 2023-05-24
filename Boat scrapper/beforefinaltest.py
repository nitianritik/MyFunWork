from telethon import TelegramClient
import secrets,time,re,helpers
import asyncio
from telethon.tl.types import PeerUser, PeerChannel, PeerChat
import json,os
import websockets
from tqdm import tqdm

imp_words = {"loot",'boat','big loot','umbrella','shirt','fast' , "big", "boat", "earphone", "protein powder","whey protein", "giveaway" , "give away"}



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
loop = 0
task  = 0
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
        # print_horizontal_line(":")
        # print(unique_set)
        # print(" ")
        # print(oldest_list)
        # print_horizontal_line(":")
        # print("🔵 End of add_to_fifo_set")
        unique_set.remove(oldest_list)

    return True




# API ID and hash key
api_id = secrets.telegram_api_id
api_hash = secrets.app_api_hash

# Create the client
while 1:
 try:
    print("Trying to commect to Telegram Client...")
    client = TelegramClient('Ritik_telegram_session', api_id, api_hash)
    print("✅ Successfully connected !!!")
    break
 except Exception as e:
    print("🟡 Telegram Client connect Exceptiton ->")
    print(f"Exception: {e}")

#Funtion to process the message
id_and_links_dict = {}

def process(message_object,Sender):
    # id = message_object.id
    # message = helpers.strip_links(message_object.message)
    message = message_object.message
    # links = helpers.get_link(message_object.message)
    important  = any(word.lower() in message.lower() for word in imp_words)
    timee = str(message_object.date.hour)+":"+str(message_object.date.minute)
    sending_list = [Sender,message.strip(),important,message_object.views,timee]
    # print(sending_list)
    flag =  add_to_fifo_set(sending_list)
    return flag 


import shutil

def print_horizontal_line(character):
    terminal_width = shutil.get_terminal_size().columns
    line = character * terminal_width
    print(line)

import asyncio
import websockets

async def send_message(websocket, path):
    global NOMS
    await client.start()

    while 1:
       
        try:
            async for dialog in client.iter_dialogs():
                # print(dialog)
                # print(" ")
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
                                await asyncio.sleep(20)  # Use asyncio.sleep instead of time.sleep
                                
                            if message.post and message.message != "" and process(message, Sender):
                                M = str(message.message).replace('\n\n', '\n')
                                # ✅❌➡️▶️ ▶►
                                M = f"▶► FROM  {entity.title} \n▶►  MESSAGE \n{M}\n"
                                print_horizontal_line("↔")   
                                print(M)
                                # print(temp_list)
                                await websocket.send(to_json_string(temp_list))
                                NOMS += 1
                                print(f"NOMS   ————————> {NOMS}")
                            if message.post:
                                pass
                                # await client.send_read_acknowledge(dialog.input_entity, message)

                        except Exception as e:
                            print(f"\n🟡 Exception in inner loop: {e}")
                            # print_horizontal_line(".")
                            # print(message)
                            # print_horizontal_line(".")
                            # asyncio.sleep(3)  # Use asyncio.sleep instead of time.sleep
                            if "going away" in str(e):
                                try:
                                    await client.start()
                                except Exception as e:
                                    print("🟡 Was 'Going Away' then Client Start Exceptiton ->")
                                    print(f"Exception: {e}")
                            print_horizontal_line("↔")   



            if dialog.unread_count == 0:
                pass

                #print(f"Unread Count is {dialog.unread_count} now")
                # loop.stop()
                # loop.close()

        except Exception as e:
            print(f"\n🟡 Exception in outer loop: {e}")

        print_horizontal_line("=")

        if client.is_connected:
          total_iterations = 10
          print(f"🔵 Client is connnected, reading new messages again after {total_iterations} seconds...")
          for _ in tqdm(range(total_iterations)):
             time.sleep(1)
          os.system('cls' if os.name == 'nt' else 'clear')

        elif not client.is_connected:
            print("❌ Client is not connected !!!") 
    
if __name__ == '__main__':
    start_server = websockets.serve(send_message, "localhost", 8000)
    # start_server = websockets.serve(send_message, "localhost", 8000)
    loop = asyncio.get_event_loop()
    task = loop.run_until_complete(start_server)

    try:
        print("Server started!")
        loop.run_forever()
    finally:
        task.cancel()
        loop.run_until_complete(task)


