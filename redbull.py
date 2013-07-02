import sys
from time import sleep
from random import randint


alertLevel = randint(25, 100)

money = randint(1, 10)


def drinkRedBull(a):
	a += randint(15, 40)
	return a

def checkPocketChange(a, m):
	if m >= 2:
		sleep(1)
		print("\n\nYou go to the gas station to buy a Red Bull.")
		sleep(2)
		print("\nYou got a Red Bull and you're FLYING!!\n")
		sleep(2)
		a = drinkRedBull(a)
		m -= 2
		return a, m
	else:
		sleep(2)
		print("\n\nYou go to the gas station to buy a Red Bull.")
		sleep(2)
		print("\nYou're out of money!\n")
		sleep(2)
		sleepMode = "sleep mode..."
		activ = "ACTIVATE!!!"
		for l in sleepMode:
			print(l,end="")
			sys.__stdout__.flush()
			sleep(0.1)
		sleep(1) 
		for l in activ:
			print(l, end="")
			sys.__stdout__.flush()
			sleep(0.1)
		for l in range(5):
			sys.stdout.write("\rsleep mode...            ")
			sys.stdout.flush()
			sleep(.1)
			sys.stdout.write("\rsleep mode... ACTIVATE!!!")
			sys.stdout.flush()
			sleep(0.5)
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

if alertLevel <= 50:
	print ("\nYou're feeling tired today...\n")
	sleep(1)


while alertLevel >= 1:
	sys.stdout.write("\r{}".format("                "))
	sys.stdout.write("\rAlert Level: {}".format(alertLevel))
	sys.stdout.flush()
	sleep(1)
	alertLevel -= 5
	if alertLevel < 10:
		aL = checkPocketChange(alertLevel, money)
		alertLevel = aL[0]
		money = aL[1]
