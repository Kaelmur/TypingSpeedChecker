import random
import tkinter as tk


screen = tk.Tk()
result = tk.Label()
again = tk.Label()
is_not_over = False
time_left = tk.Label()
label = tk.Label()
label_current = tk.Label()
labelw = tk.Label()
second_passed = 0


def stop():
    global is_not_over
    is_not_over = False
    words = len(label.cget("text").split(" "))
    time_left.destroy()
    label_current.destroy()
    label.destroy()
    labelw.destroy()
    global result
    result = tk.Label(screen, text=f"Words per Minute: {words}", fg="black")
    result.grid(column=0, row=1)
    global again
    again = tk.Button(screen, text=f"Start Again", command=restart)
    again.grid(column=0, row=0)


def restart():
    result.destroy()
    again.destroy()
    reset()


def second():
    global second_passed
    second_passed += 1
    time_left.config(text=f"{second_passed} Seconds")
    global is_not_over
    if is_not_over:
        screen.after(1000, second)


def pressed(event=None):
    try:
        if event.char.lower() == labelw.cget("text")[0].lower():
            labelw.configure(text=labelw.cget("text")[1:])
            label.configure(text=label.cget("text") + event.char.lower())
            label_current.configure(text=f'Letter to write: {labelw.cget("text")[0]}')
    except tk.TclError:
        pass


def reset():
    list_of_texts = ["Life is a journey full of twists and turns, ups and downs, and unexpected detours. We never know what's going to happen next, but that's what makes it so exciting. Whether we're soaring high or hitting rock bottom, every experience has something to teach us. It's up to us to learn from those experiences and grow into the people we were meant to be.",
                     "Success is a journey, not a destination. It's a long and winding road, full of obstacles and challenges. But with hard work and perseverance, we can overcome any obstacle and achieve our goals. It's not always easy, but it's always worth it in the end. So don't give up, no matter how difficult the journey may seem. Keep pushing forward, and eventually, you'll find your way.",
                     "We all have a story to tell, and every story is unique. Some stories are tragic, while others are filled with hope and triumph. But no matter the plot, every story has a lesson to teach us. So listen carefully, for the stories we tell may hold the key to unlocking the secrets of our lives. And remember, our stories are never truly over. As long as we're alive, we have the power to rewrite the narrative and create a new ending."]

    write_text = random.choice(list_of_texts).lower()

    point = 0
    global label
    label = tk.Label(screen, text=write_text[0:point])
    label.grid(column=0, row=1)
    global labelw
    labelw = tk.Label(screen, text=write_text[point:])
    labelw.grid(column=0, row=1)
    global label_current
    label_current = tk.Label(screen, text=f"Letter to write: {write_text[point]}", fg="black", font="bold")
    label_current.grid(column=0, row=3)
    global time_left
    time_left = tk.Label(screen, text=f"0 Seconds")
    time_left.grid(column=0, row=0)
    global is_not_over
    is_not_over = True
    screen.bind("<Key>", pressed)
    global second_passed
    second_passed = 0
    screen.after(1000, second)
    screen.after(60000, stop)


reset()
screen.mainloop()
