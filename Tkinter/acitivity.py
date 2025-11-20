import tkinter as tk

=root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x150") 

def say_hello():
    label.config(text="Hello, Tkinter!")

label = tk.Label(root, text="Welcome!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

root.mainloop()
