import pyrebase
import tkinter as tk
import tkinter.messagebox as tkmsgbox
import tkinter.scrolledtext as tksctxt


firebaseConfig = {
    "apiKey": "AIzaSyBIEOesiAKVZpMH61fijQOjEasgZH3OAyM",
    "authDomain": "lab12-4d31c.firebaseapp.com",
    "databaseURL": "https://lab12-4d31c-default-rtdb.firebaseio.com",
    "projectId": "lab12-4d31c",
    "storageBucket": "lab12-4d31c.appspot.com",
    "messagingSenderId": "326791594467",
    "appId": "1:326791594467:web:4b69be495856e74576a0d6"
    }

class Application(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
    
        #-------------------------------------------------------------------
        # row 1: connection stuff (and a clear-messages button)
        #-------------------------------------------------------------------
		self.groupCon = tk.LabelFrame(bd=0)
		self.groupCon.pack(side="top")
		#
		self.nameLbl = tk.Label(self.groupCon, text='Name', padx=10)
		self.nameLbl.pack(side="left")
		#
		self.name = tk.Entry(self.groupCon, width=20)
		self.name.insert(tk.END, '')
		self.name.bind('<Return>', streamHandler)
		self.name.pack(side="left")
		#
		padder = tk.Label(self.groupCon, padx=5)
		padder.pack(side="left")
		#
		self.subscribeButton = tk.Button(self.groupCon, text='Unsubscribe',
		command = subscribeButtonClick, width=10)
		self.subscribeButton.pack(side="left")
		#
		padder = tk.Label(self.groupCon, padx=1)
		padder.pack(side="left")


		#-------------------------------------------------------------------
		# row 2: the message field (chat messages + status messages)
		#-------------------------------------------------------------------
		self.msgText = tksctxt.ScrolledText(height=15, width=42,
		state=tk.DISABLED)
		self.msgText.pack(side="top")


		#-------------------------------------------------------------------
		# row 3: sending messages
		#-------------------------------------------------------------------
		self.groupSend = tk.LabelFrame(bd=0)
		self.groupSend.pack(side="top")
		#
		self.textInLbl = tk.Label(self.groupSend, text='message', padx=10)
		self.textInLbl.pack(side="left")
		#
		self.textIn = tk.Entry(self.groupSend, width=38)
		# if the focus is on this text field and you hit 'Enter',
		# it should (try to) send
		self.textIn.bind('<Return>', sendMessage)
		self.textIn.pack(side="left")
		#
		padder = tk.Label(self.groupSend, padx=5)
		padder.pack(side="left")
		#
		self.sendButton = tk.Button(self.groupSend, text = 'send',
		command = sendButtonClick)
		self.sendButton.pack(side="left")


		# set the focus on the IP and Port text field
		self.name.focus_set()

def clearText():
	g_app.msgText.configure(state=tk.NORMAL)
	g_app.msgText.delete(1.0, tk.END)
	g_app.msgText.see(tk.END)
	g_app.msgText.configure(state=tk.DISABLED)

def subscribeButtonClick():
	global g_subscribed

	if g_subscribed == False:
		subscribe()
	else:
		unsubscribe()

def sendButtonClick():
	global g_subscribed

	if g_subscribed == False:
		printToMessages('You have to be subscribed to send a message.')
	elif g_app.name.get() == '' or g_app.textIn.get() == '':
		printToMessages('You need to have set a name and typed a message to be able to send.')
	else:
		sendMessage(g_app)

def handleMessage(message):
	g_app.msgText.configure(state = tk.NORMAL)
	g_app.msgText.insert(tk.END, message["Name"] + ': ' + message["Text"] + '\n')
	g_app.msgText.see(tk.END)
	g_app.msgText.configure(state = tk.DISABLED)

def printToMessages(message):
	g_app.msgText.configure(state = tk.NORMAL)
	g_app.msgText.insert(tk.END, message + '\n')
	g_app.msgText.see(tk.END)
	g_app.msgText.configure(state = tk.DISABLED)

def on_closing():
	myQuit()

def myQuit():
	if g_subscribed == True:
		unsubscribe()
	g_root.destroy()

def unsubscribe():
	global g_message_stream
	global g_subscribed

	g_subscribed = False
	g_message_stream.close()
	g_app.subscribeButton['text'] = "Subscribe"
	clearText()

def subscribe():
	global g_message_stream
	global g_subscribed

	g_message_stream = g_db.child("Messages").stream(streamHandler)
	g_subscribed = True
	g_app.subscribeButton['text'] = "Unsubscribe"

def sendMessage(master):
	message = {"Name":g_app.name.get(), "Text":g_app.textIn.get()}
	g_db.child("Messages").push(message)

def streamHandler(incomingData):
	if incomingData["event"] == "put":
		if incomingData["path"] == "/":
			if incomingData["data"] != None:
				for key in incomingData["data"]:
					message = incomingData["data"][key]
					handleMessage(message)
		else:
			message = incomingData["data"]
			handleMessage(message)

#launch the gui
g_root = tk.Tk()
g_app = Application(master = g_root)

#firebase objects
g_firebase = pyrebase.initialize_app(firebaseConfig)
g_db = g_firebase.database()
g_subscribed = True
g_message_stream = g_db.child("Messages").stream(streamHandler)

# If attempting to close the window the on-close func will handle it
g_root.protocol("WM_DELETE_WINDOW", on_closing)

#Start the main loop

g_app.mainloop()
