"""<tt077.py

In this program we explore some ...

MORE ADVANCED FEATURES OF COMMAND BINDING

In our program tt075.py, we used the "command" option to bind an event handler 
to a widget. For example, in that program the statement

    self.button1 = Button(self.myContainer1, command=self.button1Click)

bound the button1Click function to the button1 widget.

And we used event binding to bind our buttons to the <Return> keyboard event.

    self.button1.bind("<Return>", self.button1Click_a)

In our earlier program, the event handlers for the two buttons performed quite 
different functions. 

But suppose that the situation was different.  Suppose that we have several 
buttons, all of which should trigger essentially the *same* type of action.  The 
best way to handle such a situation is to bind the events for all of the buttons 
to a single event handler. Each button would invoke the same handler routine, 
but pass it different arguments telling it what to do.   

That is what we are doing in this program.  


COMMAND BINDING

In this program, as you can see, we have two buttons, and we use the "command" 
option to bind them all to the same event handler -- the "buttonHandler" routine.  
We pass the buttonHandler routine three arguments: the name of the button (in 
the button_name variable), a number, and a string. 

    self.button1 = Button(self.myContainer1,
    	command=self.buttonHandler(button_name, 1, "Good stuff!")
    	)

In a serious application, the buttonHandler routine would of course do serious 
work, but in this program it merely prints the arguments that it receives.


EVENT BINDING

So much for command binding.  What about event binding?  

You will note that we have commented out the two lines that do event binding on 
the <Return> event.

  # self.button1.bind("<Return>", self.buttonHandler_a(event, button_name, 1, "Good stuff!"))

This is the first sign of a problem.  Event binding automatically passes an
event argument -- but there is simply no way to include that event argument in
our list of arguments.  

We'll have to come back to this problem later.  For now, let's simply run the 
program and see what happens.


PROGRAM BEHAVIOR

When you look at the code, this program looks quite reasonable.  But when you 
run it, you will see that it doesn't work right.  The buttonHandler routine is 
invoked even before the GUI is displayed.  In fact, it is invoked TWO times! 

And if you left-mouse-click on any of the buttons, you will find that nothing 
happens -- the "eventHandler" routine is *not* being invoked.

Note that the only way to close this program is to click the "close" icon (the 
"X" in a box) on the right side of the title bar.

So run the program now, and see what happens.  Then, in our next program, we 
will see why it happens.

[revised: 2003-02-23]
>"""
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent   
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		button_name = "OK"
		self.button1 = Button(self.myContainer1,
			command=self.buttonHandler(button_name, 1, "Good stuff!"))
			
		# self.button1.bind("<Return>", self.buttonHandler_a(event, button_name, 1, "Good stuff!"))
		self.button1.configure(text=button_name, background="green")  
		self.button1.pack(side=LEFT)
		self.button1.focus_force()  # Put keyboard focus on button1    
		
		button_name = "Cancel"
		self.button2 = Button(self.myContainer1, 
			command=self.buttonHandler(button_name, 2, "Bad  stuff!")) 
			 
		# self.button2.bind("<Return>", self.buttonHandler_a(event, button_name, 2, "Bad  stuff!"))    
		self.button2.configure(text=button_name, background="red")
		self.button2.pack(side=LEFT)   
				
		
	def buttonHandler(self, arg1, arg2, arg3):   
		print "    buttonHandler routine received arguments:", arg1.ljust(8), arg2, arg3
		
 	def buttonHandler_a(self, event, arg1, arg2, arg3):
		print "buttonHandler_a received event", event
		self.buttonHandler(arg1, arg2, arg3)
		
print "\n"*100 # clear the screen
print "Starting program tt077."							
root = Tk()
myapp = MyApp(root)
print "Ready to start executing the event loop."
root.mainloop()
print "Finished       executing the event loop."