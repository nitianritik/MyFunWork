from telethon import TelegramClient
import secrets,time,re,helpers
import asyncio
from telethon.tl.types import PeerUser, PeerChannel, PeerChat



MAX_SIZE = 100

fifo_list = []
added = []
removed = []
unique_set = set()

def add_to_fifo_set(list_item):
    tuple_item = tuple(list_item)
    
    if tuple_item[1] in unique_set:
        return False

    # print(f"Adding item -> {list_item}")
    added.append(list_item[0])
    print("ADDED = ", end="")
    for id in added: print(id, end=" | ")
    fifo_list.append(list_item)
    unique_set.add(tuple_item[1])

    if len(fifo_list) > MAX_SIZE:
        oldest_list = fifo_list.pop(0)
        removed.append(oldest_list[0])
        print("REMOVED = ", end="")
        for id in removed: print(id, end=" | ")
        unique_set.remove(tuple(oldest_list))

    return True




# API ID and hash key
api_id = secrets.telegram_api_id
api_hash = secrets.app_api_hash

# Create the client
client = 0
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

def process(message_object):
    id = message_object.id
    message = helpers.strip_links(message_object.message)
    links = helpers.get_link(message_object.message)
    sending_list = [id,message.strip(),links]
    # print(sending_list)
    flag =  add_to_fifo_set(sending_list)
    return flag 


# Set to search the keyword required in the meassage
keyword_set = {"loot", "big", "boat", "earphone", "protein powder","whey protein", "giveaway" , "give away"}

async def main():

   try:
    
    # Connect to Telegram
    await client.start()
    async for dialog in client.iter_dialogs():

        if dialog.unread_count > 0:
            messages = await client.get_messages(dialog.input_entity, limit=dialog.unread_count)
            for message in messages:
              if message.post and message.message != "" and process(message):
                  print("\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
                  entity = await client.get_entity(PeerChannel(channel_id=int(message.peer_id.channel_id)))
                  M = str(message.message)
                  M = M.replace('\n\n','\n')
                  print(f"🟣 FROM➖  {entity.title} \n\n🟡  MESSAGE➖ \n{M}\n")
                  time.sleep(3)
                  #---------------- MARK AS READ ----------------------
                #   await client.send_read_acknowledge(dialog.input_entity, message)

   except Exception as e:
      print(f"Exception: {e}")


if __name__ == '__main__':
    while 1:
        time.sleep(5)
        print("----> Request Reading...")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
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