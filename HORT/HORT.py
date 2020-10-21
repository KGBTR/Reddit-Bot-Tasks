from Common import BaseBot
from Utils.Enums import LOGIN_METHOD, BOT_TYPE

class HORTBot(BaseBot):
	Answer: str
	_BOT_TYPE: BOT_TYPE
	_LOGIN_METHOD: LOGIN_METHOD

	def __init__(self, login_method: LOGIN_METHOD):
		super().__init__(login_method, bot_type=BOT_TYPE.CURSER)

	def ReplyComment(self, answer: str=None):
		super().ReplyComment(answer)

	def ReadMD(self):
		raise NotImplementedError