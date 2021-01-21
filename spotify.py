import win32gui
import pyautogui
 
def loadwindowslist(hwnd, topwindows):
	topwindows.append((hwnd, win32gui.GetWindowText(hwnd)))

def showwindowslist():
	topwindows = []
	win32gui.EnumWindows(loadwindowslist, topwindows)
	for hwin in topwindows:	
		sappname=str(hwin[1])
		nhwnd=hwin[0]
		#print(str(nhwnd) + ": " + sappname)
		if(sappname == "Spotify Premium" or sappname == "Spotify"):
			f=open("id_spotify.txt","w")
			f.write(str(nhwnd))
			f.close()

def findandshowwindow(bshow, bbreak):
	topwindows = []
	win32gui.EnumWindows(loadwindowslist, topwindows)
	for hwin in topwindows:	
		sappname=str(hwin[0])
		f=open("id_spotify.txt")
		num_spotify = f.read()
		f.close()
		if (sappname == num_spotify):	
			nhwnd=hwin[0]
			print(">>> Found: " + str(nhwnd) + ": " + sappname)
			if(bshow):
				win32gui.ShowWindow(nhwnd,5)
				win32gui.SetForegroundWindow(nhwnd)
			if(bbreak):
				win32gui.ShowWindow(nhwnd,5)
				win32gui.SetForegroundWindow(nhwnd)

def ejecutar_spotify(operacion):
	showwindowslist()
	findandshowwindow(False, True)
	findandshowwindow(True, True)
	if(operacion == "rep" or operacion == "paus"):
		pyautogui.press(" ")
	if(operacion == "next"):
		pyautogui.keyDown('ctrl')
		pyautogui.press('right')
		pyautogui.keyUp('ctrl')
	if(operacion == "previous"):
		pyautogui.keyDown('ctrl')
		pyautogui.press('left')
		pyautogui.keyUp('ctrl')

