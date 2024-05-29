# Create your superhero vs villain story
import random
import tkinter as tk
from tkinter import ttk
import logging

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")


def generate_superhero():
    # this is the super hero segment of our game.
    superPowers = [
        "Flying",
        "Super Strength",
        "Telepathy",
        "Super Speed",
        "Unlimited Eating capability",
        "Invisibility",
        "Ice breath",
    ]
    superFirstName = [
        "Wonder",
        "Super",
        "Mad",
        "Incredible",
        "Astonishing",
        "Decent",
        "Stupendous",
        "Organised",
        "That",
        "Notably",
    ]
    superLastName = [
        "Woman",
        "Man",
        "Girl",
        "Boy",
        "Thing",
        "Treat",
        "Dude",
        "Chick",
        "Vikram",
        "Uma",
        "Macho Lady",
        "Stag",
        "Guy",
    ]

    print("lets generate your random super hero name!")
    logging.info("Generating random superhero name.")
    superName = random.choice(superFirstName) + random.choice(superLastName)
    superPower = random.choice(superPowers)
    return f"Your Super Hero Name is {superName} and your power is {superPower}"


# This is super villains segment


def gerenate_super_villain():
    villainPowers = [
        "Flying",
        "Super Strength",
        "Telepathy",
        "Super Speed",
        "Unlimited Eating capability",
        "Invisibility",
        "Ice breath",
    ]
    villan_first_name = [
        "Dark",
        "Blue",
        "Unhappy",
        "Lifeless",
        "White",
        "Unplanned",
        "Rich",
        "Psycotic",
        "Trvial",
        "Nutty",
    ]
    villan_last_name = [
        "Fly",
        "Engineer",
        "Pilot",
        "Bitch",
        "Freak",
        "Student",
        "Manager",
        "Builder",
        "Politician",
        "Cricketer",
    ]

    villainName = random.choice(villan_first_name) + random.choice(villan_last_name)
    villainpower = random.choice(villainPowers)
    logging.info("Generating random villain name.")
    return f"Your arch nemesis is {villainName} and their power is {villainpower}"


def click_to_generate():
    superhero_info = generate_superhero()
    villain_info = gerenate_super_villain()
    logging.info("Button clicked to generate superhero and supervillain.")
    output_text.set(superhero_info + "\n\n" + villain_info)


# main application
app = tk.Tk()
app.title("Superhero vs SuperVillain")


# create widgets

output_text = tk.StringVar()
output_label = tk.Label(
    app,
    textvariable=output_text,
    font=("Helvetica", 14),
    wraplength=600,
    justify="center",  # Center align the text
)
button = ttk.Button(  # Use ttk.Button for better styling
    app, text="Generate Super Hero & Villain Info!", command=click_to_generate
)

# Place widgets in the window

output_label.grid(row=0, column=0, padx=20, pady=(60, 20))
button.grid(row=5, column=0, pady=20)

# start the gui
logging.info("Starting the Superhero vs SuperVillain application.")
app.mainloop()
