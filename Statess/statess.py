from aiogram.dispatcher.filters.state import State, StatesGroup

class From(StatesGroup):
	send_msg = State()
	forward_msg = State()
	sendG_msg = State()
	forwardG_msg = State()

	Soz_add = State()

	sent_num = State()

	natijaS = State()

	natija2S = State()