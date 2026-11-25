import logging
import random

from pyrogram import Client, filters
from info import EMOJI_MODE, REACTIONS

logger = logging.getLogger(__name__)


@Client.on_message(filters.channel, group=20)
async def random_channel_reaction(client, message):
    """Add one random configured reaction to every new channel post."""
    if not EMOJI_MODE or not REACTIONS or not message or not message.id:
        return

    try:
        emoji = random.choice(REACTIONS)
        await client.send_reaction(
            chat_id=message.chat.id,
            message_id=message.id,
            emoji=emoji
        )
        logger.info(
            "Added random reaction %s to channel %s message %s",
            emoji,
            message.chat.id,
            message.id
        )
    except Exception:
        logger.exception(
            "Could not react to channel %s message %s. "
            "Check that reactions are enabled and the bot is allowed to react.",
            getattr(message.chat, "id", "unknown"),
            getattr(message, "id", "unknown")
        )
