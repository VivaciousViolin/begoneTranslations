

from PIL import Image #for image processing
import pytesseract # for photo to text
import os # for fliepaths

#add a user input to continue
def inputToContinue(question):
    ask = input(question)
    return ask

#create a relative file path to reference
userprofile = os.environ['USERPROFILE']
AppDataPath = os.path.join(userprofile, 'AppData')
print("userprofile is: " + userprofile)

#set the file location of tesseract
pytesseract.pytesseract.tesseract_cmd = AppDataPath + "\\local\\programs\\Tesseract-OCR\\tesseract.exe"

#process the image
img = Image.open(os.path.dirname(__file__) + "\\transl.PNG")
text = pytesseract.image_to_string(img, lang = 'eng')

print(text)

inputToContinue("please make revisions to the text file and press enter to continue")
print("please make revisions to text file ")


print(text)










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