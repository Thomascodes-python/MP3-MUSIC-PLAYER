# """"
# Music Player App
# """
# import tkinter 
# from tkinter import ttk,filedialog
# from pygame import mixer
# from tkinter import messagebox
# from PIL import Image, ImageTk
# mixer.init()
# import os



# def label_frame():
#     global select_musicframe,image_frame,songname_frame,selectsong_frame
#     select_musicframe = tkinter.LabelFrame(root , borderwidth=1).grid(row=1,column=0)
#     image_frame = tkinter.LabelFrame(root, borderwidth=1).grid(row=2,column=0)
#     songname_frame = tkinter.LabelFrame(root, borderwidth=1).grid(row=3,column=1)
#     selectsong_frame = tkinter.LabelFrame(root,borderwidth=1,).grid(row=4,column=0)


#     entry_frame()

    
# def selectsong():
#     file = filedialog.askdirectory()
#     if file:
#         os.chdir(file)
#         songs = os.listdir(file)
#         print(songs)
#         for song in songs:
#                 if song.endswith(".mp3"):
#                     songlist.insert(tkinter.END, song)
            
# def playsong():
#     try:
#         music = songlist.get(tkinter.ACTIVE)
#         print(music[0:-4])
#         mixer.music.load(songlist.get(tkinter.ACTIVE))
#         mixer.music.play()
#         songname.config(text=music[0:-4])
#     except Exception:
#         messagebox.showerror(title="NO SONG",message="SELECT SONG")


 
# def stopmusic():
#     mixer.music.stop()
# # mixer.music.rewind()
# def unpause():
#     mixer.music.unpause()
# def pause():
#     mixer.music.pause()


# def entry_frame():
#     global songlist,songname
    
#     selecting_button =tkinter.Button(select_musicframe,width=10,text="Select Song",command=selectsong,font=("Helvetica",12),background="#F5F5F5",)
#     selecting_button.grid(row=1,column=0,pady=10,padx=40)

    
#     image = tkinter.Label(image_frame,background="#D0CEE2",width=220,height=180,image=music_image)
#     image.grid(row=2,column=0,padx=20)
    
#     songname = tkinter.Label(songname_frame,width=30,height=2,text="",background="#666666",font=("Helvetica",10),foreground="white")
#     songname.grid(row=3,column=0,pady=10)
    
#     play_button = tkinter.Button(root,text="Play",width=5,command=playsong)
#     play_button.grid(row=4,column=0)
    
#     pause_button =tkinter.Button(root,image=pause_icon,command=pause,width=40,background="white")
#     pause_button.grid(row=5,column=0,padx=10,pady=10)
    
#     unpause_button = tkinter.Button(root,width=40,command=unpause,image=play_icon,background="white")
#     unpause_button.grid(row=5,column=0,padx=10,pady=10)
    
#     pause_button = tkinter.Button(root,text="stop",command=stopmusic,width=5)
#     pause_button.grid(row=6,column=0,pady=15)

#     songlist = tkinter.Listbox(selectsong_frame,background="#D0CEE2",width=60,height=10,cursor="hand2")
#     songlist.grid(row=7,column=0)

# if __name__ == "__main__":
#     root = tkinter.Tk()
#     root.geometry("500x600")
#     root.title("SEUN PLAY")
#     root.config(background="#7EA6E0")
#     root.resizable(0,0)
#     root.iconbitmap("icion.png")  
#     music_image = ImageTk.PhotoImage(Image.open("icion.png").resize((220,180)))
#     pause_icon = ImageTk.PhotoImage(Image.open("pause_img.png").resize((40,25)))
#     play_icon = ImageTk.PhotoImage(Image.open("play_img.png").resize((40,25)))


#     label_frame()
#     root.mainloop()
    
