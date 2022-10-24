from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import *
from Statess.statess import *
from buttons.mButtons import *
from function.functions import *


@dp.message_handler(commands = ["developer", 'coder', 'programmer'])
async def coder(msg: types.Message):
	await msg.reply("Bot dasturchisi @coder_admin_py\n\nPowered by @coder_admin_py", parse_mode='html')

Admin = [5246872049, 662638814]
markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add("🔙Orqaga qaytish")
@dp.message_handler(commands=['admin', 'panel'], user_id = Admin)
async def new(msg: types.Message):
	await msg.answer("Assalomu alaykum admin janoblari", reply_markup=main_btn)
	# await From.teststate.set()   state=From.teststate,

@dp.message_handler(text = "🔙Orqaga qaytish", user_id = Admin)
async def backs(message: types.Message):
	await message.reply("Bosh menyu", reply_markup=main_btn)

############################          STATISTIKA            """"""""""""""""""""""

@dp.message_handler( text = "📊Statistika", user_id = Admin)
async def new(msg: types.Message):
	sql.execute("SELECT COUNT(*) FROM users")
	userfollow = sql.fetchone()[0]
	sql.execute("SELECT COUNT(*) FROM groups")
	groupfollow = sql.fetchone()[0]
	await msg.answer(f"📊Botdagi foydalanuvchilar👇👇\n\n👤Botdagi userlar soni: > {userfollow}\n\n👥Botdagi guruhlar soni: {groupfollow}")



################################           user  REKLAMA          """"""""""""""""""""""

@dp.message_handler(text = "📤User reklama", user_id = Admin)
async def all_send(message: types.Message):
	await message.reply("Foydalanuvchilarga xabar yuborish bo'limi", reply_markup=reklama_btn)

@dp.message_handler(lambda message: message.text == "📨Forward xabar yuborish", user_id=Admin)
async def all_users(message: types.Message, state: FSMContext):
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add("🔙Orqaga qaytish")
	await message.answer("Forward yuboriladigan xabarni yuboring", reply_markup=markup)
	await From.forward_msg.set()

