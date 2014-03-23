"""<tt040.py

(1)
In the previous program, we created a button object, button1, and then set its
text and backround color in a fairly straightforward way.

		self.button1["text"]= "Hello, World!"
		self.button1["background"] = "green"
	


In this program, we add three more button to Container1, using slightly 
different methods.

(2) 
For button2, the process is essentially the same as for button1, but instead of 
accessing the button's dictionary, we use the button's built-in "configure" 
method.

(3) 
For button3, we see that the configure method can take multiple keyword
arguments, so we can set multiple options in a single statement.

(4)
In the previous examples, setting up the button has been a two-step process:
first we create the button, then we set its properties.  But it is possible to
specify the button's properties at the time that we create it.  The "Button" 
widget (like all widgets) expects its first argument to be its parent.  This is
a positional argument, not a keyword argument.  But after that, you can, if you wish,
add one or more keyword arguments that specify properties of the widget.


PROGRAM BEHAVIOR

When you run this program, you should see that Container1 now contains, in 
addition to the original green button, three more buttons.

Note how myContainer1 has stretched to accommodate these other buttons.

Note also that the buttons are stacked on top of each other.  In the next 
program, we will see why they arrange themselves this way, and see how to 
arrange them differently.

>"""
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1["text"] = "Hello, World!"   ### (1)
		self.button1["background"] = "green"     ### (1) 
		self.button1.pack()	

		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Off to join the circus!") ### (2)
		self.button2.configure(background="tan")               ### (2)
		self.button2.pack()	
		

		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Join me?", background="cyan")  ### (3)
		self.button3.pack()	
			
		self.button4 = Button(self.myContainer1, text="Goodbye!", background="red") ### (4)
		self.button4.pack()	
	
		
root = Tk()
myapp = MyApp(root)
root.mainloop()