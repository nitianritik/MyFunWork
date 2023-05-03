from telethon import TelegramClient
import secrets,time,re,helpers
import asyncio
from telethon.tl.types import PeerUser, PeerChannel, PeerChat
import json



def to_json_string(message_list):
        message_dict = {
            "senderName": message_list[0],
            "messageText": message_list[1],
            "links": message_list[2]
        }

        json_string = json.dumps(message_dict)
        return json_string



client = 0
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
    id = message_object.id
    # message = helpers.strip_links(message_object.message)
    message = message_object.message
    links = helpers.get_link(message_object.message)
    sending_list = [Sender,message.strip(),links]
    flag =  add_to_fifo_set(sending_list)
    return flag 


# Set to search the keyword required in the meassage
keyword_set = {"loot", "big", "boat", "earphone", "protein powder","whey protein", "giveaway" , "give away"}
import websockets
async def send_message(websocket, path):
    global NOMS
    flag = False
    try:
        # Connect to Telegram
        await client.start()
        async for dialog in client.iter_dialogs():
            if dialog.unread_count > 0:
                messages = await client.get_messages(dialog.input_entity, limit=dialog.unread_count)
                for message in messages:
                    try:
                        entity = await client.get_entity(PeerChannel(channel_id=int(message.peer_id.channel_id)))
                        Sender = entity.title

                        if message.post and message.message != "" and process(message, Sender):
                            L = "\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                            M = str(message.message).replace('\n\n', '\n')
                            M = f"🟣 FROM➖  {entity.title} \n\n🟡  MESSAGE➖ \n{M}\n"
                            print(L+M)
                            await websocket.send(to_json_string(temp_list))
                            NOMS = NOMS+1
                            print(f"NOMS   ----> {NOMS}")
                            time.sleep(1)
                            #---------------- MARK AS READ ----------------------
                            # await client.send_read_acknowledge(dialog.input_entity, message)

                    except Exception as e:
                        print(f"\n🔴Exception in inner loop: {e}")                        
                        # time.sleep(3)
                        if "going away" in str(e): flag = True; break
                if flag: print("Exiting -> going to initian of send_messsage funtion"); break
    except Exception as e:
        print(f"\n🔴Exception in outer loop: {e}")



start_server = websockets.serve(send_message, "localhost", 8000)


if __name__ == '__main__':
    while 1:
        time.sleep(5)
        print("----> Request Reading...")
        loop = asyncio.get_event_loop()
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

        print("----> Reading done !")
        # print("______________________________________")
      
        

''''

ALL OF THE ATTRIBUTES OF MESSAGE


id: The unique identifier for the message.
peer_id: The ID of the chat or channel where the message was sent.
date: The date and time when the message was sent.
message: The text content of the message.
out: A boolean indicating whether the message was sent by the current user.
mentioned: A boolean indicating whether the message contains a mention of the current user.
media_unread: A boolean indicating whether the message has been marked as unread.
silent: A boolean indicating whether the message was sent silently.
post: A boolean indicating whether the message is a post.
from_scheduled: A boolean indicating whether the message was sent as a scheduled message.
legacy: A boolean indicating whether the message is a legacy message.
edit_hide: A boolean indicating whether the message was hidden due to editing.
pinned: A boolean indicating whether the message is pinned.
noforwards: A boolean indicating whether the message cannot be forwarded.
from_id: The ID of the user who sent the message, if available.
fwd_from: The information about the forwarded message, if applicable.
via_bot_id: The ID of the bot through which the message was sent, if applicable.
reply_to: The ID of the message to which this message is a reply, if applicable.
media: The media content of the message, if any.
reply_markup: The reply markup of the message, if any.
entities: The entities (such as URLs or hashtags) present in the message, if any.
views: The number of views the message has received.
forwards: The number of times the message has been forwarded.
replies: The information about the replies to the message, if any.
edit_date: The date and time when the message was last edited, if applicable.
post_author: The author of the post, if applicable.
grouped_id: The ID of the group to which the message belongs, if applicable.
reactions: The reactions to the message, if any.
restriction_reason: The reasons for which the message is restricted, if any.
ttl_period: The time-to-live period for the message, if applicable.


'''