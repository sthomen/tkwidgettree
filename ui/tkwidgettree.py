# vim:set ts=4 sw=4:

import tkinter as tk
import tkinter.ttk as ttk

class TkWidgetTree(object):
	def __init__(self, name, parent=None, id=None, options={}, pack={}, children=[]):
		self.name=name
		self.parent=parent
		self.options=options
		self.pack=pack
		self.children=children

		self.id=id

	@staticmethod
	def from_dict(tree):
		if not tree:
			return None

		tree['children']=[TkWidgetTree.from_dict(child) for child in tree.get('children') or []]

		return TkWidgetTree(**tree)

	def find(self, id):
		if id == self.id:
			return self

		for child in self.children:
			result=child.find(id)
			if result:
				return result

		return None

	def mainloop(self):
		self.widget.mainloop()

	def render(self):
		if type(self.name) == str:
			for module in (tk, ttk):
				try:
					self.name=getattr(module, self.name)
					break
				except AttributeError as e:
					pass

		self.widget=self.name(self.parent, **self.options)

		if self.children:
			for child in self.children:
				child.parent=self.widget
				child.render()

		self.widget.pack(self.pack)
