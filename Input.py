from vgamepad import *
import threading
import time
import json

gamepad = VX360Gamepad()

digital = {
    "A": XUSB_BUTTON.XUSB_GAMEPAD_A,
    "B": XUSB_BUTTON.XUSB_GAMEPAD_B,
    "X": XUSB_BUTTON.XUSB_GAMEPAD_X,
    "Y": XUSB_BUTTON.XUSB_GAMEPAD_Y,
    "LB": XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    "RB": XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    "LSB": XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    "RSB": XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
    "DPU": XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    "DPD": XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    "DPL": XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    "DPR": XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    "BACK": XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    "START": XUSB_BUTTON.XUSB_GAMEPAD_START
}

analog = {
    "LT": gamepad.left_trigger_float,
    "RT": gamepad.right_trigger_float,
    "LS": gamepad.left_joystick_float,
    "RS": gamepad.right_joystick_float
}

with open("Actions.json") as file:
    actions = json.load(file)

def perform(action):
    def perform():
        instructions = actions["Actions"][action]
        for instruction in instructions:
            execute(*instruction.split())
    threading.Thread(target=perform).start()

def execute(command, target, direction=None):
    if command == "Wait":
        time.sleep(float(target))
        return
    if target in digital:
        if command == "Press": gamepad.press_button(digital[target])
        if command == "Release": gamepad.release_button(digital[target])
    if target in analog:
        if target.endswith("S"):
            if command == "Press": analog[target](*actions["Directions"][direction])
            if command == "Release": analog[target](0.0, 0.0)
        else:
            if command == "Press": analog[target](1.0)
            if command == "Release": analog[target](0.0)
    gamepad.update()
