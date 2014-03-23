"""
A modified copy of easygui, to serve as a driver for the programs in 
Thinking In Tkinter.

"""


"""===============================================================
REVISION HISTORY
2 2002-10-08 re-cloned from easygui.py version 24, to pick up font fixes.
1 2002-09-21 Steve Ferg cloned it from easygui.py version 23.
=================================================================="""
"""
EasyGui provides an easy-to-use interface for simple GUI interaction
with a user.  It does not require the programmer to know anything about
tkinter, frames, widgets, callbacks or lambda.  All GUI interactions are
invoked by simple function calls that return results.

Note that EasyGui requires Tk release 8.0 or greater.
Documentation is in an accompanying file, easygui_doc.txt.

"""

EasyGuiRevisionInfo = "version 0.3, revision 24, 2002-10-06"
"""===============================================================
REVISION HISTORY
24 2002-10-06 improved control over font family and font size
	Added note that EasyGui requires Tk release 8.0 or greater.
	Added check to verify that we're running Tk 8.0 or greater.

23 2002-09-06 more improvements in appearance, added items to testing choices
	changed order of parameters for textbox and codebox.
	Now ALL widgets have message and title as the first two arguments.
	Note that the fileopenbox, filesavebox, and diropenbox but ignore, the msg argument.
		To specify a title, you must pass arguments of (None, title)

23 2002-09-06 revised enterbox so it returns None if it was cancelled
22 2002-09-02 major improvements in formattting, sorting of choiceboxes, keyboard listeners

22 2002-07-22 fixed some problems cause in revision 21
21 2002-07-19 converted all indentation to tabs
20 2002-07-15 bugfix: textbox not displaying title
19 2002-06-03 added enterbox to the test suite
18 2002-05-16 added AutoListBox
17 2002-05-16 added DEFAULT_FONT_SIZE constants & reduced their size
16 2002-03-29 changed choicebox() so it shows as few lines a possible
15 2002-03-09 started work on an improved demo
14 2002-02-03 removed obsolete import of pmw
13 2002-02-02 added NW spec for choice box
12 2002-01-31 created buttonbox as basis for msgbox, etc.
11 2002-01-30 specified a minsize for msgbox()
10 2002-01-30 withdrew root on diropenbox(), fileopenbox(), filesavebox(), etc.
9 2002-01-26 pulled out winrexx routines into winrexxgui.py
	renamed listbox to choicebox
8 2002-01-25 added diropenbox(), fileopenbox(), filesavebox(), and codebox()
7 2002-01-24 disabled the textbox, so text cannot be edited
6 2002-01-22 added case-insensitive sort for choicebox choices
5 2002-01-21 reworked ynbox() and ccbox() as boolboxes. Ready for version 0.1.
4 2002-01-20 added boolbox(), ynbox(), ccbox(); got choicebox working!
3 2002-01-18 got choicebox to display... not working yet
2 2002-01-17 got the messagebox and entry functions to working OK!
1 2002-01-16 Steve Ferg wrote it.
=================================================================="""

import sys
from Tkinter import *
if TkVersion < 8.0 :
	print "\n" * 3
	print "*"*75
	print "Running Tk version:", TkVersion 
	print "You must be using Tk version 8.0 or greater to use EasyGui."
	print "Terminating."
	print "*"*75
	print "\n" * 3
	sys.exit(0)
	

rootWindowPosition = "+300+200"
import string

DEFAULT_FONT_FAMILY   = ("MS", "Sans", "Serif")
MONOSPACE_FONT_FAMILY = ("Courier")
DEFAULT_FONT_SIZE     = 10
BIG_FONT_SIZE         = 12
SMALL_FONT_SIZE       =  9
CODEBOX_FONT_SIZE     =  9
TEXTBOX_FONT_SIZE     = DEFAULT_FONT_SIZE

import tkFileDialog

#-------------------------------------------------------------------
# various boxes built on top of the basic buttonbox
#-------------------------------------------------------------------

def ynbox(message="Shall I continue?", title=""):
	"""Display a message box with choices of Yes and No.
	Return 1 if Yes was chosen, otherwise return 0

	If invoked without a message parameter, displays a generic request for a confirmation
	that the user wishes to continue.  So it can be used this way:

		if ynbox(): pass # continue
		else: sys.exit(0)  # exit the program
	"""

	choices = ["Yes", "No"]
	if title == None: title = ""
	return boolbox(message, title, choices)

