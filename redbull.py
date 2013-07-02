from time import sleep
from random import randint

alertLevel = 10
money = 2


def drinkRedBull(a):
    a += 30
    return a

def checkPocketChange(a, m):
    if m >= 2:
        print("You got a Red Bull and you're FLYING!!")
        a = drinkRedBull(a)
        m -= 2
        return a, m
    else:
        print("You're out of money!")
        print("SLEEP MODE... ACTIVATE!")
        print("...while attempting to buy a Red Bull you fall asleep on the"
        " pavement in front of the gas station...")
        for i in range(5):
            print("Zzz...")
            sleep(1)
        print("You wake up 8 hours later feeling refreshed\n")
        m = randint(1, 10)
        print("You look around and realize people mistook you for a beggar and"
        " have given you a total of ${}!".format(m))
        a = 100
        return a, m



while alertLevel >= 1:
    sleep(1)
    alertLevel -= 5
    print(alertLevel)
    if alertLevel < 10:
        aL = checkPocketChange(alertLevel, money)
        alertLevel = aL[0]
        money = aL[1]
