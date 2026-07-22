import pyttsx3

engine = pyttsx3.init()

text = f"The MRI image is classified as {predicted_class}"

engine.say(text)
engine.runAndWait()
