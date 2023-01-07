from tkinter import *
from customtkinter import *
import customtkinter
import tkinter as tk
import tkinter

root = tk.Tk()
root.title("Crypto wallet link")
root.geometry("500x400")
root.resizable(width=False,height=False)
root['bg']='black'

optionmenu_var = customtkinter.StringVar(value="option 2") 

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

segemented_button_var = customtkinter.StringVar(value="Value 1") 

segemented_button = customtkinter.CTkSegmentedButton(
master=root,
values=["Ethereum", "Solana", "Bitcoin","Dogecoin","Polygon"],
variable=segemented_button_var)
segemented_button.pack(padx=20, pady=55)

canvas = Canvas(root,width=300,height=100)
canvas.create_text(130,70,text="Decentralized Web 3.0 tool", 
fill='#051937',font=('Helvetica bold',18))
canvas.pack()
canvas.place(x=100, y=150)

img = PhotoImage(file='/Users/Mac/Desktop/img/bitcoin.png')
imger = Label(root, image=img,bd=0)
imger.pack()
imger.place(x=0,y=30)

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

def button_function():
    print("button pressed")

button = customtkinter.CTkButton(
master=root, text="Add Crypto Wallet", command=button_function)
button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

root.mainloop()

