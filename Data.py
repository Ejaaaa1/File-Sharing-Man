# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Untuk mengecek bot hidup
 └ /uptime - Untuk melihat status bot 
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - Untuk melihat logs bot
 ├ /vars - Untuk melihat variable bot
 ├ /setvar - Untuk mengatur var dengan command dibot
 ├ /delvar - Untuk menghapus var dengan command dibot
 ├ /getvar - Untuk melihat salah satu var dengan command dibot
 ├ /users - Untuk melihat statistik pengguna bot
 ├ /batch - Untuk membuat link lebih dari satu file
 ├ /speedtest - Untuk Mengetes kecepatan server bot
 └ /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

👨‍💻 Develoved by @Lunatic0de</b>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} PROMO VVIP TERBATAS🥳


✅2GRUP VVIP TERBARU HANYA 50K 
5 GROUB 100K VVIP 
ALL. GROUB 300K DAPET SEMUA 

TERDIRI DARI ( VVIP INDO ,VVIP HIJAB, VVIP LIVE , VVIP JAV ,VVIP ASIAN , ONLYFANS , VVIP AMBIYAH ) 

❗️BONUS 2 VVIP BOCIL BAGI YANG JOIN VVIP SULTAN❗️

⚠️VVIP SULTAN PERMANEN  SAMPE TOBAT , DAN UPDATE SETIAP HARI⚠️


MINAT HUBUNGI : @ownervvipterbaru19

TESTIMONI: https://t.me/Testitermurah.

 • Creator: @{}
 • Source Code: <a href='https://github.com/mrismanaziz/File-Sharing-Man'>File-Sharing-Man v4</a>
 • Owner Repo: @mrismanaziz

👨‍💻 Develoved by @Lunatic0de</b>
"""
