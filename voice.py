import pyttsx3
import subprocess

engine = pyttsx3.init()

# if you need to change the bot language to English - use: "com.apple.speech.synthesis.voice.samantha"
engine.setProperty('voice', "com.apple.speech.synthesis.voice.milena.premium")


def text_to_file(text):
    mp3_file = f"data/message.mp3"
    out_file = f"data/message_out.ogg"
    engine.save_to_file(text, mp3_file)
    engine.runAndWait()
    subprocess.run(["ffmpeg", '-i', mp3_file, '-acodec',
                    'libopus', out_file, '-y'])
    return out_file