def ccbox(message="Shall I continue?", title=""):
	"""Display a message box with choices of Continue and Cancel.
	Return 1 if Continue was chosen, otherwise return 0.

	If invoked without a message parameter, displays a generic request for a confirmation
	that the user wishes to continue.  So it can be used this way:

		if ccbox(): pass # continue
		else: sys.exit(0)  # exit the program
	"""
	choices = ["Continue", "Cancel"]
	if title == None: title = ""
	return boolbox(message, title, choices)


def boolbox(message="Shall I continue?", title="", choices=["Yes","No"]):
	"""Display a boolean message box.
	Return 1 if the first choice was selected, otherwise return 0.
	"""
	if title == None:
		if message == "Shall I continue?": title = "Confirmation"
		else: title = ""


	reply = buttonbox(message, title, choices)
	if reply == choices[0]: return 1
	else: return 0


def indexbox(message="Shall I continue?", title="", choices=["Yes","No"]):
	"""Display a buttonbox with the specified choices.
	Return the index of the choice selected.
	"""
	reply = buttonbox(message, title, choices)
	index = -1
	for choice in choices:
		index = index + 1
		if reply == choice: return index



#-------------------------------------------------------------------
# msgbox
#-------------------------------------------------------------------

def msgbox(message="Shall I continue?", title=""):
	"""Display a messagebox
	"""
	choices = ["OK"]
	reply = buttonbox(message, title, choices)
	return reply


#-------------------------------------------------------------------
# buttonbox
#-------------------------------------------------------------------
def buttonbox(message="Shall I continue?", title="", choices = ["Button1", "Button2", "Button3"]):
	"""Display a message, a title, and a set of buttons.
	The buttons are defined by the members of the choices list.
	Return the text of the button that the user selected.
	"""

	global root, __replyButtonText, __a_button_was_clicked, __widgetTexts, buttonsFrame

	if title == None: title = ""
	if message == None: message = "This is an example of a buttonbox."

	# __a_button_was_clicked will remain 0 if window is closed using the close button.
	# It will be changed to 1 if the event loop is exited by a click of one of the buttons.
	__a_button_was_clicked = 0

	# Initialize __replyButtonText to the first choice.
	# This is what will be used if the window is closed by the close button.
	__replyButtonText = choices[0]

	root = Tk()
	root.title(title)
	root.iconname('Dialog')
	root.geometry(rootWindowPosition)
	root.minsize(400, 100)

	# ------------- define the frames --------------------------------------------
	messageFrame = Frame(root)
	messageFrame.pack(side=TOP, fill=BOTH)

	buttonsFrame = Frame(root)
	buttonsFrame.pack(side=BOTTOM, fill=BOTH)

	# -------------------- place the widgets in the frames -----------------------
	messageWidget = Message(messageFrame, text=message, width=400)
	messageWidget.configure(font=(DEFAULT_FONT_FAMILY,DEFAULT_FONT_SIZE))
	messageWidget.pack(side=TOP, expand=YES, fill=X, padx='3m', pady='3m')

	__put_buttons_in_buttonframe(choices)

	# -------------- the action begins -----------
	# put the focus on the first button
	__firstWidget.focus_force()
	root.mainloop()
	if __a_button_was_clicked: root.destroy()
	return __replyButtonText

