import random, os, time

rps_dict = {
	1: "rock",
	2: "paper",
	3: "scissors",
}

score = {
  "your_score": [],
  "computer_score": [],
}
your_final_score = 0
computer_final_score = 0

for i in range(1, 6):
	print(f"Round:{i}")
	computer_choice = random.randint(1,3)
	your_choice = int(input("Enter your choice:\n 1-> rock \n 2 -> paper \n 3 -> scissors \n"))
	
	print("*******************")
	print(f"Computer has choosen:{rps_dict[computer_choice]}")
	print(f"You have choosen:{rps_dict[your_choice]}")
	if your_choice == computer_choice:
		print("Draw")
		score["your_score"].append(1)
		score["computer_score"].append(1)
	elif your_choice == 1 and computer_choice == 3:
		print("You won")
		score["your_score"].append(2)
		score["computer_score"].append(0)
	elif your_choice == 3 and computer_choice == 1:
		print("You lost")
		score["computer_score"] += 2

	elif your_choice > computer_choice:
		print("You won")
		score["your_score"].append(2)
		score["computer_score"].append(0)
	else:
		print("You lost")
		score["your_score"].append(0)
		score["computer_score"].append(2)

	time.sleep(2)
	os.system("clear")

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
''')