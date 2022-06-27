import tkinter as tk
import matplotlib
import PIL.Image
import PIL.ImageTk
from cipher import cipherFunc

# Global Variables for containing info
shift = ""
code = ""
spaces = ""
result = ""
values = []

# intiialize possible values for dropdown
for i in range(0,26):
    values.append(i)

def setLeft(self,other):
    global shift
    shift = "left"
    self.configure(bg = 'black', fg = 'light gray')
    other.configure(fg = 'black', bg = 'light gray')
    getSpaces()

def setRight(self,other):
    global shift
    shift = "right"
    self.configure(bg = 'black', fg = 'light gray')
    other.configure(fg = 'black', bg = 'light gray')
    getSpaces()

def decodeFunc(self, other):
    global root, code
    self.configure(bg = 'black', fg = 'light gray')
    other.configure(fg = 'black', bg = 'light gray')
    code = "decode"
    text = "Encoding was done in which shift"
    codeDisplay(text)

def encodeFunc(self, other):
    global root, code
    self.configure(bg = 'black', fg = 'light gray')
    other.configure(fg = 'black', bg = 'light gray')
    code = "encode"
    text = "Select shift to encode message: "
    codeDisplay(text)

def codeDisplay(txt):
    global root
    encodeFrame = tk.Frame(root, bg='light blue')
    encodeFrame.place(relheight=0.1,relwidth=0.7,relx=0.15,rely=0.4)
    encodeText = tk.Label(encodeFrame, bg='light blue', text = txt, font=1)
    encodeText.place(relheight=0.4,relwidth=0.5, relx=0,rely = 0.3)
    right = None
    left = tk.Button(encodeFrame, bg='light gray', text = "Left Shift", command = lambda : setLeft(left,right))
    left.place(relheight=0.8, relwidth= 0.2, relx = 0.55, rely = 0.1)
    right = tk.Button(encodeFrame, bg='light gray', text = "Right Shift" , command = lambda : setRight(right,left))
    right.place(relheight=0.8, relwidth= 0.2, relx = 0.775, rely = 0.1)

def getSpaces():
    global root
    clicked = tk.StringVar()
    clicked.set(1)
    spaceFrame = tk.Frame(root, bg='light blue')
    spaceFrame.place(relheight=0.1,relwidth=0.7,relx=0.15,rely=0.55)
    spaceText = tk.Label(spaceFrame, bg='light blue', text = "Select number of spaces to be shifted: ", font=1)
    spaceText.place(relheight=0.4,relwidth=0.55, relx=0,rely = 0.3)
    menu = tk.OptionMenu(spaceFrame,clicked, *values)
    menu.place(relheight=0.8, relwidth= 0.2, relx = 0.55, rely = 0.1)    
    dropButton = tk.Button(spaceFrame, bg = 'light gray', command = lambda: getInput(clicked.get()), text = 'Select')
    dropButton.place(relheight=0.8, relwidth= 0.2, relx = 0.775, rely = 0.1)    
    
def getInput(val):
    global root, spaces
    spaces = val
    entryFrame = tk.Frame(root, bg='light blue')
    entryFrame.place(relheight=0.1,relwidth=0.7,relx=0.15,rely=0.7)
    entryText = tk.Label(entryFrame, bg='light blue', text = "Enter text to be encoded.", font=1)
    entryText.place(relheight=0.4,relwidth=0.4, relx=0,rely = 0.3)
    entry = tk.Entry(entryFrame, bg='light gray')
    entry.place(relx=0.45,rely=0.1,relheight=0.8,relwidth=0.4)
    submit = tk.Button(entryFrame, text = "GO", bg='light gray', command= lambda : callCipher(entry.get()))
    submit.place(relheight=0.8, relwidth= 0.1, relx = 0.875, rely = 0.1)

def callCipher(txt):
    global shift, code, spaces, result
    result = cipherFunc(code,shift,txt,spaces)
    showOutput()

def showOutput():
    global root, result
    txt = 'So the ' + code + 'd ' + 'message is: '
    txt += result

    outputFrame = tk.Frame(root, bg='light blue')
    outputFrame.place(relheight=0.1,relwidth=0.7,relx=0.15,rely=0.85)
    outputText = tk.Entry(outputFrame, state = 'readonly' , font=1, readonlybackground='light blue', fg='black')
    var = tk.StringVar()
    var.set(txt)
    outputText.config(textvariable=var, relief='flat')
    outputText.place(relheight=0.8,relwidth=0.7, relx=0.15,rely = 0.1)

if __name__ == "__main__":
    # Create window
    root = tk.Tk()
    root.title("Caesar Cipher App")
    
    # Set window sizz
    canvas = tk.Canvas(root,height=460,width=800)
    canvas.pack()

    # Load Background image
    image = PIL.Image.open('images.jpg')
    bg_img = PIL.ImageTk.PhotoImage(image)
    bg_label = tk.Label(root, image = bg_img)
    bg_label.place(relwidth = 1, relheight = 1)

    root.resizable(False, False) 

    # Add heading to Window
    headingText = tk.Label(root, bg='light blue', text = "Welcome to Caesar Cipher App", font=1)
    headingText.place(relheight=0.1,relwidth=0.4, relx=0.3,rely = 0.1)

    # Get info for code/decode
    codeFrame = tk.Frame(root, bg='light blue')
    codeFrame.place(relheight=0.1,relwidth=0.7,relx=0.15,rely=0.25)
    codeText = tk.Label(codeFrame, bg='light blue', text = "Would you like to Encode or Decode", font=1)
    codeText.place(relheight=0.4,relwidth=0.5, relx=0,rely = 0.3)
    decodeButton = None
    encodeButton = tk.Button(codeFrame, bg='light gray', text = "Encode" , command = lambda: encodeFunc(encodeButton,decodeButton))
    encodeButton.place(relheight=0.8, relwidth= 0.2, relx = 0.55, rely = 0.1)
    decodeButton = tk.Button(codeFrame, bg='light gray', text = "Decode", command = lambda: decodeFunc(decodeButton,encodeButton))
    decodeButton.place(relheight=0.8, relwidth= 0.2, relx = 0.775, rely = 0.1)

    root.mainloop()