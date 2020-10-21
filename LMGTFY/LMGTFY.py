from Common import BaseBot
from Utils.Enums import LOGIN_METHOD, BOT_TYPE

class LMGTFYBot(BaseBot):
	Answer: str
	_BOT_TYPE: BOT_TYPE
	_LOGIN_METHOD: LOGIN_METHOD

	def __init__(self, login_method):
		super().__init__(login_method, bot_type=BOT_TYPE.CURSER)
	
	def ReadMD(self):
		raise NotImplementedError