#-------------------------------------------------------------------
# enterbox
#-------------------------------------------------------------------
def enterbox(message="Enter something.", title="", argDefaultText=None):
	"""Show a box in which a user can enter some text.
	You may optionally specify some default text, which will appear in the
	enterbox when it is displayed.
	Returns the text that the user entered, or None if he cancels the operation.
	"""

	global root, __enterboxText, __enterboxDefaultText, __a_button_was_clicked, cancelButton, entryWidget, okButton

	if title == None: title == ""
	choices = ["OK", "Cancel"]
	if argDefaultText == None:
		_enterboxDefaultText = ""
	else:
		__enterboxDefaultText = argDefaultText

	__enterboxText = __enterboxDefaultText


	# __a_button_was_clicked will remain 0 if window is closed using the close button]
	# will be changed to 1 if event-loop is quit by a click of one of the buttons.
	__a_button_was_clicked = 0

	root = Tk()
	root.title(title)
	root.iconname('Dialog')
	root.geometry(rootWindowPosition)
	root.bind("Escape", __enterboxCancel)

	# -------------------- put subframes in the root --------------------
	messageFrame = Frame(root)
	messageFrame.pack(side=TOP, fill=BOTH)

	entryFrame = Frame(root)
	entryFrame.pack(side=TOP, fill=BOTH)

	buttonsFrame = Frame(root)
	buttonsFrame.pack(side=BOTTOM, fill=BOTH)

	#-------------------- the message widget ----------------------------
	messageWidget = Message(messageFrame, width="4.5i", text=message)
	messageWidget.pack(side=RIGHT, expand=1, fill=BOTH, padx='3m', pady='3m')

	# --------- entryWidget ----------------------------------------------
	entryWidget = Entry(entryFrame, width=40)
	entryWidget.configure(font=(DEFAULT_FONT_FAMILY,BIG_FONT_SIZE))
	entryWidget.pack(side=LEFT, padx="3m")
	entryWidget.bind("<Return>", __enterboxGetText)
	entryWidget.bind("<Escape>", __enterboxCancel)
	# put text into the entryWidget
	entryWidget.insert(0,__enterboxDefaultText)

	# ------------------ ok button -------------------------------
	okButton = Button(buttonsFrame, takefocus=1, text="OK")
	okButton.pack(expand=1, side=LEFT, padx='3m', pady='3m', ipadx='2m', ipady='1m')
	okButton.bind("<Return>", __enterboxGetText)
	okButton.bind("<Button-1>", __enterboxGetText)

	# ------------------ (possible) restore button -------------------------------
	if argDefaultText != None:
		# make a button to restore the default text
		restoreButton = Button(buttonsFrame, takefocus=1, text="Restore default")
		restoreButton.pack(expand=1, side=LEFT, padx='3m', pady='3m', ipadx='2m', ipady='1m')
		restoreButton.bind("<Return>", __enterboxRestore)
		restoreButton.bind("<Button-1>", __enterboxRestore)

	# ------------------ cancel button -------------------------------
	cancelButton = Button(buttonsFrame, takefocus=1, text="Cancel")
	cancelButton.pack(expand=1, side=RIGHT, padx='3m', pady='3m', ipadx='2m', ipady='1m')
	cancelButton.bind("<Return>", __enterboxCancel)
	cancelButton.bind("<Button-1>", __enterboxCancel)

	# ------------------- time for action! -----------------
	entryWidget.focus_force()    # put the focus on the entryWidget
	root.mainloop()  # run it!

	# -------- after the run has completed ----------------------------------
	if __a_button_was_clicked:
		root.destroy()  # button_click didn't destroy root, so we do it now
		return __enterboxText
	else:
		# No button was clicked, so we know the OK button was not clicked
		__enterboxText = None
		return __enterboxText


def __enterboxGetText(event):
	global root, __enterboxText, entryWidget, __a_button_was_clicked
	__enterboxText = entryWidget.get()
	__a_button_was_clicked = 1
	root.quit()

def __enterboxRestore(event):
	global root, __enterboxText, entryWidget
	entryWidget.delete(0,len(entryWidget.get()))
	entryWidget.insert(0, __enterboxDefaultText)

def __enterboxCancel(event):
	global root,  __enterboxDefaultText, __enterboxText, __a_button_was_clicked
	__enterboxText = None
	__a_button_was_clicked = 1
	root.quit()


