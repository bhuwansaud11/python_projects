from tkinter import * 
import csv
import os

info = [
    ["questions","answers"],
    ["What is a list in Python?","An ordered collection of items"],
    ["What is a dictionary?","A collection of key-value pairs"],
    ["What is a function?","A reusable block of code"],
    ["What is OOP?","Object Oriented Programming"],
    ["What is a loop?","A block of code that repeats"]
]
filename = "Flashcard_qna.csv"
if not os.path.exists(filename):
    with open(filename,'w') as file:
    
        writer = csv.writer(file)
        for i in info:
            writer.writerow(i)
        print("File written successfully")

def load(): 
    cards=[]
    with open(filename,'r') as file:
        file = csv.DictReader(file)
        for f in file:
            cards.append(f)
        print("file read successfully")

    return cards

cards = load()
current_index = 0
card = 1
def show_card():
    if not cards:
        return
    label.config(text=f"Card {card} of {len(cards)}")
    if is_flipped:
        canvas.itemconfig(text_id,text=cards[current_index]['answers'])
    else:
        canvas.itemconfig(text_id,text=cards[current_index]['questions'])
    

def next_card():
    global current_index, is_flipped, card
    if current_index<len(cards)-1:
        is_flipped = False
        current_index+=1
        card+=1 # or use the current_index directly in show_card()
        show_card()

def previous_card():
    global current_index, is_flipped, card
    if current_index>0:
        is_flipped = False
        current_index-=1
        card-=1
        show_card()

is_flipped = False
def flip_card(event=None):
    global is_flipped
    is_flipped = not is_flipped
    show_card()
window = Tk()
window.geometry("600x600")
window.title("flash Card App")

Label(window,text="Flash Card App",font=("Arial",15),fg="black").pack()
label = Label(window,font=("Arial",15),fg="black")
label.pack()
canvas = Canvas(window,height=300,width=500,bd=3,relief=SUNKEN)
text_id = canvas.create_text(250,150,font=('Arial',20))
show_card()
canvas.bind("<Button-1>", flip_card)
canvas.pack()
Button(window,text="Previous",font=("Arial",12),bg="blue",fg="white",activebackground="blue",activeforeground="white",command=previous_card).place(x=200,y=340)
Button(window,text="Next",font=("Arial",12),bg="blue",fg="white",activebackground="blue",activeforeground="white",command=next_card).place(x=290,y=340)




window.mainloop()