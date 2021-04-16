import ctypes
import time
from utils import input_processor

keyboard_scan_codes = {
	'W': 0x11,
	'A': 0x1E,
	'S': 0x1F,
	'D': 0x20,
	'UP': 0xC8,
	'LEFT': 0xCB,
	'RIGHT': 0xCD,
	'DOWN': 0xD0,
	'ENTER': 0x1C,
	'ESC': 0x01,
	'TWO': 0x03,
	'RIGHT_SHIFT': 0x36,
	'/': 0x35,
	'K': 0x25, #fire
	'L': 0x26, #bomb
	';': 0x27, #polarity
	'Z': 0x2C
}


SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
	_fields_ = [("wVk", ctypes.c_ushort),
              ("wScan", ctypes.c_ushort),
              ("dwFlags", ctypes.c_ulong),
              ("time", ctypes.c_ulong),
              ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
	_fields_ = [("uMsg", ctypes.c_ulong),
              ("wParamL", ctypes.c_short),
              ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
	_fields_ = [("dx", ctypes.c_long),
              ("dy", ctypes.c_long),
              ("mouseData", ctypes.c_ulong),
              ("dwFlags", ctypes.c_ulong),
              ("time", ctypes.c_ulong),
              ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
	_fields_ = [("ki", KeyBdInput),
              ("mi", MouseInput),
              ("hi", HardwareInput)]


class Input(ctypes.Structure):
	_fields_ = [("type", ctypes.c_ulong),
              ("ii", Input_I)]


# Actuals Functions
def press_key(hexKeyCode):
	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
	x = Input(ctypes.c_ulong(1), ii_)
	ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def release_key(hexKeyCode):
	extra = ctypes.c_ulong(0)
	ii_ = Input_I()
	ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0,
              		ctypes.pointer(extra))
	x = Input(ctypes.c_ulong(1), ii_)
	ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def start_simulator():
  while True:
    keys = input_processor.active_keys.copy()
    if len(keys) > 0:
      print(keys)
    for key in keys:
      press_key(keyboard_scan_codes[key])
    time.sleep(0.01)
    for key in keys:
      release_key(keyboard_scan_codes[key])