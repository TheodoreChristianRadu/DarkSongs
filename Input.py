import vgamepad
import json

gamepad = vgamepad.VX360Gamepad()

digital = {
    "A": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A,
    "B": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B,
    "X": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X,
    "Y": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    "LB": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    "RB": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    "LSB": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    "RSB": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
    "DPU": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    "DPD": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    "DPL": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    "DPR": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    "BACK": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    "START": vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START
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
    instructions = actions["Actions"][action]
    for instruction in instructions:
        emulate(*instruction.split())
        gamepad.update()

def emulate(type, button, direction=None):
    if (button in digital):
        if (type == "Press"): gamepad.press_button(digital[button])
        if (type == "Release"): gamepad.release_button(digital[button])
    if (button in analog):
        if button.endswith("S"):
            if (type == "Press"): analog[button](*actions["Directions"][direction])
            if (type == "Release"): analog[button](0.0, 0.0)
        else:
            if (type == "Press"): analog[button](1.0)
            if (type == "Release"): analog[button](0.0)

while True:
    perform("Light Attack")
    perform("Switch Spells")
    perform("Walk Left")
    perform("Lock")
