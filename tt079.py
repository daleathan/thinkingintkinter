"""<tt079.py 

In the previous program, we looked at a technique involving lambda to pass 
arguments to an event-handler function.  In this program, we will look at a 
different technique, called "currying". 


ABOUT CURRY

In its very simplest sense, currying is a technique for using a function to 
construct other functions. 

Currying is a technique borrowed from functional programming.  If you would like 
to learn more about currying, there are several recipes available in the "Python 
Cookbook":

	http://aspn.activestate.com/ASPN/Python/Cookbook/

The curry class used in this program is from Scott David Daniels' recipe 
"curry -- associating parameters with a function", available at 
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52549 

As in our discussion of lambda, I'm not going to try to explain how currying 
works.  I'm simply going to treat the curry class as a black box.  I won't talk 
much about how it works -- I'll only talk about how to work with it.


CURRY -- HOW TO USE IT

The way to use curry (the technique) is to include a "curry" class in your 
program, or to import it from its own Python file.  In this program, we will 
include the curry code directly in the program.

Originally, we thought that the following statement could bind 
self.buttonHandler to self.button1's command option, but we found out that it 
didn't work the way we thought it would.

  self.button1 = Button(self.myContainer1,
       command = self.buttonHandler(button_name, 1, "Good stuff!"))

Using curry, the way to do what we want is to re-write this statement this way:

  self.button1 = Button(self.myContainer1,
       command = curry(self.buttonHandler, button_name, 1, "Good stuff!"))

As you can see, the code is quite straightforward.  Instead of invoking the 
self.buttonHandler function, we create a curry object (that is, an instance of 
the curry class), passing the self.buttonHandler function in as the first 
argument.  Basically, what happens is that the curry object remembers the name 
of the function that it was given.  Then when it (the curry object) is called, 
it -- in its own turn -- calls the function that it was given when it was 
created.


EVENT BINDING

Chad Netzer has devised a technique similar to currying, that can be used to 
parameterize event binding. [NOTE that this coding of the technique requires 
Python 2 or greater.]  It involves using an "event_lambda" function.

To use event_lambda, as with curry, you need to include the code for the 
"event_lambda" function in your program, or to import it from its own Python 
file.  In this program, we include the code for the event_lambda function 
directly in our program. 

	# ---------- code for function: event_lambda -------- 
	def event_lambda(f, *args, **kwds ): 
		"A helper function that wraps lambda in a prettier interface." 
		return lambda event, f=f, args=args, kwds=kwds : f( *args, **kwds )

Once the event_lambda function is available to us, we can use it to bind 
self.buttonHandler to the <Return> keyboard event, and pass it some arguments.
Here's how we do it:

	self.button1.bind("<Return>", 
		event_lambda( self.buttonHandler, button_name, 1, "Good stuff!" ) )

If you have an absolutely insatiable curiosity about how event_lambda works, it 
is a little bit easier to see by looking at the coding for button2.

For button2, use use a two-step process. First we invoke the event_lambda function.

	event_handler = event_lambda( self.buttonHandler, button_name, 2, "Bad  stuff!" ) 

When the event_lambda function is called, it uses lambda to create a new, un-named 
("anonymous") function object. 

		lambda event, f=f, args=args, kwds=kwds : f( *args, **kwds )

The un-named function object is a wrapper for the function we really want to 
invoke ("f", which in this program is "self.buttonHandler") and the arguments we 
specified at the time we called the event_lambda function.  

Then the event_lambda function returns this new anonymous function.

When event_lambda returns the anonymous function, we give it a name: "event_handler".

	event_handler = event_lambda( self.buttonHandler, button_name, 2, "Bad  stuff!" ) 

Then, in the second step, we bind the <Return> event to the "event_handler" 
function.

	self.button2.bind("<Return>", event_handler )

Note that for the anonymous function, 'event' is just a placeholder argument 
which is discarded and never used. Only the positional arguments (args) and the 
keyword arguments (kwds) are passed to the button-handler routine.


WOW!  I JUST BURNED OUT A BUNCH OF BRAIN CELLS!!

This is tricky stuff.  But don't think that you need to burn out a bunch of 
brain cells trying to understand how it all works.  You don't need to know HOW 
"curry" and "event_lambda" work in order to use them.  Just treat them like 
black boxes... just use them and don't worry about how they work.  


LAMBDA VS. CURRY AND EVENT_LAMBDA -- WHICH SHOULD I USE?

Well...

 * Code to invoke curry and event_lambda is relatively intuitive, short and simple.  
   The downside is that using them requires you to include them in the code for
   your program, or to import them.

 * Lambda, in contrast, is built into the Python language -- you don't need to 
   do anything special to import it; it is simply there.  
   The downside is that the code to use it can be long and a bit confusing.

So the choice is up to you.  "You pays yer money and takes yer choice," as they 
say. Use what you are most comfortable with, and/or what seems most appropriate 
to the task.

The REAL moral of this story is this...

Python is a powerful language, and it provides many tools that can be used to 
create callback functions for handling events.  "Thinking in Tkinter" is an 
introduction to basic concepts, not an encyclopedia of techniques, so we can 
explore only a few of those ways here.  But you can be confident that as you 
become more skilled with Python, and as your need for more flexibility grows, 
there are more advanced features of Python that will be available to you, and 
that can enable you to create just the kind of callback function that you need.


PROGRAM BEHAVIOR

If you run this program, it will behave exactly as the previous program did.  We 
haven't changed any of the behavior of the program, just the way the program is 
coded.

[revised: 2003-02-23]
>"""
from Tkinter import *

