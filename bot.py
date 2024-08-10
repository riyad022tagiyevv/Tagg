import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.types import ChannelParticipantsBots
from telethon.tl.functions.users import GetFullUserRequest
from time import time
from datetime import datetime
from random import choice
from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import time
from os import remove
import datetime
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import asyncio
import datetime
import shutil, psutil, traceback, os
import random
import string
import time
import traceback
import aiofiles
from pyrogram import Client, filters, __version__
from pyrogram.types import Message
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)
from pyrogram import Client, filters, idle
from pyrogram import Client as USER

from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import pyrogram
from datetime import datetime
from telethon.errors.rpcerrorlist import MessageDeleteForbiddenError
from mesaj.tag import soz, heyvan, emoji, bayrag, mafia, seher, sehidler
from mesaj.random import taım, foto

import secrets
import aiohttp
from kolge.komekci import random_line
 
 
	
	

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
BOT_ID = os.environ.get("BOT_ID")
OWNER_ID = os.environ.get("OWNER_ID")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )




anlik_calisan = []

ozel_list = [2074934667]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}



@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")


@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")



# Başlanğıc Button

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
  await event.reply(f"**👋 Salam {ad}\nMən  N A Z R Y N 𝗧𝗮𝗴𝗴𝗲𝗿**\n**N A Z R Y N Federasiyasının Rəsmi Tağ botuyam**\n**⚡ N A Z R Y N 𝗧𝗮𝗴𝗴𝗲𝗿 İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm**\n**Əmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun**\n**ℹ Mənim Qruplarda Asan Və Sürətli İşləyə Bilməyim Üçün Mənə Qrupunuzda Sadə Adminlik Vermənizi Rica Edirem**",
                    buttons=(
			    
		      [Button.url('➕ Qrupa Əlavə Et ➕', 'https://t.me/NezrinTaggerbot?startgroup=a'),
                      Button.url('🦁 D͏əs͏t͏ək͏', f'https://t.me/nezrinsupp')],
                      [Button.url('🇦🇿 ᴋᴜʀᴜᴄᴜ 🚫', f'https://t.me/hmnevar'),
                      Button.inline("⚙ Əmrlər", data="help")],
                    ),
                    link_preview=False
		   )
 
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
    await event.edit(f"**👋 Salam {ad}\n ⚡Mən  N A Z R Y N 𝗧𝗮𝗴𝗴𝗲𝗿**\n**N A Z R Y N Federasiyasının Rəsmi Tağ botuyam**\n**⚡ N A Z R Y N 𝗧𝗮𝗴𝗴𝗲𝗿 İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm**\n**ℹƏmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun**\n**ℹ Mənim Qruplarda Asan Və Sürətli İşləyə Bilməyim Üçün Mənə Qrupunuzda Sadə Adminlik Vermənizi Rica Edirem**", buttons=(
                      
                      [Button.url('➕ Qrupa Əlavə Et ➕', 'https://t.me/nezrintaggerbot?startgroup=a'),
                      Button.url('💞 Dəstək', f'https://t.me/nezrinsupp')],
                      [Button.url('🇦🇿 ᴋᴜʀᴜᴄᴜ 🚫', f'https://t.me/hmnevar'),	             
                      Button.inline("⚙ Əmrlər", data="help")],
                    ),
                    link_preview=False)
 


# furkan


