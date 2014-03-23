"""<tt035.py

USING A CLASS STRUCTURE

In this program, we introduce the concept of structuring a Tkinter application
as a set of classes. 

In this program, we have added a class called MyApp and moved some of the code 
from the previous program into its constructor (__init__) method.  In this 
restructured version of the program, we do 3 different things:

(1) 
In our code, we define a class (MyApp) that defines how we want our GUI to look.  
It defines the way we want our GUI to look and the kinds of things that we want 
to do with it.  All of this code is put into the constructor (__init__) method 
of the class. (1a)

(2)
When the program executes, the first thing it does is to create an instance of 
the class.  The statement that creates the instance is

   myapp = MyApp(root)
   
Note that the name of the class is "MyApp" (note the capitalization) and
the name of the instance is "myapp" (note the lack of capitalization).

Note also that this statement passes "root" as an argument into the constructor 
method (__init__) of MyApp.  The constructor method recognizes the root under 
the name "myParent".  (1a) 

(3) 
Finally, we run mainloop on the root.


WHY STRUCTURE YOUR APPLICATION AS A CLASS?

One of the reasons to use a class structure in your program is simply to control 
the program better.  A program that is structured into classes is probably -- 
especially if it is a very big program -- a lot easier to understand than one 
that is unstructured.

A more important consideration is that structuring your application as a
class helps you to avoid the use of global variables.  Eventually, as your
program grows, you will probably want some of your event handlers to be able
to share information among themselves.  One way is to use global variables,
but that is a very messy techniqe.  A much better way is to use instance (that is,
"self." variables), and for that you must give your application a class
structure.  We will explore this issue in a later program in this series.


WHEN TO INTRODUCE CLASS STRUCTURING

We've introduced the notion of a class structure for Tkinter programs early, in 
order to explain it and then move on to other matters.  But in actual 
development, you may choose to proceed differently.  

In many cases, a Tkinter program starts as a simple script.  All of the code is 
inline, as in our previous program.  Then, as you understand new dimensions of 
the application, the programs grows. After a while, you have a LOT of code.  You 
may have started to use global variables... maybe a LOT of global variables.  
The program starts to become difficult to understand and modify. When that 
happens, it is time to refactor your program, and to re-structure it using 
classes.

On the other hand, if you are comfortable with classes, and have a pretty good 
idea of the final shape of your program, you may choose to structure your 
program using classes from the very beginning.  

But on the other hand (back to the first hand?), early in the development 
process (Gerrit Muller has observed) often you don't yet know the best class 
structure to use -- early in the process, you simply don't have a clear enough 
understanding of the problem and the solution.  Starting to use classes too 
early in the process can introduce a lot of unnecessary structure that merely 
clutters up the code, hinders understanding, and eventually requires more 
refactoring.

So it is pretty much a matter of individual taste and experience and prevailing 
circumstances.  Do what feels right for you.  And -- no matter what you choose 
to do -- don't be afraid to do some serious refactoring when you need to.

PROGRAM BEHAVIOR

When you run this program, it will look exactly like the previous one.
No functionality has been changed -- only how the code is structured.

[revised: 2003-02-23]
>"""
from Tkinter import *

class MyApp:                         ### (1)
	def __init__(self, myParent):      ### (1a)
		self.myContainer1 = Frame(myParent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1) 
		self.button1["text"]= "Hello, World!"     
		self.button1["background"] = "green"      
		self.button1.pack()	                       
		
root = Tk()
myapp = MyApp(root)  ### (2)
root.mainloop()      ### (3)