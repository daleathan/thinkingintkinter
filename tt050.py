"""<tt050.py

In the last program, we saw two buttons, stacked on top of each other. Probably, 
however, we'd like to see them side-by-side. In this program, we do that, and we 
start to see what we can do with pack().

(1) (2) (3) (4)

Packing is a way of controlling the VISUAL relationship of components.  So what 
we are going to do now is to use the pack "side" option to put the buttons 
side-by-side rather than stacked on top of each other. We do it with the "side" 
argument to the pack() statement, for example:

		self.button1.pack(side=LEFT)	

Note that LEFT (like RIGHT, TOP, and BOTTOM) are user-friendly constants defined 
in Tkinter.  That is, "LEFT" is actually "Tkinter.LEFT" -- but because of the 
way that we imported Tkinter, we don't need to supply the "Tkinter." prefix.

WHY THE BUTTONS WERE STACKED VERTICALLY IN THE LAST PROGRAM

As you remember, in the last program, we just packed the buttons without specifying
any "side" option, and the buttons packed on top of each other.  That is because the
default "side" option is "side=TOP".  

So when we packed button1, it was packed at the top of the cavity inside of 
myContainer1.  That left the cavity for myContainer1 positioned below button1.  
Then we packed button2.  It was packed at the the top of the cavity, which means 
that it was positioned immediately below button1. And the cavity is now positioned
below button2.

If we had packed the buttons in a different order -- for example, if we had 
packed button2 first, and then packed button1 -- their positions would have been 
reversed, and button2 would have been on top.

So, as you can see, one of the ways that you can control the appearance of your
GUI is by controlling the order in which you pack widgets inside containers.


SOME TECHNICAL TERMINOLOGY -- "ORIENTATION"

"Vertical"  orientation includes the TOP and BOTTOM sides.  
"Horizonal" orientation includes the LEFT and RIGHT sides. 

When you are packing widgets and containers, it is possible to mix the two 
orientations.  For example, we could have packed one button with a vertical 
orientation (say, TOP) and the other button with a horizontal orientation (say, 
LEFT).

But mixing orientations inside a container this way is not a good idea.  If you 
use mixed orientations, then predicting what the final result will look like is 
difficult, and you will likely be surprised by the way the GUI looks if the 
window is re-sized.  

So it is a good design practice never to mix orientations with the same 
container. The way to handle complicated GUIs, where you really do want to use 
multiple orientations, is to nest containers within containers.  We'll explore 
that topic in a later program.


PROGRAM BEHAVIOR

When you run this program, you will now see the two buttons, side by side.

[revised: 2002-10-01]
>"""
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1["text"]= "Hello, World!"
		self.button1["background"] = "green"
		self.button1.pack(side=LEFT)	### (1)


		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Off to join the circus!")  
		self.button2.configure(background="tan")               
		self.button2.pack(side=LEFT)	 ### (2)
		

		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Join me?", background="cyan")  
		self.button3.pack(side=LEFT)	  ### (3)
			
		self.button4 = Button(self.myContainer1, text="Goodbye!", background="red") 
		self.button4.pack(side=LEFT)	  ### (4)
	
		
root = Tk()
myapp = MyApp(root)
root.mainloop()