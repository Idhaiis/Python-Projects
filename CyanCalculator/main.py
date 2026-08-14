#Made by Idhaiis

import customtkinter as ctk 
import tkinter as tk


app = ctk.CTk()
app.geometry("400x500")
app.title("Calculator")
app.iconbitmap("icon.ico")
app.resizable(False, False)
app._set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

frame = ctk.CTkFrame(master=app, width=400, height=500)
frame.grid(row=0, column=0, padx=0, pady=0, rowspan=5, columnspan=4, sticky="nsew")
frame._set_appearance_mode("Dark")

entry = ctk.CTkEntry(master=frame, width=400, height=100, corner_radius=20, font=("consolas", 70, "bold"), justify="right",
                     fg_color="#7da8a8", bg_color="#7da8a8", text_color="#e5eeee",)
entry.grid(row=0, column=0, columnspan=4, sticky="new")

allowable_characters = "0123456789+-*/()."

def buttonp():
    entry.insert(tk.END, "+")
def button7():
    entry.insert(tk.END, "7")
def button8():
    entry.insert(tk.END, "8")
def button9():
    entry.insert(tk.END, "9")
def buttonm():
    entry.insert(tk.END, "-")
def button4():
    entry.insert(tk.END, "4")
def button5():
    entry.insert(tk.END, "5")
def button6():
    entry.insert(tk.END, "6")
def buttoni():
    entry.insert(tk.END, "*")
def button1():
    entry.insert(tk.END, "1")
def button2():
    entry.insert(tk.END, "2")
def button3():
    entry.insert(tk.END, "3")
def buttond():
    entry.insert(tk.END, "/")
def button0():
    entry.insert(tk.END, "0")
def buttonc():
    entry.delete(0, tk.END)
def buttone():
    expr = entry.get()
    if all(char in allowable_characters for char in expr):
        try:
            result = eval(expr)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

buttonp = ctk.CTkButton(master=frame, text="+", width=100, height=100, corner_radius=20, command=buttonp,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
buttonp.grid(row = 1, column = 0)
button7 = ctk.CTkButton(master=frame, text="7", width=100, height=100, corner_radius=20, command=button7,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
button7.grid(row = 1, column = 1)
button8 = ctk.CTkButton(master=frame, text="8", width=100, height=100, corner_radius=20, command=button8,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
button8.grid(row = 1, column = 2)
button9 = ctk.CTkButton(master=frame, text="9", width=100, height=100, corner_radius=20, command=button9,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
button9.grid(row = 1, column = 3)
buttonm = ctk.CTkButton(master=frame, text="-", width=100, height=100, corner_radius=20, command=buttonm,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
buttonm.grid(row = 2, column = 0)
button4 = ctk.CTkButton(master=frame, text="4", width=100, height=100, corner_radius=20, command=button4,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
button4.grid(row = 2, column = 1)
button5 = ctk.CTkButton(master=frame, text="5", width=100, height=100, corner_radius=20, command=button5,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
button5.grid(row = 2, column = 2)
button6 = ctk.CTkButton(master=frame, text="6", width=100, height=100, corner_radius=20, command=button6,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
button6.grid(row = 2, column = 3)
buttoni = ctk.CTkButton(master=frame, text="*", width=100, height=100, corner_radius=20, command=buttoni,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
buttoni.grid(row = 3, column = 0)
button1 = ctk.CTkButton(master=frame, text="1", width=100, height=100, corner_radius=20, command=button1,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
button1.grid(row = 3, column = 1)
button2 = ctk.CTkButton(master=frame, text="2", width=100, height=100, corner_radius=20, command=button2,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
button2.grid(row = 3, column = 2)
button3 = ctk.CTkButton(master=frame, text="3", width=100, height=100, corner_radius=20, command=button3,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
button3.grid(row = 3, column = 3)
buttond = ctk.CTkButton(master=frame, text="/", width=100, height=100, corner_radius=20, command=buttond,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
buttond.grid(row = 4, column = 0)
buttone = ctk.CTkButton(master=frame, text="=", width=100, height=100, corner_radius=20, command=buttone,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
buttone.grid(row = 4, column = 1)
button0 = ctk.CTkButton(master=frame, text="0", width=100, height=100, corner_radius=20, command=button0,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
button0.grid(row = 4, column = 2)
buttonc = ctk.CTkButton(master=frame, text="C", width=100, height=100, corner_radius=20, command=buttonc,
                        fg_color="#97b9b9", hover_color="#b1cbcb", bg_color="#7da8a8", text_color="#e5eeee", font=("consolas", 50, "bold"))
buttonc.grid(row = 4, column = 3)


app.mainloop()