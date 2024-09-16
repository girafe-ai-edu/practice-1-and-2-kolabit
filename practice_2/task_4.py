# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
# Loop the console input until User enetr the 4-digits number
while True:
    print ("Please enter a integer 4-digit number")
    num = input()
    n_dig = len(num)
    if (len(num)==4):
        break
    print (f"ERROR: you have eneterd {n_dig}-digit number")

sum = int(num[0])+int(num[1])+int(num[2])+int(num[3])

print(f"{num[0]} + {num[1]} + {num[2]} + {num[3]} = {sum}")

