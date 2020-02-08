import pygame, graph, easygui

def main():
    easygui.msgbox("Welcome to GraphyPy!", title="Graphpy", ok_button = "Ok, Let's Explore!")
    if easygui.buttonbox("Would you like to read the help text?", choices = ["Yes","No"]) == "Yes":
        pass
    input = easygui.enterbox("", title = "Input")
