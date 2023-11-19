import secret
import asyncio
# import tracemalloc
from telegram import Bot


# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = secret.TeleBot_Token2
chat_id = '@offers_and_loot_deals_zone'  # Replace with your channel's username

# Create a bot instance
bot = Bot(token=bot_token)

# Define an async function to send the broadcast message
async def send_broadcast(message):
    await bot.send_message(chat_id=chat_id, text=message)

# Start the event loop and run the async function
asyncio.run(send_broadcast("Here is my message"))

# Optional: Stop the tracemalloc module
# tracemalloc.stop()