@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):	
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
    await event.edit(f"{ad}\n⚙ Əmorlər Bölümünə Xoş Gəldin.\n💡 İsdədiyiniz Əmirlə Tanış Olmaq Üçün Aşaqdakı Buttonlara Toxun 👇**", buttons=(
                      [
                      Button.inline("📌 TAĞ ƏMİRLƏRİ", data="tag"),
		      Button.inline("⛔ PROSESİ DAYANDIRMA", data="dayan")
                      ],
                      [
                      Button.inline("💡 DİGƏR ƏMİRLƏR", data="diger"),
                      Button.inline("👮‍♂️ SAHİB ƏMİRLƏRİ", data="sahib")
                      ],
                      [
                      Button.inline("ℹ  İNFO", data="info"),
		      Button.inline("◀️ Geri", data="start")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="dayan"))
async def handler(event):
    await event.edit(f"**📌 Tağ Prosesin Dayandırmaq Üçün:**\n\n• `/cancel`\n• `/dayan`", buttons=(
                      [
                      Button.inline("◀️ Geri", data="help"), 
		      Button.inline("🏠 ANA MEYNU", data="start")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="diger"))
async def handler(event):
    await event.edit(f"**🛰 Botun MS İni Və PİNG Dəyərini Ölçmək Üçün:**\n\n• `/ping`\n• `/ms`", buttons=(
                      [
                      Button.inline("◀️ Geri", data="help"), 
		      Button.inline("🏠 ANA MEYNU", data="start")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="sahib"))
async def handler(event):
    await event.edit(f"**👮‍♂️ Sahib Əmorləri:**\n\n• `/yolla` - `Qrupda Reklam Edər`\n• `/stat` - [𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ](https://t.me/XAOS_Tagbot) `İn İstatikası`\n• `/pin` - `Bir Mesajı Pin Edər`\n• `/unpin` - `Sabitlənmiş Medajı Silər`", buttons=(
                      [
                      Button.inline("◀️ Geri", data="help"),
		      Button.inline("🏠 ANA MEYNU", data="start")
                      ],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="stats"))
async def handler(event):
    await event.edit(f"📊 [N A Z R Y N 𝗧𝗮𝗴𝗴𝗲𝗿](https://t.me/NezrinTaggerBot) İn İstatisqası:\n\n🗂 Toplam Qrup Sayı: `{len(grup_sayi)}`\n📈 Aktiv Qrup Sayı: `{len(anlik_calisan)}`")


@client.on(events.callbackquery.CallbackQuery(data="tag"))
async def handler(event):
    await event.edit(f"**\n\t\t📌 TAĞ ƏMİRLƏRİ**\n\n📮 İstifadə: `/sehidler`\n📃 Açıqlama: `ŞƏHİD Adları İlə Tağ`\n\n📮 İstifadə: `/tag`\n📃 Açıqlama: `[SƏBƏB] - 5-Li Tağ Edər`\n\n📮 İstifadə: `/etag`\n📃 Açıqlama: `[SƏBƏB] - Emoji İlə Tağ`\n\n📮 İstifadə: `/btag`\n📃 Açıqlama: `[SƏBƏB] - Bayraq İlə Tag`\n\n📮 İstifadə: `/mtag`\n📃 Açıqlama: `[SƏBƏB] - Mafia Rolları İlə Tag`\n\n📮 İstifadə: `/rtag`\n📃 Açıqlama: `[SƏBƏB] - Rayon və Şəhər adları İlə Tağ`\n\n📮 İstifadə: `/htag`\n📃 Açıqlama: `[SƏBƏB] - Heyvan Adları İlə Tağ`\n\n📮 İstifadə: `/stag`\n📃 Açıqlama: `Maraqlı Sözlərlə Tağ`\n\n📮 İstifadə: `/ttag`\n📃 Açıqlama: `[SƏBƏB] - Tək-Tək Tağ`\n\n📮 İstifadə: `/admin`\n📃 Açıqlama: `[SƏBƏB] - Adminləri Tağ`", buttons=(
	              [
                      Button.inline("◀️ Geri", data="help"), 
		      Button.inline("🏠 ANA MEYNU", data="start")
                      ],
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="info"))
async def handler(event):
    await event.edit(f"ℹ  __**İNFO**__\n\n☞︎︎︎ **Şəhid Adları İlə Tağ**\n☞︎︎︎ **5-Li Tağ**\n☞︎︎︎ **Emojilərlə Tağ**\n☞︎︎︎ **Heyvan Adları İlə Tağ**\n☞︎︎︎ **Bayraqlarla Tağ Edər**\n☞︎︎︎ **Mafia Rolları İlə Tağ**\n☞︎︎︎ **Rayon Və Şəhər Adları İlə Tağ**\n☞︎︎︎ **Təkli Tağ**\n☞︎︎︎ **Maraqlı Sözlərlə Tağ**\n☞︎︎︎ **Yalnız Admimləri Tağ**\n☞︎︎︎ **Maraqlı Temalar**\n☞︎︎︎ **Qrup Və Öz İD Niz**\n☞︎︎︎ **İstənilən Mesajı Sabitləyin**\n☞︎︎︎ **İstənilən Mesaji Sabitdən Silin**\n☞︎︎︎ **Botun MS dəyərin Ölçmək**\n☞︎︎︎ **Botun Statiskası**\n☞︎︎︎ **Şəxsi Məlumatlar**\n☞︎︎︎ **Qrup Məlumatları** \n☞︎︎︎ **Qrup Daxilindəki Silinən Hesablar**\n☞︎︎︎ **Qrup Daxilindəki Botlar**\n☞︎︎︎ **Qrup Personalları**\n☞︎︎︎ **          ", buttons=(

		      [
                      Button.inline("◀️ Geri", data="help"), 
		      Button.inline("🏠 ANA MEYNU", data="start")
                      ],
                    ),
                    link_preview=False)

  
	
	

    
  
button = InlineKeyboardMarkup(
            
                [[InlineKeyboardButton(
                        "♻️ DƏYİŞ" , callback_data= "sehid"),
                    
                InlineKeyboardButton(
                        "🔐 BAĞLA", callback_data= "close")]    
            ])


buton = InlineKeyboardMarkup(
            
                [[InlineKeyboardButton(
                        "♻️ DƏYİŞ" , callback_data= "meslehet"),
                    
                InlineKeyboardButton(
                        "🔐 BAĞLA", callback_data= "close")]    
            ])

temas = InlineKeyboardMarkup(
            
                [[InlineKeyboardButton(
                        "♻️ DƏYİŞ" , callback_data= "taimm"),
                    
                InlineKeyboardButton(
                        "🔐 BAĞLA", callback_data= "close")]    
            ])

sev = InlineKeyboardMarkup(
            
                [[InlineKeyboardButton(
                        "♻️ DƏYİŞ" , callback_data= "sevgi"),
                    
                InlineKeyboardButton(
                        "🔐 BAĞLA", callback_data= "close")]    
            ])


bio = InlineKeyboardMarkup(
            
                [[InlineKeyboardButton(
                        "♻️ DƏYİŞ" , callback_data= "bio"),
                    
                InlineKeyboardButton(
                        "🔐 BAĞLA", callback_data= "close")]    
            ])


mahni = InlineKeyboardMarkup(
            
                [[InlineKeyboardButton(
                        "♻️ DƏYİŞ" , callback_data= "mahni"),
                    
                InlineKeyboardButton(
                        "🔐 BAĞLA", callback_data= "close")]    
            ])



@app.on_message(filters.command("ppp", ["!", "/", "@", "."]))
async def start(_, message):
                await message.reply_photo((await random_line('kolge/txt/pp.txt')),
                caption=(f"""**🖼  {message.from_user.mention} Üçün Random Olaraq Profil Şəkli Seçildi**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                
                
	        [
                    InlineKeyboardButton(
                        "🔐 BAĞLA", callback_data= "close"
                    )
                ]
                
           ]
        ),
    )


		
@app.on_message(filters.command("mahni", ["/", "!", "@", "."]))
async def commit(_, message): 
    await message.reply_text(f"[❤ N A Z R Y N](https://t.me/nezrintaggerbot) **Dan Sizin Üçün Random Olaraq Musiqi Sözləri:**\n\n{await random_line('kolge/txt/mahni.txt')}\n\n👤 **TƏLƏB:**  {message.from_user.mention}", reply_markup=bio)
		
		
@app.on_message(filters.command("bio", ["/", "!", "@", "."]))
async def commit(_, message): 
    await message.reply_text(f"[❤ N A Z R Y N](https://t.me/NezrinTaggerBot)\n\n{await random_line('kolge/txt/bio.txt')}\n\n👤 **TƏLƏB:**  {message.from_user.mention}", reply_markup=bio)
		
	
@app.on_message(filters.command("sevgi", ["/", "!", "@", "."]))
async def commit(_, message): 
    await message.reply_text(f"[❤ N A Z R Y N](https://t.me/NezrinTaggerbot)\n\n{await random_line('kolge/txt/sevgi.txt')}\n\n👤 **TƏLƏB:**  {message.from_user.mention}", reply_markup=sev)
	
	
@app.on_message(filters.command("tema", ["/", "!", "@", "."]))
async def commit(_, message): 
    await message.reply_text(f"💞 [N A Z R Y N](https://t.me/NezrinTaggerbot)  **SİZİN ÜÇÜN RANDOM OLARAQ TEMA SEÇDİ**\n\n{await random_line('kolge/txt/tema.txt')}\n\n👤 **İSDƏDİ:**  {message.from_user.mention}", reply_markup=temas)


@app.on_message(filters.command("meslehet", ["/", "!", "@", "."]))
async def meslehet(_, message):
    await message.reply_text(f"[❤ N A Z R Y N](https://t.me/nezrintaggerbot)\n\n{await random_line('kolge/txt/meslehet.txt')}\n\n👤 **İSDƏYƏN:** {message.from_user.mention}", reply_markup=buton)
 
 
@app.on_message(filters.command("sehid", ["/", "!", "@", "."]))
async def commit(_, message):
    await message.reply_text(f"🥀 **ŞƏHİD ADI İSDƏNİLDİ:**\n\n🥀 **ŞƏHİD:** {await random_line('kolge/txt/sehid.txt')}\n\n👤 **İSDƏYƏN:** {message.from_user.mention}", reply_markup=button)


@app.on_callback_query(filters.regex("sehid"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text(f"🥀 **ŞƏHİD ADI İSDƏNİLDİ:**\n\n🥀 **ŞƏHİD:** {await random_line('kolge/txt/sehid.txt')}\n\n👤 **İSDƏYƏN:** {query.from_user.mention}", reply_markup=button)


@app.on_callback_query(filters.regex("meslehet"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text(f"[❤ N A Z R Y N](https://t.me/nezrintaggerbot)\n\n{await random_line('kolge/txt/meslehet.txt')}\n\n👤 **İSDƏYƏN:** {query.from_user.mention}", reply_markup=buton)


@app.on_callback_query(filters.regex("taimm"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text(f"🤖 [N A Z R Y N](https://t.me/nezrintaggerbot)  **SİZİN ÜÇÜN RANDOM OLARAQ TEMA SEÇDİ**\n\n{await random_line('kolge/txt/tema.txt')}\n\n👤** İSDƏDİ:**  {query.from_user.mention}", reply_markup=temas)


@app.on_callback_query(filters.regex("sevgi"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text(f"[❤ N A Z R Y N](https://t.me/nezrintaggerbot)\n\n{await random_line('kolge/txt/sevgi.txt')}\n\n👤** TƏLƏB:**  {query.from_user.mention}", reply_markup=sev)


@app.on_callback_query(filters.regex("bio"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text(f"[❤ N A Z R Y N ](https://t.me/nezrintaggerbot)\n\n{await random_line('kolge/txt/bio.txt')}\n\n👤** TƏLƏB:**  {query.from_user.mention}", reply_markup=bio)

@app.on_callback_query(filters.regex("mahni"))
async def deyis(_, query: CallbackQuery):
    await query.edit_message_text(f"[❤ N A Z R Y N](https://t.me/nezrintaggerbot) **Dan Sizin Üçün Random Olaraq Musiqi Sözləri:**\n\n{await random_line('kolge/txt/bio.txt')}\n\n👤** TƏLƏB:**  {query.from_user.mention}", reply_markup=bio)


@app.on_message(filters.command(["pp"]))
async def pp(bot: app, m: Message):
    start = time()
    replymsg = await m.reply_text("**❤ Rondom Profil Şəkili Seçilir...**")
    end = round(time() - start, 2)
    photo = random.choice(foto)
    text = f"❤️ XAOS **Sizin Üçün Profil Şəkili Seçdi**"
    await bot.send_photo(m.chat.id, photo=photo, caption=text)
    await replymsg.delete()

@app.on_callback_query(filters.regex("close"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()
 
	

@client.on(events.NewMessage())
async def mentionalladmin(event):
  global etiketuye
  if event.is_group:
    if event.chat_id in etiketuye:
      pass
    else:
      etiketuye.append(event.chat_id)

@client.on(events.NewMessage(pattern="^.tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**🤚🏼 PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/tag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")


@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")

		
		
		

@client.on(events.NewMessage(pattern="^.ttag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("*🤚🏼 PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("** ⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("***🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver!**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/ttag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Uğurla Başladıldl.!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n📢 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n📢 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  

@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")


@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")


		
		
	
@client.on(events.NewMessage(pattern="^.stag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("🤚🏼 PM Də Tağ Olmaz**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("⛔ **Siz Admin Deyilsiz!**\n✅ **Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")

  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("ℹ **Köhnə Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Bir Mesajı Yanıtlayın Yada Tağ Edə Bilməyim Üçün Bir Səbəb Yazın\n✔ Misal Üçün:-`/etag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ Prosesi Başladıldı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅  Tağ Prosesi Uğurla Tamamlandı**\n\n**📊 Tağ Edilınlərin Sayı:-**  `{rxyzdev_tagTot[event.chat_id]}`\n**👤 Prosesi Başladan:-** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n• - [{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla tamamlandı**\n\n**⚡ Tağ Edildi:-**  `{rxyzdev_tagTot[event.chat_id]}`\n**🗣 Prosesi Başladan:-**  {rxyzdev_initT}")
 
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")


@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")


		
@client.on(events.NewMessage(pattern="^.htag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**🤚🏼 PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/htag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(heyvan)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(hayvan)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
		
  
@client.on(events.NewMessage(pattern="^.btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**🤚🏼 PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/btag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"- [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f" - [{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
		
@client.on(events.NewMessage(pattern="^.mtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**🤚🏼 PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/mtag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(mafia)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
		
@client.on(events.NewMessage(pattern="^.rtag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**🤚🏼 PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/rtag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n•- [{random.choice(seher)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 


@client.on(events.NewMessage(pattern="^.etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**🤚🏼 PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**⛔ Siz Admin Deyilsiz!**\n✅ Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**🔗 Keçmiş Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm❗**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**📌 Tağ Edə Bilməyim Üçün Mənə Mətin Ver**")
  else:
    return await event.respond("**❌ Tağ Edmək Üçün Bir Səbəb Yoxdur\n✅ Tağ Edə Bilməyim Üçün Səbəb Yazın\nℹ `/etag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**✅ Tağ Prosesi Başladıldı!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"- [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f" - [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla Tamamlandı !.\n\n📊 Tağ Edilənlərin Sayı: {rxyzdev_tagTot[event.chat_id]}\n\n👤 Prosesi Başladan: {rxyzdev_initT}**")
  
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📊 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")
 
		
@client.on(events.NewMessage(pattern="^.sehidler ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("🤚🏼 PM Də Tağ Olmaz**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("⛔ **Siz Admin Deyilsiz!**\n✅ **Bu Əmir Sadəcə Adminlər Üçün Keçərlidi**")
 
  if event.pattern_match.group(0):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(0)
  elif event.reply_to_msg_id:
    mode = ""
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("ℹ **Köhnə Mesajlar Üçün Userlərdən Bəhs Edə Bilmərəm**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Bana bir metin verin.")
  else:
    return await event.respond("**Bir Mesajı Yanıtlayın Yada Tağ Edə Bilməyim Üçün Bir Səbəb Yazın\n✔ Misal Üçün:-`/etag Salam`**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond("**✅ Tağ Prosesi Başladıldı**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n 🥀 [{random.choice(sehidler)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅  Tağ Prosesi Uğurla Tamamlandı**\n\n**📊 Tağ Edilınlərin Sayı:-**  `{rxyzdev_tagTot[event.chat_id]}`\n**👤 Prosesi Başladan:-** {rxyzdev_initT}")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n 🥀 - [{random.choice(sehidler)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Tağ Prosesi Uğurla tamamlandı**\n\n**⚡ Tağ Edildi:-**  `{rxyzdev_tagTot[event.chat_id]}`\n**🗣 Prosesi Başladan:-**  {rxyzdev_initT}")
 
 
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 
 
@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`")
 




@client.on(events.NewMessage(pattern="^.admin ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "👮‍♂️ Qrup Adminlərinin Siyahısı \n\n"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n 👮‍♂️ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation
 



 
 
@client.on(events.NewMessage(pattern='(?i)/taim+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.respond(f"\n💁‍♂️ [N A Z R Y N](https://t.me/nezrintaggerbot) **SİZİN ÜÇÜN RANDOM OLARAQ TEMA SEÇDi**\n\n🎨  [TEMA  -  TOXUN 👇]({random.choice(taım)})",
		      buttons=(
			   
                      [Button.inline("♻️ DƏYİŞ", data="tema")],
                    ),
                    link_preview=False
		   )
 
 
@client.on(events.callbackquery.CallbackQuery(data="tema"))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.respond(f"\n💁‍♂️ [N A Z R Y N](https://t.me/nezrintaggerbot) **SİZİN ÜÇÜN RANDOM OLARAQ TEMA SEÇDi**\n\n🎨  [TEMA  -  TOXUN 👇]({random.choice(taım)})",
		
		      buttons=(
		
			   
                      [Button.inline("♻️ DƏYİŞ", data="tema")],
                    ),
                    link_preview=False
		   )
 
 
SAHİB = 5663585448
@client.on(events.NewMessage(pattern="^[!/.]pin$"))
async def pin(event):
    if event.sender_id == SAHİB:
        if not event.reply_to_msg_id:
            return await event.reply("Bir mesajı cavablayın")
        await event.reply("Meeaj Pinləndi")
        await event.client.pin_message(event.chat_id, event.reply_to_msg_id, notify=True)
    else:
        await event.reply("Sən sahib deyilsən pinləməyə çalışma")
 
#Bu kodu @edalet_22 tərəfindən @RoBotlarimTg kanalı üçün yazılmışdır (bu messagı silməyin!!!!!!)
@client.on(events.NewMessage(pattern="^[!/.]unpin$"))
async def unpin(event):
    if event.sender_id == SAHİB:
        if not event.reply_to_msg_id:
            return await event.reply("Bir pinlənən mesajı cavablayın")
        await event.reply("Pinlənmiş mesaj qaldırıldı")
        await event.client.unpin_message(event.chat_id)
    else:
        await event.reply("Sən sahib deyilsən unpinləməyə çalışma")


@client.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"👋 Aramıza Xoş Gəldin")
 
@client.on(events.ChatAction)
async def handler(event):
    if event.user_left:
        await event.reply(f"Səni tanimaq gözəl idi❗")
	




@client.on(events.NewMessage(pattern='^[!/.]yolla$'))
async def duyuru(event):
 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Gruba'a mesaj gönderiliyor...")
  for x in grup_sayi:
    try:
      await client.send_message(x,f"**📣 Sponsor**\n\n{reply.message}")
    except:
      pass
  await event.respond(f"Gönderildi.")


@client.on(events.NewMessage(pattern="^[.!/]stats$"))
async def start(event):
  await event.reply(f"**📊 [N A Z R Y N 𝗧𝗮𝗴𝗴𝗲𝗿](https://t.me/NezrinTaggerBot) -Un İstatiskası**", buttons=(
                      [
                       Button.inline("Stats", data="stats")
                      ],
                    ),
                    link_preview=False)

@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(BOT_ID):
            await msg.reply(f'Hey {msg.from_user.mention} Məni {msg.chat.title} Qrupuna Aldığın Üçün Təşəkürlər⚡️`\nQrublarda 50.000 Userə Qədər İnsanları Tağ Edə Bilərəm.\nDaha Çox Məlumat Üçün\n[N A Z R Y N 𝗧𝗮𝗴𝗴𝗲𝗿](https://t.me/nezrintaggerbot) - Ə PM də Start Verin')

        elif str(new_user.id) == str(OWNER_ID):
            await msg.reply(
		f'''**👮‍♂️ Bax Bu Gələn Mənim Sahibimdir**\n**👏 Sahibim** {msg.chat.title} **Qrupuna Xoş Gəldin**''')

 
@app.on_message(filters.command('id', [".", "!", "@", "/"]))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**User MƏLUMATI:**\n"
    out_str += f"**🆔️ Grup ID:** `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f"**👤 Yanıtlanan Kullanıcı Adı:** {msg.from_user.first_name}\n"
    out_str += f"**💬 Mesaj ID:** `{msg.forward_from_message_id}`\n"
    if msg.from_user:
        out_str += f"**👤 Yanıtlanan Kullanıcı ID:** `{msg.from_user.id}`\n"
 
    await message.reply(out_str)
	

mssil = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔐  BAĞLA", callback_data="close")]
])
@app.on_message(filters.command('ping', [".", "!", "@", "/"]))
async def pingy(client, message):
    start = datetime.now()
    hmm = await message.reply("🛰 **MS** HESABLANIR!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"█▀█ █ █▄░█ █▀▀ █ \n█▀▀ █ █░▀█ █▄█ ▄\n\n**🛰 Ping: {round(ms)}**", reply_markup=mssil)
  
@app.on_callback_query(filters.regex("close"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()
 

	
	


    
	


@app.on_message(filters.command('del', [".", "!", "@", "/"]) & filters.group)
async def delAcc(client, msj):
    # ayuyes
    chat_id = msj.chat.id
    DELETED = []
    members = app.get_chat_members(chat_id)
    async for m in members:
        if m.user.is_deleted == True:
            DELETED.append(str(m.user.id)) # silinen hesablar

    shesablar = '\n'.join(DELETED) 
    await app.send_message(chat_id, f"{shesablar}\n\n🗑 **Silinən Hesabların Sayı -{len(DELETED)}**\n**🗨 Qrup:** {msj.chat.title}\n👤 **İcraçı:** {msj.from_user.mention}")	
	
	
@app.on_message(filters.command('bots', [".", "!", "@", "/"]))
async def bots(client, message):  
  try:    
    botList = []
    async for bot in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bot.user)
    lenBotList = len(botList) 
    text3  = f"{message.chat.title} - **QURUPUNDAKI BOTLAR**\n\n👮‍♂️ __**İSDƏYƏN**__ : {message.from_user.mention()}\n\n"
    while len(botList) > 1:
      bot = botList.pop(0)
      text3 += f"├ 🤖 @{bot.username}\n"    
    else:    
      bot = botList.pop(0)
      text3 += f"└ 🤖 @{bot.username}\n\n"
      text3 += f"📊 | **Botların ümumi sayı**: {lenBotList}"  
      await app.send_message(message.chat.id, text3)
  except FloodWait as e:
    await asyncio.sleep(e.value)
 
	
	
@app.on_message(filters.command('admins', [".", "!", "@", "/"]))
async def admins(client, message):
  try: 
    adminList = []
    ownerList = []
    async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
      if admin.privileges.is_anonymous == False:
        if admin.user.is_bot == True:
          pass
        elif admin.status == ChatMemberStatus.OWNER:
          ownerList.append(admin.user)
        else:  
          adminList.append(admin.user)
      else:
        pass   
    lenAdminList= len(ownerList) + len(adminList)  
    text2 = f"👮‍♂️ QRUP İDARƏÇİLƏRİ - {message.chat.title}\n\n"
    try:
      owner = ownerList[0]
      if owner.username == None:
        text2 += f"👑 Kurucu\n└ {owner.mention}\n\n👮🏻 Admin\n"
      else:
        text2 += f"👑 Kurucu\n└ @{owner.username}\n\n👮🏻 Admin\n"
    except:
      text2 += f"👑 Kuruu\n└ <i>Hidden</i>\n\n👮🏻 Admins\n"
    if len(adminList) == 0:
      text2 += "└ <i>Admins are hidden</i>"  
      await app.send_message(message.chat.id, text2)   
    else:  
      while len(adminList) > 1:
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"├ {admin.mention}\n"
        else:
          text2 += f"├ @{admin.username}\n"    
      else:    
        admin = adminList.pop(0)
        if admin.username == None:
          text2 += f"└ {admin.mention}\n\n"
        else:
          text2 += f"└ @{admin.username}\n\n"
      text2 += f"✅ | Toplam Yönətici Sayı: {lenAdminList}\n❌ | Botlar Və Gizli Yönəticilər Iəğv Edildi"  
      await app.send_message(message.chat.id, text2)           
  except FloodWait as e:
    await asyncio.sleep(e.value)
	

 
mesil = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔐  BAĞLA", callback_data="close")]
])

@app.on_message(filters.command('me', [".", "!", "@", "/"]))
async def info(bot, update):
    
    text = f"""  **ℹ MƏLUMAT**
 

🙋🏻‍♂️ **İsdifadəçi Adı:** {update.from_user.mention()}
👥 **İkinci Ad :** {update.from_user.last_name if update.from_user.last_name else 'None'}
🆔 **Telegram ID :** {update.from_user.id}
🗒 **Kulanıcı Adı :** @{update.from_user.username}
🌏 **DİL :** {update.from_user.language_code}
📱 **M.NÖMRƏ :** {update.from_user.phone_number}
🏷 **STATUS :** {str(update.from_user.status)[11:]}
🆔 **Qrup İD :** {(update.forward_from_chat or update.chat).id}
🗨 **Qrup Adı :** {update.chat.title}"""


    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=mesil
    )
 
@app.on_callback_query(filters.regex("close"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()
 
	
	
	

infosil = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔐  BAĞLA", callback_data="close")]
])

@app.on_message(filters.command('info', [".", "!", "@", "/"]))
async def get_id(client, message):
    try:
 
        if (not message.reply_to_message) and (message.chat):
            await message.reply(f"👤 **AD** {message.from_user.mention()}\n🖇 **TAĞ**: @{message.from_user.username}\n🆔️ **İD** <code>`{message.from_user.id }`</code>.\n🌏 **DİL:** {message.from_user.language.code}\n🗨 **QRUP ADI:**  {message.chat.title}\n🗨 **QRUP İD:** <code>`{message.chat.id}</code>.",  reply_markup=infosil)
        elif not message.reply_to_message:
            await message.reply(f"👤 - {message.from_user.mention}\n🆔️ - <code>`{message.from_user.id }`</code>.", reply_markup=infosil) 
 
        elif message.reply_to_message.forward_from_chat:
            await message.reply(f"🔖 **KANAL ADI** {str(message.reply_to_message.forward_from_chat.type)[9:].lower()}, {message.reply_to_message.forward_from_chat.title}\n🆔️ **KANAL İD** <code>`{message.reply_to_message.forward_from_chat.id}`</code>.", reply_markup=infosil)
 
        elif message.reply_to_message.forward_from:
            await message.reply(f"The forwarded user, {message.reply_to_message.forward_from.first_name} has an ID of <code>{message.reply_to_message.forward_from.id   }</code>.", reply_markup=infosil)
 
        elif message.reply_to_message.forward_sender_name:
            await message.reply("Sorry, you cannot get the forwarded user ID because of their privacy settings", reply_markup=infosil)
 
        else:
            await message.reply(f"👤 **AD**: {message.reply_to_message.from_user.mention}\n🖇 **TAĞ**: @{message.reply_to_message.from_user.username}\n🆔️ **İD**: <code>`{message.reply_to_message.from_user.id}`</code>\n🌏 **DİL :** {message.from_user.language_code}\n📱 **M.NÖMRƏ:** {message.from_user.phone_number}\n🗨 **QRUP ADI**: {message.chat.title}", reply_markup=infosil)   
 
    except Exception:
            await message.reply("An error occured while getting the ID.", reply_markup=infosil)
 

@app.on_callback_query(filters.regex("close"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()
 



        
 
 
################## KULLANICI KONTROLLERİ ##########
 
 
############### Broadcast araçları ###########

    














            
	

app.run()
print(">> Bot Deploy Edildi @ByMorfin bilgi alabilirsin<<")
client.run_until_disconnected()
