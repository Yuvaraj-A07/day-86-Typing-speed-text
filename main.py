import math
from tkinter import *

MIN = 1
my_timer = None

sample_txt = ("Typing speed is a crucial skill in the digital age. It helps increase productivity and efficiency in "
              "both professional and personal tasks. The ability to type quickly and accurately can significantly "
              "reduce the time spent on writing and editing documents. Practice regularly to improve your typing "
              "speed, focusing on accuracy first before increasing speed. Over time, you'll find that your typing "
              "becomes more fluid and natural, helping you accomplish tasks more effectively.")


# function to start the timer
def start_timer():
    u_text.delete("1.0", END)
    u_text.focus()
    minute = MIN * 60
    count_down(minute)


# function to process the time that is 1 min
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        window.after_cancel(my_timer)
        # u_text.focus_displayof()
        calculate_speed()


# function to calculate the typing speed

def calculate_speed():
    original_txt = text.get("1.0", END)
    user_txt = u_text.get("1.0", END)
    print(original_txt)
    print(user_txt)
    o_txt_count = len(original_txt)
    u_txt_count = len(user_txt)
    original_list = original_txt.split(" ")
    user_list = user_txt.split(" ")
    # original_list[-1] = original_txt[-1].split('')[0]
    print(original_list)
    print(user_list)

    # checking how many words per second

    gross_wpm = math.floor((u_txt_count / 5) / MIN)

    # counting error
    count = 0
    for i in range(len(user_list)):
        if original_list[i].lower() != user_list[i].lower():
            count = count + 1

    # now calculating net WPM

    net_wpm = math.floor(gross_wpm - (count / MIN)) + 1
    print(count)
    print(f"Total no of words per minute = {net_wpm}")
    acc = ((len(user_list) - count) / len(user_list)) * 100
    label = Label(text=f'Total number of WPM = {net_wpm} with an accuracy of {round(acc, 1)} %',
                  font=('Courier', 24, 'bold'), bg='white', fg='green')
    label.pack(pady=5)


# UI for Speed Text

window = Tk()
window.title("Typing Speed Test")
window.config(padx=20, pady=20)

# Title Label

title_lab = Label(text="Typing Speed Text", font=("Courier", 24, "bold"), fg="green", bg='white')
title_lab.pack(pady=5)

# Timer canvas

canvas = Canvas(width=60, height=30, bg='#88d66c')
timer_text = canvas.create_text(30, 15, text="Timer", font=('Courier', 16, 'bold'))
canvas.pack(pady=5)

# Text
text = Text(height=8, width=70, font=('Courier', 14, 'bold'), padx=10, pady=10)
text.insert(END, sample_txt)
text.pack(pady=5)

# start button

button = Button(text="Start", command=start_timer, bg='#b4e380', width=10, font=('Courier', 14, 'bold'))
button.pack(padx=5, pady=5)

# user Text

u_text = Text(height=8, width=70, font=('Courier', 14, 'bold'), padx=10, pady=10)
u_text.insert(END, "you can start typing here by clicking on the start button !")
u_text.pack(pady=5)

window.mainloop()
