# File renamer
# Copyright 2021 TiredBob
# https://github.com/TiredBob/Renamer

from guizero import App, Text, PushButton, TextBox, Box, Combo
from os import listdir, getcwd
from os.path import isfile

#Variables
cwd = getcwd()
listYOffset = 3 #Used for grid layout, to procedurally place items.
testList = [] #Global variable used as a placeholder. May get deleted later.
numBoxes = 0
xOffset = 0
#filetype = "Null" # Will be used in the future.

#Function declarations:
def updateList(): #Updates the list of files in the CWD
	fileList = [f for f in listdir(cwd) if isfile(f)]
	return fileList #Removes the need for the global variable.

def createTextBoxes(fileList, num): #Adds TextBoxes as list entries for each fileList entry.
	global numBoxes
	global xOffset
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

def list_files():
	fileList = updateList() #Updates each time the button is pressed
	combo = Combo(buttonBox, options=list_filetypes(fileList), selected="All Files", grid=[2,0])
	testList = createTextBoxes(fileList, len(fileList))
	if (len(testList) > len(fileList)): #Checks to see if any files were removed from CWD.
		removeTextBoxes(testList, (len(testList) > len(fileList)))
	for i in range(len(fileList)): #Fills TextBoxes with data from fileList.
		testList[i].value = fileList[i]
	# print("numBoxes = " + str(numBoxes))

def list_filetypes(fileList): #Not yet implemented.
	fileTypes = []
	offset = 0
	fileTypes.append("All files")
	#WIP Need to iterate the last 5 characters in each string to find the period
	#and check previous entries to make sure there are no duplicate entries
	#in the combo. Then append them to the list, and sort alphabetically.
	for i in range (len(fileList)):
		lastFive = fileList[i][len(fileList[i])-5:len(fileList[i])]
		for x in range(4,0,-1): #Counts down
			#print("Countdown: " + str(x))
			if lastFive[5-x] == ".": #Starts at the end of the filename.
				# print("X is " + str(x))
				# print("Found it " + str(fileList[i][len(fileList[i])-x:len(fileList[i])]))
				tempType = str(fileList[i][len(fileList[i])-x:len(fileList[i])])
				if tempType not in fileTypes:
					fileTypes.append(tempType)
		# fileTypes.append(fileList[i][len(fileList[i])-5:len(fileList[i])])
	return fileTypes
#Main App Declaration: 

app = App("Renamer", layout="grid")

#Manual Widget Declarations:

title = Text(app, "Push the green button to list files", grid=[0,0], align="left")
buttonBox = Box(app, grid=[0,1], align="left", layout="grid")
button = PushButton(buttonBox, list_files, text="List Files:", grid=[0,0], width=5, align="left")
button.bg = "green"
#button2 = PushButton(buttonBox, select_filetype, text="Select Filetype", grid=[1, 0], width=8, align="left")
#button2.bg = "green"

#Display // Main Program Loop.

app.display()
