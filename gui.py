import pygame, graph, easygui, sys

xinterval = 0.05
ymax = 10
xmax = 10
w, h = 500, 500

def startup():
    """
    easygui.msgbox("Welcome to GraphyPy!", title="Graphpy", ok_button = "Ok, Let's Explore!")
    if easygui.buttonbox("Would you like to read the help text?", choices = ["Yes","No"]) == "Yes":
        easygui.msgbox("Type in an equation in the input box and click Graph to graph! Click Settings to change settings.")
    """
    pass

def main():

    global xinterval, yinterval, ymax, xmax, w, h
    initial = easygui.buttonbox("Would you like to graph a function or go into settings?", title = "Graph or Settings", choices = ["Graphing","Settings"])
    cxinterval = xinterval
    cymax = ymax
    cxmax = xmax
    if initial == "Graphing":
        input = easygui.enterbox("Enter your function here: ", title = "GraphPy")
        graph.Graph(w, h, ymax, xmax, xinterval, input)
    elif initial == "Settings":
        settings_input = easygui.choicebox("Settings","Settings",["X Interval", "X Max", "Y Max", "Window Width", "Window Height"])
        if settings_input == "X Interval":
            try:
                xinterval = float(easygui.enterbox("Current value: %s Enter value: " % cxinterval))
            except:
                print()
        elif settings_input == "X Max":
            try:
                xmax = float(easygui.enterbox("Current value: %s Enter value: " % cxmax))
            except:
                print()
        elif settings_input == "Y Max":
            try:
                ymax = float(easygui.enterbox("Current value: %s Enter value: " % cymax))
            except:
                print()
        elif settings_input == "Window Width":
            try:
                w = float(easygui.enterbox("Current value: %s Enter value: " % w))
            except:
                print()
        elif settings_input == "Window Height":
            try:
                h = float(easygui.enterbox("Current value: %s Enter value: " % h))
            except:
                print()
        main()
    else:
        sys.exit()
    run += 1
