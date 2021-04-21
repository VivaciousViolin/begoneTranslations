

from PIL import Image #for image processing
import pytesseract # for photo to text
import os # for fliepaths and os things

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
try:
    #try to open tesseract to detect if it is there
    open(AppDataPath + "\\local\\programs\\Tesseract-OCR\\tesseract.exe")
except:
    #print a red error
    print(col.red + AppDataPath + "\\local\\programs\\Tesseract-OCR\\tesseract.exe" + " does not exist")
else:
    #set it so that tesseract can called with pytesseract.
    pytesseract.pytesseract.tesseract_cmd = AppDataPath + "\\local\\programs\\Tesseract-OCR\\tesseract.exe"


#process the image
img = Image.open(os.path.dirname(__file__) + "\\transl.PNG")
text = pytesseract.image_to_string(img, lang = 'eng')

#write the text to 'transl.txt' in this directory
try:
    f = open('transl.txt')
except IOError:
        print(col.red + IOError)
else:
    with open('transl.txt', mode ='w') as f:     
        f.write(text)
        print(col.green + "text file written to " + os.path.dirname(__file__) + "\\transl.txt" )
        f.close()

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