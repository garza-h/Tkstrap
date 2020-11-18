import tkstrap as tks
import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
style = tks.init(root)

btn = ttk.Button(root, text="Ahora", style=style("big1"))
btn.grid(row=0,column=0)
root.mainloop()