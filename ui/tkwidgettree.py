# vim:set ts=4 sw=4:

import tkinter as tk
import tkinter.ttk as ttk

class TkWidgetTree(object):
	"""
	This simple class wraps Tk (and ttk) widgets for easy construction from a dict
	tree.

	Usage is preferably done through the from_dict static method rather than 
	initialising the object yourself.

	example:

    --8<--

	root=tk.Tk()
	root.title('TkWidgetTree test')

	config={
		'name': 'Frame',
		'parent': root,
		'pack': { 'fill': tk.BOTH },
		'children': [
			{
				'name':	'Label',
				'options': {
					'text': 'Hello'
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
	tree.mainloop()

    --8<--

	You can add identifiers to wanted widgets and access them with the recursive
	find() method.

	--8<--

	world=tree.find('world-button')
	world.widget.config(background='red')

	--8<--

	"""
	def __init__(self, name, parent=None, id=None, options={}, pack={}, children=[]):
		self.name=name
		self.parent=parent
		self.options=options
		self.pack=pack
		self.children=children

		self.id=id

	@staticmethod
	def from_dict(tree):
		"""
		Recursively interprets a dict into wrapped Tk widgets
		"""
		if not tree:
			return None

		tree['children']=[TkWidgetTree.from_dict(child) for child in tree.get('children') or []]

		return TkWidgetTree(**tree)

	def find(self, id):
		"""
		Recursively find widgets with a given id. Once an id is found it is passed back
		through the stack, no care is taken to handle duplicate id:s.
		"""
		if id == self.id:
			return self

		for child in self.children:
			result=child.find(id)
			if result:
				return result

		return None

	def mainloop(self):
		"""
		Just call the widget's mainloop
		"""
		self.widget.mainloop()

	def render(self):
		"""
		This method recursively renders the object tree into actual Tk widgets and
		positions them using the pack method.

		Currently, only pack is supported.
		"""
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

		if not self.name.__name__ in ('Menu'):
			self.widget.pack(self.pack)
