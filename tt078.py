"""<tt078.py 

Looking at the execution of the last program, we have to ask:
"What's happening here??!! The "buttonHandler" routine is being executed for each 
button, even before the event loop is started!!"

The reason is that in a statement like

  self.button1 = Button(self.myContainer1,
       command = self.buttonHandler(button_name, 1, "Good stuff!"))

we are calling the buttonHandler function, rather than asking that it be used as 
a callback.  That's not what we intended to do, but that is what we're actually 
doing.

NOTE THAT -->

 * buttonHandler is a function object, and can be used as a callback binding.  

 * buttonHandler() (note the parenthesis) on the other hand is an actual call to 
   the "buttonHandler" function. 

At the time that the statement

  self.button1 = Button(self.myContainer1,
       command = self.buttonHandler(button_name, 1, "Good stuff!"))

is executed, it is actually making a call to the "buttonHandler" routine.  The 
buttonHandler routine executes, printing its message, and returns the results of 
the call (in this case, the None object). Then the button's "command" option is 
bound to the results of the call.  In short, the command is bound to the "None" 
object.  And that is why, when you click on either of the buttons, nothing 
happens.


IS THERE A SOLUTION?

So... what's the solution?  Is there any way to parameterize, and reuse,
an event-handler function?

Yes.  There are a couple of generally recognized techniques for doing this.  One 
uses the Python built-in "lambda" function, and the other uses a technique 
called "currying".

In this program we will discuss how to work with lambda, and in the next
program we will look at currying. 

I'm not going to try to explain how lambda and currying work -- it is too 
complicated and too far off-track from our main goal, which is to get Tkinter 
programs working.  So I'm going to simply treat them as black boxes.  I won't 
talk about how they work -- I'll only talk about how to work with them.

So let's look at lambda.


COMMAND BINDING

Originally, we thought the following statement might work:

  self.button1 = Button(self.myContainer1, 
  	command = self.buttonHandler(button_name, 1, "Good stuff!")
  	)

... but we found out that it didn't work the way we thought it would. 

The way to do what we want is to re-write this statement this way:

  self.button1 = Button(self.myContainer1,
       command = lambda 
       arg1=button_name, arg2=1, arg3="Good stuff!" : 
       self.buttonHandler(arg1, arg2, arg3)
       )


EVENT BINDING

Happily, lambda also gives us a way to parameterize event binding.  Instead of:

     self.button1.bind("<Return>", 
     	self.buttonHandler_a(event, button_name, 1, "Good stuff!"))

(which wouldn't work, because there was no way to include the event argument in
the argument list), we can use lambda, this way:

		# event binding -- passing the event as an argument
		self.button1.bind("<Return>", 
			lambda 
			event, arg1=button_name, arg2=1, arg3="Good stuff!" : 
			self.buttonHandler_a(event, arg1, arg2, arg3)
			)

[Note that "event" here is a variable name -- it is not a Python keyword or 
anything like that.  This example uses the name "event" for the event argument, 
but some discussions of this technique use the name "e" for the event argument, 
and we could just as easily have called it "event_arg" if we had wanted to.]

One of the nice features of using lambda is that we can (if we wish), simply not 
pass the event argument.  If we don't pass the event argument, then we can call 
the self.buttonHandler function directly, instead of indirectly through the 
self.buttonHandler_a function.  

To illustrate this technique, we will code the event binding for button2
differently than we did for button1. This is what we do with button2:

		# event binding -- without passing the event as an argument
		self.button2.bind("<Return>", 
			lambda 
			event, arg1=button_name, arg2=2, arg3="Bad  stuff!" : 
			self.buttonHandler(arg1, arg2, arg3)
			)


PROGRAM BEHAVIOR

If you run this program, it will behave just as we wish.  

Note that you can change the keyboard focus from the OK to the CANCEL button,
and back again, by pressing the TAB key on the keyboard.

In particular, you should experiment with invoking the OK button by pressing the 
<Return> key on the keyboard.  If you invoke the OK button via a keypress of the 
<Return> key, you will be going through the buttonHandler_a function, and you 
will also get a message from it, printing information about the event that has 
been passed to it.

In any case, whether you click on one of the button widgets with the mouse, or 
invoke a widget via a <Return> keypress on the keyboard, it will nicely print 
the arguments that were passed to the buttonHandler function.

[revised: 2003-02-23]
>"""
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent   
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		#------------------ BUTTON #1 ------------------------------------
		button_name = "OK"
		
		# command binding
		self.button1 = Button(self.myContainer1,
			command = lambda 
			arg1=button_name, arg2=1, arg3="Good stuff!" :
			self.buttonHandler(arg1, arg2, arg3)
			)
		
		# event binding -- passing the event as an argument
		self.button1.bind("<Return>", 
			lambda 
			event, arg1=button_name, arg2=1, arg3="Good stuff!" : 
			self.buttonHandler_a(event, arg1, arg2, arg3)
			)
	     	
		self.button1.configure(text=button_name, background="green")  
		self.button1.pack(side=LEFT)
		self.button1.focus_force()  # Put keyboard focus on button1    
		
		#------------------ BUTTON #2 ------------------------------------		
		button_name = "Cancel"
		
		# command binding
		self.button2 = Button(self.myContainer1,
			command = lambda 
			arg1=button_name, arg2=2, arg3="Bad  stuff!": 
			self.buttonHandler(arg1, arg2, arg3)
			)

		# event binding -- without passing the event as an argument
		self.button2.bind("<Return>", 
			lambda 
			event, arg1=button_name, arg2=2, arg3="Bad  stuff!" : 
			self.buttonHandler(arg1, arg2, arg3)
			)
	
		self.button2.configure(text=button_name, background="red")
		self.button2.pack(side=LEFT)   
		
		
	def buttonHandler(self, argument1, argument2, argument3):   
		print "    buttonHandler routine received arguments:" \
			, argument1.ljust(8), argument2, argument3
		
 	def buttonHandler_a(self, event, argument1, argument2, argument3):
		print "buttonHandler_a received event", event
		self.buttonHandler(argument1, argument2, argument3)
		
				
print "\n"*100 # clear the screen
print "Starting program tt078."								
root = Tk()
myapp = MyApp(root)
print "Ready to start executing the event loop."
root.mainloop()
print "Finished       executing the event loop."