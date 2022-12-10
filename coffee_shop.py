#~~coffee shop~~

import os
import time
from bank import *

loop = True

while loop == True:
    os.system('cls')

    print('''
 1. coffee - 15
 2. cold-coffee - 20
    ''')

    time.sleep(1)

    choice = input('''What do you want?-
    1 or 2 \n''')

    if choice == "1":
        print("""That will be 15""")

        payment = input(f'''
        yes or no
your bank balance is {Heet} \n
''')

        payment = payment.lower()

        if payment == "yes" or "ye" or "y":

            Heet1 = Heet - 15
            
            if Heet1 >= 0:
                f = open(f"bank.py", "w")
                f.write(f"Heet = {Heet1}")
                f.close()

                print(f"your new balance is {Heet1}")

                time.sleep(1)
            
                print("anything else")
                print("")

                decision = input("yes or no \n")
                decision = decision.lower()

                if decision == "yes" or "ye" or "y":
                    print("ok")
                    time.sleep(1)

                elif decision == "no" or "n":
                    print("ok")

                    loop = False
                    time.sleep(1)

                else:
                    print("ok")

                    time.sleep(1)
                    exit()

            else:
                print("Not sufficent")
                time.sleep(2)

        elif payment == "no" or "n":
            print("order cancel")
            time.sleep(1)

        else:
            print("I am not able to Understand")

            time.sleep(1)
            print("I will take it as a no")

            loop = False

    elif choice == "2":
        print("That will be 20")
        payment = input(f'''
        yes or no
your bank balance is {Heet} \n
''')

        payment = payment.lower()

        if payment == "yes" or "ye" or "y":

            Heet1 = Heet - 20
            
            if Heet1 >= 0:
                f = open(f"bank.py", "w")
                f.write(f"Heet = {Heet1}")
                f.close()

                print(f"your new balance is {Heet1}")

                time.sleep(1)
            
                print("anything else")
                print("")

                decision = input("yes or no \n")
                decision = decision.lower()

                if decision == "yes" or "ye" or "y":
                    print("ok")
                    time.sleep(1)

                elif decision == "no" or "n":
                    print("ok")

                    loop = False
                    time.sleep(1)

                else:
                    print("ok")

                    time.sleep(1)
                    exit()

            else:
                print("Not sufficent")
                time.sleep(2)

        elif payment == "no" or "n":
            print("order cancel")
            time.sleep(1)

        else:
            print("I am not able to Understand")

            time.sleep(1)
            print("I will take it as a no")

            loop = False