# File renamer
# Copyright 2021 Bob Slater.

from guizero import App, Text, PushButton, TextBox, Box
from os import listdir, getcwd
from os.path import isfile, join

# Variables
cwd = getcwd()
listYOffset = 3 #Used for grid layout, to procedurally place items.
testList = [] #Global variable used as a placeholder. May get deleted later.
#filetype = "Null" # Will be used in the future.

#Function declarations:
def updateList(): #Updates the list of files in the CWD
	fileList = [f for f in listdir(cwd) if isfile(f)]
	return fileList #Removes the need for the global variable.

def list_files():
	filelist = updateList() #Updates each time the button is pressed

	# testList = [] #Was used to reset the list on each update. No longer needed.
	print("filelist= " + str(len(filelist))) #For debug purposes.
	print("testlist= " + str(len(testList))) #For debug purposes.
	for i in range(len(filelist)): #Adds TextBoxes as list entries for each filelist entry.
		if (len(testList) < len(filelist)): #Test to make sure we aren't adding unnecessary boxes.
			print("Adding TextBox to testList at grid [0," + str(i) +"]")
			testList.append(TextBox(app, text="Not Updated Properly", grid=[0, listYOffset+len(testList)], width=48, align="left"))
		#testList[i].value = filelist[i]
		#print(len(testList))
	#Loops through to delete any listings no longer available.
	if (len(testList) > len(filelist)): 
		for i in range(len(testList) - len(filelist)):
			print ("To be removed " + str(len(testList) - len(filelist)) + " TextBox(s)")
			testList[i+1].destroy()
			testList.pop(i+1)
			print ("New testList total is " + str(len(testList)))
	#file1.value = filelist[0]
	for i in range(len(filelist)): #Fills TextBoxes with data from filelist.
		testList[i].value = filelist[i]
	#TextBox(app, text="Files will be listed here.", grid=[0, listYOffset+i], width=48, align="left")

def select_filetype():
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
