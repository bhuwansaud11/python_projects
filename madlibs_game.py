# madlibs=word game where we build a story by filling in the blanks

def words():
    name = input("Enter the name: ")
    adjective = input("Enter the adjective: ")
    noun = input("Enter the noun: ")
    verb = input("Enter the verb: ")
    place = input("Enter the place: ")
    animal = input("Enter the animal: ")
    while True:
        try:
            number = int(input("Enter the number: "))
            break
        except ValueError:
            print("Please enter a valid integer for the number.")

    return {
        "name": name,
        "adjective": adjective,
        "noun": noun,
        "verb": verb,
        "place": place,
        "animal": animal,
        "number": number
    }

def build_story(words):
    story = (
        f"One day, {words['name']} was walking through {words['place']} "
        f"when a {words['adjective']} {words['animal']} appeared out of nowhere. "
        f"Without thinking, {words['name']} grabbed a {words['noun']} and "
        f"{words['verb']} as fast as possible. "
        f"It took exactly {words['number']} seconds to escape!"
    )
    return story

def madlibs():
    w = words()
    bs = build_story(w)
    print("Your story")
    print(bs)

while True:
    madlibs()
    choice=input("Do you want to continue(y/n): ")
    if choice.lower()=="n":
        print("Thanks for playing the madlibs game!")
        break

