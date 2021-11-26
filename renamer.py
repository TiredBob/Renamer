# File renamer
# Copyright 2021 TiredBob
# https://github.com/TiredBob/Renamer

from guizero import App, Text, PushButton, TextBox, Box, Combo, MenuBar
from os import listdir, getcwd, startfile
from os.path import isfile, isdir
from tkinter import filedialog

#Variables
cwd = getcwd()
testList = [] #Global variable used as a placeholder. May get deleted later.
numBoxes = 0
fileTypes = [] # Will be used in the future.

#Function declarations:
def updateList(): #Updates the list of files in the CWD
	fileList = [f for f in listdir(cwd) if isfile(f)]
	return fileList #Removes the need for the global variable.

def menuFakeFunc(): #Placeholder
	pass

def openDirectoryDialog():
	newDirectory = filedialog.askdirectory()
	return newDirectory

def changeCWD():
	newCWD = openDirectoryDialog()
	print (newCWD)
	if newCWD == "":
		print("Canceled")
	elif isdir(newCWD):
		print("It's a directory")

def createTextBoxes(fileList, num): #Adds TextBoxes as list entries for each fileList entry.
	global numBoxes
	if (numBoxes > 0):
		offset = numBoxes + 1
	else:
		offset = numBoxes + 3
	for i in range(num): 
		if (len(testList) < num): #Test to make sure we aren't adding unnecessary boxes.
			# print("Adding TextBox to testList at grid [0," + str(offset+len(testList)) +"]") #For debug purposes.
			if (len(fileList[i]) < 28): #Set a minimum width for TextBox
				minWidth = 28
			else:
				minWidth = len(fileList[i])
			testList.append(TextBox(app, text="Error: Value not set!", grid=[0, offset+len(testList)], width=(minWidth), align="left"))
			numBoxes = numBoxes+1
	return testList #Global variable still required, for comparisons.

def removeTextBoxes(boxList, numToRemove): #Loops through to delete any listings no longer available.
	global numBoxes
	for i in range(numToRemove):
		# print ("To be removed " + str(numToRemove) + " TextBox(s)") #For debug purposes.
		testList[len(testList)-1].destroy()
		testList.pop()
		numBoxes = numBoxes - 1
		# print ("New testList total is " + str(len(testList))) #For debug purposes.

def checkFileType(fileName): #Checks the last 5 characters for a period. 
	lastFive = fileName[len(fileName)-5:len(fileName)]
	for x in range(4,0,-1): #Counts down
		if lastFive[5-x] == ".": #Starts at the end of the filename.
			tempType = str(fileName[len(fileName)-x:len(fileName)])
			return tempType #Returns the period and remaining characters.

def list_filetypes(fileList): #Creates and returns a list.
	fileTypes = []
	offset = 0
	fileTypes.append("All files")
	#WIP Need to sort alphabetically.
	for i in range (len(fileList)):
		tempType = checkFileType(str(fileList[i]))
		if tempType not in fileTypes:
			fileTypes.append(tempType)
	return fileTypes

def list_files():
	fileList = updateList() #Updates each time the button is pressed
	combo = Combo(app, options=list_filetypes(fileList), selected="All files", grid=[0,0], align="left")
	testList = createTextBoxes(fileList, len(fileList))
	if (len(testList) > len(fileList)): #Checks to see if any files were removed from CWD.
		removeTextBoxes(testList, (len(testList) > len(fileList)))
	for i in range(len(fileList)): #Fills TextBoxes with data from fileList.
		testList[i].value = fileList[i]
	button.hide()
	# print("numBoxes = " + str(numBoxes))

#Main App Declaration: 

app = App("Renamer", layout="grid")

#Manual Widget Declarations:

# title = Text(app, "Use the dropdown to list certain filetypes.", grid=[1,0], align="left")
#Spacing for readability. Will be consolidated into single line once menu is feature complete.
menubar = MenuBar(app, toplevel=["File", "Edit"], options=
	[
		[
			["Update Files", list_files],["Open Directory", changeCWD]
		],
		[
			["Option Edit", menuFakeFunc], ["Edit 2", menuFakeFunc]
		]
	])
##buttonBox = Box(app, grid=[0,1], align="left", layout="grid")
button = PushButton(app, list_files, text="List Files:", grid=[0,0], align="left")
# button.bg = "green"
#button2 = PushButton(buttonBox, select_filetype, text="Select Filetype", grid=[1, 0], width=8, align="left")
#button2.bg = "green"

#Display // Main Program Loop.

app.display()
