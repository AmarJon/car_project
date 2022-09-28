from tkinter import *
from tkinter import ttk

from Car import Car
from CarListBox import CarListBox
from CSVExporter import CSVExporter

root = Tk()
blank_space = " "  # empty string used for title
root.geometry("700x450")  # setting the size of the window
root.resizable(False, False)  # making the window non-resizeable
root.title(80 * blank_space + "Car Project")  # adding a window title and centering it
root.configure(bg="#97bbd1")  # sets the background color of the root
root.iconbitmap("car_22307.ico")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Everything goes in here
makes = dict({"Ford": ["Mustang", "F-150", "Escape", "Bronco", "Edge", "Explorer", "Expedition", "Ranger"],
              "Chevrolet": ["Corvette", "Camaro", "Spark", "Malibu", "Trax", "Trailblazer", "Equinox", "Blazer", "Traverse", "Tahoe", "Suburban", "Colorado", "Silverado", "Bolt"],
              "Honda": ["Accord", "Civic", "Ridgeline", "Crossovers", "CR-V", "Pilot", "Passport", "Insight", "Odyssey", ],
              "Hyundai": ["Sonata", "Elantra", "Venue", "Kona", "Tucson", "Santa Cruz", "Santa Fe", "Palisade", "Ioniq 5", "Nexo Fuel Cell", "Accent", "Elantran", "Veloster"],
              "Toyota": ["Camry", "Corolla", "Prius", "Tacoma", "Tundra", "Avalon", "Mirai", "GR86", "GR Supra", "Sienna", "Highlander", "bZ4X", "Venza", "C-HR", "RAV4", "4Runner", "Corolla Cross", "Sequoia"],
              "Mercedes": ["GLA", "GLB", "GLC", "GLE", "GLS", "Maybach GLS", "G-Class", "A-Class", "C-Class", "E-Class", "EQS", "S-Class", "Maybach S-Class", "E-Class Wagon", "CLA", "CLS", "AMG GT", "SL Roadster"],
              "Nissan": ["Kicks", "Rogue", "Murano", "Pathfinder", "Armada", "ARIYA", "Versa", "Sentra", "Altima", "Maxima", "LEAF", "370z", "GT-R", "Frontier", "TITAN"],
              "Audi": ["R8", "TT", "A8", "A7", "A6", "A5", "A4", "A3", "e-tron", "Q3", "Q4", "Q4 e-tron", "Q5", "Q7", "Q8", "e-tron GT"],
              "Dodge": ["Charger", "Challenger", "Durango", "RAM 1500", "RAM 2500", "RAM 3500"],
              "Volkswagen": ["ID.4", "Atlas", "Tiguan", "taos", "Jetta", "Arteon", "Golf"],
              "Acura": ["ILX", "Integra", "tlx", "RDX", "MDX", "NSX TYPE S"],
              "Jeep": ["Grand Wagoner", "Wagoneer", "Grand Cherokee", "Wrangler", "Compass", "Gladiator", "Cherokee", "Wrangler", "Renegade"],
              "Chrysler": ["Pacifica", "300"],
              "Tesla": ["Model 3", "Model S", "Model X", "Model Y"],
              "Kia": ["Soul", "Seltos", "Niro", "Sportage", "Sorento", "Carnival MPV", "Telluride", "EV6", "Rio", "Forte", "K5", "Stinger"],
              "GMC": ["Canyon", "Sierra 1500", "Hummer EV", "Terrian", "Acadia", "Yukon"],
              "Mazda": ["3", "CX-50", "CX-30", "CX-5", "CX-9", "MX-5 Miata"],
              "Mitsubishi": ["Outlander", "Eclipse Cross", "Mirage"],
              "Subaru": ["Crosstrek", "Forester", "Outback", "Ascent", "Impreza", "Legacy", "BRZ", "WRX"],
              "Lexus": ["UX", "NX", "RX", "GX", "LX", "IS", "ES", "LS", "RC", "LC"],
              "Alfa Romeo": ["Stelvio", "Giulia", "Tonale"],
              "Fiat": ["500x"]})

# Color of car
car_colors = [
    "Red",
    "Blue",
    ""
]

car_list = []

# ----------------------FUNCTIONS---------------------------------------------------------------------------------
def did_select_make(e):
    make = firstCombo.get()
    secondCombo.config(values=sorted(makes[make]))
    if firstCombo.get() and secondCombo.get():
        thirdCombo.config(values=sorted(car_colors))

def did_select_model(e):
    if firstCombo.get() and secondCombo.get():
        thirdCombo.config(values=sorted(car_colors))

# Function to clear selection
def clear():
    firstCombo.set('Brand') or secondCombo.set('') or thirdCombo.set('')
    secondCombo.config(values=[" "])
    thirdCombo.config(values=[" "])

def save():
    car_list.append(Car(firstCombo.get(), secondCombo.get(), thirdCombo.get()))
    print(car_list)

def validate():
    return True

def did_tap_save():
    if validate():
        save()
        clear()
        listbox.update_listbox(car_list)
    else: # pop up warning
        return

def did_tap_remove():
    listbox.delete_car()

def did_tap_export():
    # build an array of exportable strings
    exportable_list = []
    for car in car_list:
        exportable_list.append(car.export_prepared_string())
    # Call CSV Exporter list
    CSVExporter().export_list(exportable_list)
    pass


# Creating top frame of the GUI
top_frame = Frame(root, background="#97bbd1", highlightthickness=2, highlightbackground="black", width=600, height=100)
top_frame.grid_propagate(False)
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=1)
top_frame.grid_columnconfigure(3, weight=1)
top_frame.grid_columnconfigure(4, weight=1)
top_frame.grid_rowconfigure(0, weight=1)
top_frame.grid(row=0, column=0)

# Creating ComboBox
firstCombo = ttk.Combobox(top_frame, values=sorted(list(makes.keys())), width=10)
firstCombo.set("Brand")
firstCombo.bind("<<ComboboxSelected>>", did_select_make)
firstCombo.grid(row=0, column=0)

secondCombo = ttk.Combobox(top_frame, values=[" "], width=10)
secondCombo.bind("<<ComboboxSelected>>", did_select_model)
secondCombo.grid(row=0, column=1)

thirdCombo = ttk.Combobox(top_frame, values=[" "], width=10)
thirdCombo.grid(row=0, column=2)

# Buttons
saveBtn = Button(top_frame, text="Save", foreground="black", width=8, command=did_tap_save)
saveBtn.grid(row=0, column=3)

clearBtn = Button(top_frame, text="Clear", foreground="black", width=8, command=clear)
clearBtn.grid(row=0, column=4)

# Creating bottom frame of the GUI
bottom_frame = Frame(root, background="#97bbd1", highlightthickness=2, highlightbackground="black", width=600, height=300)
bottom_frame.pack_propagate(False)
bottom_frame.grid(row=1, column=0)

listbox = CarListBox(bottom_frame, car_list)

deleteBtn = Button(bottom_frame, text="remove", command=did_tap_remove)
deleteBtn.pack(anchor='s')

exportBtn = Button(bottom_frame, text="export", command=did_tap_export)
exportBtn.pack(anchor='s')

root.mainloop()


