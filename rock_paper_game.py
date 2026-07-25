# Python Rock, Paper, Scissor Game
import random
def get_computer():
    return random.choice(['rock','paper','scissors'])

def winner(player,computer):
    if player==computer:
        return "tie"

    wins_against={
        'rock':'scissors',
        'paper':'rock',
        'scissors':'paper'
    }

    if wins_against[player]==computer:
        return "Player"
    else:
        return "Computer"

def play_round(score):
    player=input("Choose(rock, paper, scissors): ").lower()
    if player not in ['rock','paper','scissors']:
        print("Invalid choice. Try again")
        return
    computer=get_computer()
    result=winner(player,computer)

    if result=='tie':
        print("You chose: ",player)
        print("Computer chose: ",computer)
        print("Its a tie.")
        score['ties']+=1
    elif result=='Player':
        print("You chose: ",player)
        print("Computer chose: ",computer)
        print("You won this round.")
        
        score['wins']+=1
    else:
        print("You chose: ",player)
        print("Computer chose",computer)
        print("Computer won this round")
        score['loss']+=1


def main():
    score={"wins":0,"loss":0,"ties":0}
    print("---Welcome to Rock Paper Scissors Game---")
    print("------------------------------------------")
    while True:
        play_round(score)
        print(f"\n Score-> You: {score['wins']} Computer: {score['loss']} Ties: {score['ties']}")

        if score['wins']==5:
            print("You won the match")
            break
        elif score['loss']==5:
            print("Computer won this match. Better Luck next time! ")
            break
        again=input("Do you want to play again?(y or n): ").lower()
        if again == 'n':
            print("Thanks for trying it out!!!")
            break
main()
    