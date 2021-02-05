from pytube import YouTube
import os
from tkinter import *

root=Tk()
root.geometry('600x200')
root.title('Youtube Video Downloader')


Label_1=Label(root,text="Paste The Youtube Link Here", font=("bold",20))
Label_1.place(x=120,y=20)


mylink=StringVar()

pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=140, y=80)

#link="https://www.youtube.com/watch?v=0NV1KdWRHck"

def downloadVideo():
    x=str(mylink.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('F:/letsupgrade'):
        os.makedirs('F:/Letsupgrade')
    ytvideo.download('F:/Letsupgrade') 

Button(root,text="Download Video", width=20, bg='green',fg="white", command=downloadVideo).place(x=220, y=110)

root.mainloop()
