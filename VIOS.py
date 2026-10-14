# ==========================================
# VI OS 3.0 - VISHAL INTERFACE
# TI-84 Evo / Built-in Python
# ICE WHITE EDITION
# ==========================================

import ti_draw as d
import ti_system as sys
import time

W = 319
H = 209

# Edit these lines to change the notes shown in the Notes app.
NOTES = [
    "-b plusminus root (b^2 - 4ac) / 2a",
    "y2 - y1",
    "note 3",
    "note 4"
]

# ---------- WHITE THEME ----------

BLACK = (255, 255, 255)
PANEL = (230, 230, 230)
CYAN = (0, 0, 0)
WHITE = (0, 0, 0)
GRAY = (90, 90, 90)
GREEN = (0, 0, 0)


# ---------- GRAPHICS ----------

def color(c):
    d.set_color(c[0], c[1], c[2])


def text(x, y, s, c=WHITE):
    color(c)
    d.draw_text(x, y, str(s))


def rect(x, y, w, h, c):
    color(c)
    d.fill_rect(x, y, w, h)


def line(x1, y1, x2, y2, c=CYAN):
    color(c)
    d.draw_line(x1, y1, x2, y2)


def clear_screen():
    rect(0, 0, W, H, BLACK)


def frame(title):
    clear_screen()
    text(10, 30, "VI OS", CYAN)
    text(90, 30, title, WHITE)
    line(8, 34, 310, 34, GRAY)


# ---------- BOOT ----------

def boot():
    clear_screen()
    text(130, 38, "VI OS", CYAN)
    text(130, 60, "v.0.1", WHITE)
    text(95, 96, "INITIALIZING", GRAY)

    rect(35, 120, 249, 12, PANEL)
    for i in range(1, 101, 5):
        rect(38, 123, 243, 6, PANEL)
        rect(38, 123, int(243 * i / 100), 6, CYAN)
        rect(120, 139, 100, 18, BLACK)
        text(139, 141, str(i) + "%", WHITE)
        time.sleep(0.06)

    clear_screen()
    text(105, 78, "SYSTEM READY", GREEN)
    text(105, 101, "Hey, Vishal", CYAN)
    time.sleep(0.7)


# ---------- KEY HANDLING ----------

def read_key():
    return sys.wait_key()


def is_up(k):
    return k == 3 or k == 25


def is_down(k):
    return k == 4 or k == 34


def is_left(k):
    return k == 2 or k == 24


def is_right(k):
    return k == 1 or k == 26
    

def is_enter(k):
    return k == 105 or k == 5


def is_clear(k):
    return k == 9 or k == 45


# ---------- HOME MENU ----------

def home():
    selected = 0
    options = ["Notes", "System Info", "Exit VI OS"]

    while True:
        frame("HOME")

        for i in range(len(options)):
            y = 78 + i * 29
            if i == selected:
                text(28, y, ">", GREEN)
            text(48, y, options[i], WHITE)

        line(12, 168, 307, 168, GRAY)
        text(14, 187, "UP/DOWN: SELECT", GRAY)
        text(174, 187, "ENTER: OPEN", GRAY)

        k = read_key()
        if is_up(k):
            selected = (selected - 1) % len(options)
        elif is_down(k):
            selected = (selected + 1) % len(options)
        elif is_enter(k) or is_right(k):
            if selected == 0:
                notes_app()
            elif selected == 1:
                system_info()
            else:
                clear_screen()
                text(100, 95, "VI OS CLOSED", CYAN)
                time.sleep(0.5)
                return
        elif is_clear(k) or is_left(k):
            return


# ---------- NOTES APP ----------

def notes_app():
    first_note = 0
    visible_notes = 5

    while True:
        frame("NOTES")

        for row in range(visible_notes):
            index = first_note + row
            if index >= len(NOTES):
                break

            note = str(NOTES[index])
            if len(note) > 48:
                note = note[:45] + "..."

            y = 60 + row * 25
            text(15, y, note, WHITE)

        line(12, 168, 307, 168, GRAY)
        text(15, 187, "UP/DOWN: SCROLL", GRAY)
        text(190, 187, "CLEAR: BACK", GRAY)

        k = read_key()
        if is_up(k):
            if first_note > 0:
                first_note -= 1
        elif is_down(k):
            if first_note + visible_notes < len(NOTES):
                first_note += 1
        elif is_clear(k) or is_left(k) or is_enter(k):
            return


# ---------- SYSTEM INFO ----------

def system_info():
    while True:
        frame("SYSTEM INFO")
        text(15, 60, "VI OS VERSION: 3.0", CYAN)
        text(15, 85, "DEVICE: TI-84 EVO", WHITE)
        text(15, 110, "MODE: PYTHON APP", WHITE)
        text(15, 135, "INTERFACE: GRAPHICS", WHITE)
        text(15, 160, "STATUS: ONLINE", GREEN)

        line(12, 168, 307, 168, GRAY)
        text(15, 190, "CLEAR OR LEFT: BACK", GRAY)

        k = read_key()
        if is_clear(k) or is_left(k) or is_enter(k):
            return


# ---------- START VI OS ----------

boot()
home()
