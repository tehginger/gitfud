# gitfud
# a simple recipe viewer
# author: Noah Garringer

# Load Libraries
import curses


# Settings for curses
curses.noecho()
curses.cbreak()
stdscr.keypad(False)

# Load Existing Recipes


# This is what the real main menu will be.  it will just be a list of the currently "owned" recipes
# Launch Main Menu List
# print(recipeList)


# fake main menu.  this is being created simply to get me to other parts of the program...
# I don't want to start with writing the "load existing recipes" function
print("Main Menu")
print("1.  View Recipes")
print("2.  Add Recipe")
print("3.  Edit Recipe")
print("4.  Remove Recipe")