@dp.message_handler(state=From.forward_msg, text = "🔙Orqaga qaytish", content_types=ContentType.ANY, user_id=Admin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	await message.reply("Orqaga qaytildi", reply_markup=main_btn)

@dp.message_handler(state=From.forward_msg, content_types=ContentType.ANY, user_id=Admin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add("🔙Orqaga qaytish")
	rows = sql.execute(f"SELECT user_id FROM users ").fetchall()
	for row in rows:
		id = row[0]
		await forward_send_msg(from_chat_id=message.chat.id, message_id=message.message_id, chat_id=id)

	await message.answer("Xabar yuborish yakunlandi", reply_markup=reklama_btn)


@dp.message_handler(lambda message: message.text == "📬Oddiy xabar yuborish", user_id=Admin)
async def all_users(message: types.Message, state: FSMContext):
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add("🔙Orqaga qaytish")
	await message.answer("Yuborilishi kerak bo'lgan xabarni yuboring", reply_markup=markup)
	await From.send_msg.set()

@dp.message_handler(state=From.send_msg, text = "🔙Orqaga qaytish", content_types=ContentType.ANY, user_id=Admin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	await message.reply("Orqaga qaytildi", reply_markup=main_btn)

@dp.message_handler(state=From.send_msg, content_types=ContentType.ANY, user_id=Admin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add("🔙Orqaga qaytish")
	rows = sql.execute(f"SELECT user_id FROM users ").fetchall()
	for row in rows:
		id = row[0]
		await send_message_chats(from_chat_id=message.chat.id, message_id=message.message_id, chat_id=id)

	await message.answer("Xabar yuborish yakunlandi", reply_markup=reklama_btn)



################################         guruh   REKLAMA          """"""""""""""""""""""

@dp.message_handler(text = "📤Guruh reklama", user_id = Admin)
async def all_send(message: types.Message):
	await message.reply("Foydalanuvchilarga xabar yuborish bo'limi", reply_markup=G_reklama_btn)

@dp.message_handler(lambda message: message.text == "📨Forward xabar yuborish.", user_id=Admin)
async def all_users(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add("🔙Orqaga qaytish")
	await message.answer("Forward yuboriladigan xabarni yuboring", reply_markup=markup)
	await From.forwardG_msg.set()

@dp.message_handler(state=From.forwardG_msg, text = "🔙Orqaga qaytish", content_types=ContentType.ANY, user_id=Admin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	await message.reply("Orqaga qaytildi", reply_markup=main_btn)

@dp.message_handler(state=From.forwardG_msg, content_types=ContentType.ANY, user_id=Admin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add("🔙Orqaga qaytish")
	rows = sql.execute(f"SELECT group_id FROM groups ").fetchall()
	for row in rows:
		id = row[0]
		await Gforward_send_msg(from_chat_id=message.chat.id, message_id=message.message_id, chat_id=id)

	await message.answer("Xabar yuborish yakunlandi", reply_markup=G_reklama_btn)


@dp.message_handler(lambda message: message.text == "📬Oddiy xabar yuborish.", user_id=Admin)
async def all_users(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add("🔙Orqaga qaytish")
	await message.answer("Yuborilishi kerak bo'lgan xabarni yuboring", reply_markup=markup)
	await From.sendG_msg.set()

@dp.message_handler(state=From.sendG_msg, text = "🔙Orqaga qaytish", user_id=Admin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	await message.reply("Orqaga qaytildi", reply_markup=main_btn)

@dp.message_handler(state=From.sendG_msg, content_types=ContentType.ANY, user_id=Admin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add("🔙Orqaga qaytish")
	rows = sql.execute(f"SELECT group_id FROM groups ").fetchall()
	for row in rows:
		id = row[0]
		await Gsend_message_chats(from_chat_id=message.chat.id, message_id=message.message_id, chat_id=id)

	await message.answer("Xabar yuborish yakunlandi", reply_markup=G_reklama_btn)





###########################           so'kinishlar              """""""""""""""""""""

@dp.message_handler(text = "🤬So'kinishlar", user_id = Admin)
async def new(msg: types.Message):
	await msg.answer("Tanlang", reply_markup=S_baza)


@dp.message_handler(text = "So'z qo'shish", user_id = Admin)
async def channel_add(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add("🔙Orqaga qaytish")
	await message.reply("So'kinishlar sirasiga kiradigan so'z yuboring", reply_markup=markup)
	await From.Soz_add.set()

@dp.message_handler(state=From.Soz_add, text = "🔙Orqaga qaytish", user_id=Admin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	await message.reply("Orqaga qaytildi", reply_markup=main_btn)

@dp.message_handler(state=From.Soz_add, user_id = Admin)
async def channelAdd1(message: types.Message, state: FSMContext):
	sql.execute("""CREATE TABLE IF NOT EXISTS words(word, fake)""")
	db.commit()
	data = sql.execute(f"SELECT word FROM words WHERE word = '{message.text.upper()}'").fetchone()
	if data is None:
		sql.execute(f"""INSERT INTO words (word, fake) VALUES ('{message.text}', 'fake')""")
		db.commit()
		await message.answer("So'z qo'shildi", reply_markup=S_baza)
		await state.finish()
	else:
		await message.reply("Bu so'z avvaldan bor", reply_markup=S_baza)
	await state.finish()


@dp.message_handler(text = "So'zlar ko'rish")
async def channelList(message: types.Message):
	sql.execute("SELECT COUNT(*) FROM words ")
	check = sql.fetchone()[0]
	if check == None:
		await message.reply("Hozircha so'zlar yo'q")
	else:
		datas = sql.execute(f"SELECT word FROM words").fetchall()
		text = ''
		for data in datas:
			text = text + data[0] + '\n'

		await message.answer(text)