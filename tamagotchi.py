import curses
import time

__author__ = "Estêvão Fonseca"
class Tamagotchi:
    def __init__(self):
        self.life = 100
        self.evolved = False


tamagotchi = Tamagotchi()
fed = time.time()
born = time.time()

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    height, width = stdscr.getmaxyx()
    win = curses.newwin(6, 30, height//2 - 1, width // 2 - 7)
    win.bkgd(' ', curses.color_pair(1))
    menu = curses.newwin(6, 30, height//2 - 10,  width // 2 - 7)
    menu.bkgd(' ', curses.color_pair(2))

    while True:
        stdscr.keypad(True)
        stdscr.nodelay(True)
        c = stdscr.getch()
        if c == ord('1'):
            feed_animation(win)
            win.addstr(1, 8, "    ")
        if c == ord('2'):
            die(win)
            time.sleep(30)
            win.addstr(1, 8, "    ")
        if tamagotchi.life > 0:
            if not tamagotchi.evolved:
                idle(win)
            else:
                evolve(win)
        menu.addstr(5, 0, "1. Alimentar")
        menu.addstr(4, 0, f"Vida: {tamagotchi.life}%")
        menu.refresh()
        menu.addstr(4, 0, f" " * len(f"Vida: {tamagotchi.life}%" + " "))
        time.sleep(0.5)
        global fed
        if time.time() - fed > 20:
            tamagotchi.life -= 10
        if tamagotchi.life <= 0:
            tamagotchi.life = 0
            menu.addstr(4, 0, f"Vida: {tamagotchi.life}%")
            win.refresh()
            time.sleep(0.5)
            die(win)
        if time.time() - born > 120:
            tamagotchi.evolved = True
def idle(win):
    win.refresh()
    win.addstr(2, 1, "(=^ .^=) ")
    win.refresh()
    time.sleep(0.5)
    win.addstr(2, 1, "(= '.'=)")
    win.refresh()
    time.sleep(0.5)

def die(win):
    win.addstr(4, 0, "            ")
    win.addstr(2, 1, "(=X-X=) ")
    win.refresh()
    time.sleep(0.5)
    win.addstr(2, 1, "(=X.X=) ")
    win.refresh()
    time.sleep(0.5)
    win.addstr(0, 8, "  | ")
    win.addstr(1,8, "-----")
    win.addstr(2,8, "  | ")
    win.refresh()
    time.sleep(0.5)


def evolve(win):
    win.addstr(1, 1, " /\ /\\")
    win.refresh()
    time.sleep(0.5)
    win.addstr(2, 1, "(=^ .^=) ")
    win.refresh()
    time.sleep(0.5)
    win.addstr(2, 1, "(= '.'=)")
    win.refresh()
    time.sleep(0.5)
    win.addstr(3, 1, "( u   u )")
    win.refresh()
    time.sleep(0.5)


def feed_animation(win):
    global fed
    fed = time.time()
    tamagotchi.life += 30
    if tamagotchi.life > 100:
        tamagotchi.life = 100
    win.addstr(2, 1, "(=^-^=) ")
    win.refresh()
    time.sleep(0.5)
    win.addstr(2, 1, "(=^o^=) ")
    win.refresh()
    time.sleep(0.5)
    win.addstr(1,8, "(  )")
    win.addstr(2,8, " V ")
    win.refresh()
    time.sleep(0.5)

curses.wrapper(main)