#-------Importing Libraries-----------------------------------------------------
import io
import pygame           #pip install pygame
from gtts import gTTS   #pip install gTTS
#-------------END---------------------------------------------------------------

#-------Conversion--------------------------------------------------------------
def speak(text):
    with io.BytesIO() as file:
        gTTS(text=text,lang="en").write_to_fp(file)#Converting text to audio
        file.seek(0)
        pygame.mixer.init()#playing with pygame player
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
#-----------END-----------------------------------------------------------------

#-----------Calling the function------------------------------------------------
if __name__=='__main__':
    text=input("What should I say? > ")
    speak(text)
    
