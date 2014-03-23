"""<tt075.py

In the previous program, we introduced "command binding" and pointed out some of 
the differences between event binding and command binding.  In this program, we 
explore those differences in a bit more detail.


WHAT EVENTS DOES "COMMAND" BIND TO?

In the previous program, if you use the TAB key to put the focus on the "OK" 
button, pressing the spacebar causes the button to change color, but pressing 
the RETURN key has no effect.

The reason for this is that the "command" option for a Button widget provides 
keyboard-event awareness as well as mouse-event awareness.  The keyboard event
that it listens for is a press of the spacebar, not of the RETURN key.  So, with
command binding, pressing the spacebar will cause the OK button to change color,
but pressing the RETURN key will have no effect.  

This behavior seems (to me, at least, with my Windows background) unusual.  So 
part of the moral here is that if you are going to use command binding, it is a 
good idea to understand exactly what it is you are binding to.  That is, it is a 
good idea to understand exactly what keyboard and/or mouse events cause the 
command to be invoked.  

Unfortunately, the only really reliable source of this information is the Tk 
source code itself.  For more accessible information, you can check books about 
Tk (Brent Welch's "Practical Programming in Tcl and Tk" is especially good) or 
about Tkinter.  The Tk documentation is spotty, but available online. For 
version 8.4 of Tcl, the online documentation is available at: 

      http://www.tcl.tk/man/tcl8.4/TkCmd/contents.htm

You should also know that not all widgets provide a "command" option.  Most of 
the various Button widgets (RadioButton, CheckButton, etc.) do.  And others 
provide similar options (e.g. scrollcommand).  But you really have to 
investigate each different kind of widget to find out whether it supports 
command binding.  But by all means learn about the "command" option for the 
widgets that you will be using.  It will improve the behavior of your GUI, and 
make your life as a coder easier.


USING EVENT BINDING AND COMMAND BINDING TOGETHER

We noted in our last program that command binding, unlike event binding, does 
NOT automatically pass an event object as an argument.  This can make life a 
little complicated if you want to bind an event handler to a widget using *both* 
event binding *and* command binding.

For example, in this program we really would like our buttons to respond to 
presses of the RETURN key as well as the spacebar.  But to get them to do that, 
we will have to use event binding to the <Return> keyboard event, like we did in 
our earlier program. (1)  

The problem is that the command binding will not pass an event object as an 
argument, but the event binding will.  So how should we write our event handler?

There are a number of solutions to this problem, but the simplest is to write 
two event handlers.  The "real" event handler (2) will be the one used by the 
"command" binding, and it won't expect an event object.  

The other event handler (3) will just be a wrapper for the real event-handler.  
This wrapper will expect the event-object argument, but will ignore it and call 
the real event-handler without it.  We will give the wrapper the same name as 
the real event-handler, but with an added "_a" suffix.

PROGRAM BEHAVIOR

If you run this program, the behavior will be the same as the previous program, 
except for the fact that now the buttons will respond to a press of the RETURN 
key as well as the spacebar. 

[revised: 2002-10-01]
>"""
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent   
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1, command=self.button1Click)  
		self.button1.bind("<Return>", self.button1Click_a)    ### (1)
		self.button1.configure(text="OK", background= "green")
		self.button1.pack(side=LEFT)
		self.button1.focus_force()       
		
		self.button2 = Button(self.myContainer1, command=self.button2Click)   
		self.button2.bind("<Return>", self.button2Click_a)    ### (1)
		self.button2.configure(text="Cancel", background="red")   	
		self.button2.pack(side=RIGHT)
		
	def button1Click(self):  ### (2)
		print "button1Click event handler" 
		if self.button1["background"] == "green":  
			self.button1["background"] = "yellow"
		else:
			self.button1["background"] = "green"
	
	def button2Click(self): ### (2)
		print "button2Click event handler" 
		self.myParent.destroy()      
  
	def button1Click_a(self, event):  ### (3)
		print "button1Click_a event handler (a wrapper)" 
		self.button1Click()
				
	def button2Click_a(self, event):  ### (3)
		print "button2Click_a event handler (a wrapper)" 
		self.button2Click()
				
							
root = Tk()
myapp = MyApp(root)
root.mainloop()