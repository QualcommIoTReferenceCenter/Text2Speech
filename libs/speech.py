from gtts import gTTS
import os

# creates a mp3 with the spoken text and reproduces it
# then erases the mp3
def speech(text_string,lang_dest):
    speech = gTTS(text=text_string, lang=lang_dest, slow=False)
    speech.save("speech.mp3")
    os.system("mpg321 -q speech.mp3")
    os.remove("speech.mp3")
