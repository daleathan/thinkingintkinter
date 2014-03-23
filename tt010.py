"""<tt010.py

THE SIMPLEST POSSIBLE TKINTER PROGRAM -- THREE STATEMENTS!

Of the four basic GUI tasks that we discussed in the last program,
this program does only one -- it runs the event loop.

(1)
The first statement imports Tkinter, so that it is available for use. Note that 
the form of the import ("from Tkinter import *") means that we will not have to 
qualify anything that we get from Tkinter with a "Tkinter." prefix.

(2)
The second statement creates a "toplevel" window. Technically, what the the 
second statement is doing, is creating an instance of the class "Tkinter.Tk". 

This toplevel window is the highest-level GUI component in any 
Tkinter application.  By convention, the toplevel window is usually
named "root".  

(3)
The third statement executes the "mainloop" (that is, the event loop) method of 
the "root" object.  As the mainloop runs, it waits for events to happen in root.  
If an event occurs, then it is handled and the loop continues running, waiting 
for the next evernt.  The loop continues to execute until a "destroy" event 
happens to the root window.  A "destroy" event is one that closes a window.  
When the root is destroyed, the window is closed and the event loop is exited.

PROGRAM BEHAVIOR 

When you run this program, you will see that (thanks to Tk) the toplevel window 
automatically comes furnished with widgets to minimize, maximize, and close the 
window.  Try them -- you'll see that they really do work.

Clicking on the "close" widget (the "x" in a box, at the right of the title bar) 
generates a "destroy" event. The destroy event terminates the main event loop. 
And since there are no statements after "root.mainloop()", the program has nothing 
more to do, and ends.

[revised: 2003-02-23]
>""" 

from Tkinter import * ### (1)

root = Tk()           ### (2) 
root.mainloop()       ### (3)