from PIL import Image #for image processing
import pytesseract # for photo to text
import os # for fliepaths and os things
from docx import Document #to write to .docs files   INSTALL python-docx
import unicodedata #remove unicode to transfer to .docx
import re # REGEX LET'S GO
import tkinter as tk

#https://github.com/UB-Mannheim/tesseract/wiki


#add color class so you can print in colors easily
class col:
    white = '\033[0;37;40m'
    green = '\033[92m'
    red = '\033[93m'
    pink = '\033[95m'

#add a user input to continue
def inputToContinue(question):
    ask = input(question)
    return ask

#create a relative file path to reference
userprofile = os.environ['USERPROFILE']
AppDataPath = os.path.join(userprofile, 'AppData')
print(col.green + "userprofile is: " + userprofile)

#set the file location of tesseract
pytesseract.pytesseract.tesseract_cmd = AppDataPath + "\\local\\programs\\Tesseract-OCR\\tesseract.exe"


#write to .docx prerequesites
document = Document()


##############################################################################################
##############################################################################################

def processImage():
    #process the image
    img = Image.open(os.path.dirname(__file__) + "\\transl.PNG")
    global text
    text = pytesseract.image_to_string(img, lang = 'eng')
    return text



def writeToDoc(writeBackup):
    #write the text to 'transl.docx' in this directory
    try:
        document.add_paragraph('Translations:')
    except IOError:
            print(col.red + IOError)
    else:
        with open('transl.docx', mode ='w'):
            #re.match("[a-zA-Z0-9 ,.'\"\n:();]")
            formattedText = re.sub("[^a-zA-Z0-9 ,.'\"\n]", " ", text)
            print(col.white + formattedText)
            document.add_paragraph(formattedText)
            document.save('transl.docx')

        if writeBackup == True:
            with open('translBackup.docx', mode ='w'):
                formattedText = re.sub("[^a-zA-Z0-9 ,.'\"\n]", " ", text)
                print(col.white + formattedText)
                document.add_paragraph(formattedText)
                document.save('translBackup.docx')

            #write to the console
            print(col.green + "text file written to " + os.path.dirname(__file__) + "\\transl.docx" )

def askForRevisions():
    #code asks you to edit before you continue
    inputToContinue(col.white + "please press enter to make revisions to the text file")

    #run the text file to edit
    os.startfile(os.path.dirname(__file__) + "\\transl.docx")
    os.startfile(os.path.dirname(__file__) + "\\transl.png")

    #asks you to enter once you are done editing
    inputToContinue(col.white + "please press enter once you are done with revisions to the document")

##################################################################################################
##################################################################################################
def main():
    processImage()
    writeToDoc(True)
    askForRevisions()

main()
##################################################################################################
##################################################################################################

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()
