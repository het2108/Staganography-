
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
root.title("Steganography - Hide a Secret Message/File In an Image")
root.geometry("500x500")
root.resizable(False, False)
root.configure(bg="#000000")

root.attributes("-fullscreen", True)

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File ',
                                          filetype=(("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All file", "*.*")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img, width=400, height=400)
    lb1.image = img

def hide_text():
    global filename
    message = text1.get(1.0, END)
    lsb.hide(filename, message).save("hidden_image.png")
    show_message("Text hidden successfully!")

def hide_file():
    global filename
    file_to_hide = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File to Hide',
                                              filetype=(("All files", "*.*"),))
    lsb.hide(filename, file_to_hide).save("hidden_image.png")
    show_message("File hidden successfully!")

def show_data():
    global filename
    hidden_data = lsb.reveal(filename)
    if hidden_data:
        
        if os.path.isfile(hidden_data):
            try:
                with open(hidden_data, "r") as file:
                    hidden_content = file.read()
                show_message("Hidden data from file: \n" + hidden_content)
            except Exception as e:
                show_message("Error reading hidden file data: " + str(e))
        else:
            
            show_message("Hidden text inside the image: \n" + hidden_data)
    else:
        show_message("No hidden data found!")


def save():
    global filename
    lsb.hide(filename, text1.get(1.0, END)).save("hidden_image.png")
    show_message("Text saved successfully!")

def show_message(message):
    text1.delete(1.0, END)
    text1.insert(END, message)


try:
    img = Image.open("logo2.jpg")
    img = ImageTk.PhotoImage(img)
    
except Exception as e:
    print("Error loading image:", e)

root.iconphoto(False, img)

try:
    logo = Image.open("img2.jpg")
    logo = ImageTk.PhotoImage(logo)
 
except Exception as e:
    print("Error loading image:", e)
Label(root, image=logo, bg="#000000").place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.15)

Label(root, text="VEILED VECTOR", bg="#000320", fg="Cyan", font="arial 25 bold").place(relx=0.2, rely=0.05)

# first frame
frame1 = Frame(root, bd=3, bg="black", relief=GROOVE)
frame1.place(relx=0.05, rely=0.2, relwidth=0.55, relheight=0.7)

lb1 = Label(frame1, bg="black")
lb1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.85)

# second frame
frame2 = Frame(root, bd=3, bg="black", relief=GROOVE)
frame2.place(relx=0.62, rely=0.2, relwidth=0.33, relheight=0.2)

text1 = Text(frame2, font="Roboto 12", bg="black", fg="white", insertbackground="white", relief=GROOVE, wrap=WORD)

text1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)  

# Scrollbar
scrollbar = Scrollbar(frame2)
scrollbar.place(relx=0.95, rely=0.05, relheight=0.9)

scrollbar.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar.set)

# 3rd Frame
frame3 = Frame(root, bd=3, bg="#000000", relief=GROOVE)
frame3.place(relx=0.62, rely=0.45, relwidth=0.33, relheight=0.2)

Button(frame3, text="Open Image", font="arial 10 bold", bg="black", fg="white", command=showimage).place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.6)
Button(frame3, text="Hide Text", font="arial 10 bold", bg="black", fg="white", command=hide_text).place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.6)

Label(frame3, text="Picture, Image, Photo File", bg="#000000", fg="yellow").place(relx=0.05, rely=0.1, relwidth=0.9)

# 4th frame
frame4 = Frame(root, bd=3, bg="#000000", relief=GROOVE)
frame4.place(relx=0.62, rely=0.7, relwidth=0.33, relheight=0.2)

Button(frame4, text="Show Text", font="arial 10 bold", bg="black", fg="white", command=show_data).place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.6)

Button(frame4, text="Hide File", font="arial 10 bold", bg="black", fg="white", command=hide_file).place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.6)
Label(frame4, text="Picture, Image, Photo File", bg="#000000", fg="yellow").place(relx=0.05, rely=0.1, relwidth=0.9)

root.mainloop()