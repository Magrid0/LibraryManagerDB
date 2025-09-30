from pyfiglet import Figlet

def figPrint(text):
    f = Figlet(font='slant')
    print(f.renderText(text))

def clearScreen():
    print("\033c")

