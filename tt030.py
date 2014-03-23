"""<tt030.py

In this program, we create our first widget, and put it into myContainer1.

(1)
The widget will be a button -- that is, it will be an instance of the Tkinter 
"Button" class.  The statement:

		button1 = Button(myContainer1)

creates the button, gives it the name "button1", and associates it with its 
parent, the container object called myContainer1.

(2)(3)
Widgets have many attributes, which are stored in their local namespace 
dictionary. Button widgets have attributes to control their size, their 
foreground and background colors, the text that they display, how their borders 
look, and so on.  In this example, we will set just two of button1's
attributes: the background color and the text.  We do it by setting the values
in the button's dictionary with the keys "text" and "background".

		button1["text"]= "Hello, World!"
		button1["background"] = "green"

(4)	
And of course, we pack button1.

		button1.pack()	

SOME USEFUL TECHNICAL TERMINOLOGY

Sometimes the relationship between a container and the widget(s) that it
contains is referred to as a "parent/child" relationship.  It is also 
referred to as a "master/slave" relationship. 

PROGRAM BEHAVIOR

When you run this program, you should see that Container1 now contains a green 
button with the text "Hello, World!".  When you click on it, it won't do 
anything, because we haven't yet specified what we want to happen when the
button is clicked. (We'll do that later.)  

For now, you will have to close the window, as before, by clicking the CLOSE 
icon on the title bar.

Note how myContainer1 has stretched to accommodate button1.

[revised: 2002-10-01]
>"""
from Tkinter import *

root = Tk()
 
myContainer1 = Frame(root)
myContainer1.pack()

button1 = Button(myContainer1)      ### (1)
button1["text"]= "Hello, World!"    ### (2)
button1["background"] = "green"     ### (3)
button1.pack()	                    ### (4)

root.mainloop()