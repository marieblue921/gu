from datetime import datetime

class TimeModule():
	def __init__(self):
		self.now = datetime.now()
	def getDate(self):
		return self.now.strftime("%Y-%m-%d")
	
	def getTime(self):
		return self.now.strftime("%H:%M:%S")
	def getDateTime(self):
		return self.now

