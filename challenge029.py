#Challenge 029 - The Secrets of print
def printInColor(color, text):
    if color == "green":
        print("\033[32m", text, sep="", end="")
    elif color == "blue":
        print("\033[34m", text, sep="", end="")
    elif color == "yellow":
        print("\033[1;33m", text, sep="", end="")
    elif color == "red":
        print("\033[31m", text, sep="", end="")
    else:
        print("\033[0m", text, sep="", end="")

print("This is a ", end="")
printInColor("green", "program")
printInColor("reset", " which prints in different ")
printInColor("blue", "colors")
printInColor("reset", " just like ")
printInColor("yellow", "this")
printInColor("reset", "! ")
printInColor("red", "Bye")
printInColor("reset", "!")