def question_bank():
    # return a list of question dictionaries
    questions = [
        {
            "Q": "what is my name",
            "option": ["A. boss", "B. Bhuwan", "C. god"],
            "ans": "B",
        },
        {
            "Q": "what is my age",
            "option": ["A. 12", "B. 23", "C. 19"],
            "ans": "C",
        },
    ]
    return questions


guesses = []


def display(questions):
    global score
    for question in questions:
        print(question["Q"])
        for choice in question["option"]:
            print(choice)

        guess = input("Enter the choice(A B C): ").upper()
        guesses.append(guess)

        if guess == question["ans"]:
            print("Correct")
            score += 1
        else:
            print("incorrect")


score = 0

def main():
    q=question_bank()
    display(q)
    print("Your score is",score)
    if score==2:
        print("You scored in all")
    elif score==1:
        print("You scored half")
    else:
        print("Better luck next time!!")
    
main()