from telethon import TelegramClient, events
import os

api_id = int(os.environ.get('API_ID'))
api_hash = os.environ.get('API_HASH')

client = TelegramClient('session', api_id, api_hash)

palavras_chave = ['ps5', 'iphone', 'monitor', 'rtx', 'airfryer']

@client.on(events.NewMessage)
async def handler(event):
    texto = event.raw_text.lower()
    if any(p in texto for p in palavras_chave):
        msg = f"📦 Produto encontrado:\n\n{event.raw_text}"
        await client.send_message('me', msg)

async def main():
    print("🤖 Bot rodando...")
    await client.run_until_disconnected()

client.start()
client.loop.run_until_complete(main())
