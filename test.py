#!/usr/bin/env python3
# vim:set ts=4 sw=4:

import tkinter as tk

from ui.fileparser import FileParser
from ui.tkwidgettree import TkWidgetTree

root=tk.Tk()
root.title('TkWidgetTree test')

tree=TkWidgetTree.from_dict(FileParser().parse("test.json"))
tree.render()

hello=tree.find('hello-button')
hello.widget.config(command=quit)

world=tree.find('world-button')
world.widget.config(background='red', command=quit)

tree.mainloop()
