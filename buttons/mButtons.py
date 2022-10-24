from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


main_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_btn.add("📊Statistika", "📤User reklama", "📤Guruh reklama", "🤬So'kinishlar")


reklama_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
reklama_btn.add("📨Forward xabar yuborish", "📬Oddiy xabar yuborish", "🔙Orqaga qaytish")


G_reklama_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
G_reklama_btn.add("📨Forward xabar yuborish.", "📬Oddiy xabar yuborish.", "🔙Orqaga qaytish")


join_chat = InlineKeyboardButton("💸100 mln so‘m aksiya💸", url="http://t.me/Millitsiyabot?startgroup")
join_chat = InlineKeyboardMarkup().add(join_chat)


join_chat1 = InlineKeyboardMarkup().add(InlineKeyboardButton("Botni guruhga qo'shish", url="http://t.me/Millitsiyabot?startgroup"))


S_baza = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
S_baza.add("So'z qo'shish", "So'zlar ko'rish", "🔙Orqaga qaytish")