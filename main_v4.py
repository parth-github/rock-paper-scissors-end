import random, os, time, cursor

rps_dict = {
    1: "rock",
    2: "paper",
    3: "scissors",
}

score = {
    "your_score": [],
    "computer_score": [],
}
rules_list = [
	[1,1,1],
	[1,2,0],
	[1,3,2],
	[2,1,2],
	[2,2,1],
	[2,3,0],
	[3,1,0],
	[3,2,2],
	[3,3,0]
]

won_case = [(1,3),(2,1),(3,2)]


your_final_score = 0
computer_final_score = 0


def update_score(result):
    if result == "Draw":
        score["your_score"].append(1)
        score["computer_score"].append(1)
    elif result == "You won":
        score["your_score"].append(2)
        score["computer_score"].append(0)
    elif result == "Penalty":
        score["your_score"].append(-1)
        score["computer_score"].append(1)
    elif result == "You lost":
        score["your_score"].append(0)
        score["computer_score"].append(2)


rounds = int(input("Enter the number of rounds you want to play:\n"))

for i in range(1, rounds + 1):
    result = ""
    cursor.show()
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

    # if your_choice < 1 or your_choice > 3:
    #     print("Enter correct choice: 1 or 2 or 3")
    #     result = "Penalty"
    #     update_score(result)
    #     time.sleep(2)
    #     os.system("clear")
    #     continue

    print("*******************")
    print(f"Computer has choosen: ###{rps_dict[computer_choice]}###")
    print(f"You have choosen: ***{rps_dict[your_choice]}***")
    
		if your_choice == computer_choice:
			result = "Draw"
			print("Draw")
    elif (your_choice, computer_choice) in won_case:
			result = "You won"
			print("You won")
		else:
			result = "You lost"
			print("You lost")

    update_score(result)
    cursor.hide()
    time.sleep(2)
    print("-----------------")
    #os.system("clear")

for your_score in score["your_score"]:
    your_final_score += your_score

for computer_score in score["computer_score"]:
    computer_final_score += computer_score

print(f'''
Final score board:
******************
Your score\t|Computer score
---------------------------
{score["your_score"]}\t|{score["computer_score"]}
----------------------------
{your_final_score}\t|{computer_final_score}
----------------------------

''')

if your_final_score > computer_final_score:
    print("You won the game!!!")
elif your_final_score == computer_final_score:
    print("Draw!!!")
else:
    print("You lost the game!!!")
