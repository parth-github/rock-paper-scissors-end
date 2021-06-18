import random, os, time
from rps import RPS

rps = RPS()
rounds = int(input("Enter the number of rounds you want to play:\n"))

for i in range(1, rounds + 1):
    print(f"Round:{i}")
    computer_choice = random.randint(1, 3)
    your_choice = int(
        input(
            "Enter your choice:\n 1-> rock \n 2 -> paper \n 3 -> scissors \n"))
    while your_choice < 1 or your_choice > 3:
        your_choice = int(
            input(
                "You have entered a wrong choice.\nEnter correct choice: 1 or 2 or 3:\n"
            ))
    print("*******************")
    print(f"Computer has choosen: ###{rps.choice_dict[computer_choice]}###")
    print(f"You have choosen: ***{rps.choice_dict[your_choice]}***")

    rps.check_result(your_choice, computer_choice)
    # RPS.update_score("You won")
    time.sleep(2)
    print("-----------------")
    #os.system("clear")

rps.show_final_result()
