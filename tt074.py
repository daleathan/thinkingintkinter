"""<tt074.py

In an earlier program, we introduced "event binding".  There is another way of 
binding an event_handler to a widget.  It is called "command binding" and we 
will look at it in this program. 

COMMAND BINDING

You will remember that in our previous programs, we bound the "<Button-1>" mouse 
event to our button widget.  "Button" is another name for a "ButtonPress" mouse 
event.  And a "ButtonPress" mouse event is different from a "ButtonRelease" 
mouse event.  The "ButtonPress" event is the act of pushing down on the mouse 
button, BUT NOT RELEASING IT.  The "ButtonRelease" event is the act of releasing 
the mouse button -- letting it up again.  

We need to distinguish a mouse ButtonPress from a mouse ButtonRelease in order 
to support such features as "drag and drop", in which we do a ButtonPress on 
some GUI component, drag the component somewhere, and then "drop" it in the new 
location by by releasing the mouse button.

But button widgets are not the kind of thing that can be dragged-and-dropped.  
If a user thought that he could drag and drop a button, he might do a 
ButtonPress on the button widget, then drag the mouse pointer to someplace else 
on the screen, and release the mouse button.  This is NOT the kind of activity 
that we want to recognize as a "push" (or -- technical term -- "invocation") of 
the button widget.  For us to consider a button widget as having been pushed, we 
want the user to do a ButtonPress on the widget, and then -- WITHOUT moving the 
mouse pointer away from the widget -- to do a ButtonRelease.  *THAT* is what we 
will consider to be a button press.

This is a more complicated notion of button invocation than we have used in our
previous programs, where we simply bound a "Button-1" event to the button widget
using event binding.

Fortunately, there is another form of binding that supports this more 
complicated notion of widget invocation.  It is called "command binding" because 
it uses the widget's "command" option.  

In this program, look at the lines with comments (1) and (2) to see how command 
binding is done.  In those lines, we use the "command" option to bind button1 to 
the "self.button1Click" event handler, and to bind button2 to the 
"self.button2Click" event handler.

(3) (4)

Look at the definition of the event handlers themselves.  Note that -- unlike 
the event handlers in the previous program -- they are NOT expecting an event 
object as an argument.  That is because command binding, unlike event binding, 
does NOT automatically pass an event object as an argument.  And of course, this 
makes sense.  A command binding doesn't bind a single event to a handler.  It 
binds multiple events to a handler.  For a Button widget, for instance, it binds 
a pattern of a ButtonPress followed by a ButtonRelease to a handler.  If it were 
to pass an event to its event handler, which event would it pass: ButtonPress or 
ButtonRelease? Neither would be exactly correct.  This is why command binding, 
unlike event binding, does not pass an event object.

We will look a little bit more at this difference in our next program, but for 
now, let's run the program.


PROGRAM BEHAVIOR

When you run this program, the buttons that you see will look exactly like the
buttons in the previous program... but they will behave differently.  

Compare their behavior when doing a mouse ButtonPress on one of the buttons. For 
example, move the mouse pointer on the screen until it is positioned over the 
"OK" button widget, and then press down on the left mouse button BUT 
DO NOT LET THE MOUSE BUTTON UP.  

If you do this with the previous example, the button1Click handler will be run 
immediately and you will see a message printed.  But if you do this with this program,
nothing will happen... UNTIL YOU RELEASE THE MOUSE BUTTON.  When you release the mouse
button, you will see a printed message.

There is another difference.  Compare their behaviour when you do a keypress of 
the spacebar, and of the RETURN key.   For example, use the TAB key to put the focus
on the "OK" button, then press the spacebar or the RETURN key.

In the previous program (where we bound the "OK" button to the "Return" keypress 
event), pressing the spacebar has no effect but pressing the RETURN key causes the
button to change color.  In this program, on the other hand, the behavior is just
the reverse -- pressing the spacebar causes the button to change color, but pressing
the RETURN key has no effect.

We'll look at these behaviors in our next program.

[revised: 2002-10-01]
>"""
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent   
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1, command=self.button1Click) ### (1)
		self.button1.configure(text="OK", background= "green")
		self.button1.pack(side=LEFT)
		self.button1.focus_force()         

		
		self.button2 = Button(self.myContainer1, command=self.button2Click)  ### (2)
		self.button2.configure(text="Cancel", background="red")   	
		self.button2.pack(side=RIGHT)

		
	def button1Click(self):  ### (3)
		print "button1Click event handler" 
		if self.button1["background"] == "green":  
			self.button1["background"] = "yellow"
		else:
			self.button1["background"] = "green"
	
	def button2Click(self): ### (4)
		print "button2Click event handler" 
		self.myParent.destroy()      
  
		
			
root = Tk()
myapp = MyApp(root)
root.mainloop()