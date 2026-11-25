import random
from pyrogram import Client, filters
from pyrogram.types import Message
from info import EMOJI_MODE, REACTIONS


async def random_message_reaction(client: Client, message: Message):
    if not EMOJI_MODE or not message.from_user:
        return
    try:
        await message.react(emoji=random.choice(REACTIONS), big=True)
    except Exception:
        try:
            await message.react(emoji="⚡️")
        except Exception:
            pass


@Client.on_message(filters.private & filters.incoming, group=1)
async def react_to_private_messages(client: Client, message: Message):
    await random_message_reaction(client, message)


@Client.on_message(filters.channel & filters.incoming, group=1)
async def react_to_channel_posts(client: Client, message: Message):
    await random_message_reaction(client, message)
