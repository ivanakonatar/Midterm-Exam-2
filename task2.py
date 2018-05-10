"""
===================   TASK 2   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

from random import randint

bacanja= int(input("Koliko puta bacate kocku? "))

palo_1 = palo_2 = palo_3 = palo_4 = palo_5 = palo_6 = 0

for i in range(bacanja):

    palo = randint(1,6)

    if palo == 1:
        palo_1+=1

    elif palo ==2:
        palo_2 +=1

    elif palo== 3:
        palo_3+=1

    elif palo ==4:
        palo_4 +=1

    elif palo ==5:
        palo_5+=1

    else:
        palo_6+=1

print("1 je pala " + str(palo_1) + " put/a.")
print("2 je pala " + str(palo_2) + " put/a.")
print("3 je pala " + str(palo_3) + " put/a.")
print("4 je pala " + str(palo_4) + " put/a.")
print("5 je pala " + str(palo_5) + " put/a.")
print("6 je pala " + str(palo_6) + " put/a.")