import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from ShizukaXMusic.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "📻᎘ᷩ-ᷧ-ⷷ࿎ᷓ𝀚ᷤ𝀚ⷮ𝀚ⷶ𝀚ᷣ𝀚ⷮ𝀚࿆ⷷᷘ🎧"
    elif 10 < anon < 20:
        bar = "ﮩ٨ــﮩ٨ـﮩ♡ﮩ٨ﮩﮩ٨ـ"
    elif 20 <= anon < 30:
        bar = "ﮩﮩ٨ـ᯳᯳᯳᯳᯳᯳᯳᯳᯳᯳᯳᯳᯳ᷟᷴᷤᷝᷗᷫⷷⷷᷯᷝᷠᷚﮩ٨ﮩ"
    elif 30 <= anon < 40:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ﮩـ"
    elif 40 <= anon < 50:
        bar = "ﮩ٨ﮩﮩ٨ـ٨ᱼᷫᱼⷷᱼⷷᱼᷞᱼᱼᷡᱼⷪᱼᱼⷬᱼⷶᱼᷝᱼᷠﮩﮩ٨ـ"
    elif 50 <= anon < 60:
        bar = "ﮩ٨ﮩﮩ٨ـ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= anon < 70:
        bar = "٨ﮩﮩ٨ـᱼᷫᱼⷷᱼⷷᱼᷞᱼᱼⷮᱼⷩᱼⷷᱼᱼᷞᱼⷱᱼᷣᱼᷝᱼᷗᱼᷤﮩ٨ﮩﮩ٨ـ"
    elif 70 <= anon < 80:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= anon < 95:
        bar = "ﮩ٨ﮩᱼᷫᱼⷷᱼⷷᱼᷞᱼᷝᱼᷡᱼᷛ♪ᱼᷘᱼⷷᱼᷞᱼⷷᱼⷮᱼⷷᱼᷘ٨ـﮩﮩ"
    else:
        bar = "⇜ɢᴏɪɴɢ ᴛᴏ ᴇɴᴅ⇝"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="⩺",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⇅", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="༒", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="⧐⧐⧽", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⬗", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⦳ ᴄʟᴏsᴇ ⦴", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "📻᎘ᷩ-ᷧ-ⷷ࿎ᷓ𝀚ᷤ𝀚ⷮ𝀚ⷶ𝀚ᷣ𝀚ⷮ𝀚࿆ⷷᷘ🎧"
    elif 10 < anon < 20:
        bar = "ﮩ٨ــﮩ٨ـﮩ♡ﮩ٨ﮩﮩ٨ـ"
    elif 20 <= anon < 30:
        bar = "ﮩﮩ٨ـ᯳᯳᯳᯳᯳᯳᯳᯳᯳᯳᯳᯳᯳ᷟᷴᷤᷝᷗᷫⷷⷷᷯᷝᷠᷚﮩ٨ﮩ"
    elif 30 <= anon < 40:
        bar = "ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ﮩـ"
    elif 40 <= anon < 50:
        bar = "ﮩ٨ﮩﮩ٨ـ٨ᱼᷫᱼⷷᱼⷷᱼᷞᱼᱼᷡᱼⷪᱼᱼⷬᱼⷶᱼᷝᱼᷠﮩﮩ٨ـ"
    elif 50 <= anon < 60:
        bar = "ﮩ٨ﮩﮩ٨ـ♡ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= anon < 70:
        bar = "٨ﮩﮩ٨ـᱼᷫᱼⷷᱼⷷᱼᷞᱼᱼⷮᱼⷩᱼⷷᱼᱼᷞᱼⷱᱼᷣᱼᷝᱼᷗᱼᷤﮩ٨ﮩﮩ٨ـ"
    elif 70 <= anon < 80:
        bar = "ﮩ♡٨ـﮩﮩ٨ـﮩ٨ـﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= anon < 95:
        bar = "ﮩ٨ﮩᱼᷫᱼⷷᱼⷷᱼᷞᱼᷝᱼᷡᱼᷛ♪ᱼᷘᱼⷷᱼᷞᱼⷷᱼⷮᱼⷷᱼᷘ٨ـﮩﮩ"
    else:
        bar = "⇜ɢᴏɪɴɢ ᴛᴏ ᴇɴᴅ⇝"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="⩺",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⇅", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⧐⧐⧽", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⬗", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⦳ ᴄʟᴏsᴇ ⦴", callback_data=f"close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⩺",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⇅", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="༒", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="⧐⧐⧽", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⬗", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⎏ ᴄʟᴏsᴇ ⎐", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⩺",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⇅", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⧐⧐⧽", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⬗", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⦳ ᴄʟᴏsᴇ ⦴", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="⦳ ᴄʟᴏsᴇ ⦴", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="⩺",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="⇅", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="༒", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="⧐⧐⧽", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="⬗", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⦳ ᴄʟᴏsᴇ ⦴", callback_data=f"close"
            )
        ],
    ]
    return buttons
