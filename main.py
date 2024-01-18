import logging
from telegram.ext import *

with open("token.txt", "r") as f:
    TOKEN = f.read()

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# Source and target group chat IDs
with open("source_chat_id.txt", "r") as f:
    source_chat_id = int(f.read())
with open("target_chat_id.txt", "r") as f:
    target_chat_id = int(f.read())

# Define the message handler function
async def forward_message(update, context):
    message =  update.message
    if [x for x in message.text.split(" ") if x.lower() == 'bar']:
        await context.bot.forward_message(chat_id=target_chat_id,
                                    from_chat_id=source_chat_id,
                                    message_id=message.message_id)


application = Application.builder().token(TOKEN).build()

# Register the message handler
application.add_handler(MessageHandler(filters.TEXT, forward_message))

# Start the bot
application.run_polling()