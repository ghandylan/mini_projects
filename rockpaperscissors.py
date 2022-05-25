import random
import time
import os

class RockPaperScissors:
    def cls(self):
        print("\n"*100)
    def cpuchoice(self):
        choices = ["rock", "paper", "scissors"]
        cpu = random.choice(choices)    
        return cpu
    
    def mainloop(self):
        print("""
play against an AI
best of 3""")
        cpu_score = 0
        user_score = 0
        self.cls()
        while True:
            choice = str(input(("""

choices:
rock
paper
scissors

enter choice: """)))
            choices = ["rock", "paper", "scissors"]
            if choice == "scores":
                print("your score =",user_score)
                print("AI score =", cpu_score)
                continue
            if choice not in choices:
                print("Invalid choice!")
                continue
            else:
                time.sleep(1.2)
                cpu_choice_storage = self.cpuchoice()
                if choice == "rock": # if user chooses rock
                    if cpu_choice_storage == "rock": # rock vs rock = tie
                        print(f"You chose {choice}")
                        time.sleep(1)
                        print(f"AI chose {cpu_choice_storage}")
                        print("It's a tie!")
                    elif cpu_choice_storage == "paper": # rock vs paper = rock loses
                        print(f"You chose {choice}")
                        time.sleep(1)
                        print(f"AI chose {cpu_choice_storage}")
                        print(f"You lose! {cpu_choice_storage} beats {choice}!")
                        cpu_score += 1
                    else:
                        print(f"You chose {choice}") # rock vs scissors = rock wins
                        time.sleep(1)
                        print(f"AI chose {cpu_choice_storage}")
                        print(f"You win! {choice} beats {cpu_choice_storage}!")
                        user_score += 1

                elif choice == "paper": # if user chooses paper
                    if cpu_choice_storage == "paper": # paper vs paper = tie
                        print(f"You chose {choice}")
                        time.sleep(1)
                        print(f"AI chose {cpu_choice_storage}")
                        print("It's a tie!")  
                    elif cpu_choice_storage == "paper": # paper vs scissors = paper loses
                        print(f"You chose {choice}")
                        time.sleep(1)
                        print(f"AI chose {cpu_choice_storage}")
                        print(f"You lose! {cpu_choice_storage} beats {choice}!")
                        cpu_score += 1                                          
                    else:
                        print(f"You chose {choice}") # paper vs rock = paper wins
                        time.sleep(1)
                        print(f"AI chose {cpu_choice_storage}")
                        print(f"You win! {choice} beats {cpu_choice_storage}!")
                        user_score += 1

                else: # if user chooses scissors
                    if cpu_choice_storage == "scissors": # scissors vs scissors = tie
                        print(f"You chose {choice}")
                        time.sleep(1)
                        print(f"AI chose {cpu_choice_storage}")
                        print("It's a tie!")  
                    elif cpu_choice_storage == "rock": # scissors vs rock = scissors loses
                        print(f"You chose {choice}")
                        time.sleep(1)
                        print(f"AI chose {cpu_choice_storage}")
                        print(f"You lose! {cpu_choice_storage} beats {choice}!")
                        cpu_score += 1                                          
                    else:
                        print(f"You chose {choice}") # scissors vs paper = paper wins
                        time.sleep(1)
                        print(f"AI chose {cpu_choice_storage}")
                        print(f"You win! {choice} beats {cpu_choice_storage}!")
                        user_score += 1
start = RockPaperScissors()
start.mainloop() 