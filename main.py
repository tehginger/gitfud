# gitfud
# a simple recipe viewer
# author: Noah Garringer

# Load Libraries
import curses

stdscr = curses.initscr()

# Initialize screen
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
    # Add Top Bar (name of program, eventually will add a version number)
    stdscr.addstr(0, 0, "gitfud", curses.A_REVERSE)
    stdscr.chgat(-1, curses.A_REVERSE)

    # Add Bottom Line (instructions to user go here)
    stdscr.addstr(curses.LINES-1, 0, "Press Q to quit")

    # Chanage the Q to red
    stdscr.chgat(curses.LINES-1, 6, 1, curses.A_BOLD | curses.color_pair(1))

    # Create List Window
    list_window = curses.newwin(curses.LINES-2, curses.COLS, 1, 0)

    # Create sub-window for list of recipes (seperates from the border)
    list_text_window = list_window.subwin(curses.LINES-6, curses.COLS-4, 3, 2)

    # Load recipes

    # List recipes
    list_text_window.addstr("Stuff will go here later")

    # Draw list border
    list_window.box()

    # refresh internal window structures
    stdscr.noutrefresh()
    list_window.noutrefresh()

    # redraw screen
    curses.doupdate()

    # Main Event Loop
    while True:
        # Wait for user input
        c = list_window.getch()

        # Evaluates the input

        # Selection Up
        # if c == curses.KEY_UP:
            #
        # Selection Down
        # elif c == curses.KEY_DOWN:
            #
        # Close the Program
        if c == ord('q') or c == ord('Q'):
            break
        
        # Refresh the Screen from the bottom up
        stdscr.noutrefresh()
        list_window.noutrefresh()
        list_text_window.noutrefresh()
        curses.doupdate()

    return 0


def main():

    # Initialize screen
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

    # Start the Main Menu
    mainMenu()

    # Restore terminal settings
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.curs_set(1)

    # restore normal terminal functionality
    curses.endwin()

    return 0


main()
