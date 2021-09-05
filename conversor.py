import tkinter
from tkinter import Button, Canvas, Frame, Label, LabelFrame, PhotoImage, StringVar, Text, Tk
from tkinter.constants import ACTIVE, CENTER, DISABLED, FLAT, NONE, NW, RADIOBUTTON
import tkinter.font as font 
from tkinter import filedialog as fd
from tkinter import messagebox

import shutil
import os

from PIL import Image,ImageTk



def exit() -> None:
    global root
    root.destroy()

def converter() -> None:
    global image_path
    global image_name

    try:
        try:
            im = Image.open(image_path)

        except NameError:
            messagebox.showerror(title="Error!", message="You must select a file!")

        #I convert the image to jpg
        im.save(f'output_file_jpg/{image_name}', quality=95)
        img_name_var.set(image_name)


    except OSError:
        #If the image has transparency I remove it
        rgb_im = Image.open(image_path)
        rgb_im = im.convert('RGB')
        rgb_im.save(f'output_file_jpg/{image_name}')
        img_name_var.set(image_name)
    
    image_path = ""
    image_name = ""
    messagebox.showinfo(title="Success!",message="successfully converted!")


def get_image() -> None:
    global image_path
    global image_name


    try:
        #I look for the route and the name of the image
        image_path = fd.askopenfilenames(filetypes=[("Image Files", ".png")])
        image_path = image_path[0]
        
        image_name = image_path.split("/") 
        image_name = image_name[-1]
        img_name_var.set(image_name)
        image_name = image_name.replace('.png',".jpg")

        #Display Image 
        img = Image.open(image_path)
        img = img.resize((180, 160), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(master=root, image=img)
        panel.image = img
        panel.grid(row=1,column=0,pady=1,sticky="N")
        bttn_convert['state'] = ACTIVE

    except IndexError:
        pass

def main_window() -> None:
    try:
        os.mkdir('output_file_jpg')
        
    except FileExistsError:
        pass
    
    global root
    global image_path
    global img_name_var
    global bttn_convert

    #Main Window config 
    root.config(background="white")
    root.resizable(False,False)
    root.title("V1.0")

    screen_width  = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    screen_width  = screen_width / 5
    root.geometry(f"600x450+{round(screen_width)}+90")

    #Cool Colors
    navy_blue     = "#2A73D9"
    emerald_green = "#33b864"
    soft_red      = "#b83333"

    #Cool Fonts
    bttn_font        = font.Font(family="Helvetica,Arial,sans-serif", size=12)
    title_font       = font.Font(family="Poppins",size=15)
    subtitle_font    = font.Font(family="Poppins",size=12)
    
    


    #Texts
    title            = Label(master=root)
    title.config(text="CONVERTER",bg="white",font=subtitle_font)
    title.grid(row=0,column=0,pady=30)

    subtitle         = Label(master=root)
    subtitle.config(text="PNG TO JPG",bg="white",font=title_font)
    subtitle.grid(row=0,column=0,sticky="N")


    softwere_version =  Label(master=root)
    softwere_version.config(text="V1.0",background="white")
    softwere_version.grid(row=1,column=0,padx=20,pady=120,sticky="SW")

    img_name_var     = StringVar(master=root,value='')

    img_name         = Label(master=root)
    img_name.configure(textvariable=img_name_var,bg="white")
    img_name.grid(row=1,column=0,pady=180,sticky="N")


    #Buttons
    frame_buttons = Frame(master=root)
    frame_buttons.config(bg="white")
    frame_buttons.grid(row=1,column=0,pady=220,padx=110)

    bttn_upload = Button(master=frame_buttons)    
    bttn_upload.configure(text="UPLOAD A IMAGE",font=bttn_font,activeforeground="white",fg="white",activebackground=navy_blue,bg=navy_blue,borderwidth=0,cursor="hand2",command=get_image)
    bttn_upload.grid(row=1,column=1,padx=20)

    bttn_convert = Button(master=frame_buttons)
    bttn_convert['state'] = DISABLED
    bttn_convert.configure(text="CONVERT",font=bttn_font,activeforeground="white",fg="white",activebackground=emerald_green,bg=emerald_green,borderwidth=0,cursor="hand2",command=converter)
    bttn_convert.grid(row=1,column=2)

    

    bttn_exit = Button(master=frame_buttons)
    bttn_exit.configure(text="EXIT",font=bttn_font,activeforeground="white",fg="white",activebackground=soft_red,bg=soft_red,borderwidth=0,cursor="hand2",command=exit)
    bttn_exit.grid(row=1,column=3,padx=15)


if __name__ == "__main__":
    root = Tk()

    main_window()
    root.mainloop()