from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEKCJBgq8KxpydoS5K4XW4gWtjZ_8HqYAAC3AIAAqBRaFXazyUnPKCKIB8E")
    await message.reply_text(                               
        f"""<b>Hey {message.from_user.mention} !!
\nI'm Here to Play music In your voice chat...
maintain by SPRAYGOD..✨
\nuse this inline buttons to know more 😉😉.
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚑 Support group 🚑", url="https://t.me/TWO_AM_CHATS")
                  ],[
                    InlineKeyboardButton(
                        " channel", url="https://t.me/TWO_AM_FEELINGS"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Creator 👨‍💻", url="https://t.me/SPR4YGOD"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "💁 Assistant 💁", url="https://t.me/SPRAY_x_ASSISTANT"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/spray_X_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )
   
@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yoo Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚑 SUPPORT GROUP 🚑", url="https://t.me/TWO_AM_CHATS")
                ]
            ]
        )
   )     
            
@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
      await message.reply_text("""**Cᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴍ ғᴏʀ ʜᴇʟᴘ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🆘 help 🆘", url="https://t.me/spray_X_bot?start=help")
                ]
            ]
        )
   )  
            
@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n❖ /play <song name> - play song you requested
❖ /dplay <song name> - play song you requested via deezer
❖ /splay <song name> - play song you requested via jio saavn
❖ /playlist - Show now playing list
❖ /current - Show now playing
❖/song <song name> - download songs you want quickly
❖ /search <query> - search videos on youtube with details
❖ /deezer <song name> - download songs you want quickly via deezer
❖ /saavn <song name> - download songs you want quickly via saavn
❖ /video <song name> - download videos you want quickly
\n*Admins only*
✪ /player - open music player settings panel
✪ /pause - pause song play
✪ /resume - resume song play
✪ /skip - play next song
✪ /end - stop music play
✪ /userbotjoin - invite assistant to your chat
✪ /admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/TWO_AM_FEELINGS"
                    ),
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/TWO_AM_CHATS"
                    )
                ]
            ]
        )
    )                
