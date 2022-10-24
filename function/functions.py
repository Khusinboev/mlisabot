from sqlite3 import connect
from key import *
from databas import *
from aiogram import *
from aiogram.types import *

import asyncio
from buttons.mButtons import *


class functions:
	@staticmethod
	async def check_on_start(user_id):
		rows = sql.execute("SELECT id FROM channels").fetchall()
		error_code = 0
		for row in rows:
			r = await dp.bot.get_chat_member(chat_id=row[0], user_id=user_id)
			if r.status in ['member', 'creator', 'admin']:
				pass
			else:
				error_code = 1
		if error_code == 0:
			return True
		else:
			return False


async def forward_send_msg(chat_id: int, from_chat_id: int, message_id: int) -> bool:
	try:
		await dp.bot.forward_message(chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id)
	except exceptions.BotBlocked:
		sql.execute(f"DELETE FROM users WHERE user_id ='{chat_id}'")
		db.commit()
	except exceptions.ChatNotFound:
		sql.execute(f"DELETE FROM users WHERE user_id ='{chat_id}'")
		db.commit()
	except exceptions.UserDeactivated:
		sql.execute(f"DELETE FROM users WHERE user_id ='{chat_id}'")
		db.commit()
	except exceptions.TelegramAPIError:
		sql.execute(f"DELETE FROM users WHERE user_id ='{chat_id}'")
		db.commit()
	else:
		return True
	return False


async def send_message_chats(chat_id: int, from_chat_id: int, message_id: int) -> bool:
	try:
		await dp.bot.copy_message(chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id)
	except exceptions.BotBlocked:
		sql.execute(f"DELETE FROM users WHERE user_id ='{chat_id}'")
		db.commit()
	except exceptions.ChatNotFound:
		sql.execute(f"DELETE FROM users WHERE user_id ='{chat_id}'")
		db.commit()
	except exceptions.UserDeactivated:
		sql.execute(f"DELETE FROM users WHERE user_id ='{chat_id}'")
		db.commit()
	except exceptions.TelegramAPIError:
		sql.execute(f"DELETE FROM users WHERE user_id ='{chat_id}'")
		db.commit()
	else:
		return True
	return False


async def Gforward_send_msg(chat_id: int, from_chat_id: int, message_id: int) -> bool:
	try:
		await dp.bot.forward_message(chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id)
	except exceptions.BotBlocked:
		sql.execute(f"DELETE FROM groups WHERE group_id ='{chat_id}'")
		db.commit()
	except exceptions.ChatNotFound:
		sql.execute(f"DELETE FROM groups WHERE group_id ='{chat_id}'")
		db.commit()
	except exceptions.UserDeactivated:
		sql.execute(f"DELETE FROM groups WHERE group_id ='{chat_id}'")
		db.commit()
	except exceptions.TelegramAPIError:
		sql.execute(f"DELETE FROM groups WHERE group_id ='{chat_id}'")
		db.commit()
	else:
		return True
	return False


async def Gsend_message_chats(chat_id: int, from_chat_id: int, message_id: int) -> bool:
	try:
		await dp.bot.copy_message(chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id)
	except exceptions.BotBlocked:
		sql.execute(f"DELETE FROM groups WHERE group_id ='{chat_id}'")
		db.commit()
	except exceptions.ChatNotFound:
		sql.execute(f"DELETE FROM groups WHERE group_id ='{chat_id}'")
		db.commit()
	except exceptions.UserDeactivated:
		sql.execute(f"DELETE FROM groups WHERE group_id ='{chat_id}'")
		db.commit()
	except exceptions.TelegramAPIError:
		sql.execute(f"DELETE FROM groups WHERE group_id ='{chat_id}'")
		db.commit()
	else:
		return True
	return False


#########################              chat rek delete

async def delete_msg(message):
	r = await dp.bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
	if r.status in ['creator', 'admin', 'administrator']:
		pass
	else:

		for i in message.caption_entities:
			if i.type == 'text_link':
				try:
					await message.delete()
					await message.answer(
						f"<b><a href = 'tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n\nIltimos reklama tarqatmang</b>",
						reply_markup=join_chat)
				except:
					pass
				pass
			if i.type == 'url':
				try:
					await message.delete()
					await message.answer(
						f"<b><a href = 'tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n\nIltimos reklama tarqatmang</b>",
						reply_markup=join_chat)
				except:
					pass
				pass
			if i.type == 'mention':
				try:
					await message.delete()
					await message.answer(
						f"<b><a href = 'tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n\nIltimos reklama tarqatmang</b>",
						reply_markup=join_chat)
				except:
					pass
				pass


		for i in message.entities:
			if i.type == 'url':
				try:
					await message.delete()
					await message.answer(
						f"<b><a href = 'tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n\nIltimos reklama tarqatmang</b>",
						reply_markup=join_chat)
				except:
					pass
				pass

			elif i.type == 'mention':
				try:
					await message.delete()
					await message.answer(
						f"<b><a href = 'tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n\nIltimos reklama tarqatmang</b>",
						reply_markup=join_chat)
				except:
					pass
				pass

			elif i.type == 'text_link':
				try:
					await message.delete()
					await message.answer(
						f"<b><a href = 'tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n\nIltimos reklama tarqatmang</b>",
						reply_markup=join_chat)
				except:
					pass
				pass
			else:
				pass


		try:
			for i in message.reply_markup.inline_keyboard:
				for j in i:
					if j.url:
						try:
							await message.delete()
							await message.answer(
								f"<b><a href = 'tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> \n\nIltimos reklama tarqatmang</b>",
								reply_markup=join_chat)
						except:
							pass
						pass
		except:
			pass