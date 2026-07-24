import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time
import subprocess
import os
# ============================
# WINDOW
# ============================

root = tk.Tk()

root.title("Chaya")
root.geometry("340x680")
root.configure(bg="#111111")

# Keep on top
root.attributes("-topmost", True)

# Remove ability to resize
root.resizable(False, False)
# ============================
# DIALOGUES
# ============================

idle_dialogues = [
    "The moon has been waiting for you.",
    "Drink some water before I start judging you.",
    "The jasmine still blooms.",
    "Back already?",
    "You know what needs to be done."
]

study_dialogues = [
    "I'll guard your focus.",
    "One task. Nothing else.",
    "The outside world can wait.",
    "Stay with me.",
    "You're doing well."
]

break_dialogues = [
    "Wonderful work.",
    "Stretch a little.",
    "Take a breath.",
    "You've earned this break.",
    "I'll be here when you're ready."
]
# ============================
# FOCUS SESSION DATA
# ============================

focus_sessions = 0

mode = "idle"

study_seconds = 25 * 60

break_seconds = 10 * 60
# ============================
# WOLF IMAGE
# ============================

wolf = Image.open("assets/wolf.png")

# Crop the poster to focus on the wolf
wolf = wolf.crop((170, 20, 1080, 980))

# Resize
wolf = wolf.resize((220,220))

wolf_photo = ImageTk.PhotoImage(wolf)

wolf_label = tk.Label(
    root,
    image=wolf_photo,
    bg="#111111",
    borderwidth=0,
    highlightthickness=0
)

wolf_label.pack(pady=(20,10))
# ============================
# TITLE
# ============================

title = tk.Label(

    root,

    text="CHAYA",

   font=("Georgia",30,"bold"),

   fg="#ff5ca8",

    bg="#111111"

)

title.pack()
flowers = tk.Label(

    root,

    text="✦ ❀ ✦",

    font=("Georgia",14),

    fg="#ff4fa3",

    bg="#111111"

)

flowers.pack(pady=(0,15))
dialogue = tk.Label(

    root,

    text=random.choice(idle_dialogues),

    wraplength=220,

    justify="center",

    font=("Georgia",12),

    fg="white",

    bg="#111111"

)

dialogue.pack(pady=10)
timer_label = tk.Label(

    root,

    text="",

    font=("Consolas",24,"bold"),

    fg="#ff4fa3",

    bg="#111111"

)

timer_label.pack(pady=10)
timer_label.pack_forget()

timer_running = False


def start_focus():

    global mode, timer_running

    if timer_running:
        return

    timer_running = True
    mode = "study"

    status_label.config(text="📚 Guarding Your Focus")

    dialogue.config(text="I'll guard your focus.")

    timer_label.pack(pady=10)

    study_button.config(
        text="📚 Focus Session Running...",
        state="disabled"
    )

    countdown(study_seconds)

def countdown(seconds):

    mins = seconds // 60
    secs = seconds % 60

    timer_label.config(text=f"{mins:02}:{secs:02}")

    if seconds > 0:

        root.after(1000, lambda: countdown(seconds-1))

    else:

        start_break()
divider = tk.Label(
    root,
    text="━━━━━━━━━━━━━━━━",
    fg="#ff4fa3",
    bg="#111111",
    font=("Arial",11)
)

divider.pack(pady=10)
# ============================
# STUDY BUTTON
# ============================

study_button = tk.Button(

    root,

    text="📚 Start Focus Session",

    command=start_focus,

    font=("Georgia",12,"bold"),

    fg="white",

    bg="#ff4fa3",

    activebackground="#ff6bb3",

    activeforeground="white",

    relief="flat",

    padx=20,

    pady=8

)

study_button.pack(pady=10)
# ============================
# PROGRESS
# ============================

progress_label = tk.Label(

    root,

   text="🌸 Today's Sessions: 0",

    font=("Georgia",11),

    fg="white",

    bg="#111111"

)

progress_label.pack(pady=(12,5))
# ============================
# STATUS
# ============================

status_label = tk.Label(

    root,

    text="🌙 Waiting",

    font=("Georgia",11,"italic"),

    fg="#ff5ca8",

    bg="#111111"

)

status_label.pack()
root.mainloop()