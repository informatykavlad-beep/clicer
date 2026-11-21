from tkinter import *
from tkinter import messagebox

def start():
    messagebox.showinfo(
        "Game Rules",
        "Click the bomb and collect points.\nYou have only 10 seconds."
    )

window = Tk()
window.title("CLICKER GAME")
window.geometry("600x500")
window.config(bg="teal")

btn = Button(window, text="START GAME", font=("Arial", 20), command=start)
btn.place(x=210, y=220)

window.mainloop()