from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⎆ ⌜ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ⌟",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𐏕ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ𐏕",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⧮ sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="⎆ ⌜ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ⌟",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="𐏕ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ𐏕", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="⧠ Sᴜᴘᴘᴏʀᴛ⬏", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="⏍ Cʜᴀɴɴᴇʟ⬏", url=config.SUPPORT_CHANNEL
            ),
          ],
          [
            InlineKeyboardButton(
                text="『Oᴡɴᴇʀ』", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="✪ ʙᴀᴅ ʙᴏʏ ✪", url="https://t.me/badboybiografia"
            )
        ],
     ]
    return buttons
