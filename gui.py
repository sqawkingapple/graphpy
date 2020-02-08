import pygame, graph, easygui

def startup():
    easygui.msgbox("Welcome to GraphyPy!", title="Graphpy", ok_button = "Ok, Let's Explore!")
    if easygui.buttonbox("Would you like to read the help text?", choices = ["Yes","No"]) == "Yes":
        easygui.msgbox("Type in an equation in the input box and click Graph to graph! Click Settings to change settings.")

def main():
    if easygui.buttonbox("Would you like to graph a function or go into settings?", title = "Graph or Settings", choices = ["Graphing","Settings"]) == "Graphing":
        input = easygui.enterbox("Enter your function here: ", title = "GraphPy", ok_button = "Graph")
    elif easygui.buttonbox("Would you like to graph a function or go into settings?", title = "Graph or Settings", choices = ["Graphing","Settings"]) == "Settings":
        settings_input = easygui.choicebox("Settings","Settings",["X Interval", "Y Interval", "X Max", "Y Max"])
