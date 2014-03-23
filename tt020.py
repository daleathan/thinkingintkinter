"""<tt020.py

Now we tackle another of the four main GUI tasks -- specifying how the GUI 
should look.

In this program, we introduce three major concepts of Tkinter programming:

	* creating a GUI object and associating it with its parent 	
	* packing 
	* containers vs. widgets

From now on, I'm going to distinguish between a container component and a 
widget.  As I will be using the terms, a "widget" is a GUI component that 
(usually) is visible and does things.  A "container" in contrast is simply a 
container -- a basket, as it were -- into which we can put widgets.

Tkinter provides a number of containers.  "Canvas" is a container for drawing
applications.  The most frequently used container is a "frame".

Frames are provided by Tkinter in a class called "Frame".  An expression like: 

	Frame(myParent)

creates an instance of the Frame class (that is, it creates a frame), and 
associates the frame instance with its parent, myParent.  Or another way of 
looking at it is: such an expression adds a child frame to the myParent 
component.

So in this program, statement (1): 

	myContainer1 = Frame(myParent)

creates a frame whose parent is myParent (that is, root), and gives it the name 
"myContainer1".  In short, it creates a container into which we can put widgets.  
(We won't put any widgets into in this program.  We'll do that in later programs.)

Note that the parent/child relationship here is a LOGICAL one, not a visual one.  
This relationship exists to support such things as the destroy event -- so that 
when a parent component (such as the root) is destroyed, the parent knows who 
its children are, and can destroy them before destroying itself.  

(2)
The next statement "packs" myContainer1. 

     myContainer1.pack()

Simply put, "packing" is a process of setting up a VISUAL relationship between a 
GUI component and its parent.  If you don't pack a component, you will never see 
it.

"Pack" invokes the Tkinter "pack" geometry manager.  A geometry manager is 
essentially an API -- a way of talking to Tkinter -- for telling Tkinter how you 
want containers and widgets to be visually presented. Tkinter supports three 
geometry managers: pack, grid, and place.  Pack (and to a lesser extent) grid 
are the most widely used, because they are the easiest to use.  All of the
examples in "Thinking in Tkinter" use the pack geometry manager.

So here you see a basic pattern for Tkinter programming that we will see 
over and over again.

  (1) an instance (of a widget or a container) is created, and associated with its parent	
  (2) the instance is packed.


PROGRAM BEHAVIOR

When you run this program, it will look very much like the previous one, except 
that there will be less to see.  That is because ...

FRAMES ARE ELASTIC

A frame is basically a container.  The interior of a container -- the "space" as 
it were, inside the container -- is called the "cavity".  ("Cavity" is a 
technical term that Tkinter gets from Tk.)

This cavity is "stretchy" or elastic, like a rubber band.  Unless you specify an 
minimum or maximum size for the frame, the cavity will stretch or shrink to 
accommodate whatever is placed inside the frame.  

In the previous program, because we hadn't put anything into it, the root 
displayed itself with its default size. 

But in this program, we *have* put something into the root's cavity -- we have 
put Container1 into it.  So the root frame shrinks to accommodate the size of 
Container1. But since we haven't put any widgets into Container1, and we haven't 
specified a minimum size for Container1, the root's cavity shrinks down to 
nothing.  That is why there is nothing to see below the title bar.

In the next few programs, we will put widgets and other containers into 
Container1, and you will see how Container1 stretches to accommodate them.

[revised: 2003-02-24]
>"""
from Tkinter import *

root = Tk()

myContainer1 = Frame(root)  ### (1)
myContainer1.pack()         ### (2)

root.mainloop()       