MAX_SIZE = 100

# Initialize an empty list to store the lists
fifo_list = []

# Initialize an empty set to keep track of the unique lists
unique_set = set()

import socketio
sio = socketio.Client()
sio.connect('http://localhost:8000')


# Add tuples to the FIFO set
def add_to_fifo_set(list_item):
    # Convert the list to a tuple for set membership testing
    tuple_item = tuple(list_item)
    
    # Check if the tuple is already in the set
    if tuple_item[1] in unique_set:
        return False

    # Add the list to the list and set
    print(f"Adding item -> {list_item}")
    fifo_list.append(list_item)
    unique_set.add(tuple_item[1])

    # Remove the oldest list if the list size exceeds the maximum
    if len(fifo_list) > MAX_SIZE:
        oldest_list = fifo_list.pop(0)
        unique_set.remove(tuple(oldest_list))

    return True




from telethon import TelegramClient
# from telethon.sync import TelegramClient, events, mark_read
import secrets,time,re,helpers

# import sys
# sys.path.append('../Secrets')

# import secrets 

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
    # print("hello")
  
    sending_list = [id,message.strip(),links]
    
    print(sending_list)
   
    flag =  add_to_fifo_set(sending_list)
     

    return flag
   
   



 


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
             
                
              if message.post and message.message != "" and process(message):

                  print(message)
                  text = message.message.strip()
                  print(text)
                  sio.emit('message', text)

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
        print("----> Request Reading...")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        print("----> Reading done !")
        print("______________________________________")
      
        

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