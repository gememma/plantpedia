from dataclasses import dataclass
from typing import List
import pandas as pd

import colorama
import constants

@dataclass
class Plant:
    common_name: str
    latin_name: str
    date: str
    notes: str

def get_plants() -> List[Plant]:
    df = pd.read_csv('data/data.csv', header=None)
    (rows, columns) = df.shape
    if columns != len(constants.edit_menu):
        raise IndexError("Error while reading data/data.csv, unexpected number of columns")
    plants = []
    for entry in df.itertuples():
        plants.append(Plant(
            common_name=entry[1],
            latin_name=entry[2],
            date=entry[3],
            notes=entry[4],
            )
        )
    # TODO: return dataframe instead of custom dataclass
    return plants

def edit_csv(row: int, field: int, new: str):
    df = pd.read_csv('data/data.csv', header=None)
    df.loc[row, field] = new
    df.to_csv('data/data.csv', header=False, index=False)

def push_to_csv(new_row: pd.DataFrame):
    df = pd.read_csv('data/data.csv', header=None)
    df = pd.concat([df, new_row.transpose()])
    df.to_csv('data/data.csv', header=False, index=False)
    pass

def serve_menu(options: List[str], prompt: str) -> int:
    print(colorama.Fore.YELLOW + prompt)
    print(colorama.Fore.GREEN)
    i=0
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
    while True:
        selection = serve_menu([f"{x.common_name} ({x.latin_name})" for x in plants], "SELECT PLANT\n------------")
        if selection < len(plants):
            print_entry(plants[selection])
        elif selection == len(plants):
            break
        else:
            print("Invalid selection :(")

def serve_edit():
    plants = get_plants()
    selection = serve_menu([f"{x.common_name} ({x.latin_name})" for x in plants], "SELECT PLANT\n------------")
    if selection < len(plants):
        print_entry(plants[selection])
        field = serve_menu(constants.edit_menu, "\nWhat do you want to change?")
        new_value = input("Enter a new value: ")
        edit_csv(selection, field, new_value)
        print("Value changed\n")
    elif selection == len(plants):
        return
    else:
        print("Invalid selection :(")
        return

def serve_add():
    new_entry = []
    for field in constants.edit_menu:
        new_value = input("Enter a value for " + field + ": ")
        new_entry.append(new_value)
    df = pd.DataFrame(data=new_entry)
    push_to_csv(df)

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
    print("\n")

def main():
    colorama.init()
    print(colorama.Fore.GREEN)
    while True:
        serve_main_menu()
        

main()