#-------------------------------------------------------------------
# choicebox
#-------------------------------------------------------------------
def choicebox(message="Pick something.", title="", choices=["program logic error - no choices specified"]):
	"""Present the user with a list of choices.
	Return the choice that he selected, or return None if he cancelled selection.
	"""
	global root, __choiceboxText, choiceboxWidget, defaultText
	global __a_button_was_clicked # cancelButton, okButton
	global choiceboxWidget, choiceboxChoices, choiceboxChoices

	choiceboxButtons = ["OK", "Cancel"]

	lines_to_show = min(len(choices), 20)
	lines_to_show = 20

	if title == None: title = ""

	# Initialize __choiceboxText
	# This is the value that will be returned if the user clicks the close icon
	__choiceboxText = None

	# __a_button_was_clicked will remain 0 if window is closed using the close button]
	# will be changed to 1 if event-loop is quit by a click of one of the buttons.
	__a_button_was_clicked = 0

	root = Tk()
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	root_width = int((screen_width * 0.8))
	root_height = int((screen_height * 0.5))
	root_xpos = int((screen_width * 0.1))
	root_ypos = int((screen_height * 0.05))

	root.title(title)
	root.iconname('Dialog')
	rootWindowPosition = "+0+0"
	root.geometry(rootWindowPosition)
	root.expand=NO
	root.minsize(root_width, root_height)
	rootWindowPosition = "+" + str(root_xpos) + "+" + str(root_ypos)
	root.geometry(rootWindowPosition)



	# ---------------- put the frames in the window -----------------------------------------
	message_and_buttonsFrame = Frame(root)
	message_and_buttonsFrame.pack(side=TOP, fill=X, expand=YES, pady=0, ipady=0)

	messageFrame = Frame(message_and_buttonsFrame)
	messageFrame.pack(side=LEFT, fill=X, expand=YES)

	buttonsFrame = Frame(message_and_buttonsFrame)
	buttonsFrame.pack(side=RIGHT, expand=NO, pady=0)

	choiceboxFrame = Frame(root)
	choiceboxFrame.pack(side=BOTTOM, fill=BOTH, expand=YES)

	# -------------------------- put the widgets in the frames ------------------------------

	# ---------- put a message widget in the message frame-------------------
	messageWidget = Message(messageFrame, anchor=NW, text=message, width=int(root_width * 0.9))
	messageWidget.configure(font=(DEFAULT_FONT_FAMILY,DEFAULT_FONT_SIZE))
	messageWidget.pack(side=LEFT, expand=YES, fill=BOTH, padx='1m', pady='1m')

	# --------  put the choiceboxWidget in the choiceboxFrame ---------------------------
	choiceboxWidget = Listbox(choiceboxFrame
		, height=lines_to_show
		, borderwidth="1m"
		, relief="flat"
		, bg="white"
		)
	choiceboxWidget.configure(font=(DEFAULT_FONT_FAMILY,DEFAULT_FONT_SIZE))

		# add a vertical scrollbar to the frame
	rightScrollbar = Scrollbar(choiceboxFrame, orient=VERTICAL, command=choiceboxWidget.yview)
	choiceboxWidget.configure(yscrollcommand = rightScrollbar.set)

	# add a horizontal scrollbar to the frame
	bottomScrollbar = Scrollbar(choiceboxFrame, orient=HORIZONTAL, command=choiceboxWidget.xview)
	choiceboxWidget.configure(xscrollcommand = bottomScrollbar.set)

	# pack the Listbox and the scrollbars.  Note that although we must define
	# the textbox first, we must pack it last, so that the bottomScrollbar will
	# be located properly.

	bottomScrollbar.pack(side=BOTTOM, fill = X)
	rightScrollbar.pack(side=RIGHT, fill = Y)

	choiceboxWidget.pack(side=LEFT, padx="1m", pady="1m", expand=YES, fill=BOTH)

	# sort the choices, eliminate duplicates, and put the choices into the choiceboxWidget
	choices.sort( lambda x,y: cmp(x.lower(),    y.lower())) # case-insensitive sort
	lastInserted = None
	choiceboxChoices = []
	for choice in choices:
		if choice == lastInserted: pass
		else:
			choiceboxWidget.insert(END, choice)
			choiceboxChoices.append(choice)
			lastInserted = choice

	root.bind('<Any-Key>', KeyboardListener)

	# put the buttons in the buttonsFrame
	if len(choices) > 0:
		okButton = Button(buttonsFrame, takefocus=YES, text="OK", height=1, width=6)
		okButton.pack(expand=NO, side=TOP,  padx='2m', pady='1m', ipady="1m", ipadx="2m")
		okButton.bind("<Return>", __choiceboxChoice)
		okButton.bind("<Button-1>",__choiceboxChoice)

		# now bind the keyboard events
		choiceboxWidget.bind("<Return>", __choiceboxChoice)
		choiceboxWidget.bind("<Double-Button-1>", __choiceboxChoice)
	else:
		# now bind the keyboard events
		choiceboxWidget.bind("<Return>", __choiceboxCancel)
		choiceboxWidget.bind("<Double-Button-1>", __choiceboxCancel)

	cancelButton = Button(buttonsFrame, takefocus=YES, text="Cancel", height=1, width=6)
	cancelButton.pack(expand=NO, side=BOTTOM, padx='2m', pady='1m', ipady="1m", ipadx="2m")
	cancelButton.bind("<Return>", __choiceboxCancel)
	cancelButton.bind("<Button-1>", __choiceboxCancel)

	# -------------------- bind some keyboard events ----------------------------


	root.bind("<Escape>", __choiceboxCancel)

	# --------------------- the action begins -----------------------------------
	# put the focus on the choiceboxWidget, and the select highlight on the first item
	choiceboxWidget.select_set(0)
	choiceboxWidget.focus_force()

	# --- run it! -----
	root.mainloop()
	if __a_button_was_clicked: root.destroy()
	return __choiceboxText


