message_1 = (
    "đđģ Hi, {m} and <b>Welcome.</b>\n\n"
    "đ­ @{bn} allows you to download"
    " media from TikTok, YouTube, Pinterest, Spotify and Instagram. "
    "To find out more about how to use me press the 'đŽ <b>Help</b>' button."
)
message_2 = "đ­ Hello {}!"
message_3 = (
    "đŽ <b>Help</b>\n\n"
    "<b>YouTube command:</b>\n"
    "Just type /song [song title]"
    " you can get audio or video from YouTube.\n"
    "You can also get lyrics from genius.com via me, use the command /lyrics [title]\n\n"
    "<b>TikTok command:</b>\n"
    "How to download video from TikTok?\n"
    "  <b>1.</b> Go to the TikTok app\n"
    "  <b>2.</b> Choose a video that interests you\n"
    "  <b>3.</b> Click on the âĒī¸ button or the three dots on the top right corner\n"
    "  <b>4.</b> Click the 'Copy' button\n"
    "  <b>5.</b> Send a link to the bot after using the /tiktok command, and in a couple of seconds you will receive a video without a watermark.\n\n"
    "<b>Pinterest command:</b>\n"
    "Pinterest has 3 types of media such as: Image, GIF, video.\n"
    "You just copy the link from pinterest to me by using the /pints [pint link] command.\n\n"
    "<b>Wikipedia command:</b>\n"
    "Just type /wiki [word] and I will look it up on Wikipedia.\n\n"
    "You can find this bot source code in github with type /source"
)
message_4 = (
    "âšī¸ <b>Info</b>\n\n"
    "Yue is a bot developed in <b>Python3</b>"
    " and uses <a href='https://github.com/pyrogram/pyrogram'>Pyrogram</a> as a framework with MongoDB as database.\n\n"
    "đ Version<b>:</b> {} | đŖ Channel<b>:</b> @yueblog"
)
# download module 
message_5 = "đ <b>Loading...</b>"
message_6 = "To download a song do /song [Song name]"
message_7 = (
    "{}\n\n"
    "<b>1.</b> <i>{}</i>\n<b>2.</b> <i>{}</i>\n<b>3.</b> <i>{}</i>\n<b>4.</b> <i>{}</i>\n<b>5.</b> <i>{}</i>\n"
    "<b>6.</b> <i>{}</i>\n<b>7.</b> <i>{}</i>\n<b>8.</b> <i>{}</i>\n<b>9.</b> <i>{}</i>\n<b>10.</b> <i>{}</i>"
)
message_9 = "đ Sorry, live videos are not supported."
message_10 = "đ Sorry this option is not for you, please search for yourself."
message_11 = "â Duration error, only allowed duration 1000seconds"
# bans module
message_12 = "đˇ You've been <b>banned</b>"
message_13 = "đ You've been <b>unbanned</b>"
message_14 = "đˇ {} [<code>{}</code>] has been <b>banned</b>"
message_15 = "đ {} [<code>{}</code>] has been <b>unbanned</b>"
message_16 = "đˇ <b>The user is already banned</b>"
message_17 = "đ <b>User not banned</b>"
message_18 = "â ī¸ <b>Invalid syntax</b>\nđ­ Use the <b>command specifying the ID</b> or replying to a <b>users message</b>"
message_19 = "\nâĸ <b>Due to:</b> {}"
# bot broadcast 
message_20 = "<b>Usage:</b> <code>/broadcast [your message]</code> or you can reply to a message."
message_21 = "â <b>Progress the broadcast message...</b> Will take <code>{}</code> seconds."
message_22 = "â Successfully broadcast message in {} chats"
# pinterest text
message_23 = "To get a pinterest media do /pints [Pinterest URL]"
message_24 = "â <b>Sending...</b>"
message_25 = (
   "<b>Pinterest Downloader</b>\n"
   "<a href='https://t.me/yueblog'>Channel</a> | <a href='https://t.me/shin_yue'>Developer</a>"
)
message_26 = "đ <b>No results found, please try again.</b>"
# TikTok Module
message_27 = "To download a tiktok video do /tiktok [TikTok URL]"
message_28 = "âĸ Via @Yuedlbot"
message_29 = "đ <b>No results found, please try again.</b>"
message_30 = "Sorry, I was unable to get information about this file.\nTry again later or send another link."

