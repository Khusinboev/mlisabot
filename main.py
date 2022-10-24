from handlaers.startFor import *
from handlaers.admin_panel import *

# @dp.message_handler(commands='toshiqoy')
# async def helper(message: types.Message):
#     # await message.reply('hoz')
#     # import shutil
#     # shutil.make_archive("../for_mandat", 'zip', "../for_mandat")
#     await message.reply_document(document=open("databasa/database.sqlite3", 'rb'))


@dp.message_handler(content_types="any")
async def helper(message: types.Message):
    status = await dp.bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    print(status.status)
    kerak = await delete_msg(message)
    datas = sql.execute(f"SELECT word FROM words").fetchall()
    text = []
    for data in datas:
        text.append(data[0].lower())
    Sokinishlar = text
    try:
        soz = message.text.lower().split()
    except:
        soz = ''

    group_id = message.chat.id
    sql.execute(
        """CREATE TABLE IF NOT EXISTS groups ("group_id"  INTEGER,"date"  INTEGER);""")
    db.commit()
    check = sql.execute(f"""SELECT group_id FROM groups WHERE group_id = {group_id}""").fetchone()
    if check == None:
        if message.chat.type == 'supergroup':
            sana = datetime.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%d-%m-%Y %H:%M')
            sql.execute(
                f"""INSERT INTO groups (group_id, date) VALUES ('{group_id}', '{sana}')""")
            db.commit()
    else:
        pass


    if "new_chat_member" in message.as_json():
        user = message.new_chat_members
        if user[0].username == "Millitsiyabot":
            await message.answer("""👋 Assalomu alakum!

👮🏻‍♂️ Men guruhlardagi kirdi-chiqdi xabarlarni guruhlardan o'chirib turaman. 

😄 Ishimni boshlashim uchun meni guruhingizda qo'shing va ADMIN qiling""", reply_markup=join_chat)
        else:
            try:
                await message.delete()
            except:
                pass


    elif "left_chat_participant" in message.as_json():
        if message.left_chat_member.username == "Millitsiyabot":
            sql.execute(f"DELETE FROM groups WHERE group_id ='Millitsiyabot'")
            db.commit()
        else:
            await message.delete()

    elif "sender_chat" in message:
        if message.is_automatic_forward:
            pass
        else:
            print(message.from_user.first_name)
            if message.from_user.first_name == 'Group':
                pass
            else:
                # msg = await dp.bot.get_chat_member(chat_id=message.sender_chat.id, user_id=message.chat.id)
                # print(msg)
                try:
                    await message.delete()
                    await message.answer(f"<b><a href = 'tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> <b>Iltimos kanal nomidan yozmang</b>")
                except:
                    pass


    else:
            try:
                for s in soz:
                    s = [s]
                    if set(s).issubset(Sokinishlar) == True:
                        await message.delete()
                        await message.answer(
                            f"❗<b><a href = 'tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> So'kinish mumkinmas")
            except:
                pass


if __name__ == "__main__":
    executor.start_polling(dp)