def __choiceboxChoice(event):
	global root, __choiceboxText, __a_button_was_clicked, choiceboxWidget
	choice_index = choiceboxWidget.curselection()
	__choiceboxText = choiceboxWidget.get(choice_index)
	__a_button_was_clicked = 1
	# print "Debugging> mouse-event=", event, " event.type=", event.type
	# print "Debugging> choice =", choice_index, __choiceboxText
	root.quit()


def __choiceboxCancel(event):
	global root, __choiceboxText, __a_button_was_clicked
	__a_button_was_clicked = 1
	__choiceboxText = None
	root.quit()


def KeyboardListener(event):
	global choiceboxChoices, choiceboxWidget
	key = event.keysym
	if len(key) <= 1:
		if key in string.printable:
			## print key
			# now find it in list.....

			## before we clear the list, remember the selected member
			try:
				start_n = int(choiceboxWidget.curselection()[0])
			except IndexError:
				start_n = -1

			## clear the selection.
			choiceboxWidget.selection_clear(0, 'end')

			## start from previous selection +1
			for n in range(start_n+1, len(choiceboxChoices)):
				item = choiceboxChoices[n]
				if item[0].lower() == key.lower():
					choiceboxWidget.selection_set(first=n)
					return
			else:
				# has not found it so loop from top
				for n in range(len(choiceboxChoices)):
					item = choiceboxChoices[n]
					if item[0].lower() == key.lower():
						choiceboxWidget.selection_set(first = n)
						## should call see method but don't have
						## scrollbars in this demo!
						return

				# nothing matched -- we'll look for the next logical choice
				for n in range(len(choiceboxChoices)):
					item = choiceboxChoices[n]
					if item[0].lower() > key.lower():
						if n > 0:
							choiceboxWidget.selection_set(first = (n-1))
						else:
							choiceboxWidget.selection_set(first = 0)
						## should call see method but don't have
						## scrollbars in this demo!
						return

				# still no match (nothing was greater than the key)
				# we set the selection to the first item in the list
				choiceboxWidget.selection_set(first = (len(choiceboxChoices)-1))
				## should call see method but don't have
				## scrollbars in this demo!
				return

#-------------------------------------------------------------------
# codebox
#-------------------------------------------------------------------

def codebox(message="", title="", text=""):
	"""
	Display some text in a monospaced font, with no line wrapping.
	This function is suitable for displaying code and text that is
	formatted using spaces.

	The text parameter should be a string, or a list or tuple of lines to be
	displayed in the textbox.
	"""
	textbox(message, title, text, codebox=1 )

