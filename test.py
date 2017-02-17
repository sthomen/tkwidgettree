#!/usr/bin/env python3
# vim:set ts=4 sw=4:

import tkinter as tk

from ui.tkwidgettree import TkWidgetTree

root=tk.Tk()
root.title('TkWidgetTree test')

config={
	'name': 'Frame',
	'parent': root,
	'pack': { 'fill': tk.BOTH },
	'children': [
		{
			'name':	'Button',
			'options': {
				'text': 'Hello',
				'command': quit
			},
			'pack': { 'side': tk.LEFT }
		},
		{
			'id': 'world-button',
			'name':	'Button',
			'options': {
				'text': 'World',
				'command': quit
			},
			'pack': { 'side': tk.LEFT }
		}
	]
}

tree=TkWidgetTree.from_dict(config)
tree.render()

world=tree.find('world-button')
world.widget.config(background='red')

tree.mainloop()
