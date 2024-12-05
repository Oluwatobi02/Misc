def onColorClick(color):
    print(color,'clicked')

def onHobbyEnter(e):
    print("Oh thats nice!!")

def onSeriesEnter(e):
    global done
    series = series_text.get("1.0", "end-1c")
    print(series)
    done = True
def end_program():
    Label(root, text="Thank you for participating").pack()
    Button(root, text="Exit", command=root.quit).pack()

from tkinter import *

root = Tk()

header = Label(root, text="Welcome to My application").pack()


color_frame = Frame(root)
color_frame.pack()
question1 = Label(color_frame, text= "What is your favorite color?")
question1.pack()
selected_color = StringVar(value='none')
Radiobutton(color_frame, text="blue", value="blue", variable=selected_color, command=lambda: onColorClick("blue")).pack()
Radiobutton(color_frame, text="red", value="red", variable=selected_color, command=lambda: onColorClick("red")).pack()
Radiobutton(color_frame, text="green", value="green", variable=selected_color, command=lambda: onColorClick("green")).pack()
Radiobutton(color_frame, text="yellow", value="yellow", variable=selected_color, command=lambda: onColorClick("yellow")).pack()
Radiobutton(color_frame, text="purple", value="purple", variable=selected_color, command=lambda: onColorClick("purple")).pack()

hobby_frame = Frame(root)
hobby_frame.pack()
question2 = Label(hobby_frame, text= "What is your favorite hobby?")
question2.pack()
hobby_text = Text(root, width=40, height=1)
hobby_text.bind("<Return>", onHobbyEnter)
hobby_text.pack()

    
series_frame = Frame(root)
series_frame.pack()
series = Label(series_frame, text= "What is your favorite kdrama series?").pack()
series_text = Text(root, width=40, height=1)
series_text.bind("<Return>", onSeriesEnter)
series_text.pack()

    
next_button = Button(root, text="Next", command=end_program).pack()


root.mainloop()