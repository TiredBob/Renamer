# File renamer
# Copyright 2021 Bob Slater. // TiredBob
# https://github.com/TiredBob/Renamer

from guizero import App, Text, PushButton, TextBox, Box
from os import listdir, getcwd
from os.path import isfile

# Variables
cwd = getcwd()
listYOffset = 3 #Used for grid layout, to procedurally place items.
testList = [] #Global variable used as a placeholder. May get deleted later.
numBoxes = 0
#filetype = "Null" # Will be used in the future.

#Function declarations:
def updateList(): #Updates the list of files in the CWD
	fileList = [f for f in listdir(cwd) if isfile(f)]
	return fileList #Removes the need for the global variable.

def createTextBoxes(fileList, numBoxes): #Adds TextBoxes as list entries for each fileList entry.
	for i in range(len(fileList)): 
		if (len(testList) < len(fileList)): #Test to make sure we aren't adding unnecessary boxes.
			print("Adding TextBox to testList at grid [0," + str(i) +"]")
			testList.append(TextBox(app, text="Error: Value not set!", grid=[0, listYOffset+len(testList)], width=48, align="left"))
			numBoxes+=1
	return testList #Global variable still required, for comparisons.

def removeTextBoxes(boxList, numToRemove): #Loops through to delete any listings no longer available.
	for i in range(numToRemove):
		print ("To be removed " + str(numToRemove) + " TextBox(s)")
		testList[i+1].destroy()
		testList.pop(i+1)
		print ("New testList total is " + str(len(testList)))

def list_files():
	fileList = updateList() #Updates each time the button is pressed
	testList = createTextBoxes(fileList, numBoxes) 
	if (len(testList) > len(fileList)): #Checks to see if any files were removed from CWD.
		removeTextBoxes(testList, (len(testList) > len(fileList)))
	for i in range(len(fileList)): #Fills TextBoxes with data from fileList.
		testList[i].value = fileList[i]

def select_filetype(): #Not yet implemented.
	pass

#Main App Declaration: 

app = App("Renamer", layout="grid")

#Manual Widget Declarations:

title = Text(app, "Push the green button to list files", grid=[0,0], align="left")
buttonBox = Box(app, grid=[0,1], align="left", layout="grid")
button = PushButton(buttonBox, list_files, text="List Files:", grid=[0,0], width=5, align="left")
button2 = PushButton(buttonBox, select_filetype, text="Select Filetype", grid=[1, 0], width=8, align="left")
button.bg = "green"
button2.bg = "green"

#Display // Main Program Loop.

app.display()
