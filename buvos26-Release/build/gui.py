import sys
import tkinter
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from links import inftab

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.geometry("769x705")
window.configure(bg = "#202020")
window.overrideredirect(False)
icon = tkinter.PhotoImage(file="./assets/favicon.png")
icon = window.iconphoto(True, icon) #Ikonfotó definiálása
window.title("Bűvös26 - GDE")

import subprocess
import re
import os

def regenerate_numbers():
    all_random_numbers.clear()  # Törli az előzőleg generált számokat
    for i in range(3):
        result = subprocess.run(['python', script_path], capture_output=True, text=True)

        # Ellenőrizzük, hogy a script sikeresen lefutott-e
        if result.returncode == 0:
            match = re.search(r'\[(.*?)\]', result.stdout)
            if match:
                random_numbers_str = match.group(1)
                random_numbers = tuple(int(num) for num in random_numbers_str.split(','))
                all_random_numbers.append(random_numbers)
    # Frissítsük a gombok szövegét az új számokkal
    button_1.config(text=all_random_numbers[0][0])
    button_2.config(text=all_random_numbers[0][1])
    button_3.config(text=all_random_numbers[0][2])
    button_4.config(text=all_random_numbers[0][3])
    button_5.config(text=all_random_numbers[1][0])
    button_6.config(text=all_random_numbers[1][1])
    button_7.config(text=all_random_numbers[1][2])
    button_8.config(text=all_random_numbers[1][3])
    button_9.config(text=all_random_numbers[2][0])
    button_10.config(text=all_random_numbers[2][1])
    button_11.config(text=all_random_numbers[2][2])
    button_12.config(text=all_random_numbers[2][3])


# Replace 'your_script.py' with the path to your Python file
script_path = 'generating/26-random.py'
print("Current working directory:", os.getcwd())

# List to store all sets of random numbers
all_random_numbers = []

# Run the script three times and capture the outputs
for i in range(3):
    result = subprocess.run(['python', script_path], capture_output=True, text=True)

    # Check if the script ran successfully
    if result.returncode == 0:
        print(f"Script {i + 1} executed successfully!")
        print("Output:")
        print(result.stdout)

        # Extract random numbers from the output using regular expression
        match = re.search(r'\[(.*?)\]', result.stdout)
        if match:
            random_numbers_str = match.group(1)
            random_numbers = tuple(int(num) for num in random_numbers_str.split(','))
            print(f"Random numbers for Invite {i + 1}:", random_numbers)  # Print extracted random numbers for debugging

            # Append random numbers to the list
            all_random_numbers.append(random_numbers)

            # Print invitation numbers and corresponding random numbers
            print(f"inv{i + 1} | number {random_numbers[0]}")
    else:
        print(f"Error running script {i + 1}:")
        print(result.stderr)

# Print all random numbers in a multi-list format
print("All random numbers:", all_random_numbers)

canvas = Canvas(
    window,
    bg = "#202020",
    height = 705,
    width = 769,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    384.0,
    43.0,
    image=image_image_1
)

canvas.create_rectangle(
    285.0,
    142.0,
    384.0,
    242.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    408.0,
    142.0,
    507.0,
    242.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    285.0,
    508.0,
    384.0,
    608.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    408.0,
    508.0,
    507.0,
    608.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    285.0,
    264.0,
    384.0,
    364.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    408.0,
    264.0,
    507.0,
    364.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    285.0,
    386.0,
    384.0,
    486.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    408.0,
    386.0,
    507.0,
    486.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    162.0,
    264.0,
    261.0,
    364.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    162.0,
    386.0,
    261.0,
    486.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    531.0,
    264.0,
    630.0,
    364.0,
    fill="#202020",
    outline="")

canvas.create_rectangle(
    531.0,
    386.0,
    630.0,
    486.0,
    fill="#202020",
    outline="")

def open_gui2(color, text):
    import gui2
    gui2.display_info(color, text)

button_1 = Button(
    text=all_random_numbers[0][0],
    background='#FFD166',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#FFD166', all_random_numbers[0]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)

)
button_1.place(
    x=285.0,
    y=142.0,
    width=99.0,
    height=100.0
)

#button_image_2 = PhotoImage(
   # file=relative_to_assets("button_2.png"))
button_2 = Button(
    text=all_random_numbers[0][1],
    background='#FFD166',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#FFD166', all_random_numbers[0]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_2.place(
    x=408.0,
    y=142.0,
    width=99.0,
    height=100.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    text=all_random_numbers[0][2],
    background='#FFD166',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#FFD166', all_random_numbers[0]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_3.place(
    x=285.0,
    y=508.0,
    width=99.0,
    height=100.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    text=all_random_numbers[0][3],
    background='#FFD166',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#FFD166', all_random_numbers[0]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_4.place(
    x=408.0,
    y=508.0,
    width=99.0,
    height=100.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    text=all_random_numbers[1][0],
    background='#EF476F',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#EF476F', all_random_numbers[1]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_5.place(
    x=285.0,
    y=386.0,
    width=99.0,
    height=100.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    text=all_random_numbers[1][1],
    background='#EF476F',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#EF476F', all_random_numbers[1]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_6.place(
    x=285.0,
    y=264.0,
    width=99.0,
    height=100.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    text=all_random_numbers[1][2],
    background='#EF476F',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#EF476F', all_random_numbers[1]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_7.place(
    x=408.0,
    y=386.0,
    width=99.0,
    height=100.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    text=all_random_numbers[1][3],
    background='#EF476F',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#EF476F', all_random_numbers[1]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_8.place(
    x=408.0,
    y=264.0,
    width=99.0,
    height=100.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    text=all_random_numbers[2][0],
    background='#06D6A0',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#06D6A0', all_random_numbers[2]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_9.place(
    x=531.0,
    y=386.0,
    width=99.0,
    height=100.0
)


button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    text=all_random_numbers[2][1],
    background='#06D6A0',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#06D6A0', all_random_numbers[2]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_10.place(
    x=531.0,
    y=264.0,
    width=99.0,
    height=100.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    text=all_random_numbers[2][2],
    background='#06D6A0',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#06D6A0', all_random_numbers[2]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_11.place(
    x=162.0,
    y=386.0,
    width=99.0,
    height=100.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    text=all_random_numbers[2][2],
    background='#06D6A0',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_gui2('#06D6A0', all_random_numbers[2]),  # Pass color and text,
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_12.place(
    x=162.0,
    y=264.0,
    width=99.0,
    height=100.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: regenerate_numbers(),
    relief="flat",
    font=("RacingSansOne-Regular",32*-1)
)
button_13.place(
    x=695.0,
    y=94.0,
    width=56.0,
    height=56.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: sys.exit(),
    relief="flat"
)
button_14.place(
    x=736.0,
    y=6.0,
    width=32.0,
    height=30.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: inftab(),
    relief="flat"
)
button_15.place(
    x=630.0,
    y=608.0,
    width=132.0,
    height=86.0
)
window.resizable(False, False)
window.mainloop()