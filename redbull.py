import sys
from time import sleep
from random import randint

alertLevel = 100
money = 3


def drinkRedBull(a):
	a += 30
	return a

def checkPocketChange(a, m):
	if m >= 2:
		print("\n\nYou go to the gas station to buy a Red Bull.")
		sleep(2)
		print("\nYou got a Red Bull and you're FLYING!!\n")
		sleep(2)
		a = drinkRedBull(a)
		m -= 2
		return a, m
	else:
		print("\n\nYou go to the gas station to buy a Red Bull.")
		print("\nYou're out of money!\n")
		sleepMode = "SLEEP MODE..."
		activ = "ACTIVATE!!!"
		for l in sleepMode:
			print(l,end="")
			sys.__stdout__.flush()
			sleep(0.1)
		sleep(2) 
		for l in activ:
			print(l, end="")
			sys.__stdout__.flush()
			sleep(0.1)
		sleep(2) 
		print("\n")
		print("\n...while attempting to buy a Red Bull you fall asleep\n on the"
		" pavement in front of the gas station...\n")
		sleep(2)
		zees = "Zzzz..."
		for l in zees:
			print(l, end = "")
			sys.__stdout__.flush()
			sleep(1)
		sleep(1)
		print("\n")
		print("\nYou wake up 8 hours later feeling refreshed!\n")
		m = randint(1, 10)
		print("You look around and realize people mistook you for a beggar and"
		" have given you a total of ${}!\n".format(m))
		sleep(2)
		a = 100
		return a, m



while alertLevel >= 1:
	sys.stdout.write("\r{}".format(""))
	sys.stdout.write("\r{}".format(alertLevel))
	sys.stdout.flush()
	sleep(1)
	alertLevel -= 5
	if alertLevel < 10:
		aL = checkPocketChange(alertLevel, money)
		alertLevel = aL[0]
		money = aL[1]
