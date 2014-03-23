"""<tt076.py

In the last few programs, we explored ways to make your programs actually do
work with event handlers.

In this program, we take a quick look at sharing information between event
handlers.


SHARING INFORMATION BETWEEN EVENT-HANDLER FUNCTIONS

There are a variety of situations in which you might want an event handler to 
perform some task, and then share the results of that task with other event 
handlers in your program. 

A common pattern is that you have an application with two sets of widgets. One 
set of widgets sets up, or chooses, some piece of information, and the other set 
of widgets does something with the information.  

For example, you might have a widget that allows a user to pick a filename from 
a list of filenames, and another set of widgets that offer various operations on 
the file that was picked -- opening the file, deleting it, copying it, renaming 
it, and so on.  

Or you might have one set of widgets that sets various configuration options for 
your application, and another set (buttons offering SAVE and CANCEL options, 
perhaps) that either save those settings to disk, or cancel without saving them.
 
Or you might have one set of widgets that sets up parameters for a program that 
you want to run, and another widget (probably a button with a name like RUN or 
EXECUTE) that starts the program running with those parameters.

Or you might need one invocation of an event-handler function to pass information 
to a later invocation of the same function.  Consider an event handler that 
simply toggles a variable back and forth between two different values. In order 
for it to assign a new value to the variable, it has to know what value it 
assigned to the variable the last time it was run.


THE PROBLEM

The problem here is that each event handler is a separate function.  Each event 
handler has its own local variables that it does not share with other 
event-handler functions, or even with later invocations of itself.  So the 
problem is this -- How can an event-handler function share data with other 
handlers, if it can't share its local variables with them?

The solution, of course, is that the variables that need to be shared cannot be 
local to the event handler functions.  They must be stored *outside* of the
event handler functions. 


SOLUTION 1 -- USE GLOBAL VARIABLES

One technique for doing this is to make them (the variables that you want to 
share) global.  For example, in each handler that needs to change or see 
myVariable1 and myVariable2, you can put the statement:

		global myVariable1, myVariable2

But the use of global variables is potentially dangerous, and is generally 
frowned upon as sloppy programming.


SOLUTION 2 -- USE INSTANCE VARIABLES

A much cleaner technique is to use "instance variables" (that is, "self." 
variables) to hold the information that you want to share between event 
handlers.  To do this, of course, your application must be implemented in a 
class, and not simply as in-line code.  

This was one of the reasons that (earlier in this series) we put our application 
into a class.  Since we did that earlier, at this point our application already 
has an infrastructure that will allow us to use instance variables. 

In this program, we are going to remember and share a very simple piece of 
information: the name of the last button that was invoked.  We will store it in 
an instance variable called "self.myLastButtonInvoked". [see ### 1 comments]

And to show that we actually are remembering this information, whenever a button 
handler is invoked, it will print out this information. [see ### 2 comments]


PROGRAM BEHAVIOR

This program shows three buttons. When you run this program, if you click on any 
of the buttons, it will display its own name, and the name of the previous 
button that was clicked.

Note that none of the buttons will close the application, so when you are ready
to close it, you must use the CLOSE widget (the icon with an "X" in a box, at
the right side of the titlebar). 

[revised: 2002-10-05]
>"""
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		
		### 1 -- At the outset, we haven't yet invoked any button handler.
		self.myLastButtonInvoked = None  	
		
		self.myParent = parent   
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.yellowButton = Button(self.myContainer1, command=self.yellowButtonClick)   
		self.yellowButton.configure(text="YELLOW", background="yellow")   	
		self.yellowButton.pack(side=LEFT)

		self.redButton = Button(self.myContainer1, command=self.redButtonClick)  
		self.redButton.configure(text="RED", background= "red")
		self.redButton.pack(side=LEFT)  
		
		self.whiteButton = Button(self.myContainer1, command=self.whiteButtonClick)   
		self.whiteButton.configure(text="WHITE", background="white")   	
		self.whiteButton.pack(side=LEFT)
		
	def redButtonClick(self):   
		print "RED    button clicked.  Previous button invoked was", self.myLastButtonInvoked  ### 2
		self.myLastButtonInvoked = "RED"  ### 1
		
	def yellowButtonClick(self):  
		print "YELLOW button clicked.  Previous button invoked was", self.myLastButtonInvoked ### 2
		self.myLastButtonInvoked = "YELLOW" ### 1
				
	def whiteButtonClick(self):  
		print "WHITE  button clicked.  Previous button invoked was", self.myLastButtonInvoked ### 2
		self.myLastButtonInvoked = "WHITE" ### 1
       
		
print "\n"*100 # a simple way to clear the screen
print "Starting..."					
root = Tk()
myapp = MyApp(root)
root.mainloop()
print "... Done!"