# button
from pyrogram import types

def keyboard_song(
    id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9, id_10, 
    duration_1, duration_2, duration_3, duration_4, duration_5, 
    duration_6, duration_7, duration_8, duration_9, duration_10, 
    user_id, value
):
    buttons = (
        types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(text='1', callback_data=f'download {id_1}|{duration_1}|{user_id}'),
                    types.InlineKeyboardButton(text='2', callback_data=f'download {id_2}|{duration_2}|{user_id}'),
                    types.InlineKeyboardButton(text='3', callback_data=f'download {id_3}|{duration_3}|{user_id}'),
                    types.InlineKeyboardButton(text='4', callback_data=f'download {id_4}|{duration_4}|{user_id}'),
                    types.InlineKeyboardButton(text='5', callback_data=f'download {id_5}|{duration_5}|{user_id}'),
                ],
                [
                    types.InlineKeyboardButton(text='6', callback_data=f'download {id_6}|{duration_6}|{user_id}'),
                    types.InlineKeyboardButton(text='7', callback_data=f'download {id_7}|{duration_7}|{user_id}'),
                    types.InlineKeyboardButton(text='8', callback_data=f'download {id_8}|{duration_8}|{user_id}'),
                    types.InlineKeyboardButton(text='9', callback_data=f'download {id_9}|{duration_9}|{user_id}'),
                    types.InlineKeyboardButton(text='10', callback_data=f'download {id_10}|{duration_10}|{user_id}')
                ],
                [
                    types.InlineKeyboardButton(text='x', callback_data=f'close |{user_id}'),
                    types.InlineKeyboardButton(text='Âģ', callback_data=f'change 1|{value}|{user_id}')
                ]
            ]
        )
    )
    return buttons

def keyboard_song2(
    id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9, id_10, 
    duration_1, duration_2, duration_3, duration_4, duration_5, 
    duration_6, duration_7, duration_8, duration_9, duration_10, 
    user_id, value
):
    buttons = (
        types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(text='1', callback_data=f'download {id_1}|{duration_1}|{user_id}'),
                    types.InlineKeyboardButton(text='2', callback_data=f'download {id_2}|{duration_2}|{user_id}'),
                    types.InlineKeyboardButton(text='3', callback_data=f'download {id_3}|{duration_3}|{user_id}'),
                    types.InlineKeyboardButton(text='4', callback_data=f'download {id_4}|{duration_4}|{user_id}'),
                    types.InlineKeyboardButton(text='5', callback_data=f'download {id_5}|{duration_5}|{user_id}'),
                ],
                [
                    types.InlineKeyboardButton(text='6', callback_data=f'download {id_6}|{duration_6}|{user_id}'),
                    types.InlineKeyboardButton(text='7', callback_data=f'download {id_7}|{duration_7}|{user_id}'),
                    types.InlineKeyboardButton(text='8', callback_data=f'download {id_8}|{duration_8}|{user_id}'),
                    types.InlineKeyboardButton(text='9', callback_data=f'download {id_9}|{duration_9}|{user_id}'),
                    types.InlineKeyboardButton(text='10', callback_data=f'download {id_10}|{duration_10}|{user_id}')
                ],
                [
                    types.InlineKeyboardButton(text='ÂĢ', callback_data=f'change 2|{value}|{user_id}')
                ]
            ]
        )
    )
    return buttons

def keyboard_down(id, duration, user_id):
    buttons = (
        types.InlineKeyboardMarkup(
            [
                [
                    types.InlineKeyboardButton(text="đŊī¸ Download Video", callback_data=f'video_ {id}|{duration}|{user_id}')
                ]
            ]
        )
    )
    return buttons


keyboard = (
    types.InlineKeyboardMarkup(
        [
            [
                types.InlineKeyboardButton(text='đŽ Help', callback_data='self_help'),
                types.InlineKeyboardButton(text='đŖ Channel', url='https://t.me/yueblog')
            ]
        ]
    )
)

back_kb = (types.InlineKeyboardMarkup([
     [types.InlineKeyboardButton(text='đ', callback_data='self_backhome')]])
)