#-------------------------------------------------------------------
# textbox
#-------------------------------------------------------------------
def textbox(message="", title="", text="", codebox=0):
	"""Display some text in a proportional font with line wrapping at word breaks.
	This function is suitable for displaying general written text.

	The text parameter should be a string, or a list or tuple of lines to be
	displayed in the textbox.
	"""

	if message == None: message = ""
	if title == None: title = ""

	global root, __replyButtonText, __a_button_was_clicked, __widgetTexts, buttonsFrame
	choices = ["0K"]
	__replyButtonText = choices[0]
	__a_button_was_clicked = 0

	root = Tk()

	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	root_width = int((screen_width * 0.8))
	root_height = int((screen_height * 0.5))
	root_xpos = int((screen_width * 0.1))
	root_ypos = int((screen_height * 0.05))

	root.title(title)
	root.iconname('Dialog')
	rootWindowPosition = "+0+0"
	root.geometry(rootWindowPosition)
	root.expand=NO
	root.minsize(root_width, root_height)
	rootWindowPosition = "+" + str(root_xpos) + "+" + str(root_ypos)
	root.geometry(rootWindowPosition)


	mainframe = Frame(root)
	mainframe.pack(side=TOP, fill=BOTH, expand=YES)

	# ----  put frames in the window -----------------------------------
	# we pack the textboxFrame first, so it will expand first
	textboxFrame = Frame(mainframe, borderwidth=3)
	textboxFrame.pack(side=BOTTOM , fill=BOTH, expand=YES)

	message_and_buttonsFrame = Frame(mainframe)
	message_and_buttonsFrame.pack(side=TOP, fill=X, expand=NO)

	messageFrame = Frame(message_and_buttonsFrame)
	messageFrame.pack(side=LEFT, fill=X, expand=YES)

	buttonsFrame = Frame(message_and_buttonsFrame)
	buttonsFrame.pack(side=RIGHT, expand=NO)

	# -------------------- put widgets in the frames --------------------

	# put a textbox in the top frame
	if codebox:
		character_width = int((root_width * 0.6) / CODEBOX_FONT_SIZE)
		textbox = Text(textboxFrame,height=25,width=character_width, padx="2m", pady="1m")
		textbox.configure(wrap=NONE)
		textbox.configure(font=(MONOSPACE_FONT_FAMILY, CODEBOX_FONT_SIZE))

	else:
		character_width = int((root_width * 0.6) / SMALL_FONT_SIZE)
		textbox = Text(
			textboxFrame
			, height=25
			,width=character_width
			, padx="2m"
			, pady="1m"
			)
		textbox.configure(wrap=WORD)
		textbox.configure(font=(DEFAULT_FONT_FAMILY,TEXTBOX_FONT_SIZE))
 

	# add a vertical scrollbar to the frame
	rightScrollbar = Scrollbar(textboxFrame, orient=VERTICAL, command=textbox.yview)
	textbox.configure(yscrollcommand = rightScrollbar.set)

	# add a horizontal scrollbar to the frame
	bottomScrollbar = Scrollbar(textboxFrame, orient=HORIZONTAL, command=textbox.xview)
	textbox.configure(xscrollcommand = bottomScrollbar.set)

	# pack the textbox and the scrollbars.  Note that although we must define
	# the textbox first, we must pack it last, so that the bottomScrollbar will
	# be located properly.

	# Note that we need a bottom scrollbar only for code.
	# Text will be displayed with wordwrap, so we don't need to have a horizontal
	# scroll for it.
	if codebox:
		bottomScrollbar.pack(side=BOTTOM, fill=X)
	rightScrollbar.pack(side=RIGHT, fill=Y)

	textbox.pack(side=LEFT, fill=BOTH, expand=YES)


	# ---------- put a message widget in the message frame-------------------
	messageWidget = Message(messageFrame, anchor=NW, text=message, width=int(root_width * 0.9))
	messageWidget.configure(font=(DEFAULT_FONT_FAMILY,DEFAULT_FONT_SIZE))
	messageWidget.pack(side=LEFT, expand=YES, fill=BOTH, padx='1m', pady='1m')

	# put the buttons in the buttonsFrame
	okButton = Button(buttonsFrame, takefocus=YES, text="OK", height=1, width=6)
	okButton.pack(expand=NO, side=TOP,  padx='2m', pady='1m', ipady="1m", ipadx="2m")
	okButton.bind("<Return>", __textboxOK)
	okButton.bind("<Button-1>",__textboxOK)


	# ----------------- the action begins ----------------------------------------
	try:
		# load the text into the textbox
		if type(text) == type("abc"): pass
		else:
			try:
				text = "".join(text)  # convert a list or a tuple to a string
			except:
				msgbox("Exception when trying to convert "+ str(type(text)) + " to text in textbox")
				sys.exit(16)
		textbox.insert(END,text, "normal")

		# disable the textbox, so the text cannot be edited
		textbox.configure(state=DISABLED)
	except:
		msgbox("Exception when trying to load the textbox.")
		sys.exit(16)

	try:
		okButton.focus_force()
	except:
		msgbox("Exception when trying to put focus on okButton.")
		sys.exit(16)



	root.mainloop()
	if __a_button_was_clicked: root.destroy()
	return __replyButtonText

def __textboxOK(event):
	global root, __a_button_was_clicked
	__a_button_was_clicked = 1
	root.quit()



