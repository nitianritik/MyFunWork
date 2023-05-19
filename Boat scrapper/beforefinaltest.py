from telethon import TelegramClient
import secrets,time,re,helpers
import asyncio
from telethon.tl.types import PeerUser, PeerChannel, PeerChat
import json
import websockets

imp_words = {"loot",'boat','big loot','umbrella','shirt','fast' , "big", "boat", "earphone", "protein powder","whey protein", "giveaway" , "give away"}



def to_json_string(message_list):
        message_dict = {
            "senderName": message_list[0],
            "messageText": message_list[1],
            # "links": message_list[2]
             "important": message_list[2]
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
    global Duplicate_count
    tuple_item = tuple(list_item)
    
    if tuple_item[1] in unique_set:
        Duplicate_count = Duplicate_count+1
        return False

    global temp_list
    temp_list = list_item
    print(f"Duplicate count ----> {Duplicate_count}")
    print(f"Unique Set size ----> {len(unique_set)}")

    fifo_list.append(list_item)
    unique_set.add(list_item[1])

    if len(fifo_list) > MAX_SIZE:
        oldest_list = fifo_list.pop(0)
        unique_set.remove(oldest_list[1])

    return True




# API ID and hash key
api_id = secrets.telegram_api_id
api_hash = secrets.app_api_hash

# Create the client
while 1:
 try:
    print("Trying to commect to Telegram Client...")
    client = TelegramClient('Ritik_telegram_session', api_id, api_hash)
    print("Successfully connected !!!")
    break
 except Exception as e:
    print(f"Exception: {e}")

#Funtion to process the message
id_and_links_dict = {}

def process(message_object,Sender):
    # id = message_object.id
    # message = helpers.strip_links(message_object.message)
    message = message_object.message
    # links = helpers.get_link(message_object.message)
    important  = any(word.lower() in message.lower() for word in imp_words)
    sending_list = [Sender,message.strip(),important]
    flag =  add_to_fifo_set(sending_list)
    return flag 


# Set to search the keyword required in the meassage
async def send_message(websocket, path):
    global NOMS
    flag = False
    try:
        # Connect to Telegram
        await client.start()
        print("🔵 Client Started.")
        async for dialog in client.iter_dialogs():
            if dialog.unread_count > 0:
                unread  = dialog.unread_count
                print("THIS IS UNREAD CONT -------------> ",end=" ")
                print(unread)
                messages = await client.get_messages(dialog.input_entity, limit=dialog.unread_count)
                for message in messages:
                    # print(message)
                    if unread==0: return
                    try:
                        try:
                            entity = await client.get_entity(PeerChannel(channel_id=int(message.peer_id.channel_id)))
                            Sender = entity.title
                            # print("*****************")
                            # print(entity)
                            # print("*****************")
                        except:
                            
                            print("*****************")
                            print(entity)
                            print("*****************")
                            entity = await client.get_entity(PeerUser(user_id=int(message.peer_id.user_id)))
                            Sender = entity.first_name + " " + entity.last_name
                            time.sleep(20)
                        if message.post and message.message != "" and process(message, Sender):
                            L = "\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            M = str(message.message).replace('\n\n', '\n')
                            M = f"🟣 FROM➖  {entity.title} \n\n🟡  MESSAGE➖ \n{M}\n"
                            print(L+M)
                            await websocket.send(to_json_string(temp_list))
                            NOMS = NOMS+1
                            print(f"NOMS   ----> {NOMS}")
                            # time.sleep(1)
                            #---------------- MARK AS READ ----------------------
                            await client.send_read_acknowledge(dialog.input_entity, message)

                    except Exception as e:
                        if dialog.unread_count==0: break
                        print(f"\n🔴Exception in inner loop: {e}")                        
                        # time.sleep(3)
                        if "going away" in str(e): return
                    unread = unread-1

                if flag: print("Exiting -> going to initian of send_messsage funtion");  break
        if dialog.unread_count==0: print("======== inside if ======="); loop.stop(); loop.close()

    except Exception as e:
        print(f"\n🔴Exception in outer loop: {e}")


start_server = websockets.serve(send_message, "localhost", 8000)
flag = False
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = asyncio.get_event_loop().run_until_complete(start_server)
    while 1:
        time.sleep(5)
        print("----> Request Reading...")
        if flag: 
            pass
        asyncio.get_event_loop().run_forever()
        print("----> Reading done !")
        flag = True

        print("______________________________________")
      
        
