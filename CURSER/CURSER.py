from Common import BaseBot
from Utils.Enums import LOGIN_METHOD, BOT_TYPE, BOT_TRIGGER_WORD, BOT_TRIGGER_MARK

class CurseBot(BaseBot):
	def __init__(self, login_method: LOGIN_METHOD, bot_trigger_mark: BOT_TRIGGER_MARK):
		super().__init__(
			login_method=login_method,
			bot_type=BOT_TYPE.CURSER,
			bot_trigger_word=BOT_TRIGGER_WORD.CURSER,
			bot_trigger_mark=bot_trigger_mark
		)

	def ReadMD(self):
		raise NotImplementedError

	def ReplyComment(self, answer: str=None):
		super().ReplyComment(answer)