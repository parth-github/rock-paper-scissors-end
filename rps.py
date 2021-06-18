class RPS:
    choice_dict = {
        1: "rock",
        2: "paper",
        3: "scissors",
    }
    score = {
        "your_score": [],
        "computer_score": [],
    }
    won_case = ((1, 3), (2, 1), (3, 2))
    your_final_score = 0
    computer_final_score = 0

    def update_score(result):
        if result == "Draw":
            RPS.score["your_score"].append(1)
            RPS.score["computer_score"].append(1)
        elif result == "You won":
            RPS.score["your_score"].append(2)
            RPS.score["computer_score"].append(0)
        elif result == "Penalty":
            RPS.score["your_score"].append(-1)
            RPS.score["computer_score"].append(1)
        elif result == "You lost":
            RPS.score["your_score"].append(0)
            RPS.score["computer_score"].append(2)

    def check_result(self, your_choice, computer_choice):
        result = ""
        if your_choice == computer_choice:
            result = "Draw"
            print("Draw")
        elif (your_choice, computer_choice) in RPS.won_case:
            result = "You won"
            print("You won")
        else:
            result = "You lost"
            print("You lost")
        RPS.update_score(result)

    def show_final_result(self):
        for your_score in RPS.score["your_score"]:
            RPS.your_final_score += your_score

        for computer_score in RPS.score["computer_score"]:
            RPS.computer_final_score += computer_score

        print(f'''
            Final score board:
            ******************
            Your score\t|Computer score
            ---------------------------
            {RPS.score["your_score"]}\t|{RPS.score["computer_score"]}
            ----------------------------
            {RPS.your_final_score}\t|{RPS.computer_final_score}
            ----------------------------
            ''')
        if RPS.your_final_score > RPS.computer_final_score:
            print("You won the game!!!")
        elif RPS.your_final_score == RPS.computer_final_score:
            print("Draw!!!")
        else:
            print("You lost the game!!!")
