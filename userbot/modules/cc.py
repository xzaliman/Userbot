#credit @V_6_Y do not steal
from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio
from userbot import bot
from userbot.utils import admin_cmd

@bot.on(admin_cmd(pattern="bin ?(.*)"))
async def sed(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Please input bin who want to check!..__")
    await event.edit(f"```𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 𝙱𝙸𝙽 𝚆𝙰𝙸𝚃...```")
    async with bot.conversation("@uchihasgroup") as conv:
        try:
            jemboed = await conv.send_message(f"!bin {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await event.reply("Unblock @uchihasgroup or chat first")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"Bin {query} Invalid!")
        else:
            await event.edit(asu.message)
            await event.client(conv.chat_id, [jemboed.id, asu.id])
            
@bot.on(admin_cmd(pattern="ch ?(.*)"))
async def sed(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Please input cc who want to check!..__")
    await event.edit(f"```𝙲𝙷𝙴𝙲𝙺𝙸𝙽𝙶 𝙲𝙲 𝚆𝙰𝙸𝚃...```")
    async with bot.conversation("@uchihasgroup") as conv:
        try:
            jemboed = await conv.send_message(f"!chk {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)			
        except YouBlockedUserError:
            return await event.reply("Unblock @uchihasgroup or chat first")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"cc {query} Invalid!")
        else:
            await event.edit(asu.message)
            await event.client(conv.chat_id, [jemboed.id, asu.id])
            
@bot.on(admin_cmd(pattern="gen ?(.*)"))
async def sed(event):
    if event.fwd_from:
        return
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("__Please input cc who want to check!..__")
    await event.edit(f"`𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙴 𝙲𝙲 𝚆𝙰𝙸𝚃...`")
    async with bot.conversation("@uchihasgroup") as conv:
        try:
            jemboed = await conv.send_message(f"/gen {query}")
            await asyncio.sleep(10)
            asu = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)			
        except YouBlockedUserError:
            return await event.reply("Unblock @uchihasgroup or chat first")
        if asu.text.startswith("Wait for result..."):
            return await event.edit(f"bin {query} Invalid!")
        else:
            await event.edit(asu.message)
            await event.client(conv.chat_id, [jemboed.id, asu.id])