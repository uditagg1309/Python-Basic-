import moviepy.editor as mp
from tkinter import *
from tkinter import filedialog

def convert():
    videoclip = mp.VideoFileClip(fname)
    videoclip.audio.write_audiofile("voice_hindi.mp3")
    messageToGenerate.set("Audio file is ready")

def upload():
    filename = filedialog.askopenfilename(filetype = [('Mp4 Files','*.mp4'), ('ogg files','*.ogg')])
    messageForUpload.set("File uploaded" + filename)
    global fname
    fname = filename

window = Tk()
window.geometry("700x250")
window["bg"] = "aqua"
window.title("Video to audio")
global messageForUpload
global messageToGenerate
messageForUpload = StringVar()
messageToGenerate = StringVar()
Label(window, text = "Hello", textvar = messageForUpload, font = "Arial 12 ", fg = "white").place( x = 100, y = 40)
Button(window, text = "Upload Video", command = upload, font = "Arial 12 ", fg = "red").place( x = 100, y = 70)
Button(window, text = "Convert Video", command = convert, font = "Arial 12 ", fg = "red").place( x = 350, y = 70)

Label(window, text = "Hello", textvar = messageToGenerate, font = "Arial 12 ", fg = "white").place( x = 100, y = 120)


window.mainloop()
    
