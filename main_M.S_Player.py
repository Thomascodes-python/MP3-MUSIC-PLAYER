import tkinter 
from tkinter import ttk,filedialog
from pygame import mixer
from PIL import Image, ImageTk
mixer.init()
import os



def label_frame():
    global select_musicframe,songlist_frame,songname_frame,pauseframe
    select_musicframe = tkinter.LabelFrame(root , borderwidth=1).grid(row=1,column=0)
    songlist_frame = tkinter.LabelFrame(root, borderwidth=5).grid(row=2,column=1)
    songname_frame = tkinter.LabelFrame(root, borderwidth=1).grid(row=3,column=1)
    pauseframe = tkinter.LabelFrame(root,borderwidth=1).grid(row=5,column=0,padx=30)


    entry_frame()

    
def selectsong():
    file = filedialog.askdirectory()
    if file:
        os.chdir(file)
        songs = os.listdir(file)
        print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                song_list.insert(tkinter.END, song)


def playsong():
    music = song_list.get(tkinter.ACTIVE)
    print(music[0:-4])
    mixer.music.load(song_list.get(tkinter.ACTIVE))
    mixer.music.play()
    songname.config(text=music[0:-4])


 
def stopmusic():
    mixer.music.stop()
def unpause():
    mixer.music.unpause()
def pause():
    mixer.music.pause()


def entry_frame():
    global song_list,songname
    
    selecting_button =tkinter.Button(select_musicframe,width=10,text="Select Song",command=selectsong,font=("Helvetica",12),background="#F5F5F5",)
    selecting_button.grid(row=1,column=0,padx=10,pady=10 )

    exit_button = tkinter.Button(select_musicframe,command=root.destroy,text="Exit",font=("Helvetica",12))
    exit_button.grid(row=1,column=2)

    song_list = tkinter.Listbox(songlist_frame,background="#D0CEE2",width=46,height=10,cursor="hand2")
    song_list.grid(row=2,column=1)
    
    songname = tkinter.Label(songname_frame,width=36,height=2,text="",background="#666666",font=("Helvetica",10),foreground="white")
    songname.grid(row=3,column=1,pady=10)
    
    play_button = tkinter.Button(root,text="Play",width=5,command=playsong)
    play_button.grid(row=4,column=1)
    
    pause_button =tkinter.Button(pauseframe,image=pause_icon,command=pause,width=40,background="white")
    pause_button.grid(row=5,column=0,padx=20,pady=5)
    
    unpause_button = tkinter.Button(root,width=40,command=unpause,image=play_icon,background="white")
    unpause_button.grid(row=5,column=2,padx=20)
    
    pause_button = tkinter.Button(root,text="stop",command=stopmusic,width=5)
    pause_button.grid(row=6,column=1,pady=5)


    

if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("500x400")
    root.title("SEUN PLAY")
    root.config(background="#7EA6E0")
    root.resizable(0,0)
    root.iconbitmap(r"C:\Users\User\Downloads\icion.png")

    pause_icon = ImageTk.PhotoImage(Image.open("pause_img.png").resize((40,25)))
    play_icon = ImageTk.PhotoImage(Image.open("play_img.png").resize((40,25)))

    label_frame()
    root.mainloop()
    
