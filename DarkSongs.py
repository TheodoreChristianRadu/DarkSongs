import customtkinter
import Music
import Input
import json

with open("Configuration.json") as file:
    configuration = json.load(file)

window = customtkinter.CTk()

left = customtkinter.CTkFrame(master=window)
left.pack(side=customtkinter.LEFT)

actions = list(Input.actions["Actions"].keys())
def select(interval):
    def select(action):
        configuration["Mappings"][interval] = action
    return select
for index, interval in enumerate(Music.intervals):
    customtkinter.CTkLabel(master=left, text=interval).grid(row=index, column=1)
    customtkinter.CTkOptionMenu(master=left, values=actions, command=select(interval)).grid(row=index, column=2)

right = customtkinter.CTkFrame(master=window)
right.pack(side=customtkinter.LEFT)

def process(note, ratio, interval):
    print(note, ratio, interval)
    if interval in configuration["Mappings"]:
        print("Performing {}".format(configuration["Mappings"][interval]))
        Input.perform(configuration["Mappings"][interval])
start = lambda: Music.Player(process)
customtkinter.CTkButton(master=right, text="Start", command=start).pack()
stop = lambda: Music.Player.stop()
customtkinter.CTkButton(master=right, text="Stop", command=stop).pack()

window.mainloop()
