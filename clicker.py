from tkinter import *
from tkinter import messagebox
points = 0
time = 10
def click():
    global points
    points += 1
    l2.config(text="POINTS: " + str(points))

def timer():
    global time
    if time > 0:
        time -= 1
        l1.config(text="TIME: " + str(time))
        window.after(1000, timer)
    else:
        b2.place_forget()
        messagebox.showinfo("GAME OVER", "POINTS: " + str(points))

def start():
    b1.place_forget()

    messagebox.showinfo(
        "GAME RULES",
        "Click the bomb.\nYou have 10 seconds."
    )
    l1.place(x=30, y=30)
    l2.place(x=400, y=30)
    b2.place(x=250, y=200)

    timer()

window = Tk()
window.title("CLICKER GAME")
window.geometry("600x500")
window.config(bg="teal")
l1 = Label(window, text="TIME: 10", bg="teal", font=("Arial", 16))
l2 = Label(window, text="POINTS: 0", bg="teal", font=("Arial", 16))
b1 = Button(window, text="START GAME", font=("Arial", 20), command=start)
b1.place(x=200, y=220)

b2 = Button(window, text="BOMB", font=("Arial", 20), command=click)

window.mainloop()