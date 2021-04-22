

from PIL import Image #for image processing
import pytesseract # for photo to text
import os # for fliepaths and os things
from docx import Document #to write to .docs files   INSTALL python-docx
import unicodedata #remove unicode to transfer to .docx

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


#process the image
img = Image.open(os.path.dirname(__file__) + "\\transl.PNG")
text = pytesseract.image_to_string(img, lang = 'eng')


#write to .docx prerequesites
document = Document()


import re
#write the text to 'transl.docx' in this directory
try:
    d = document.add_paragraph('Translations:')
except IOError:
        print(col.red + IOError)
else:
    with open('transl.docx', mode ='w') as d:
        #re.match("[a-zA-Z0-9 ,.'\"\n:();]")
        formattedText = re.sub("[a-zA-Z0-9 ,.'\"\n]", " ", text)
        print(formattedText)
        #document.add_paragraph(formattedText)
        #document.save('transl.docx')
        print(col.green + "text file written to " + os.path.dirname(__file__) + "\\transl.docx" )



"""
#write the text to 'transl.docx' in this directory
try:
    f = open('transl.txt')
except IOError:
        print(col.red + IOError)
else:
    with open('transl.txt', mode ='w') as f:     
        f.write(text)
        print(col.green + "text file written to " + os.path.dirname(__file__) + "\\transl.txt" )
        f.close()
"""


#code asks you to edit before you continue
inputToContinue(col.white + "please press enter to make revisions to the text file")

#run the text file to edit
os.startfile(os.path.dirname(__file__) + "\\transl.txt")
os.startfile(os.path.dirname(__file__) + "\\transl.png")

#asks you to enter once you are done editing
inputToContinue(col.white + "please press enter once you are done with revisions to the document")













"""
# import the following libraries
# will convert the image to text string
import pytesseract      
  
# adds image processing capabilities
from PIL import Image    
  
 # converts the text to speech  
import pyttsx3           
  
#translates into the mentioned language
from googletrans import Translator      
  
 # opening an image from the source path
img = Image.open('transl.png')     
  
# describes image format in the output
print(img)                          
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'   
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path   
with open('abc.txt',mode ='w') as file:     
    file.write(result)
    print(result)
                   
p = Translator()                      
# translates the text into german language
k = p.translate(result,dest='german')      
print(k)
engine = pyttsx3.init()
  
# an audio will be played which speaks the test if pyttsx3 recognizes it
engine.say(k)                             
engine.runAndWait()
"""