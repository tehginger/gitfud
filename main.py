# gitfud
# a simple recipe viewer
# author: Noah Garringer

# Load Libraries
import curses

stdscr = curses.initscr()

# Properly initialize screen
curses.noecho()
curses.cbreak()
curses.curs_set(0)

# Check for and begin color support
if curses.has_colors():
    curses.start_color()

# enable multibyte keysignal support
stdscr.keypad(1)

# Set curses colors
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)


# Create UI
def mainMenu():
    stdscr.addstr(0, 0, "gitfud", curses.A_REVERSE)
    stdscr.addstr(curses.LINES-1, 0, "Press q to quit")

    stdscr.refresh()

    return 0


def main():

    curses.endwin()

    return 0


main()
