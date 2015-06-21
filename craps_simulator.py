from random import randint

class Craps:

	def __init__(self):
		self.point = 0 #if this isn't 0 it is on a point
		self.off_bets = {
			"pass_line": 1/1.0,
			"dont_pass_line": 1/1.0
		};
		self.on_bets = {

		}


	def roll_dice(self):
		d1_time = randint(1,100)
		d2_time = randint(1,100)
		for i in range(d1_time):
			dice1 =  randint(1,6)
		for i in  range(d2_time):
			dice2 =  randint(1,6)

		return [dice1, dice2, dice1+dice2]



craps = Craps()
print craps.roll_dice()

print craps.off_bets["pass_line"]