#-------------------------------------------------------------------
# diropenbox
#-------------------------------------------------------------------
def diropenbox(msg=None, title=None, startpos=None):
	"""A dialog to get a directory name.
	Returns the name of a directory, or None if user chose to cancel.
	"""
	root = Tk()
	root.withdraw()
	f = tkFileDialog.askdirectory(parent=root, title=title)
	if f == "": return None
	return f

#-------------------------------------------------------------------
# fileopenbox
#-------------------------------------------------------------------
def fileopenbox(msg=None, title=None, startpos=None):
	"""A dialog to get a file name.
	Returns the name of a file, or None if user chose to cancel.
	"""
	root = Tk()
	root.withdraw()
	f = tkFileDialog.askopenfilename(parent=root,title=title)
	if f == "": return None
	return f


#-------------------------------------------------------------------
# filesavebox
#-------------------------------------------------------------------
def filesavebox(msg=None, title=None, startpos=None):
	"""A file to get the name of a file to save.
	Returns the name of a file, or None if user chose to cancel.
	"""
	root = Tk()
	root.withdraw()
	f = tkFileDialog.asksaveasfilename(parent=root, title=title)
	if f == "": return None
	return f


#-------------------------------------------------------------------
# utility routines
#-------------------------------------------------------------------
# These routines are used by several other functions in the EasyGui module.

def __buttonEvent(event):
	"""Handle an event that is generated by a person clicking a button.
	"""
	global  root, __a_button_was_clicked, __widgetTexts, __replyButtonText
	__replyButtonText = __widgetTexts[event.widget]
	__a_button_was_clicked = 1
	root.quit() # quit the main loop


def __put_buttons_in_buttonframe(choices):
	"""Put the buttons in the buttons frame
	"""
	global __widgetTexts, __firstWidget, buttonsFrame

	__widgetTexts = {}
	i = 0

	for buttonText in choices:
		tempButton = Button(buttonsFrame, takefocus=1, text=buttonText)
		tempButton.pack(expand=YES, side=LEFT, padx='1m', pady='1m', ipadx='2m', ipady='1m')

		# remember the text associated with this widget
		__widgetTexts[tempButton] = buttonText

		# remember the first widget, so we can put the focus there
		if i == 0:
			__firstWidget = tempButton
			i = 1

		# bind the keyboard events to the widget
		tempButton.bind("<Return>", __buttonEvent)
		tempButton.bind("<Button-1>", __buttonEvent)



def run_thinking():

	choices = string.split(
"""tt000.py - introduction 
tt010.py - simplest possible Tkinter program: 3 statements 
tt020.py - creating a GUI object; packing; containers vs. widgets 
tt030.py - creating a widget and putting it in a frame 
tt035.py - using a class structure in the program 
tt040.py - some other ways to define a widget 
tt050.py - packing 
tt060.py - event binding 
tt070.py - "focus" and binding a widget to keyboard events 
tt074.py - command binding 
tt075.py - using event binding and command binding together 
tt076.py - sharing information among event handlers 
tt077.py - passing arguments to event handlers (part 1) - the problem 
tt078.py - passing arguments to event handlers (part 2) - solving it with lambda 
tt079.py - passing arguments to event handlers (part 3) - solving it with currying 
tt080.py - widget options and pack settings 
tt090.py - nesting frames 
tt095.py - Window Manager methods & controlling the size of windows with the geometry option 
tt100.py - pack options: side, expand, fill, anchor """, "\n")
	

	title = "Thinking in Tkinter"
	msg = "Pick the 'Thinking in Tkinter' program that you wish to view and run."

	#========================================== END DEMONSTRATION DATA


	while 1: # do forever
		choice = choicebox(msg, title, choices)
		if choice == None: 
			msg = "Thank you for looking at 'Thinking in Tkinter'."
			msgbox(msg, title)
			break
		
		program_filename = choice.split()[0]
		program_name = program_filename.split(".")[0]
		f = open(program_filename, "r")
		t = f.readlines()
		f.close
		msg2 = "Here is the text of " + program_filename \
			+ "\n\nAfter you view the source code of the program, clicking the 'OK'" \
			+" button will run the program."
		codebox(msg2, title, t)

		try:
			exec "reload(" + program_name + ")"
		except:
			exec "import " + program_name 


if __name__ == '__main__':
	run_thinking()
