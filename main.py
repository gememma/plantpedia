from dataclasses import dataclass
from typing import List
import csv

import colorama
import constants

@dataclass
class Plant:
    common_name: str
    latin_name: str
    date: str
    notes: str
    link: str

def get_plants() -> List[Plant]:
    with open("data/data.csv", "r") as read_obj:
        csv_reader = csv.reader(read_obj)
        rows = list(csv_reader)
    plants = []
    for entry in rows:
        filename = entry[0].replace(" ", "").lower()
        plants.append(Plant(
            common_name=entry[0],
            latin_name=entry[1],
            date=entry[2],
            notes=entry[3],
            link=entry[4],
            )
        )
    return plants

def serve_menu(options: List[str], prompt: str) -> int:
    print(colorama.Fore.YELLOW + prompt)
    print(colorama.Fore.GREEN)
    for i,option in enumerate(options):
        print(f"[{i}] {option}")
    print(f"[{i+1}] Exit\n")
    choice = input(colorama.Fore.WHITE + "Menu selection: ")
    print(colorama.Fore.GREEN)
    return int(choice)

def serve_main_menu():
    selection = serve_menu(constants.main_menu, "MAIN MENU\n---------")
    if selection == 0:
        serve_view()
    elif selection == 1:
        serve_edit()
    elif selection == 2:
        serve_add()
    elif selection == 3:
        serve_remove()
    elif selection == 4:
        print("Bye!")
        exit(0)
    else:
        print("Invalid selection :(")
        return

def serve_view():
    plants = get_plants()
    selection = serve_menu([f"{x.common_name} ({x.latin_name})" for x in plants], "SELECT PLANT\n------------")
    if selection < len(plants):
        print_entry(plants[selection])
    elif selection == len(plants):
        return
    else:
        print("Invalid selection :(")
        return

def serve_edit():
    pass

def serve_add():
    pass

def serve_remove():
    pass

def print_entry(plant: Plant):
    print(f"{plant.common_name} ({plant.latin_name})")
    print(f"Date of purchase: {plant.date}")
    print("\nNotes:")
    note_list = plant.notes.split(".")
    note_list.pop()
    for note in note_list:
        print(f"> {note.strip()}")
    while True:
        selection = serve_menu(constants.entry_menu, "\nWhat now?")
        if selection == 0:
            print(plant.link, "\n")
            break
        elif selection == 1:
            return
        else:
            print("Invalid selection :(")

def main():
    colorama.init()
    print(colorama.Fore.GREEN)
    while True:
        serve_main_menu()
        

main()