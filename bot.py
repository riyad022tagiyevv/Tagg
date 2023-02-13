import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

from datetime import datetime

from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import time

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
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import pyrogram
from datetime import datetime
from telethon.errors.rpcerrorlist import MessageDeleteForbiddenError
 


	
	
	

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
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")


@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")



# Başlanğıc Button

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
  await event.reply(f"**👋 Salam {ad}\nMən  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ**\n**𝕏𝔸𝕆𝕊 Federasiyasının Rəsmi Tağ botuyam**\n**⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm**\n**Əmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun**\n**ℹ Mənim Qruplarda Asan Və Sürətli İşləyə Bilməyim Üçün Mənə Qrupunuzda Sadə Adminlik Vermənizi Rica Edirem**",
                    buttons=(
			    
		      [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a'),
                      Button.url('⚡ 𝕏𝔸𝕆𝕊 𝔽𝔹𝔸ℕ', f'https://t.me/XaosResmii')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/sesizKOLGE'),
                      Button.inline("⚙ Ə𝕄ℝ𝕃Əℝ", data="help")],
                    ),
                    link_preview=False
		   )
 
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
    await event.edit(f"**👋 Salam {ad}\n ⚡Mən  𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ**\n**𝕏𝔸𝕆𝕊 Federasiyasının Rəsmi Tağ botuyam**\n**⚡ 𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ İlə Qrupunuzdakı Üyələri Etiket Edə Bilərəm**\n**ℹƏmrlərlə Tanış Olmaq Üçün __ƏMRLƏR__ Butonuna Toxun**\n**ℹ Mənim Qruplarda Asan Və Sürətli İşləyə Bilməyim Üçün Mənə Qrupunuzda Sadə Adminlik Vermənizi Rica Edirem**", buttons=(
                      
                      [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Tagbot?startgroup=a'),
                      Button.url('⚡ 𝕏𝔸𝕆𝕊 𝔽𝔹𝔸ℕ', f'https://t.me/XaosResmii')],
                      [Button.url('🇦🇿 𝕆𝕎ℕ𝔼ℝ 👨‍💻', f'https://t.me/sesizKOLGE'),	             
                      Button.inline("⚙ Ə𝕄ℝ𝕃Əℝ", data="help")],
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
    await event.edit(f"📊 [𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ](https://t.me/XAOS_Tagbot) İn İstatisqası:\n\n🗂 Toplam Qrup Sayı: `{len(grup_sayi)}`\n📈 Aktiv Qrup Sayı: `{len(anlik_calisan)}`")


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
    await event.edit(f"ℹ  __**İNFO**__\n\n☞︎︎︎ **Şəhid Adları İlə Tağ**\n☞︎︎︎ **5-Li Tağ**\n☞︎︎︎ **Emojilərlə Tağ**\n☞︎︎︎ **Heyvan Adları İlə Tağ**\n☞︎︎︎ **Bayraqlarla Tağ Edər**\n☞︎︎︎ **Mafia Rolları İlə Tağ**\n☞︎︎︎ **Rayon Və Şəhər Adları İlə Tağ**\n☞︎︎︎ **Təkli Tağ**\n☞︎︎︎ **Maraqlı Sözlərlə Tağ**\n☞︎︎︎  **Yalnız Admimləri Tağ**\n☞︎︎︎ **Maraqlı Temalar**\n☞︎︎︎ **Qrup Və Öz İD Niz**\n☞︎︎︎ **İstənilən Mesajı Sabitləyin**\n☞︎︎︎ **İstənilən Mesaji Sabitdən Silin**\n☞︎︎︎ **Botun MS dəyərin Ölçmək**\n☞︎︎︎ **Botun Statiskası**", buttons=(

		      [
                      Button.inline("◀️ Geri", data="help"), 
		      Button.inline("🏠 ANA MEYNU", data="start")
                      ],
                    ),
                    link_preview=False)




@client.on(events.NewMessage())
async def mentionalladmin(event):
  global etiketuye
  if event.is_group:
    if event.chat_id in etiketuye:
      pass
    else:
      etiketuye.append(event.chat_id)

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**❌ PM Də Tağ Olmaz**\n**✅ Bu Əmr Sadəcə Qruplarda Və Kanallarda Keçərlidi!**")
  
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
        return await event.respond("**Eski Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Bana Bir Metin Ver!**")
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
      usrtxt += f"\n👤 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket İşlemi Başarıyla Tamamlandı !.\n\nEtiketlerin Sayları: {rxyzdev_tagTot[event.chat_id]}\n\nEtiket İşlemini Başlatan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n👤 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket İşlemi Başarıyla Tamamlandı !.\n\nEtiketlerin Sayları: {rxyzdev_tagTot[event.chat_id]}\n\nEtiket İşlemini Başlatan: {rxyzdev_initT}**")
		
@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")


@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")

		
		
		

@client.on(events.NewMessage(pattern="^.ttag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  rxyzdev_tagTot[event.chat_id] = 0
  if event.is_private:
    return await event.respond("**Bu Komut Sadacə Grublarda ve Kanallarda Kullanıma Bilir**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Yalnızca Yöneticiler Etiket işlemini Yapabilir**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Köhnə Mesajlar için Üyelerden Bahsedemem! (gruba eklemeden önce gönderilen mesajlar)**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Bana Bir Metin Ver!**")
  else:
    return await event.respond("**Bir Mesajı Yanıtlayın veya Başkalarından Bahsetmem için Bana Bir Betin Verin!!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    await event.respond(f"**Etiket işlemi Başarıyla Başlatıldı.!**")
        
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n👤 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{msg}\n{usrtxt}")
        await asyncio.sleep(3)
        usrnum = 0
        usrtxt = ""
        
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket İşlemi Başarıyla Tamamlandı !.\n\nEtiketlerin Sayları: {rxyzdev_tagTot[event.chat_id]}\n\nEtiket İşlemini Başlatan: {rxyzdev_initT}**")
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id, aggressive=False):
      rxyzdev_tagTot[event.chat_id] += 1
      usrnum += 1
      usrtxt += f"\n👤 - [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
     
    sender = await event.get_sender()
    rxyzdev_initT = f"[{sender.first_name}](tg://user?id={sender.id})"      
    if event.chat_id in rxyzdev_tagTot:await event.respond(f"**✅ Etiket İşlemi Başarıyla Tamamlandı !.\n\nEtiketlerin Sayları: {rxyzdev_tagTot[event.chat_id]}\n\nEtiket İşlemini Başlatan: {rxyzdev_initT}**")


@client.on(events.NewMessage(pattern='^.cancel ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")


@client.on(events.NewMessage(pattern='^.dayan ?(.*)'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"✅**Tağ Prosesi Dayandırıldı.**\n\n📋 **Tağ Edilənərin Sayı:** `{rxyzdev_tagTot[event.chat_id]}`**")

    
 

	
	
  




@client.on(events.NewMessage(pattern='^/yolla ?(.*)'))
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


@client.on(events.NewMessage(pattern="^.stats.?(.*)"))
async def start(event):
  await event.reply(f"**📊 [𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ](https://t.me/XAOS_Tagbot) -Un İstatiskası**", buttons=(
                      [
                       Button.inline("Stats", data="stats")
                      ],
                    ),
                    link_preview=False)

@app.on_message(filters.new_chat_members, group=1)
async def hg(bot: Client, msg: Message):
    for new_user in msg.new_chat_members:
        if str(new_user.id) == str(BOT_ID):
            await msg.reply(f'Hey {msg.from_user.mention} Məni {msg.chat.title} Qrupuna Aldığın Üçün Təşəkürlər⚡️`\nQrublarda 50.000 Userə Qədər İnsanları Tağ Edə Bilərəm.\nDaha Çox Məlumat Üçün\n[𝕏𝔸𝕆𝕊 𝕋𝔸𝔾𝔾𝔼ℝ](https://t.me/XAOS_Tagbot) - Ə PM də Start Verin')

        elif str(new_user.id) == str(OWNER_ID):
            await msg.reply(
		f'''**👮‍♂️ Bax Bu Gələn Mənim Sahibimdir**\n**👏 Sahibim** {msg.chat.title} **Qrupuna Xoş Gəldin**''')

 
@app.on_message(filters.command("id"))
async def _id(_, message: Message):
    msg = message.reply_to_message or message
    out_str = "**User MƏLUMATI:**\n"
    out_str += f"**🆔️ Grup ID:** `{(msg.forward_from_chat or msg.chat).id}`\n"
    out_str += f"**👤 Yanıtlanan Kullanıcı Adı:** {msg.from_user.first_name}\n"
    out_str += f"**💬 Mesaj ID:** `{msg.forward_from_message_id}`\n"
    if msg.from_user:
        out_str += f"**👤 Yanıtlanan Kullanıcı ID:** `{msg.from_user.id}`\n"
 
    await message.reply(out_str)
	


@app.on_message(filters.command(["ping", "ms"]))
async def pingy(client, message):
    start = datetime.now()
    hmm = await message.reply("🛰 **MS** HESABLANIR!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await hmm.edit(
        f"█▀█ █ █▄░█ █▀▀ █ \n█▀▀ █ █░▀█ █▄█ ▄\n\n**🛰 Ping: {round(ms)}**")
  
	
	

@app.on_message(filters.command("del") & filters.group)
async def delAcc(client, msj):
    # ayuyes
    chat_id = msj.chat.id
    DELETED = []
    members = app.get_chat_members(chat_id)
    async for m in members:
        if m.user.is_deleted == True:
            DELETED.append(str(m.user.id)) # silinen hesablar

    shesablar = '\n'.join(DELETED) 
    await app.send_message(chat_id, f"{shesablar}\n\n🗑 Silinən hesabların sayı - {len(DELETED)}")	
	
	
@app.on_message(filters.command("bots"))
async def bots(client, message):  
  try:    
    botList = []
    async for bot in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bot.user)
    lenBotList = len(botList) 
    text3  = f"{message.chat.title} - **QURUPUNDAKI BOTLAR**\n\n🤖 __Bots__\n"
    while len(botList) > 1:
      bot = botList.pop(0)
      text3 += f"├ @{bot.username}\n"    
    else:    
      bot = botList.pop(0)
      text3 += f"└ @{bot.username}\n\n"
      text3 += f"✅ | **Botların ümumi sayı**: {lenBotList}"  
      await app.send_message(message.chat.id, text3)
  except FloodWait as e:
    await asyncio.sleep(e.value)
 
	
	
@app.on_message(filters.command(["admins","ytlist"]))
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
	
BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="➕ QRUPA ƏLAVƏ ET➕", url=f"https://t.me/XAOS_Tagbot?startgroup=a")]])
 	
 

@app.on_message(filters.command(["info", "me"]))
async def info(bot, update):
    
    text = f"""  **ℹ MƏLUMAT**
 
**🙋🏻‍♂️ İsdifadəçi Adı:** {update.from_user.first_name}
**🧖‍♂️ İkinci Ad :** {update.from_user.last_name if update.from_user.last_name else 'None'}
**🆔 Telegram ID :** `{update.from_user.id}`
**🗒 Kulanıcı Adı :**  @{update.from_user.username}
**🖇 Profil Linki :** [TOXUN 👇](tg://settings)
**qrup :**  `{(update.forward_from_chat or update.chat).id}`"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )
 
	



            
	

app.run()
print(">> Bot Deploy Edildi @ByMorfin bilgi alabilirsin<<")
client.run_until_disconnected()
