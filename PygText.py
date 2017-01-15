import tkinter as tk
from tkinter import ttk

import pyfiglet

class Window (tk.Tk):
    def __init__ (self, *args, **kwargs):
        tk.Tk.__init__ (self, *args, **kwargs)
        self.title ("PygText")
        self.rowconfigure (1, weight = 1)
        self.columnconfigure (1, weight = 1)

        self.textVariable = tk.StringVar ()
        self.textVariable.set ("PygText")
        self.fontVariable = tk.StringVar ()
        self.fontVariable.set ("standard")

        self.figlet = pyfiglet.Figlet (font = self.fontVariable.get ())

        ttk.Label (self, text = "Enter Text:").grid (row = 0, column = 0, sticky = "w")
        self.textBox = ttk.Entry (self, textvariable = self.textVariable)
        self.textBox.grid (row = 0, column = 1, sticky = "ew")
        self.textBox.bind ("<KeyRelease>", self.update_text)

        self.bigText = tk.Text (self, wrap = "none", state = "disabled")
        self.bigText.grid (row = 1, column = 0, columnspan = 2, sticky = "nesw")

        self.horizontalScrollbar = ttk.Scrollbar (self, orient = "horizontal", command = self.bigText.xview)
        self.horizontalScrollbar.grid (row = 2, column = 0, columnspan = 2, sticky = "we")

        self.verticalScrollbar = ttk.Scrollbar (self, orient = "vertical", command = self.bigText.yview)
        self.verticalScrollbar.grid (row = 1, column = 2, sticky = "ns")

        self.bigText.configure (xscrollcommand = self.horizontalScrollbar.set, yscrollcommand = self.verticalScrollbar.set)

        #self.bigText.insert ("end", self.figlet.renderText ("Hello"))

        ttk.Label (self, text = "Font:").grid (row = 3, column = 0, sticky = "w")
        self.fontBox = ttk.Combobox (self, values = pyfiglet.FigletFont.getFonts (), textvariable = self.fontVariable, state = "readonly")
        self.fontBox.grid (row = 3, column = 1, sticky = "ew")
        self.fontBox.bind ("<<ComboboxSelected>>", self.update_text)

        self.update_text ()

    def update_text (self, *args):
        self.bigText.configure (state = "normal")
        self.figlet = pyfiglet.Figlet (font = self.fontVariable.get ())
        self.bigText.delete (1.0, "end")
        self.bigText.insert (1.0, self.figlet.renderText (self.textVariable.get ()))
        #print (self.textVariable.get (), self.fontVariable.get ())
        self.bigText.configure (state = "disabled")

def Main ():
    app = Window ()
    app.mainloop ()

if __name__ == "__main__":
    Main ()