# ---------- code for class: curry (begin) ---------------------
class curry:
	"""from Scott David Daniels'recipe 
	"curry -- associating parameters with a function"
	in the "Python Cookbook" 
	http://aspn.activestate.com/ASPN/Python/Cookbook/
	"""

	def __init__(self, fun, *args, **kwargs):
		self.fun = fun
		self.pending = args[:]
		self.kwargs = kwargs.copy()

	def __call__(self, *args, **kwargs):
		if kwargs and self.kwargs:
			kw = self.kwargs.copy()
			kw.update(kwargs)
		else:
			kw = kwargs or self.kwargs
		return self.fun(*(self.pending + args), **kw)
# ---------- code for class: curry (end) ---------------------


# ---------- code for function: event_lambda (begin) --------
def event_lambda(f, *args, **kwds ):
	"""A helper function that wraps lambda in a prettier interface.
	Thanks to Chad Netzer for the code."""
	return lambda event, f=f, args=args, kwds=kwds : f( *args, **kwds )
# ---------- code for function: event_lambda (end) -----------
		
		
class MyApp:
	def __init__(self, parent):
		self.myParent = parent   
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		button_name = "OK"
		
		# command binding -- using curry
		self.button1 = Button(self.myContainer1,
		   command = curry(self.buttonHandler, button_name, 1, "Good stuff!"))

		# event binding -- using the event_lambda helper function
		self.button1.bind("<Return>", 
			event_lambda( self.buttonHandler, button_name, 1, "Good stuff!" ) )
			     	
		self.button1.configure(text=button_name, background="green")  
		self.button1.pack(side=LEFT)
		self.button1.focus_force()  # Put keyboard focus on button1    
		
		
		button_name = "Cancel"
		
		# command binding -- using curry
		self.button2 = Button(self.myContainer1,
			command = curry(self.buttonHandler, button_name, 2, "Bad  stuff!"))
			
		# event binding -- using the event_lambda helper function in two steps
		event_handler = event_lambda( self.buttonHandler, button_name, 2, "Bad  stuff!" ) 
		self.button2.bind("<Return>", event_handler )
		
		self.button2.configure(text=button_name, background="red")
		self.button2.pack(side=LEFT)   

	
	def buttonHandler(self, argument1, argument2, argument3):   
		print "    buttonHandler routine received arguments:", \
			argument1.ljust(8), argument2, argument3
		
	def buttonHandler_a(self, event, argument1, argument2, argument3):
		print "buttonHandler_a received event", event
		self.buttonHandler(argument1, argument2, argument3)
		
print "\n"*100 # clear the screen
print "Starting program tt079."							
root = Tk()
myapp = MyApp(root)
print "Ready to start executing the event loop."
root.mainloop()
print "Finished       executing the event loop."