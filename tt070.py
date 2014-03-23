"""<tt070.py

In the previous program, you could make the buttons do something by clicking on 
them with the mouse, but you couldn't make them do something by pressing a key 
on the keyboard.  In this program, we see how to make them react to keyboard 
events as well as mouse events.

First, we need the concept of "input focus", or simply "focus".  

If you're familiar with Greek mythology (or if you saw the Disney animated movie 
"Hercules") you may remember the Fates.  The Fates were three old women who 
controlled the destinies of men.  Each human life was a thread in the hands of 
the Fates, and when they cut the thread, the life ended.

The remarkable thing about the Fates was that they shared only one eye among 
all three of them.  The one with the eye had to do all of the seeing, and tell 
the other two what she saw.  The eye could be passed from one Fate to another, 
so they could take turns seeing.  And of course, if you could steal the eye, you 
had a MAJOR bargaining chip when negotiating with the Fates.

"Focus" is what allows the widgets on your GUI to see keyboard events. It is to 
the widgets on your GUI, what the single eye was to the Fates. 

Only one widget at a time can have the focus, and the widget that "has focus" is 
the widget that sees, and responds to, keyboard events.  "Setting focus" on a 
widget is the process of giving the focus to the widget. 

In this program, for example, our GUI has two buttons: "OK" and "Cancel".  
Suppose I hit the RETURN button on the keyboard.  Will that keypress "Return" 
event be seen by (or sent to) the "OK" button, indicating the user has accepted 
his choice?  Or will the "Return" event be seen by (or sent to) the "Cancel" 
button, indicating that the user has cancelled the operation?  It depends on 
where the "focus" is.  That is, it depends on which (if any) of the buttons "has 
focus".

Like the Fates' eye, which could be passed from one Fate to another, focus can 
be passed from one GUI widget to another.  There are several ways of passing, or 
moving, the focus from one widget to another.  One way is with the mouse.  You 
can "set focus" on a widget by clicking on the widget with the left mouse 
button.  (At least, this model, which is called the "click to type" model, is 
the way it works on Windows and Macintosh, and in Tk and Tkinter.  There are 
some systems that use a "focus follows mouse" convention in which the widget 
that is under the mouse automatically has focus, and no click is necessary.  You 
can get the same effect in Tk by using the tk_focusFollowsMouse procedure.)

Another way to set focus is with the keyboard.  The set of widgets that are 
capable of receiving the focus are stored in a circular list (the "traversal 
order") in the order in which the widgets were created.  Hitting the TAB key on 
the keyboard moves the focus from its current location (which may be nowhere) to 
the next widget in the list. At the end of the list, the focus moves to the 
widget at the head of the list.  And hitting SHIFT+TAB moves the focus backward, 
rather than forward, in the list.

When a GUI button has focus, the fact that it has focus is shown by a small 
dotted box around the text of the button.  Here's how to see it.  Run our 
previous program.  When the program starts, and the GUI displays, neither of the 
buttons has focus, so you don't see the dotted box.  Now hit the TAB key.  You 
will see the little dotted box appear around the left button, showing that focus 
has been given to it.  Now hit the TAB key again, and again.  You will see how 
the focus jumps to the next button, and when it reaches the last button, it 
wraps around again to the first one.  (Since the program shows only two buttons, 
the effect is that the focus jumps back and forth between the two buttons.)

(0)
In this program, we would like the OK button to have focus from the very 
beginning. So we use the "focus_force()" method, which forces the focus to go to 
the OK button. When you run this program, you will see that the OK button has 
focus from the time the application starts.

In the last program, our buttons responded to only one keyboard event -- a keyprees 
of the TAB key -- which moved the focus back and forth between the two buttons. 
But if you hit the ENTER/RETURN key on the keyboard, nothing happened.  That is 
because we had bound only mouse clicks, not keyboard events, to our buttons.  

In this program we will also bind keyboard events to the buttons.

(1) (2)
The statements to bind keyboard events to the buttons are quite simple -- they 
have the same format as statements to bind mouse events.  The only difference is 
that the name of the event is the name of a keyboard event (in this case, 
"<Return>") rather than a mouse event.

We want a press of the RETURN key on the keyboard and a click of the left mouse 
button to have the same effect on the widget, so we bind the same event handler 
to both types of events.

This program shows that you can bind multiple types of events to a single widget 
(such as a button).  And you can bind multiple <widget, event> combinations to 
the same event handler.  

(3) (4)
Now that our button widgets respond to multiple kinds of events, we can 
demonstrate how to retrieve information from an event object.  What we will do 
is to pass the event objects to (5) a "report_event" routine that will (6) print 
out information about the event that it obtains from the event's attributes.

Note that in order to see this information printed out on the console, you
must run this program using python (not pythonw) from a console window.

PROGRAM BEHAVIOR

When you run this program, you will see two buttons. Clicking on the left 
button, or pressing the RETURN key when the button has the keyboard focus, will 
change its color.  Clicking on the right button, or pressing the RETURN key when 
the button has the keyboard focus, will shut down the application. For any of 
these keyboard or mouse events, you should see a printed message giving the time 
of the event and describing the event.

[Revised: 2002-09-26]
>"""
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent   
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="OK", background= "green")
		self.button1.pack(side=LEFT)
		self.button1.focus_force()         ### (0)	
		self.button1.bind("<Button-1>", self.button1Click)  
		self.button1.bind("<Return>", self.button1Click)  ### (1)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Cancel", background="red")   
		self.button2.pack(side=RIGHT)
		self.button2.bind("<Button-1>", self.button2Click)   
		self.button2.bind("<Return>", self.button2Click)  ### (2)
		
	def button1Click(self, event): 
		report_event(event)        ### (3)
		if self.button1["background"] == "green":  
			self.button1["background"] = "yellow"
		else:
			self.button1["background"] = "green"
	
	def button2Click(self, event):
		report_event(event)   ### (4)
		self.myParent.destroy()      
  
def report_event(event):     ### (5)
	"""Print a description of an event, based on its attributes.
	"""
	event_name = {"2": "KeyPress", "4": "ButtonPress"}
	print "Time:", str(event.time)   ### (6)
	print "EventType=" + str(event.type), \
		event_name[str(event.type)],\
		"EventWidgetId=" + str(event.widget), \
		"EventKeySymbol=" + str(event.keysym)
		
			
root = Tk()
myapp = MyApp(root)
root.mainloop()