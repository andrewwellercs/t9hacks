import random

class Enemy:
	def __init__(self):
		self.name = random.choice(['skeleton', \
									'spider', \
									'ghoul',\
									'zombie'])
		self.health = 10

	def getDamage(self):
		return random.randint(6,20)