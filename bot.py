from telethon import TelegramClient, events

# Твої дані
api_id = 31878682
api_hash = '5b919d00f8418040d65adff6b432f382'

# Список ID всіх твоїх чатів
channels_to_listen = [1800718395, -1001561984537, 5402761583] 

# Змінна стану бота
is_active = False

client = TelegramClient('my_session', api_id, api_hash)

# Команди керування з "Збереженого"
@client.on(events.NewMessage(from_users='me'))
async def controller(event):
    global is_active
    if event.raw_text == '/on':
        is_active = True
        await event.reply("✅ Бот активовано! Працюю по всіх каналах.")
    elif event.raw_text == '/off':
        is_active = False
        await event.reply("⛔ Бот зупинений. Відпочиваємо.")

# Обробник вакансій
@client.on(events.NewMessage(chats=channels_to_listen))
async def handler(event):
    if is_active:
        text = event.raw_text.lower()
        if "операціоніст" in text and "ерц" in text:
            print(f"Потрібна вакансія в чаті {event.chat_id}! Тисну кнопку...")
            await event.click(0)
            print("Готово! Запит відправлено.")

print("Система готова.")
print("Слухаю канали:", channels_to_listen)
client.start()
client.run_until_disconnected()
