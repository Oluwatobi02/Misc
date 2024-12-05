from tkinter import *
def printName(name):
    Label(top_frame, text="Hello, " + name).pack()

def getName(event):
    name = name_text.get("1.0", "end-1c")
    printName(name)

def printGame(game):
    Label(games_frame, text="Your favorite game is " + game).pack()

def getGame(event):
    game = games_text.get("1.0", "end-1c")
    printGame(game)   


root = Tk()

top_frame = Frame(root)
top_frame.pack()
top = Label(top_frame, text="Welcome! Whats your name? ").pack()
name_text = Text(top_frame, width=40, height=1)
name_text.bind("<Return>", getName)
name_text.pack()


games_frame = Frame(root)
games_frame.pack()
games = Label(games_frame, text= "What is your favorite game?").pack()
games_text = Text(root, width=40, height=1)
games_text.bind("<Return>", getGame)
games_text.pack()

selected_game = StringVar(value='none')
games_review_frame = Frame(root)
games_review_frame.pack()
question1 = Label(games_review_frame, text= "Do you like this game?").pack()
Radiobutton(games_review_frame, text="yes", value="yes", variable=selected_game,).pack()
Radiobutton(games_review_frame, text="no", value="no", variable=selected_game).pack()

next_button = Button(root, text="End", command=root.quit).pack()

root.mainloop()